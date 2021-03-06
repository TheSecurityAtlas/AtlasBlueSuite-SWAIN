# importing modules
import subprocess as sp
import os

# this will change the default shell to use powershell instead of cmd.exe or /bin/sh
os.environ["COMSPEC"] = "powershell"

def Query_info():
    print("Search Query Quick Reference Guide: \nFor more about Search Query Syntax please visit Syntax_Guide.txt\n\nFrom\n  from:<email@domain.com> -- can also be just domain: from:<domain.com>\n\nRecipients (includes all recipients in 'To' 'cc' 'bcc')\n  recipients:<email@domain.com> can also be just domain: recipients:<domain.com>\n\nSubject (the query doesn't return only those messages that have an exact match.)\n subject:<insert subject here> \n\nReceived \nThe date that an email message was received by a recipient \n  received:2021-04-15 -- date is a single day\n   received>=2021-01-01 AND received<=2021-03-31 -- date is a range\n\n\nExample query:\n from:hotsauce@aol.com AND subject:Budget Reports AND received:2022-02-10\n\n")

def CSCT():
    

    print("\n\nWelcome to the CSCT: Content Search Creation Tool")
    CSCT_Connect = input("Please provide your domain email address: ")
    CSCT_Name = input("What is the name of your Content Search? ")
    CSCT_Description = input("Please give this Content Search a concise description: ")
    CSCT_Location = input("Which mailboxes would you like to search? 'Please use (All) to search all mailboxes' : ")
    Query_info()
    CSCT_Query = input("What are the search parameters? ")
        
    sp.run(f"Connect-IPPSSession -UserPrincipalName {CSCT_Connect} ; New-ComplianceSearch -Name {CSCT_Name!r} -AllowNotFoundExchangeLocationsEnabled $true -ContentMatchQuery {CSCT_Query!r} -Description {CSCT_Description!r} -ExchangeLocation {CSCT_Location} ; Start-ComplianceSearch -Identity {CSCT_Name}", shell=True)
    print(f"{CSCT_Name} has been started, Search will be complete soon, please wait 2-5 minitues: Happy Hunting")

CSCT()