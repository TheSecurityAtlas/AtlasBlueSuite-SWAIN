# import Author as Andrew Heishman
# Install these dependencies first

import subprocess as sp
import os

os.environ["COMSPEC"] = "powershell"
Dependencies = "Install-Module -Name ExchangeOnlineManagement ; Set-PSRepository -Name PSGallery -InstallationPolicy Trusted"


sp.run(Dependencies, shell=True)