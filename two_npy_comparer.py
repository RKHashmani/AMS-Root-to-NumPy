import numpy as np


def two_file_combiner(set_1_dir, set_2_dir):

    set_1 = np.load(set_1_dir)

    x_set_1 = set_1["x"]
    # y_set_1 = set_1["y"]
    # EcalEMlhd_set_1 = set_1["EcalEMlhd"]
    # ecal3dbdt_set_1 = set_1["ecal3dbdt"]
    # mom_set_1 = set_1["mom"]
    # en3d_set_1 = set_1["en3d"]
    # Trk_Ecal_Inci_X_set_1 = set_1["Trk_Ecal_Inci_X"]
    # Trk_Ecal_Inci_Y_set_1 = set_1["Trk_Ecal_Inci_Y"]
    # Trk_Ecal_Inci_Z_set_1 = set_1["Trk_Ecal_Inci_Z"]
    # Trk_Ecal_Inci_Zenith_set_1 = set_1["Trk_Ecal_Inci_Zenith"]
    # Trk_Ecal_Inci_Azimutal_set_1 = set_1["Trk_Ecal_Inci_Azimutal"]
    # Ecal_ShwrX0_set_1 = set_1["Ecal_ShwrX0"]
    # Ecal_ShwrY0_set_1 = set_1["Ecal_ShwrY0"]
    # Ecal_ShwrZ0_set_1 = set_1["Ecal_ShwrZ0"]
    # Ecal_Zenith_set_1 = set_1["Ecal_Zenith"]
    # Ecal_Azimutal_set_1 = set_1["Ecal_Azimutal"]
    # Ecal_ShwrE0_set_1 = set_1["Ecal_ShwrE0"]
    # Ecal_ShwrA0_set_1 = set_1["Ecal_ShwrA0"]

    set_2 = np.load(set_2_dir)

    x_set_2 = set_2["x"]
    # y_set_2 = set_2["y"]
    # EcalEMlhd_set_2 = set_2["EcalEMlhd"]
    # ecal3dbdt_set_2 = set_2["ecal3dbdt"]
    # mom_set_2 = set_2["mom"]
    # en3d_set_2 = set_2["en3d"]
    # Trk_Ecal_Inci_X_set_2 = set_2["Trk_Ecal_Inci_X"]
    # Trk_Ecal_Inci_Y_set_2 = set_2["Trk_Ecal_Inci_Y"]
    # Trk_Ecal_Inci_Z_set_2 = set_2["Trk_Ecal_Inci_Z"]
    # Trk_Ecal_Inci_Zenith_set_2 = set_2["Trk_Ecal_Inci_Zenith"]
    # Trk_Ecal_Inci_Azimutal_set_2 = set_2["Trk_Ecal_Inci_Azimutal"]
    # Ecal_ShwrX0_set_2 = set_2["Ecal_ShwrX0"]
    # Ecal_ShwrY0_set_2 = set_2["Ecal_ShwrY0"]
    # Ecal_ShwrZ0_set_2 = set_2["Ecal_ShwrZ0"]
    # Ecal_Zenith_set_2 = set_2["Ecal_Zenith"]
    # Ecal_Azimutal_set_2 = set_2["Ecal_Azimutal"]
    # Ecal_ShwrE0_set_2 = set_2["Ecal_ShwrE0"]
    # Ecal_ShwrA0_set_2 = set_2["Ecal_ShwrA0"]

    print(f"Are the x values the same? {np.array_equal(x_set_1, x_set_2)}")



def main():
    # set_1 = "../../../datasets/in_progress/ISS/ISS.B1236_pass8/ISS.B1236_pass8_421_test.npz"
    # set_2 = "../../../datasets/in_progress/ISS/ISS.B1236_pass8/ISS.B1236_pass8_0421.npz"

    set_1 = "../../../../../../shared/datasets/rhashmani/generated_GeV/2ch_200600/events_train.npz"
    set_2 = "../../../../../../shared/datasets/rhashmani/generated_GeV/2ch_200600/events_test.npz"

    two_file_combiner(set_1, set_2)


if __name__ == "__main__":
    main()