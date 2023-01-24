#!/bin/bash
curl -sSO https://dl.google.com/cloudagents/install-logging-agent.sh sudo bash install-logging-agent.sh
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    software-properties-common \
    python3-dateutil \
    python3.8 \
    python3.8-dev \
    python3.8-distutils \
    python3.8-venv
sudo ln -s /usr/bin/python3 /usr/bin/python
python3.8 -m venv prefect-env
source prefect-env/bin/activate
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
PATH="$HOME/.local/bin:$PATH"
export PATH
pip3 install prefect==2.7.7 prefect-gcp
export PREFECT_API_KEY=`curl  -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/attributes/PREFECT_API_KEY"`
export PREFECT_WORKSPACE=`curl  -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/attributes/PREFECT_WORKSPACE"`
prefect cloud workspace set -w $PREFECT_WORKSPACE
prefect cloud login -k $PREFECT_API_KEY
prefect agent start -q main