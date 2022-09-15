# import Author as Andrew Heishman
# v1.2

# importing modules
import time
import subprocess as sp
import os

# this will change the default shell to use powershell instead of cmd.exe or /bin/sh
os.environ["COMSPEC"] = "powershell"

Content_Search = input("  _______          __     _____ _   _ \n / ____\ \        / /\   |_   _| \ | |\n| (___  \ \  /\  / /  \    | | |  \| |\n \___ \  \ \/  \/ / /\ \   | | | . ` |\n ____) |  \  /\  / ____ \ _| |_| |\  |\n|_____/    \/  \/_/    \_\_____|_| \_|\n\nThis tool will start the purging process by having you create a 'Content Search'. Or maybe you'd like to do something different?\n\n'1': Start the search for emails\n'2': Purge emails using the search created in option 1\n'3': Block an email address\n\nWhat would you like to do?:")

def Query_info():
    print("Search Query Quick Reference Guide: \nFor more about Search Query Syntax please visit Syntax_Guide.txt\n\nFrom\n  from:<email@domain.com> -- can also be just domain: from:<domain.com>\n\nRecipients (includes all recipients in 'To' 'cc' 'bcc')\n  recipients:<email@domain.com> can also be just domain: recipients:<domain.com>\n\nSubject (the query doesn't return only those messages that have an exact match.)\n subject:<insert subject here> \n\nReceived \nThe date that an email message was received by a recipient \n  received:2021-04-15 -- date is a single day\n   received>=2021-01-01 AND received<=2021-03-31 -- date is a range\n\n\nExample query:\n from:hotsauce@aol.com AND subject:Budget Reports AND received:2022-02-10\n\n")

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print("The search is now complete. Thank you!\n")

# A List of Items
items = list(range(0, 57))
l = len(items)

# Initial call to print 0% progress

def CSCT():
    

    print("\n\nWelcome to the CSCT: Content Search Creation Tool")
    CSCT_Connect = input("Please provide your domain email address: ")
    CSCT_Name = input("What is the name of your Content Search? ")
    CSCT_Description = input("Please give this Content Search a concise description: ")
    CSCT_Location = input("Which mailboxes would you like to search? 'Please use 'All' to search all mailboxes' : ")
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
        print(f"\n\n{Search_Name} has been started. \nIf you would like to see the status of your purge -- please use Get-ComplianceSearchAction <insert name here> (remember to include _purge) ")
        input("Please press enter to close this application")
    else:
        print("Please enter 'SoftDelete' or 'HardDelete'")


if Content_Search == "1":
    SWAIN()
elif Content_Search == "2":
    CSCT()
    print("Content search should take about 2 - 5 minutes")
    time.sleep(300)
    SWAIN()
elif Content_Search == "3":
    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    time.sleep(0.9)
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    
    
