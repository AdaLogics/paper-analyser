# Install some needed packages
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt install graphviz

# Create a virtual environment
virtualenv venv

# Launch the virtual environment
. venv/bin/activate

# Install various packages
pip install -r requirements.txt
