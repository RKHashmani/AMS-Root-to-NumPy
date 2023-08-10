"""
This script takes in a train/val/test dataset and creates 2 new datasets, one for each particle.
"""

import os
import time
import argparse
import numpy as np

# Variables to Fill In
events_directory = "../../datasets/200600_rec_GeV/"
dataset_type = "events_test.npz"
new_dir_location = "../../datasets/200600_rec_GeV/events_test_particles/"

t0 = time.time()
x = np.load(events_directory + dataset_type)["x"]
y = np.load(events_directory + dataset_type)["y"]
mom = np.load(events_directory + dataset_type)["mom"]
en3d = np.load(events_directory + dataset_type)["en3d"]
EcalEMlhd = np.load(events_directory + dataset_type)["EcalEMlhd"]
ecal3dbdt = np.load(events_directory + dataset_type)["ecal3dbdt"]
print("Time taken to load", dataset_type, "dataset:", time.time() - t0)

# Protons Split:
p_x = x[y == 0]
p_y = y[y == 0]
p_mom = mom[y == 0]
p_en3d = en3d[y == 0]
p_EcalEMlhd = EcalEMlhd[y == 0]
p_ecal3dbdt = ecal3dbdt[y == 0]

# Electrons Split:
e_x = x[y == 1]
e_y = y[y == 1]
e_mom = mom[y == 1]
e_en3d = en3d[y == 1]
e_EcalEMlhd = EcalEMlhd[y == 1]
e_ecal3dbdt = ecal3dbdt[y == 1]

# Saving

np.savez(new_dir_location + "protons", x=p_x, y=p_y, mom=p_mom, en3d=p_en3d, EcalEMlhd=p_EcalEMlhd, ecal3dbdt=p_ecal3dbdt)
print("Done Protons")
np.savez(new_dir_location + "electrons", x=e_x, y=e_y, mom=e_mom, en3d=e_en3d, EcalEMlhd=e_EcalEMlhd, ecal3dbdt=e_ecal3dbdt)
print("Done Electrons")
