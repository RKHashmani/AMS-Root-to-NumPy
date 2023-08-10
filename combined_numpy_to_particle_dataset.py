"""
Please run numpy_combiner.py first to generate all x dataset.
Run this to make "total.npz" datasets for Protons and Electrons containing x, y, en3d, etc

Author: Raheem Hashmani

"""

import ROOT
import numpy as np
import time
import argparse

# To parse arguments:
parser = argparse.ArgumentParser()
parser.add_argument('--particle', type=str, choices=['electron', 'proton', None], help='Particle Type')
parser.add_argument('--data_name', type=str,
                        choices=['el.pl1.2004000', 'pr.pl1phpsa.l1o9.5016000.4_00', 'el.pl1.0_25200',
                                 'ISS.B1236_pass8'], help='ROOT Dataset Name')
parser.add_argument('--data_path', help='Path to ROOT dataset directory')
parser.add_argument('-e', '--energy_range', type=str, choices=['2001000', '10002000', None], help='Energy Range')
parser = parser.parse_args()


def root_to_Cond_NumPy(particle, data_path, numpy_data_dir, numpy_all_x_name, split_particle_dataset_sav_dir, data_name,
                       energy_range):
    start_time = time.time()

    if energy_range == "2001000":
        dataset = (ROOT.RDataFrame("t1", data_path + "/" + data_name + "_*.root")
                   .Filter(
            "en3d >= 200 && en3d < 1000")
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
    elif energy_range == "10002000":
        dataset = (ROOT.RDataFrame("t1", data_path + "/" + data_name + "_*.root")
                   .Filter(
            "en3d >= 1000 && en3d <= 2000")
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
    elif energy_range is None:
        dataset = (ROOT.RDataFrame("t1", data_path + "/" + data_name + "_*.root")
                   .Filter("en3d >= 25 && en3d <= 2000")
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
                   .Define("trd_lik_0", "trd_lik[0]")
                   .Define("trd_lik_1", "trd_lik[1]")
                   .Define("trd_lik_2", "trd_lik[2]")
                   .Define("trd_like_0", "trd_like[0]")
                   .Define("trd_like_1", "trd_like[1]")
                   .Define("trd_like_2", "trd_like[2]")
                   .Define("trd_qk_0", "trd_qk[0]")
                   # .Define("trd_qnhk_0", "trd_qnhk[0]")
                   .Define("trd_qrmsk_0", "trd_qrmsk[0]")
                   )
    else:
        print("ERROR: Incorrect Energy Range")

    x = np.load(numpy_data_dir + "/" + numpy_all_x_name)["x"]

    if particle == "proton":
        y = np.zeros(x.shape[0])
    elif particle == "electron":
        y = np.ones(x.shape[0])
    elif particle == None:
        y = np.full(x.shape[0], -1)
    else:
        print("ERROR: Incorrect Particle Type")

    # print("Converting to float32...")
    # x = x.astype('float32')
    # print("Conversion done.")

    dataset = dataset.AsNumpy(columns=["mom",
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
                                       "Ecal_ShwrA0_0",
                                       "trd_lik_0",
                                       "trd_lik_1",
                                       "trd_lik_2",
                                       "trd_like_0",
                                       "trd_like_1",
                                       "trd_like_2",
                                       "IsGoodBeta",
                                       "betaH_pattern",
                                       "Rigidity_proton_fit",
                                       "Rigidity_electron_fit",
                                       "n_trd_rawhits",
                                       "n_Trd_Cluster",
                                       "nTRDseg",
                                       "n_TrdH_Segment",
                                       "n_TrdH_Track",
                                       "N_TRDH_TR_hits",
                                       "e_trdHtrk_LHD",
                                       "prob_e",
                                       "prob_p",
                                       "prob_he",
                                       "TRD_e_likelihood",
                                       "TRD_p_likelihood",
                                       "TRD_he_likelihood",
                                       "GetNCC",
                                       "TRD_charge",
                                       "trd_statk",
                                       "trd_nhitk",
                                       "trd_onhitk",
                                       "trd_oampk",
                                       "trd_qrmsk_0",
                                       # "trd_qnhk_0",
                                       "trd_qk_0"
                                       ])

    print("Time Taken to load Dataset:", time.time() - start_time)

    mom = np.asarray(dataset["mom"])
    en3d = np.asarray(dataset["en3d"])
    ecal3dbdt = np.asarray(dataset["ecal3dbdt"])
    EcalEMlhd = np.asarray(dataset["EcalEMlhd_0"])
    Trk_Ecal_Inci_X = np.asarray(dataset["Trk_Ecal_Inci_X_0"])
    Trk_Ecal_Inci_Y = np.asarray(dataset["Trk_Ecal_Inci_Y_0"])
    Trk_Ecal_Inci_Z = np.asarray(dataset["Trk_Ecal_Inci_Z_0"])
    Trk_Ecal_Inci_Zenith = np.asarray(dataset["Trk_Ecal_Inci_Zenith_0"])
    Trk_Ecal_Inci_Azimutal = np.asarray(dataset["Trk_Ecal_Inci_Azimutal_0"])
    Ecal_ShwrX0 = np.asarray(dataset["Ecal_ShwrX0_0"])
    Ecal_ShwrY0 = np.asarray(dataset["Ecal_ShwrY0_0"])
    Ecal_ShwrZ0 = np.asarray(dataset["Ecal_ShwrZ0_0"])
    Ecal_Zenith = np.asarray(dataset["Ecal_Zenith_0"])
    Ecal_Azimutal = np.asarray(dataset["Ecal_Azimutal_0"])
    Ecal_ShwrE0 = np.asarray(dataset["Ecal_ShwrE0_0"])
    Ecal_ShwrA0 = np.asarray(dataset["Ecal_ShwrA0_0"])
    trd_lik_0 = np.asarray(dataset["trd_lik_0"])
    trd_lik_1 = np.asarray(dataset["trd_lik_1"])
    trd_lik_2 = np.asarray(dataset["trd_lik_2"])
    trd_like_0 = np.asarray(dataset["trd_like_0"])
    trd_like_1 = np.asarray(dataset["trd_like_1"])
    trd_like_2 = np.asarray(dataset["trd_like_2"])
    IsGoodBeta = np.asarray(dataset["IsGoodBeta"])
    betaH_pattern = np.asarray(dataset["betaH_pattern"])
    Rigidity_proton_fit = np.asarray(dataset["Rigidity_proton_fit"])
    Rigidity_electron_fit = np.asarray(dataset["Rigidity_electron_fit"])
    n_trd_rawhits = np.asarray(dataset["n_trd_rawhits"])
    n_Trd_Cluster = np.asarray(dataset["n_Trd_Cluster"])
    nTRDseg = np.asarray(dataset["nTRDseg"])
    n_TrdH_Segment = np.asarray(dataset["n_TrdH_Segment"])
    n_TrdH_Track = np.asarray(dataset["n_TrdH_Track"])
    N_TRDH_TR_hits = np.asarray(dataset["N_TRDH_TR_hits"])
    e_trdHtrk_LHD = np.asarray(dataset["e_trdHtrk_LHD"])
    prob_e = np.asarray(dataset["prob_e"])
    prob_p = np.asarray(dataset["prob_p"])
    prob_he = np.asarray(dataset["prob_he"])
    TRD_e_likelihood = np.asarray(dataset["TRD_e_likelihood"])
    TRD_p_likelihood = np.asarray(dataset["TRD_p_likelihood"])
    TRD_he_likelihood = np.asarray(dataset["TRD_he_likelihood"])
    GetNCC = np.asarray(dataset["GetNCC"])
    TRD_charge = np.asarray(dataset["TRD_charge"])
    trd_statk = np.asarray(dataset["trd_statk"])
    trd_nhitk = np.asarray(dataset["trd_nhitk"])
    trd_onhitk = np.asarray(dataset["trd_onhitk"])
    trd_oampk = np.asarray(dataset["trd_oampk"])
    trd_qrmsk_0 = np.asarray(dataset["trd_qrmsk_0"])
    # trd_qnhk_0 = np.asarray(dataset["trd_qnhk_0"])
    trd_qk_0 = np.asarray(dataset["trd_qk_0"])



    no_of_events = ecal3dbdt.shape[0]
    if particle is not None:
        print("Number of " + particle + "s are: ", no_of_events)
        final_sav = split_particle_dataset_sav_dir + "/" + particle + "s_total"
    else:
        print("Number of particles are: ", no_of_events)
        final_sav = split_particle_dataset_sav_dir + "/ISS_total"


    np.savez(final_sav,
             x=x, y=y, mom=mom, en3d=en3d, ecal3dbdt=ecal3dbdt, EcalEMlhd=EcalEMlhd,
             Trk_Ecal_Inci_X=Trk_Ecal_Inci_X, Trk_Ecal_Inci_Y=Trk_Ecal_Inci_Y, Trk_Ecal_Inci_Z=Trk_Ecal_Inci_Z,
             Trk_Ecal_Inci_Zenith=Trk_Ecal_Inci_Zenith, Trk_Ecal_Inci_Azimutal=Trk_Ecal_Inci_Azimutal,
             Ecal_ShwrX0=Ecal_ShwrX0, Ecal_ShwrY0=Ecal_ShwrY0, Ecal_ShwrZ0=Ecal_ShwrZ0,
             Ecal_Zenith=Ecal_Zenith, Ecal_Azimutal=Ecal_Azimutal,
             Ecal_ShwrE0=Ecal_ShwrE0, Ecal_ShwrA0=Ecal_ShwrA0,
             trd_lik_0=trd_lik_0, trd_lik_1=trd_lik_1, trd_lik_2=trd_lik_2,
             trd_like_0=trd_like_0, trd_like_1=trd_like_1, trd_like_2=trd_like_2,
             IsGoodBeta=IsGoodBeta, betaH_pattern=betaH_pattern,
             Rigidity_proton_fit=Rigidity_proton_fit, Rigidity_electron_fit=Rigidity_electron_fit,
             n_trd_rawhits=n_trd_rawhits, n_Trd_Cluster=n_Trd_Cluster, nTRDseg=nTRDseg,
             n_TrdH_Segment=n_TrdH_Segment, n_TrdH_Track=n_TrdH_Track, N_TRDH_TR_hits=N_TRDH_TR_hits,
             e_trdHtrk_LHD=e_trdHtrk_LHD, prob_e=prob_e, prob_p=prob_p, prob_he=prob_he,
             TRD_e_likelihood=TRD_e_likelihood, TRD_p_likelihood=TRD_p_likelihood, TRD_he_likelihood=TRD_he_likelihood,
             GetNCC=GetNCC, TRD_charge=TRD_charge, trd_statk=trd_statk, trd_nhitk=trd_nhitk,
             trd_onhitk=trd_onhitk, trd_oampk=trd_oampk, trd_qrmsk_0=trd_qrmsk_0, #trd_qnhk_0=trd_qnhk_0,
             trd_qk_0=trd_qk_0)


def main():

    print("Particle Type chosen:", parser.particle)
    # ROOT Dataset Name:
    print(f"ROOT Path: {parser.data_path}/{parser.data_name}")

    numpy_data_dir = "../../../datasets/in_progress/ISS"

    if parser.energy_range is None:
        numpy_all_x_name = parser.data_name + "_all_x.npz"
    else:
        numpy_all_x_name = parser.data_name + "_" + parser.energy_range + "_all_x.npz"
    print(f"Loading x data from: {numpy_data_dir}/{numpy_all_x_name}")

    save_dir = numpy_data_dir + "/split_particles"  # Change Dataset Name Here
    if parser.energy_range is None:
        split_particle_dataset_sav_dir = save_dir
    else:
        split_particle_dataset_sav_dir = save_dir + "_" + parser.energy_range  # Proper Energy Range folder chosen here
    root_to_Cond_NumPy(parser.particle, parser.data_path, numpy_data_dir, numpy_all_x_name, split_particle_dataset_sav_dir,
                       parser.data_name, parser.energy_range)

    print("DONE!")


if __name__ == "__main__":
    main()
