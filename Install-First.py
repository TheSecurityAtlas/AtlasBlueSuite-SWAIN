# import Author as Andrew Heishman
# Install these dependencies first

import subprocess as sp

Dependencies = "Install-Module -Name ExchangeOnlineManagement ; Set-ExecutionPolicy RemoteSigned"


sp.run(Dependencies, shell=True)