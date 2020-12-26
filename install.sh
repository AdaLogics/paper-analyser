# Install some needed packages
sudo apt-get install python3
sudo apt-get install python3-pip

# Create a virtual environment
virtualenv venv

# Launch the virtual environment
. venv/bin/activate

# Install various packages
pip3 install graphviz
pip3 install matplotlib
pip3 install pdf2txt
pip3 install requests
pip3 install simplejson
