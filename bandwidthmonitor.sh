#!/bin/bash


username=public
ipaddress=xxx.xxx.xxx.xxx


#Fucntions that pull an actual value.
#The x.x.x.x.x number is an SNMP OID number. You would need to find the correct OID for your use case.
#http://oid-info.com/
#Because of how the script is written, the download and upload will happen on alternate seconds.
download() {
  #ifHCInOctets
  in=$(snmpwalk -v 2c -c $username $ipaddress x.x.x.x.x | awk -F'64: ' '{print $2}')
  kbin=$(expr $in / 1000)
  echo $kbin
}

upload() {
  #ifHCOutOctets
  out=$(snmpwalk -v 2c -c $username $ipaddress x.x.x.x.x | awk -F'64: ' '{print $2}')
  kbout=$(expr $out / 1000)
  echo $kbout
}


#Functions that give a kb/sec type value.
down() {
  initialkbin=$(download)
  sleep 1
  oneseckbin=$(download)
  kbinpersec=$(expr $oneseckbin - $initialkbin)
  #in_pretty_output=("$kbinpersec kb/sec down")
  #echo $in_pretty_output
  echo $kbinpersec
}

up() {
  initialkbout=$(upload)
  sleep 1
  oneseckbout=$(upload)
  kboutpersec=$(expr $oneseckbout - $initialkbout)
  #out_pretty_output=("$kboutpersec kb/sec up")
  #echo $out_pretty_output
  echo $kboutpersec
}

#Function that returns the date in the correct format.
printdate() {
  now="$(date +'%Y-%m-%d %H:%M:%S')"
  echo $now
}

newline() {
  printf "\n" >> bandwidth.csv
}

csvwriteup() {
  printf "$(printdate)," >> bandwidthup.csv
  printf "$(up)" >> bandwidthup.csv
  printf "\n" >> bandwidthup.csv
}

csvwritedown() {
  printf "$(printdate)," >> bandwidthdown.csv
  printf "$(down)" >> bandwidthdown.csv
  printf "\n" >> bandwidthdown.csv
}

#Clears the csv files of any previous lines
printf "" > bandwidthdown.csv
printf "" > bandwidthup.csv

#Main loop
for i in {1..100}; do
  csvwriteup &
  csvwritedown &
  wait
done
