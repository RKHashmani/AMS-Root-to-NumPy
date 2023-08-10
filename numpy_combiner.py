"""
Run after root_to_numpy_script.sh
Combines numerous .npz files into a single npz file. To be used later with combined_numpy_to_particle_dataset.py

Author: Raheem Hashmani

"""

import time
import argparse
import numpy as np
import glob

# To parse arguments:
parser = argparse.ArgumentParser()
parser.add_argument('--data_name', type=str,
                        choices=['el.pl1.2004000', 'pr.pl1phpsa.l1o9.5016000.4_00', 'el.pl1.0_25200',
                                 'ISS.B1236_pass8'], help='ROOT Dataset Name')
parser.add_argument('-e', '--energy_range', type=str, choices=['2001000', '10002000', None], help='Energy Range')
parser = parser.parse_args()

start_time = time.time()

print("Dataset chosen:", parser.data_name)
print("Energy Range chosen:", parser.energy_range)

directory = "../../../datasets/in_progress/ISS"
if parser.energy_range is None:
    subdir = parser.data_name
else:
    subdir = parser.data_name + "_" + parser.energy_range

print("Save Location:", directory + "/" + subdir + "_all_x.npz")

npzfiles = glob.glob(directory + "/" + subdir + "/*.npz")
npzfiles.sort()
all_arrays = []
print_freq_iterations = 10
for i, npzfile in enumerate(npzfiles):
    if (i + 1) % (len(list(npzfiles)) // print_freq_iterations) == 0:
        print(f"Progress: [Step [{i + 1}/{len(list(npzfiles))}]")
        print("------------------------------", flush=True)
    all_arrays.append(np.load(npzfile)['x'])

x = np.concatenate(all_arrays)
print(f"Saving to {directory}/{subdir}_all_x.npz")
np.savez(directory + "/" + subdir + "_all_x", x=x)

print("DONE!")
