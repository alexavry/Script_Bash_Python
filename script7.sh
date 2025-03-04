#!/bin/bash
read -p "Enter website to ping: " website
echo "Pinging $website..."
ping -c 4 $website
