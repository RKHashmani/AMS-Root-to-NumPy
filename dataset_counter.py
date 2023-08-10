"""
This script is used to count the number of events in a root dataset.
"""

import time
import argparse
import ROOT
import numpy as np

from likelihood_helpers import edep_2d_to_3d


def dataset_counter_min(data_name, data_path, total):
    #  To parse arguments:

    # ROOT Dataset Name:
    print("Chosen ROOT Dataset:", data_name)
    # path to dataset
    print("Directory of ROOT Files:", data_path)

    count = 0


    for i in range(1, total):
        # print(f"{i:04d}")
        # print(data_path + "/" + data_name + f"_{i:04d}.root")
        try:
            particles = (ROOT.RDataFrame("t1", data_path + "/" + data_name + f"_{i:05d}.root")
                         # .Filter("en3d >= 1000 && en3d <= 2000")  # Make sure to do >= 200 but < 1000 for < 1 TeV set.
                         )
        except:
            print("File not found:")
            print(data_path + "/" + data_name + f"_{i:04d}.root")
            continue

        try:
            particles = particles.AsNumpy(columns=["mom",
                                                   "en3d"
                                                   ])
        except:
            print("No events in file:")
            print(data_path + "/" + data_name + f"_{i:05d}.root")
            print(data_path + "/" + data_name + f"_{i:05d}.root")
            continue

        en3d = np.asarray(particles["en3d"])
        count_temp = np.asarray(particles["en3d"]).shape[0]
        count += count_temp

    print(f'-------------------------------en3d = {count}-------------------------------')

    particles = (ROOT.RDataFrame("t1", data_path + "/" + data_name + "_*.root")
                 #.Filter("en3d >= 1000 && en3d <= 2000")  # Make sure to do >= 200 but < 1000 for < 1 TeV set.
                 )
    particles = particles.AsNumpy(columns=["mom",
                                           "en3d"
                                           ])

    en3d = np.asarray(particles["en3d"])
    print(f'en3d = {np.asarray(particles["en3d"]).shape}')

    return en3d.shape[0]


def dataset_counter(data_name, data_path, total):
    #  To parse arguments:


    # ROOT Dataset Name:
    print("Chosen ROOT Dataset:", data_name)
    # path to dataset
    print("Directory of ROOT Files:", data_path)

    particles = (ROOT.RDataFrame("t1", data_path + "/" + data_name + "_*.root")
                 .Filter("en3d >= 1000 && en3d <= 2000")  # Make sure to do en3d >= 200 && en3d < 1000 for < 1 TeV set and en3d >= 1000 && en3d <= 2000 for > 1 TeV
                 .Define("EcalEMlhd_0", "EcalEMlhd[0]")
                 .Define("Trk_Ecal_Inci_X_0", "Trk_Ecal_Inci_X[0]")
                 .Define("Trk_Ecal_Inci_Y_0", "Trk_Ecal_Inci_Y[0]")
                 .Define("Trk_Ecal_Inci_Z_0", "Trk_Ecal_Inci_Z[0]")
                 .Define("Trk_Ecal_Inci_Zenith_0", "Trk_Ecal_Inci_Zenith[0]")
                 .Define("Trk_Ecal_Inci_Azimutal_0", "Trk_Ecal_Inci_Azimutal[0]")
                 .Define("Ecal_ShwrX0_0", "Ecal_ShwrX0[0]")
                 .Define("Ecal_ShwrY0_0", "Ecal_ShwrY0[0]")
                 .Define("Ecal_ShwrZ0_0", "Ecal_ShwrZ0[0]")
                 .Define("Ecal_Zenith_0", "Ecal_Zenith[0]")
                 .Define("Ecal_Azimutal_0", "Ecal_Azimutal[0]")
                 .Define("Ecal_ShwrE0_0", "Ecal_ShwrE0[0]")
                 .Define("Ecal_ShwrA0_0", "Ecal_ShwrA0[0]")
                 )
    particles = particles.AsNumpy(columns=["mom",
                                           "en3d",
                                           "ecal3dbdt",
                                           "EcalEMlhd_0",
                                           "Trk_Ecal_Inci_X_0",
                                           "Trk_Ecal_Inci_Y_0",
                                           "Trk_Ecal_Inci_Z_0",
                                           "Trk_Ecal_Inci_Zenith_0",
                                           "Trk_Ecal_Inci_Azimutal_0",
                                           "Ecal_ShwrX0_0",
                                           "Ecal_ShwrY0_0",
                                           "Ecal_ShwrZ0_0",
                                           "Ecal_Zenith_0",
                                           "Ecal_Azimutal_0",
                                           "Ecal_ShwrE0_0",
                                           "Ecal_ShwrA0_0"
                                           ])

    en3d = np.asarray(particles["en3d"])
    Trk_Ecal_Inci_X_0 = np.asarray(particles["Trk_Ecal_Inci_X_0"])
    Trk_Ecal_Inci_Y_0 = np.asarray(particles["Trk_Ecal_Inci_Y_0"])
    Trk_Ecal_Inci_Z_0 = np.asarray(particles["Trk_Ecal_Inci_Z_0"])
    Trk_Ecal_Inci_Zenith_0 = np.asarray(particles["Trk_Ecal_Inci_Zenith_0"])
    Trk_Ecal_Inci_Azimutal_0 = np.asarray(particles["Trk_Ecal_Inci_Azimutal_0"])
    Ecal_ShwrX0_0 = np.asarray(particles["Ecal_ShwrX0_0"])
    Ecal_ShwrY0_0 = np.asarray(particles["Ecal_ShwrY0_0"])
    Ecal_ShwrZ0_0 = np.asarray(particles["Ecal_ShwrZ0_0"])
    Ecal_Zenith_0 = np.asarray(particles["Ecal_Zenith_0"])
    Ecal_Azimutal_0 = np.asarray(particles["Ecal_Azimutal_0"])
    Ecal_ShwrE0_0 = np.asarray(particles["Ecal_ShwrE0_0"])
    Ecal_ShwrA0_0 = np.asarray(particles["Ecal_ShwrA0_0"])


    print(f'Trk_Ecal_Inci_X_0 = {np.asarray(particles["Trk_Ecal_Inci_X_0"]).shape}')
    print(f'Trk_Ecal_Inci_Y_0 = {np.asarray(particles["Trk_Ecal_Inci_Y_0"]).shape}')
    print(f'Trk_Ecal_Inci_Z_0 = {np.asarray(particles["Trk_Ecal_Inci_Z_0"]).shape}')
    print(f'Trk_Ecal_Inci_Zenith_0 = {np.asarray(particles["Trk_Ecal_Inci_Zenith_0"]).shape}')
    print(f'Trk_Ecal_Inci_Azimutal_0 = {np.asarray(particles["Trk_Ecal_Inci_Azimutal_0"]).shape}')
    print(f'Ecal_ShwrX0_0 = {np.asarray(particles["Ecal_ShwrX0_0"]).shape}')
    print(f'Ecal_ShwrY0_0 = {np.asarray(particles["Ecal_ShwrY0_0"]).shape}')
    print(f'Ecal_ShwrZ0_0 = {np.asarray(particles["Ecal_ShwrZ0_0"]).shape}')
    print(f'Ecal_Zenith_0 = {np.asarray(particles["Ecal_Zenith_0"]).shape}')
    print(f'Ecal_Azimutal_0 = {np.asarray(particles["Ecal_Azimutal_0"]).shape}')
    print(f'Ecal_ShwrE0_0 = {np.asarray(particles["Ecal_ShwrE0_0"]).shape}')
    print(f'Ecal_ShwrA0_0 = {np.asarray(particles["Ecal_ShwrA0_0"]).shape}')




    return en3d.shape[0]


