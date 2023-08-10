"""
To create smaller datasets.
"""

import time
import numpy as np
import sys
from sklearn.model_selection import StratifiedShuffleSplit
sys.path.append("..")
from directory_check import directory_check


def smaller_dataset_maker(source_dir, target_dir, dataset_type, amount):

    directory_check(target_dir)

    particles = np.load(source_dir + "/" + dataset_type + ".npz")

    x = particles["x"]
    y = particles["y"]
    EcalEMlhd = particles["EcalEMlhd"]
    ecal3dbdt = particles["ecal3dbdt"]
    mom = particles["mom"]
    en3d = particles["en3d"]
    Trk_Ecal_Inci_X = particles["Trk_Ecal_Inci_X"]
    Trk_Ecal_Inci_Y = particles["Trk_Ecal_Inci_Y"]
    Trk_Ecal_Inci_Z = particles["Trk_Ecal_Inci_Z"]
    Trk_Ecal_Inci_Zenith = particles["Trk_Ecal_Inci_Zenith"]
    Trk_Ecal_Inci_Azimutal = particles["Trk_Ecal_Inci_Azimutal"]
    Ecal_ShwrX0 = particles["Ecal_ShwrX0"]
    Ecal_ShwrY0 = particles["Ecal_ShwrY0"]
    Ecal_ShwrZ0 = particles["Ecal_ShwrZ0"]
    Ecal_Zenith = particles["Ecal_Zenith"]
    Ecal_Azimutal = particles["Ecal_Azimutal"]
    Ecal_ShwrE0 = particles["Ecal_ShwrE0"]
    Ecal_ShwrA0 = particles["Ecal_ShwrA0"]

    print("First StratifiedShuffleSplit")
    sss = StratifiedShuffleSplit(n_splits=10, test_size=amount, random_state=0)
    sss.get_n_splits(x, y)

    for i, (train_index, test_index) in enumerate(sss.split(x, y)):
        print("iteration:", i, "TRAIN:", train_index, "TEST:", test_index)
        if i == 9:
            x_train, x_temp = x[train_index], x[test_index]
            y_train, y_temp = y[train_index], y[test_index]
            EcalEMlhd_train, EcalEMlhd_temp = EcalEMlhd[train_index], EcalEMlhd[test_index]
            ecal3dbdt_train, ecal3dbdt_temp = ecal3dbdt[train_index], ecal3dbdt[test_index]
            mom_train, mom_temp = mom[train_index], mom[test_index]
            en3d_train, en3d_temp = en3d[train_index], en3d[test_index]
            Trk_Ecal_Inci_X_train, Trk_Ecal_Inci_X_temp = Trk_Ecal_Inci_X[train_index], Trk_Ecal_Inci_X[test_index]
            Trk_Ecal_Inci_Y_train, Trk_Ecal_Inci_Y_temp = Trk_Ecal_Inci_Y[train_index], Trk_Ecal_Inci_Y[test_index]
            Trk_Ecal_Inci_Z_train, Trk_Ecal_Inci_Z_temp = Trk_Ecal_Inci_Z[train_index], Trk_Ecal_Inci_Z[test_index]
            Trk_Ecal_Inci_Zenith_train, Trk_Ecal_Inci_Zenith_temp = Trk_Ecal_Inci_Zenith[train_index], Trk_Ecal_Inci_Zenith[test_index]
            Trk_Ecal_Inci_Azimutal_train, Trk_Ecal_Inci_Azimutal_temp = Trk_Ecal_Inci_Azimutal[train_index], Trk_Ecal_Inci_Azimutal[test_index]
            Ecal_ShwrX0_train, Ecal_ShwrX0_temp = Ecal_ShwrX0[train_index], Ecal_ShwrX0[test_index]
            Ecal_ShwrY0_train, Ecal_ShwrY0_temp = Ecal_ShwrY0[train_index], Ecal_ShwrY0[test_index]
            Ecal_ShwrZ0_train, Ecal_ShwrZ0_temp = Ecal_ShwrZ0[train_index], Ecal_ShwrZ0[test_index]
            Ecal_Zenith_train, Ecal_Zenith_temp = Ecal_Zenith[train_index], Ecal_Zenith[test_index]
            Ecal_Azimutal_train, Ecal_Azimutal_temp = Ecal_Azimutal[train_index], Ecal_Azimutal[test_index]
            Ecal_ShwrE0_train, Ecal_ShwrE0_temp = Ecal_ShwrE0[train_index], Ecal_ShwrE0[test_index]
            Ecal_ShwrA0_train, Ecal_ShwrA0_temp = Ecal_ShwrA0[train_index], Ecal_ShwrA0[test_index]

    print(f"Number of events discarded:{x_train.shape}")
    print(f"Number of events being saving: {x_temp.shape}")
    print(f"Number of Protons being saving: {y_temp[y_temp==0].shape}")
    print(f"Number of Electrons being saving: {y_temp[y_temp==1].shape}")

    np.savez(target_dir + "/" + dataset_type, x=x_temp, y=y_temp,
             mom=mom_temp, en3d=en3d_temp, EcalEMlhd=EcalEMlhd_temp, ecal3dbdt=ecal3dbdt_temp,
             Trk_Ecal_Inci_X=Trk_Ecal_Inci_X_temp, Trk_Ecal_Inci_Y=Trk_Ecal_Inci_Y_temp,
             Trk_Ecal_Inci_Z=Trk_Ecal_Inci_Z_temp,
             Trk_Ecal_Inci_Zenith=Trk_Ecal_Inci_Zenith_temp, Trk_Ecal_Inci_Azimutal=Trk_Ecal_Inci_Azimutal_temp,
             Ecal_ShwrX0=Ecal_ShwrX0_temp, Ecal_ShwrY0=Ecal_ShwrY0_temp, Ecal_ShwrZ0=Ecal_ShwrZ0_temp,
             Ecal_Zenith=Ecal_Zenith_temp, Ecal_Azimutal=Ecal_Azimutal_temp,
             Ecal_ShwrE0=Ecal_ShwrE0_temp, Ecal_ShwrA0=Ecal_ShwrA0_temp)

    np.savez(target_dir + "/" + "remaining_train", x=x_train, y=y_train,
             mom=mom_train, en3d=en3d_train, EcalEMlhd=EcalEMlhd_train, ecal3dbdt=ecal3dbdt_train,
             Trk_Ecal_Inci_X=Trk_Ecal_Inci_X_train, Trk_Ecal_Inci_Y=Trk_Ecal_Inci_Y_train,
             Trk_Ecal_Inci_Z=Trk_Ecal_Inci_Z_train,
             Trk_Ecal_Inci_Zenith=Trk_Ecal_Inci_Zenith_train, Trk_Ecal_Inci_Azimutal=Trk_Ecal_Inci_Azimutal_train,
             Ecal_ShwrX0=Ecal_ShwrX0_train, Ecal_ShwrY0=Ecal_ShwrY0_train, Ecal_ShwrZ0=Ecal_ShwrZ0_train,
             Ecal_Zenith=Ecal_Zenith_train, Ecal_Azimutal=Ecal_Azimutal_train,
             Ecal_ShwrE0=Ecal_ShwrE0_train, Ecal_ShwrA0=Ecal_ShwrA0_train)
    print("Done Test")


def main():
    source_dir = "../../../../../../shared/datasets/rhashmani/0.05_mixed_1ch_train2001000_val2002000_test10002000"
    target_dir = "../../../../../../shared/datasets/rhashmani/0.05_mixed_1ch_train2001000_val2002000_test10002000/WIP"
    dataset_type = "remaining_0.95_train"
    amount = 0.3750257179  # 5% of the data

    smaller_dataset_maker(source_dir, target_dir, dataset_type, amount)


if __name__ == "__main__":
    main()
