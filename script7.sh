#!/bin/bash
read -p "Entrez l'adresse du site à ping: " website
echo "Pinging $website..."
ping -c 4 $website