def main():
    data_name = "el.pl1.2004000"
    total = 4306  # Electrons
    # data_path = "/home/rhashmani/Files/ECAL/datasets/ROOT/electron_debug"
    data_path = "/home/rhashmani/Files/ECAL/datasets/ROOT/el.pl1.2004000_trk_var"  # 13,498,758 no. of events
    no_of_electrons = dataset_counter(data_name, data_path, total)
    print("Number of electrons: {}--------------------------------------------------".format(no_of_electrons))

    # data_name = "pr.pl1phpsa.l1o9.5016000.4_00"
    # total = 2286  # Protons
    # # data_path = "/home/rhashmani/Files/ECAL/datasets/ROOT/proton_debug"
    # data_path = "/home/rhashmani/Files/ECAL/datasets/ROOT/pr.pl1phpsa.l1o9.5016000.4_00_trk_var"  #  no. of events
    # # data_path = "/home/rhashmani/Files/ECAL/datasets/ROOT/pr.pl1phpsa.l1o9.5016000.4_00_eosams"  # 631072  no. of events
    # no_of_protons = dataset_counter(data_name, data_path)
    # print("Number of protons: {}--------------------------------------------------".format(no_of_protons))

    # data_name = "Proton_Rec_200600"
    # data_path = "/home/rhashmani/Files/ECAL/datasets/ROOT/pr.pl1phpsa.l1o9.5016000.4_00_oldeos"  # 11191775 no. of events
    # no_of_protons = dataset_counter_min(data_name, data_path)
    # print("Number of protons: {}--------------------------------------------------".format(no_of_protons))

    # data_name = "pr.pl1phpsa.l1o9.5016000.4_00"
    # data_path = "/home/rhashmani/Files/ECAL/datasets/ROOT/pr.pl1phpsa.l1o9.5016000.4_00_eospub"  #  no. of events
    # no_of_protons = dataset_counter_min(data_name, data_path)
    # print("Number of protons: {}--------------------------------------------------".format(no_of_protons))

    # data_name = "pr.pl1phpsa.l1o9.5016000.4_00"
    # data_path = "/home/rhashmani/Files/ECAL/datasets/ROOT/pr.pl1phpsa.l1o9.5016000.4_00_eosams3"  # no. of events
    # no_of_protons = dataset_counter_min(data_name, data_path)
    # print("Number of protons: {}--------------------------------------------------".format(no_of_protons))

    # data_name = "pr.pl1phpsa.l1o9.5016000.4_00"
    # data_path = "/home/rhashmani/Files/ECAL/datasets/ROOT/proton_debug"  # no. of events
    # no_of_protons = dataset_counter(data_name, data_path)
    # print("Number of protons: {}--------------------------------------------------".format(no_of_protons))

    data_name = "pos180"
    data_path = "/home/rhashmani/Files/ECAL/datasets/ROOT/pos180"  # no. of events
    no_of_protons = dataset_counter_min(data_name, data_path, 9)
    print("Number of protons: {}--------------------------------------------------".format(no_of_protons))

if __name__ == "__main__":
    main()