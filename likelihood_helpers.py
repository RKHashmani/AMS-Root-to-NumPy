import matplotlib.pyplot as plt
import numpy as np


def plot_likelihood_hist(e_EcalEMlhd, p_EcalEMlhd, title, min_x, max_x, bins=100, density=False):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    p_count, _ = np.histogram(p_EcalEMlhd, bins=bins, range=(min_x, max_x))
    e_count, _ = np.histogram(e_EcalEMlhd, bins=bins, range=(min_x, max_x))

    ax.hist(p_EcalEMlhd,
            bins=bins,
            range=(min_x, max_x),
            density = density,
            edgecolor=(1, 0, 0, 1),
            facecolor=(1, 0, 0, 0.35),
            histtype="stepfilled",  # Fill and Outline
            label="Protons (" + format(p_count.sum(), ",") + " events)")

    ax.hist(e_EcalEMlhd,
            bins=bins,
            range=(min_x, max_x),
            density = density,
            edgecolor=(0, 0, 1, 1),
            facecolor=(0, 0, 1, 0.35),
            histtype="stepfilled",  # Fill and Outline
            label="Electrons (" + format(e_count.sum(), ",") + " events)")

    # ax.yaxis.get_ticklocs(minor=True)
    ax.minorticks_on()

    plt.title(title)
    plt.xlabel("Likelihood Values")
    plt.ylabel("Count")

    plt.legend()
    plt.savefig(title + '.png', dpi=600, facecolor="white", edgecolor='none')
    plt.show()

def plot_3dbdt_hist(e_ecal3dbdt, p_ecal3dbdt, title, min_x, max_x, bins=100, density=False):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    p_count, _ = np.histogram(p_ecal3dbdt, bins=bins, range=(min_x, max_x))
    e_count, _ = np.histogram(e_ecal3dbdt, bins=bins, range=(min_x, max_x))

    ax.hist(p_ecal3dbdt,
            bins=bins,
            range=(min_x, max_x),
            density = density,
            edgecolor=(1, 0, 0, 1),
            facecolor=(1, 0, 0, 0.35),
            histtype="stepfilled",  # Fill and Outline
            label="Protons (" + format(p_count.sum(), ",") + " events)")

    ax.hist(e_ecal3dbdt,
            bins=bins,
            range=(min_x, max_x),
            density = density,
            edgecolor=(0, 0, 1, 1),
            facecolor=(0, 0, 1, 0.35),
            histtype="stepfilled",  # Fill and Outline
            label="Electrons (" + format(e_count.sum(), ",") + " events)")

    # ax.yaxis.get_ticklocs(minor=True)
    ax.minorticks_on()

    plt.title(title)
    plt.xlabel("BDT Values")
    plt.ylabel("Count")

    plt.legend()
    plt.savefig(title + '.png', dpi=600, facecolor="white", edgecolor='none')
    plt.show()

def proton_rejection_calc(protons, electrons, threshold=4):
    p_mom = np.asarray(protons["mom"])
    p_EcalEMlhd = np.asarray(protons["EcalEMlhd_0"])
    e_mom = np.asarray(electrons["mom"])
    e_EcalEMlhd = np.asarray(electrons["EcalEMlhd_0"])

    e_percent = (e_EcalEMlhd < threshold).sum() / e_EcalEMlhd.size * 100
    print("Electron Efficiency:", e_percent)

    print("Total protons:", p_EcalEMlhd.size)
    print("Protons classified as electrons:", (p_EcalEMlhd < threshold).sum())

    p_rejection = p_EcalEMlhd.size / (p_EcalEMlhd < threshold).sum()
    print("Total Proton Rejection:", p_rejection)

    p200 = p_EcalEMlhd[p_mom <= 300]
    p300 = p_EcalEMlhd[(p_mom > 300) & (p_mom <= 400)]
    p400 = p_EcalEMlhd[(p_mom > 400) & (p_mom <= 500)]
    p500 = p_EcalEMlhd[(p_mom > 500)]
    print("Total 200-300 GeV:", p200.size)
    print("Total 300-400 GeV:", p300.size)
    print("Total 400-500 GeV:", p400.size)
    print("Total 500-600 GeV:", p500.size)

    p200_rejection = (p200 > threshold).sum()
    p300_rejection = (p300 > threshold).sum()
    p400_rejection = (p400 > threshold).sum()
    p500_rejection = (p500 > threshold).sum()

    print("Rejection 200-300 GeV:", p200_rejection)
    print("Rejection 300-400 GeV:", p300_rejection)
    print("Rejection 400-500 GeV:", p400_rejection)
    print("Rejection 500-600 GeV:", p500_rejection)


def plot_2d_hist(x, y, title, xlabel, ylabel, bins=10, range=False, density=False):
    # Use range=[[xmin, xmax], [ymin, ymax]] or range = None for no range.
    fig = plt.figure()
    ax = fig.add_subplot(111)

    h = ax.hist2d(x, y, bins, range, density, cmap=plt.cm.jet)

    ax.minorticks_on()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.savefig(title + '.png', dpi=600, facecolor="white", edgecolor='none')
    plt.show()


