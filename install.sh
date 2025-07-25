#!/bin/bash

pkg update -y && yes | pkg upgrade -y
pkg install tsu git python -y
pip install pycryptodome pyfiglet pyDes
echo "Installed! Now you can run \"sudo python $(pwd)/shoulxing.py\""