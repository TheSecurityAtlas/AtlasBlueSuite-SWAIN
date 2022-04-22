# importing modules
import subprocess as sp
import os

# this will change the default shell to use powershell instead of cmd.exe or /bin/sh
os.environ["COMSPEC"] = "powershell"

# domain email needed to insert into IPPSSession | Connecting to ExchangeOnlineManagement
Email = input("Please provide your domain email address ")

sp.run(f"Connect-IPPSSession -UserPrincipalName {Email}", shell=True)

# ask user name of content search | Will inject into PS script
Search_Name = input("What is the name of the Content Search? ")

# this var will instruct ExchangeOnlineManagement whether to Soft Delete or Hard Delete when purging
Purge_Type = input("Would you like to (S)oft Delete or (H)ard Delete? ")


if Purge_Type == "S":
    print("Soft Delete Initiated on " + Search_Name)
    sp.run(f"New-ComplianceSearchAction -SearchName {Search_Name!r} -purge -PurgeType SoftDelete", shell=True)
elif Purge_Type == "H":
    print("Hard Delete Initiated on " + Search_Name)
    sp.run(f"New-ComplianceSearchAction -SearchName {Search_Name!r} -purge -PurgeType HardDelete", shell=True)
else:
    print("Please enter S or H. Try again")
