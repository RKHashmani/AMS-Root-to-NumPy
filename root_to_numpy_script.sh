#!/usr/bin/bash

particle_type="$1"

proton_sets=457
electron_sets=445
electron_sets_2=778
ISS_sets=1238

if [ "$particle_type" = "pr.pl1phpsa.l1o9.5016000.4_00" ];
then
  echo "$particle_type"
  for ((i=455; i<proton_sets; i++))
  do
    python root_to_numpy.py --data_name pr.pl1phpsa.l1o9.5016000.4_00 --data_path /home/rhashmani/Files/ECAL/datasets/ROOT/ISS/pr.pl1phpsa.l1o9.5016000.4_00 --iter "$i" &
    if (("$((i+1))" % 5 == 0));
    then
      echo "BREAK TIME!"
      sleep 4m
    fi
  done
  python root_to_numpy_remainder.py --data_name pr.pl1phpsa.l1o9.5016000.4_00 --data_path /home/rhashmani/Files/ECAL/datasets/ROOT/ISS/pr.pl1phpsa.l1o9.5016000.4_00 --iter "$proton_sets" &

elif [ "$particle_type" = "el.pl1.2004000" ];
then
  echo "$particle_type"
  for ((i=0; i<electron_sets; i++))
  do
    python root_to_numpy.py --data_name el.pl1.2004000 --data_path /home/rhashmani/Files/ECAL/datasets/ROOT/ISS/el.pl1.2004000 --iter "$i" &
    if (("$((i+1))" % 5 == 0));
    then
      echo "BREAK TIME!"
      sleep 4m
    fi
  done
  python root_to_numpy_remainder.py --data_name el.pl1.2004000 --data_path /home/rhashmani/Files/ECAL/datasets/ROOT/ISS/el.pl1.2004000 --iter "$electron_sets" &

elif [ "$particle_type" = "el.pl1.0_25200" ];
then
  echo "$particle_type"
  for ((i=778; i<electron_sets_2; i++))
  do
    python root_to_numpy.py --data_name el.pl1.0_25200 --data_path /home/rhashmani/Files/ECAL/datasets/ROOT/ISS/el.pl1.0_25200 --iter "$i" &
    if (("$((i+1))" % 5 == 0));
    then
      echo "BREAK TIME!"
      sleep 3m 30s
    fi
  done
  python root_to_numpy_remainder.py --data_name el.pl1.0_25200 --data_path /home/rhashmani/Files/ECAL/datasets/ROOT/ISS/el.pl1.0_25200 --iter "$electron_sets_2" &

elif [ "$particle_type" = "ISS.B1236_pass8" ];
then
  echo "$particle_type"
  for ((i=70; i<ISS_sets+1; i++))
  do
    python root_to_numpy.py --data_name ISS.B1236_pass8 --data_path /home/rhashmani/Files/ECAL/datasets/ROOT/ISS/ISS.B1236_pass8 --iter "$i" &
    if (("$((i+1))" % 35 == 0));
    then
      echo "BREAK TIME!"
      sleep 300s
    fi
  done

else
  echo "Wrong Particle Type"
fi
