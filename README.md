# pi_home_automation

## Description
This repository contains a list of home automation scripts I have created using [energenie sockets](https://energenie4u.co.uk/catalogue/product/ENER002), a rasperry pi (model 3b+ with Raspbian installed) with [pi-mote hat](https://uk.pi-supply.com/products/energenie-pi-mote-control-board) and the gpiozero Python package.
Energenie sockets are a cheaper alternative to other sockets available because they are based on RF signals rather than wifi.
These sockets take more time to get setup than alternatives but can be setup in a couple of hours on a wet Sunday morning.
This was a simple weekend project that allowed me to automate some boring tasks that I have to regularly do whilst WFH, including resetting my router.

----

## Contents
This repository contains several Python scripts;
- check_conn.py - pings several sites and if no pings are returned, reset router through Energenie socket

----
## Future work
Going forward, I plan to incorporate Alexa skills to turn on sockets with voice commands.
