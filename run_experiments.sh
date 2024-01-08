#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python run_experiments.py --second_half
python run_experiments.py 
