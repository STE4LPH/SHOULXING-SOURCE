#!/bin/bash

pkg update -y && pkg upgrade -y
pkg install tsu git python -y
pip install pycryptodome pyfiglet pyDes
echo "Installed! Now you can run \"python shoulxing.py\""