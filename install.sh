#!/bin/sh

python_installed() {
	command -v "$1" > /dev/null 2>&1
}

if python_installed() python3 && which python3-pip; then
	pip3 install --user --upgrade psutil
else
	echo "Missing python3 or pip3!"
fi
