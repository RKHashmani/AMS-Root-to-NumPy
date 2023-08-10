########################################
#
# Use with root_to_numpy_script.sh
# Author: Raheem Hashmani
#
########################################


import time
import argparse
import ROOT
import numpy as np

from likelihood_helpers import edep_2d_to_3d


def main():
    #  To parse arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_name', type=str,
                        choices=['el.pl1.2004000', 'pr.pl1phpsa.l1o9.5016000.4_00', 'el.pl1.0_25200',
                                 'ISS.B1236_pass8'], help='ROOT Dataset Name')
    parser.add_argument('--data_path', help='Path to dataset directory')
    parser.add_argument('--iter', type=int, help='Iteration_Number')
    parser = parser.parse_args()

    # ROOT Dataset Name:
    print("Chosen ROOT Dataset:", parser.data_name)
    # path to dataset
    print("Directory of ROOT Files:", parser.data_path)

    is_final_iter = final_iter_check(parser.data_name, parser.iter)

    batch_size = 10000

    # Iteration No.
    iteration = parser.iter
    print("Current Iteration:", iteration)
    range_start = iteration * batch_size
    print("iteration Start", range_start)

    if is_final_iter:
        print("Final Iteration Activated")
        range_end = 0  # For Range Function, "0 means that the range goes until the end of the dataset".
    else:
        range_end = (iteration + 1) * batch_size
    print("iteration End", range_end)

    t0 = time.time()

    particles = (ROOT.RDataFrame("t1", parser.data_path + "/" + parser.data_name + "_*.root")
                 .Filter("en3d >= 25 && en3d <= 2000")  # Make sure to do en3d >= 200 && en3d < 1000 for < 1 TeV set and en3d >= 1000 && en3d <= 2000 for > 1 TeV
                 .Range(range_start, range_end, 1)
                 )
    particles = particles.AsNumpy(columns=["edep_cell"])
    edep_cell = np.asarray(particles["edep_cell"])

    no_of_events = edep_cell.size
    print(f"Total no. of events in this dataset: {no_of_events}---------------------------------------")

    list_3d = []  # Method from: https://stackoverflow.com/questions/48077432/numpy-dstack-for-3d-arrays

    for event in range(0, no_of_events):  # Running till the next batch_size limit.
        edep_cell_event = np.asarray(edep_cell[event]).reshape(18, -1)
        # edep_vec = edep_2d_to_3d(edep_cell_event)  # To convert 18x72 to 2x18x72
        edep_vec = np.expand_dims(edep_cell_event, axis=0)  # To convert 18x72 to 1x18x72
        list_3d.append(edep_vec)
    edep_cell_stacked = np.stack(list_3d)
    edep_cell_stacked = edep_cell_stacked.astype('float32')
    np.savez_compressed(
        '../../../datasets/in_progress/ISS/' + parser.data_name + '/' + parser.data_name + '_' +
        str(iteration).zfill(4), x=edep_cell_stacked)
    print("DONE with iteration:" + str(iteration) + "! Time taken:", time.time() - t0)


def final_iter_check (data_name, iteration):
    if data_name == 'el.pl1.2004000':
        final_iter = 445
    elif data_name == 'pr.pl1phpsa.l1o9.5016000.4_00':
        final_iter = 457
    elif data_name == 'el.pl1.0_25200':
        final_iter = 778
    elif data_name == 'ISS.B1236_pass8':
        final_iter = 1238
    else:
        print("Data Name not found!")
        return None

    return iteration == final_iter


if __name__ == "__main__":
    main()
