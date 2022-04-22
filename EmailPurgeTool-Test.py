# importing modules
import subprocess as sp
import os

# this will change the default shell to use powershell instead of cmd.exe or /bin/sh
os.environ["COMSPEC"] = "powershell"

# domain email needed to insert into IPPSSession | Connecting to ExchangeOnlineManagement
Email = input("Please provide your domain email address ")

# ask user name of content search | Will inject into PS script
Search_Name = input("What is the name of the Content Search? ")

# this var will instruct ExchangeOnlineManagement whether to Soft Delete or Hard Delete when purging
Purge_Type = input("Would you like to SoftDelete or HardDelete? ")

Email_Purge = f"Connect-IPPSSession -UserPrincipalName {Email} ; New-ComplianceSearchAction -SearchName {Search_Name!r} -purge -PurgeType {Purge_Type}"

if Purge_Type == "SoftDelete" or Purge_Type == "HardDelete":
    sp.run(Email_Purge)
else:
    print("Please enter [SoftDelete] or [HardDelete]")
