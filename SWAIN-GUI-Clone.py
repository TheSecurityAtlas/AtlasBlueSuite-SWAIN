# import Author as Andrew Heishman
# v1.2

# importing modules
from logging import root
from tkinter import *
from tkinter import ttk
import time
import subprocess as sp

import os

root = Tk()
root.title("SWAIN: Content Search & Purge Tool")
root.geometry("500x500")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=50, row=50, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()








# this will change the default shell to use powershell instead of cmd.exe
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
    print(f"{CSCT_Name} has been started, Search will be complete soon, Happy Hunting!")

def SWAIN():
    print("\n\nWelcome to SWAIN: Email Purge Tool")
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
#    print("Please wait for 120 seconds...")
#    time.sleep(120)
#    SWAIN()
