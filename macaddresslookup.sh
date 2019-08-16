#!/bin/bash

#Replace admin with your router login name and xxx.xxx.xxx.xx with the IP address of the router.

grabmac() {
  snmpwalk -v 2c -c admin xxx.xxx.xxx.xxx 1.3.6.1.2.1.4.22.1.2 | awk '{print $4":"$5":"$6":"$7":"$8":"$9}'
}


printf "$(grabmac)" > mac.csv
