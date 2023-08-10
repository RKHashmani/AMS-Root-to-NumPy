"""
Please run combined_numpy_to_particle_dataset.py first to generate all "total.npz" datasets for protons and electrons.

Author: Raheem Hashmani

"""

import time
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

electrons = np.load("../../../datasets/in_progress/split_particles/trk_var_2001000/electrons_total.npz")
print("electrons loaded")
protons = np.load("../../../datasets/in_progress/split_particles/trk_var_2001000/protons_total.npz")
print("protons loaded")

x = np.concatenate((electrons["x"], protons["x"]))
print("x concatenated")
y = np.concatenate((electrons["y"], protons["y"]))
EcalEMlhd = np.concatenate((electrons["EcalEMlhd"], protons["EcalEMlhd"]))
ecal3dbdt = np.concatenate((electrons["ecal3dbdt"], protons["ecal3dbdt"]))
mom = np.concatenate((electrons["mom"], protons["mom"]))
en3d = np.concatenate((electrons["en3d"], protons["en3d"]))
Trk_Ecal_Inci_X = np.concatenate((electrons["Trk_Ecal_Inci_X"], protons["Trk_Ecal_Inci_X"]))
Trk_Ecal_Inci_Y = np.concatenate((electrons["Trk_Ecal_Inci_Y"], protons["Trk_Ecal_Inci_Y"]))
Trk_Ecal_Inci_Z = np.concatenate((electrons["Trk_Ecal_Inci_Z"], protons["Trk_Ecal_Inci_Z"]))
Trk_Ecal_Inci_Zenith = np.concatenate((electrons["Trk_Ecal_Inci_Zenith"], protons["Trk_Ecal_Inci_Zenith"]))
Trk_Ecal_Inci_Azimutal = np.concatenate((electrons["Trk_Ecal_Inci_Azimutal"], protons["Trk_Ecal_Inci_Azimutal"]))
Ecal_ShwrX0 = np.concatenate((electrons["Ecal_ShwrX0"], protons["Ecal_ShwrX0"]))
Ecal_ShwrY0 = np.concatenate((electrons["Ecal_ShwrY0"], protons["Ecal_ShwrY0"]))
Ecal_ShwrZ0 = np.concatenate((electrons["Ecal_ShwrZ0"], protons["Ecal_ShwrZ0"]))
Ecal_Zenith = np.concatenate((electrons["Ecal_Zenith"], protons["Ecal_Zenith"]))
Ecal_Azimutal = np.concatenate((electrons["Ecal_Azimutal"], protons["Ecal_Azimutal"]))
Ecal_ShwrE0 = np.concatenate((electrons["Ecal_ShwrE0"], protons["Ecal_ShwrE0"]))
Ecal_ShwrA0 = np.concatenate((electrons["Ecal_ShwrA0"], protons["Ecal_ShwrA0"]))


del protons, electrons
# split_type = "3-way"  # (60/20/20 Split)
split_type = "2-way"  # (50/50 Split)
print("Split Type:", split_type)

if split_type == "3-way":
    print("First StratifiedShuffleSplit")
    sss = StratifiedShuffleSplit(test_size=0.4, random_state=0)
    sss.get_n_splits(x, y)
    for train_index, test_index in sss.split(x, y):
        print("TRAIN:", train_index, "TEST:", test_index)
        x_train, x_temp = x[train_index], x[test_index]
        y_train, y_temp = y[train_index], y[test_index]
        EcalEMlhd_train, EcalEMlhd_temp = EcalEMlhd[train_index], EcalEMlhd[test_index]
        ecal3dbdt_train, ecal3dbdt_temp = ecal3dbdt[train_index], ecal3dbdt[test_index]
        mom_train, mom_temp = mom[train_index], mom[test_index]
        en3d_train, en3d_temp = en3d[train_index], en3d[test_index]

    del x, y, EcalEMlhd, ecal3dbdt, mom, en3d

    print("Second StratifiedShuffleSplit")
    sss2 = StratifiedShuffleSplit(test_size=0.5, random_state=0)
    sss2.get_n_splits(x_temp, y_temp)
    for train_index, test_index in sss2.split(x_temp, y_temp):
        print("TRAIN:", train_index, "TEST:", test_index)
        x_test, x_val = x_temp[train_index], x_temp[test_index]
        y_test, y_val = y_temp[train_index], y_temp[test_index]
        EcalEMlhd_test, EcalEMlhd_val = EcalEMlhd_temp[train_index], EcalEMlhd_temp[test_index]
        ecal3dbdt_test, ecal3dbdt_val = ecal3dbdt_temp[train_index], ecal3dbdt_temp[test_index]
        mom_test, mom_val = mom_temp[train_index], mom_temp[test_index]
        en3d_test, en3d_val = en3d_temp[train_index], en3d_temp[test_index]

    print(x_train.shape)
    print(x_val.shape)
    print(x_test.shape)

    np.savez("../datasets/200600_rec_GeV/events_train", x=x_train, y=y_train, mom=mom_train, en3d=en3d_train,
             EcalEMlhd=EcalEMlhd_train, ecal3dbdt=ecal3dbdt_train)
    print("Done Train")
    np.savez("../datasets/200600_rec_GeV/events_val", x=x_val, y=y_val, mom=mom_val, en3d=en3d_val,
             EcalEMlhd=EcalEMlhd_val, ecal3dbdt=ecal3dbdt_val)
    print("Done Val")
    np.savez("../datasets/200600_rec_GeV/events_test", x=x_test, y=y_test, mom=mom_test, en3d=en3d_test,
             EcalEMlhd=EcalEMlhd_test, ecal3dbdt=ecal3dbdt_test)
    print("Done Test")

