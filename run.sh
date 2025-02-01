#!/bin/bash


python3 -m venv .venv
source .venv/bin/activate
pip install telebot

while true
do
	if ! pgrep -f "python.*main.py" > /dev/null
	then
    		echo "main.py is not running. Starting it now..."

    		# Activate the virtual environment
    		source .venv/bin/activate

    		# Start main.py in the background
    		nohup python main.py > /dev/null 2>&1 &

   		echo "main.py has been started."
		else
    		echo "main.py is already running."
	fi

	sleep 1
done
