"""
This script is designed to take in events_train.npz, events_val.npz, or events_test.npz files which are structured
as [batch_size, 2, 18, 72] and turn them into single channel images, [batch_size, 1, 18, 72], combining the ZY and ZX
layers into 1.
"""

import numpy as np
from likelihood_helpers import edep_3d_to_2d


def one_channel_maker(dataset_name, extension, data_dir, save_dir):
    """
    Takes in strings to find dataset structured as [batch_size, 2, 18, 72], then combines the 2 channels to create a
    structure [batch_size, 1, 18, 72]. Finally, saves this structure into the save_dir.

    :param dataset_name: String of the name of the dataset, e.g. "events_train"
    :param extension: String of file extension, e.g. ".npz"
    :param data_dir: Location of original dataset, e.g. "../../datasets/berk_train2001000_val10002000/"
    :param save_dir: Where to save the new 1 Channel dataset, e.g. "../../datasets/1channel_train2001000_val10002000/"
    :return: Nothing
    """
    dataset = np.load(data_dir + dataset_name + extension)
    x = dataset['x']
    x_1channel = edep_3d_to_2d(x)
    print(f"The shape of the output is {x_1channel.shape}.")
    np.savez(save_dir + dataset_name, x=x_1channel, y=dataset['y'], mom=dataset['mom'], en3d=dataset['en3d'],
             EcalEMlhd=dataset['EcalEMlhd'], ecal3dbdt=dataset['ecal3dbdt'])
    print("Done!")


def main():
    data_dir = "../../datasets/berk_train2001000_val10002000/"
    save_dir = "../../datasets/1channel_train2001000_val10002000/"

    # one_channel_maker("events_train", ".npz", data_dir, save_dir)
    # one_channel_maker("events_val", ".npz", data_dir, save_dir)
    # one_channel_maker("events_test", ".npz", data_dir, save_dir)

    data_dir = "../../datasets/test2001000/"
    save_dir = "../../datasets/1channel_test2001000/"
    one_channel_maker("events_test", ".npz", data_dir, save_dir)


if __name__ == "__main__":
    main()
