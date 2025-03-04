#!/bin/bash

read -p "Veuillez entrer l'adresse de l'hôte (ex: user@hostname ou IP) : " host
read -sp "Veuillez entrer le mot de passe : " password

echo "Connexion à $host..."
sshpass -p "$password" ssh "$host"
