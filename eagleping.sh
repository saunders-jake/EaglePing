#!/bin/bash
clear
echo "##########################
........EAGLE PING........
##########################
  Made by: Jake Saunders  
##########################"
echo
#Set to path of your desired output file.
logpath="output.txt" 
#Set to the amount of packets to be sent per address, per ping "round" (I recommend 2)
packettotal=2 

#Gets the users desired ping interval, and performs input validation on it. 
while :
do
  read -p "Enter ping interval(seconds): " pingint
  if [[ $pingint != ?(-)+([0-9]) ]]; then
    echo "Please enter a positive integer."
    echo
  else
    break
  fi
done
echo
#Gets the users desired number of addresses to be pinged, and performs input validation on it.
while :
do
  read -p "Enter number of addresses: " ipct
  if [[ $pingint != ?(-)+([0-9]*) ]]; then
    echo "Please enter a positive integer."
    echo
  else
    break
  fi
done
#Gets the ip adddresses to be pinged, and appends them to the ipct array.
for i in $(seq $ipct)
do
  read -p "Address ${i}: " z
  iplst+=($z)
done
echo

for q in $(seq "${#iplst[@]}"); do
  for i in $(seq "${packettotal}"); do
    ping -c1 "${iplst[q-1]}"
    if [ $? -ne 0 ]; then
      #If you want a different output to the log file, edit the following line.
      printf "%s   %s   Ping error code: %d \n" "$(date "+%m-%d-%Y %H:%M:%S")" ${iplst[q-1]} $? >> output.txt 
    fi 
  done
done




#Known bugs - typing non-integer into the "Enter number of addresses: " promt causes program to crash.



