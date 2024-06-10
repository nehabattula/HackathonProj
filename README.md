# HackathonProj

conda create -p venv python==3.10 -y
conda activate venv/

pip install -r requirements.txt
aws configure

## For installing any other packages
pip install -r requirements.txt / pip install --user -r requirements.txt

## Alternative to requirements.txt
pip install pandas faker

python GenerateData.py
