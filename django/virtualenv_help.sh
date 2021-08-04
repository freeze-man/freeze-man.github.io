

# How to install virtualenv:

$ python3 -m pip install --upgrade pip

# Then install virtualenv using pip3

$ pip3 install virtualenv

# Now create a virtual environment

$ virtualenv myvenvname 

# You can also use a Python interpreter of your choice

$ virtualenv -p /usr/bin/python2.7 myvenvname

# Create virtualenv using Python3

$ virtualenv -p python3 myvenvname

# Instead of using virtualenv you can use this command in Python3

$ python3 -m venv myvenvname



#Errors creating a virtualenv
#You may see the following errors when attempting to create a virtualenv using Python 3.7.

#AttributeError: module 'importlib._bootstrap' has no attribute 'SourceFileLoader'

#OSError: Command /home/username/venv/bin/python3 -c "import sys, pip; sys...d\"] + sys.argv[1:]))" setuptools pip failed with error code 1

#Adding the following line when installing a custom version of OpenSSL to your .bash_profile resolves this.

$ export LC_ALL="en_US.UTF-8"



# Active your virtual environment:

$ source venv/bin/activate

# Using fish shell:

$ source venv/bin/activate.fish

# To deactivate:

$ deactivate


