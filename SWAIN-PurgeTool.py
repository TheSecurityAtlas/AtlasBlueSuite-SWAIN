# import Author as Andrew Heishman
# v1.2

# importing modules
import subprocess as sp
import os

# this will change the default shell to use powershell instead of cmd.exe or /bin/sh
os.environ["COMSPEC"] = "powershell"

def CSCT():
    CSCT_Connect = input("Please provide your domain email address: ")
    CSCT_Name = input("What is the name of your Content Search? ")
    CSCT_Description = input("Please give this Content Search a concise description: ")
    CSCT_Location = input("Which mailboxes would you like to search? 'Please use (All) to search all mailboxes': ")
    CSCT_Query = input("What are the search parameters? (Please consult the 'Search Parameters.txt' documentations) : ")
        
    sp.run(f"Connect-IPPSSession -UserPrincipalName {CSCT_Connect} ; New-ComplianceSearch -Name {CSCT_Name!r} -AllowNotFoundExchangeLocationsEnabled $true -ContentMatchQuery {CSCT_Query!r} -Description {CSCT_Description!r} -ExchangeLocation {CSCT_Location} ; Start-ComplianceSearch -Identity {CSCT_Name}", shell=True)
    print(f"{CSCT_Name} has been started, Search will be complete soon, please wait 2-5 minitues")

def SWAIN():
    Email = input("Please provide your domain email address ")
    Search_Name = input("What is the name of the Content Search? ")
    Purge_Type = input("Would you like to SoftDelete or HardDelete? ")
    Email_Purge = f"Connect-IPPSSession -UserPrincipalName {Email} ; New-ComplianceSearchAction -SearchName {Search_Name!r} -purge -PurgeType {Purge_Type}"
    if Purge_Type == "SoftDelete" or Purge_Type == "HardDelete":
        sp.run(Email_Purge, shell=True)
    else:
        print("Please enter [SoftDelete] or [HardDelete]")


#Content_Search = input("Have you started a Content Search yet? (Y) or (N) ")

#if Content_Search == "Y":
#    SWAIN()
#elif Content_Search == "N":
#    CSCT()
#    SWAIN()



print("Search Query Quick Reference Guide \nFor more about Search Query Syntax please visit  'Syntax Guide.txt'")