def edep_2d_to_3d(edep_cell_event):
    # Takes in NumPy array of [18,72], Adds another dimension of 0s to make it [2, 18, 72]
    # Swaps the 0s of the new dimension only for XZ dimension.
    # Returns a single 3d Numpy Matrix Ready for use in Machine Learning

    edep_cell_stacked = np.stack((edep_cell_event, np.zeros([18, 72])))  # Adds 3rd dim of 0s.

    # Swaps X dimension rows from Z = 0 to Z = 1 dimension, effectively sending the XZ layer to the 1st channel.
    edep_cell_stacked[[0, 1], 2, :] = edep_cell_stacked[[1, 0], 2, :]
    edep_cell_stacked[[0, 1], 3, :] = edep_cell_stacked[[1, 0], 3, :]
    edep_cell_stacked[[0, 1], 6, :] = edep_cell_stacked[[1, 0], 6, :]
    edep_cell_stacked[[0, 1], 7, :] = edep_cell_stacked[[1, 0], 7, :]
    edep_cell_stacked[[0, 1], 10, :] = edep_cell_stacked[[1, 0], 10, :]
    edep_cell_stacked[[0, 1], 11, :] = edep_cell_stacked[[1, 0], 11, :]
    edep_cell_stacked[[0, 1], 14, :] = edep_cell_stacked[[1, 0], 14, :]
    edep_cell_stacked[[0, 1], 15, :] = edep_cell_stacked[[1, 0], 15, :]

    return edep_cell_stacked


def edep_3d_to_2d(edep_cell_stacked):
    """
    Takes in NumPy array of [sample_size,2,18,72], swaps the 0s in the 0th channels with the values on the 1st
    channel, effectively making the 1st channel be full of 0s, then deletes the 1st channel entirely. This gives us
    the original 18x72 ECAL hit with XZ and YZ layers together in a single channel, ready for machine learning.

    Bug: Seems to edit the inputted edep_cell_stacked as well, keeping the dimensions the same but performing the
    channel swap option. Why does it do the latter, but not remove the extra channel, i.e. the last step of this
    function?

    :param edep_cell_stacked: NumPy array of [sample_size,2,18,72]
    :return: NumPy array of [sample_size,1,18,72]
    """

    # Swaps X dimension rows from Z = 1 to Z = 0 dimension, effectively combining the XZ layer to the 0th channel.
    edep_cell_stacked[:, [1, 0], 2, :] = edep_cell_stacked[:, [0, 1], 2, :]
    edep_cell_stacked[:, [1, 0], 3, :] = edep_cell_stacked[:, [0, 1], 3, :]
    edep_cell_stacked[:, [1, 0], 6, :] = edep_cell_stacked[:, [0, 1], 6, :]
    edep_cell_stacked[:, [1, 0], 7, :] = edep_cell_stacked[:, [0, 1], 7, :]
    edep_cell_stacked[:, [1, 0], 10, :] = edep_cell_stacked[:, [0, 1], 10, :]
    edep_cell_stacked[:, [1, 0], 11, :] = edep_cell_stacked[:, [0, 1], 11, :]
    edep_cell_stacked[:, [1, 0], 14, :] = edep_cell_stacked[:, [0, 1], 14, :]
    edep_cell_stacked[:, [1, 0], 15, :] = edep_cell_stacked[:, [0, 1], 15, :]

    edep_cell_stacked = edep_cell_stacked[:, 0, :, :]  # Removes the 1st channel, leaving only 0th channel.
    # Adds an extra dimension, turning [batch_size,18,72] into [batch_size,1,18,72]
    edep_cell_stacked = np.expand_dims(edep_cell_stacked, axis=1)

    return edep_cell_stacked


def classical_ml_accuracy(protons, electrons, threshold=4):
    p_mom = np.asarray(protons["mom"])
    p_EcalEMlhd = np.asarray(protons["EcalEMlhd_0"])
    e_mom = np.asarray(electrons["mom"])
    e_EcalEMlhd = np.asarray(electrons["EcalEMlhd_0"])

    print("Total Electrons:", e_EcalEMlhd.size)
    print("Total protons:", p_EcalEMlhd.size)
    total_no = e_EcalEMlhd.size + p_EcalEMlhd.size
    print ("Total Particles:", total_no)
    
    proton_as_proton = (p_EcalEMlhd > threshold).sum()
    proton_as_electron = (p_EcalEMlhd < threshold).sum()
    electron_as_proton = (e_EcalEMlhd > threshold).sum()
    electron_as_electron = (e_EcalEMlhd < threshold).sum()
    
    print ("Confusion Matrix:")
    print("0 predicted as 0:", proton_as_proton)
    print("0 predicted as 1:", proton_as_electron)
    print("1 predicted as 0:", electron_as_proton)
    print("1 predicted as 1:", electron_as_electron)
    
    total_accuracy = (proton_as_proton + electron_as_electron) / total_no * 100
    print ("Total ML Accuracy:", total_accuracy)
    
    e_percent = electron_as_electron / e_EcalEMlhd.size * 100
    print("Electron Efficiency:", e_percent)
    
    # Proton Rejection:
    print("Proton Rejection Power:", proton_as_proton)