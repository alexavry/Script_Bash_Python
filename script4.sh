#!/bin/bash

read -p "Veuillez entrer le chemin du fichier : " file_path

if [ ! -f "$file_path" ]; then
    echo "Le fichier $file_path n'existe pas."
    exit 1
fi

char_count=$(wc -m < "$file_path")

echo "Le fichier $file_path contient $char_count caractères."

