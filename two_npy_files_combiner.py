import numpy as np


def two_file_combiner(below_1_TeV_dir, above_1_TeV_dir, target_dir):

    below_1_TeV = np.load(below_1_TeV_dir)

    x_below_1_TeV = below_1_TeV["x"]
    y_below_1_TeV = below_1_TeV["y"]
    EcalEMlhd_below_1_TeV = below_1_TeV["EcalEMlhd"]
    ecal3dbdt_below_1_TeV = below_1_TeV["ecal3dbdt"]
    mom_below_1_TeV = below_1_TeV["mom"]
    en3d_below_1_TeV = below_1_TeV["en3d"]
    Trk_Ecal_Inci_X_below_1_TeV = below_1_TeV["Trk_Ecal_Inci_X"]
    Trk_Ecal_Inci_Y_below_1_TeV = below_1_TeV["Trk_Ecal_Inci_Y"]
    Trk_Ecal_Inci_Z_below_1_TeV = below_1_TeV["Trk_Ecal_Inci_Z"]
    Trk_Ecal_Inci_Zenith_below_1_TeV = below_1_TeV["Trk_Ecal_Inci_Zenith"]
    Trk_Ecal_Inci_Azimutal_below_1_TeV = below_1_TeV["Trk_Ecal_Inci_Azimutal"]
    Ecal_ShwrX0_below_1_TeV = below_1_TeV["Ecal_ShwrX0"]
    Ecal_ShwrY0_below_1_TeV = below_1_TeV["Ecal_ShwrY0"]
    Ecal_ShwrZ0_below_1_TeV = below_1_TeV["Ecal_ShwrZ0"]
    Ecal_Zenith_below_1_TeV = below_1_TeV["Ecal_Zenith"]
    Ecal_Azimutal_below_1_TeV = below_1_TeV["Ecal_Azimutal"]
    Ecal_ShwrE0_below_1_TeV = below_1_TeV["Ecal_ShwrE0"]
    Ecal_ShwrA0_below_1_TeV = below_1_TeV["Ecal_ShwrA0"]

    above_1_TeV = np.load(above_1_TeV_dir)

    x_above_1_TeV = above_1_TeV["x"]
    y_above_1_TeV = above_1_TeV["y"]
    EcalEMlhd_above_1_TeV = above_1_TeV["EcalEMlhd"]
    ecal3dbdt_above_1_TeV = above_1_TeV["ecal3dbdt"]
    mom_above_1_TeV = above_1_TeV["mom"]
    en3d_above_1_TeV = above_1_TeV["en3d"]
    Trk_Ecal_Inci_X_above_1_TeV = above_1_TeV["Trk_Ecal_Inci_X"]
    Trk_Ecal_Inci_Y_above_1_TeV = above_1_TeV["Trk_Ecal_Inci_Y"]
    Trk_Ecal_Inci_Z_above_1_TeV = above_1_TeV["Trk_Ecal_Inci_Z"]
    Trk_Ecal_Inci_Zenith_above_1_TeV = above_1_TeV["Trk_Ecal_Inci_Zenith"]
    Trk_Ecal_Inci_Azimutal_above_1_TeV = above_1_TeV["Trk_Ecal_Inci_Azimutal"]
    Ecal_ShwrX0_above_1_TeV = above_1_TeV["Ecal_ShwrX0"]
    Ecal_ShwrY0_above_1_TeV = above_1_TeV["Ecal_ShwrY0"]
    Ecal_ShwrZ0_above_1_TeV = above_1_TeV["Ecal_ShwrZ0"]
    Ecal_Zenith_above_1_TeV = above_1_TeV["Ecal_Zenith"]
    Ecal_Azimutal_above_1_TeV = above_1_TeV["Ecal_Azimutal"]
    Ecal_ShwrE0_above_1_TeV = above_1_TeV["Ecal_ShwrE0"]
    Ecal_ShwrA0_above_1_TeV = above_1_TeV["Ecal_ShwrA0"]

    x = np.concatenate((x_below_1_TeV, x_above_1_TeV))
    y = np.concatenate((y_below_1_TeV, y_above_1_TeV))
    EcalEMlhd = np.concatenate((EcalEMlhd_below_1_TeV, EcalEMlhd_above_1_TeV))
    ecal3dbdt = np.concatenate((ecal3dbdt_below_1_TeV, ecal3dbdt_above_1_TeV))
    mom = np.concatenate((mom_below_1_TeV, mom_above_1_TeV))
    en3d = np.concatenate((en3d_below_1_TeV, en3d_above_1_TeV))
    Trk_Ecal_Inci_X = np.concatenate((Trk_Ecal_Inci_X_below_1_TeV, Trk_Ecal_Inci_X_above_1_TeV))
    Trk_Ecal_Inci_Y = np.concatenate((Trk_Ecal_Inci_Y_below_1_TeV, Trk_Ecal_Inci_Y_above_1_TeV))
    Trk_Ecal_Inci_Z = np.concatenate((Trk_Ecal_Inci_Z_below_1_TeV, Trk_Ecal_Inci_Z_above_1_TeV))
    Trk_Ecal_Inci_Zenith = np.concatenate((Trk_Ecal_Inci_Zenith_below_1_TeV, Trk_Ecal_Inci_Zenith_above_1_TeV))
    Trk_Ecal_Inci_Azimutal = np.concatenate((Trk_Ecal_Inci_Azimutal_below_1_TeV, Trk_Ecal_Inci_Azimutal_above_1_TeV))
    Ecal_ShwrX0 = np.concatenate((Ecal_ShwrX0_below_1_TeV, Ecal_ShwrX0_above_1_TeV))
    Ecal_ShwrY0 = np.concatenate((Ecal_ShwrY0_below_1_TeV, Ecal_ShwrY0_above_1_TeV))
    Ecal_ShwrZ0 = np.concatenate((Ecal_ShwrZ0_below_1_TeV, Ecal_ShwrZ0_above_1_TeV))
    Ecal_Zenith = np.concatenate((Ecal_Zenith_below_1_TeV, Ecal_Zenith_above_1_TeV))
    Ecal_Azimutal = np.concatenate((Ecal_Azimutal_below_1_TeV, Ecal_Azimutal_above_1_TeV))
    Ecal_ShwrE0 = np.concatenate((Ecal_ShwrE0_below_1_TeV, Ecal_ShwrE0_above_1_TeV))
    Ecal_ShwrA0 = np.concatenate((Ecal_ShwrA0_below_1_TeV, Ecal_ShwrA0_above_1_TeV))

    np.savez(target_dir + "/" + "events_val", x=x, y=y,
             mom=mom, en3d=en3d, EcalEMlhd=EcalEMlhd, ecal3dbdt=ecal3dbdt,
             Trk_Ecal_Inci_X=Trk_Ecal_Inci_X, Trk_Ecal_Inci_Y=Trk_Ecal_Inci_Y,
             Trk_Ecal_Inci_Z=Trk_Ecal_Inci_Z,
             Trk_Ecal_Inci_Zenith=Trk_Ecal_Inci_Zenith, Trk_Ecal_Inci_Azimutal=Trk_Ecal_Inci_Azimutal,
             Ecal_ShwrX0=Ecal_ShwrX0, Ecal_ShwrY0=Ecal_ShwrY0, Ecal_ShwrZ0=Ecal_ShwrZ0,
             Ecal_Zenith=Ecal_Zenith, Ecal_Azimutal=Ecal_Azimutal,
             Ecal_ShwrE0=Ecal_ShwrE0, Ecal_ShwrA0=Ecal_ShwrA0)


def main():
    below_1_TeV = "../../../../../../shared/datasets/rhashmani/0.05_mixed_1ch_train2001000_val2002000_test10002000/WIP/below_1_TeV_events_val.npz"
    above_1_TeV = "../../../../../../shared/datasets/rhashmani/0.05_mixed_1ch_train2001000_val2002000_test10002000/WIP/above_1_TeV_events_val.npz"
    target_dir = "../../../../../../shared/datasets/rhashmani/0.05_mixed_1ch_train2001000_val2002000_test10002000/WIP"

    two_file_combiner(below_1_TeV, above_1_TeV, target_dir)


if __name__ == "__main__":
    main()