elif split_type == "2-way":
    print("First StratifiedShuffleSplit")
    sss = StratifiedShuffleSplit(n_splits=10, test_size=0.5, random_state=0)
    sss.get_n_splits(x, y)
    # for train_index, test_index in sss.split(x, y):
    #     print("TRAIN:", train_index, "TEST:", test_index)
    #     x_train, x_temp = x[train_index], x[test_index]
    #     y_train, y_temp = y[train_index], y[test_index]
    #     EcalEMlhd_train, EcalEMlhd_temp = EcalEMlhd[train_index], EcalEMlhd[test_index]
    #     ecal3dbdt_train, ecal3dbdt_temp = ecal3dbdt[train_index], ecal3dbdt[test_index]
    #     mom_train, mom_temp = mom[train_index], mom[test_index]
    #     en3d_train, en3d_temp = en3d[train_index], en3d[test_index]

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


    print(x_train.shape)
    print(x_temp.shape)

    np.savez("../../../datasets/trk_var_2001000/events_train", x=x_train, y=y_train,
             mom=mom_train, en3d=en3d_train, EcalEMlhd=EcalEMlhd_train, ecal3dbdt=ecal3dbdt_train,
             Trk_Ecal_Inci_X=Trk_Ecal_Inci_X_train, Trk_Ecal_Inci_Y=Trk_Ecal_Inci_Y_train, Trk_Ecal_Inci_Z=Trk_Ecal_Inci_Z_train,
             Trk_Ecal_Inci_Zenith=Trk_Ecal_Inci_Zenith_train, Trk_Ecal_Inci_Azimutal=Trk_Ecal_Inci_Azimutal_train,
             Ecal_ShwrX0=Ecal_ShwrX0_train, Ecal_ShwrY0=Ecal_ShwrY0_train, Ecal_ShwrZ0=Ecal_ShwrZ0_train,
             Ecal_Zenith=Ecal_Zenith_train, Ecal_Azimutal=Ecal_Azimutal_train,
             Ecal_ShwrE0=Ecal_ShwrE0_train, Ecal_ShwrA0=Ecal_ShwrA0_train)
    print("Done Train")
    np.savez("../../../datasets/trk_var_2001000/events_test", x=x_temp, y=y_temp,
             mom=mom_temp, en3d=en3d_temp, EcalEMlhd=EcalEMlhd_temp, ecal3dbdt=ecal3dbdt_temp,
             Trk_Ecal_Inci_X=Trk_Ecal_Inci_X_temp, Trk_Ecal_Inci_Y=Trk_Ecal_Inci_Y_temp, Trk_Ecal_Inci_Z=Trk_Ecal_Inci_Z_temp,
             Trk_Ecal_Inci_Zenith=Trk_Ecal_Inci_Zenith_temp, Trk_Ecal_Inci_Azimutal=Trk_Ecal_Inci_Azimutal_temp,
             Ecal_ShwrX0=Ecal_ShwrX0_temp, Ecal_ShwrY0=Ecal_ShwrY0_temp, Ecal_ShwrZ0=Ecal_ShwrZ0_temp,
             Ecal_Zenith=Ecal_Zenith_temp, Ecal_Azimutal=Ecal_Azimutal_temp,
             Ecal_ShwrE0=Ecal_ShwrE0_temp, Ecal_ShwrA0=Ecal_ShwrA0_temp)
    print("Done Test")

