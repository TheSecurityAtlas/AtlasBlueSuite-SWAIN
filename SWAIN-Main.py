# import Author as Andrew Heishman
# v1.2

# importing modules
import time
import subprocess as sp
import os
# this will change the default shell to use powershell instead of cmd
os.environ["COMSPEC"] = "powershell"

# range for progress bar
progress = list(range(0, 2))
l = len(progress)

# main header for SWAIN 
print("  _______          __     _____ _   _ \n / ____\ \        / /\   |_   _| \ | |\n| (___  \ \  /\  / /  \    | | |  \| |\n \___ \  \ \/  \/ / /\ \   | | | . ` |\n ____) |  \  /\  / ____ \ _| |_| |\  |\n|_____/    \/  \/_/    \_\_____|_| \_|\n")

# long query for syntax
def Query_info():
    print("Search Query Quick Reference Guide: \nFor more about Search Query Syntax please visit Syntax_Guide.txt\n\nFrom\n  from:<email@domain.com> -- can also be just domain: from:<domain.com>\n\nRecipients (includes all recipients in 'To' 'cc' 'bcc')\n  recipients:<email@domain.com> can also be just domain: recipients:<domain.com>\n\nSubject (the query doesn't return only those messages that have an exact match.)\n subject:<insert subject here> \n\nReceived \nThe date that an email message was received by a recipient \n  received:2021-04-15 -- date is a single day\n   received>=2021-01-01 AND received<=2021-03-31 -- date is a range\n\n\nExample query:\n from:hotsauce@aol.com AND subject:Budget Reports AND received:2022-02-10\n\n")

# progress bar first function
def SWAIN_bar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print("\n")
        
# progress bar second function
def ProgressBar():
    SWAIN_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, item in enumerate(progress):
        time.sleep(1)
        SWAIN_bar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

# function for finding email -- including powershell commands
def SWAIN_CSCT():
    print("\n\nWelcome to the CSCT: Content Search Creation Tool")
    CSCT_Connect = input("Please provide your domain email address: ")
    CSCT_Name = input("What is the name of your Content Search? ")
    CSCT_Location = input("Which mailboxes would you like to search? 'Please use 'All' to search all mailboxes' : ")
    Query_info()
    CSCT_Query = input("What are the search parameters? ")
    sp.run(f"Connect-IPPSSession -UserPrincipalName {CSCT_Connect} ; New-ComplianceSearch -Name {CSCT_Name!r} -AllowNotFoundExchangeLocationsEnabled $true -ContentMatchQuery {CSCT_Query!r} -Description Search started from SWAIN by {CSCT_Name} -ExchangeLocation {CSCT_Location} ; Start-ComplianceSearch -Identity {CSCT_Name}", shell=True)
    print(f"{CSCT_Name} has been started, Search will be complete soon, Happy Hunting!")

# function for purging emails -- including powershell commands
def SWAIN():
    print("\n\nWelcome to SWAIN: Email Purge Tool")
    Email = input("Please provide your domain email address ")
    Search_Name = input("What is the name of the Content Search? ")
    Purge_Type = input("Would you like to SoftDelete or HardDelete? ")
    Email_Purge = f"Connect-IPPSSession -UserPrincipalName {Email} ; New-ComplianceSearchAction -SearchName {Search_Name!r} -purge -PurgeType {Purge_Type}"
    if Purge_Type == "SoftDelete" or Purge_Type == "HardDelete":
        sp.run(Email_Purge, shell=True)
        input("Please press enter to close this application")
    else:
        print("Please enter 'SoftDelete' or 'HardDelete'")

def SWAIN_block():
    Email = input("Please provide your domain email address: ")
    Email_blocking = input("Please enter the email you would like to block: ")
    Email_notes = input("Please include any notes you would like to be submitted with the block: ")
    block_query = f"Connect-ExchangeOnline -UserPrincipalName {Email} ; New-TenantAllowBlockListItems -ListType Sender -Block -Entries {Email_blocking!r} -NoExpiration -Notes {Email_notes!r}"
    sp.run(block_query, shell=True)

def SWAIN_update():
    command = "powershell.exe"
    update_swain = f"Start-Process -FilePath \"powershell.exe\" -Verb RunAs ; Set-ExecutionPolicy RemoteSigned ; Install-Module -Name ExchangeOnlineManagement ; Import-Module ExchangeOnlineManagement"
    sp.run(update_swain, shell=True)
    
# main loop for SWAIN
while True:
    try:
      Main_Query = input("\nThis tool will start the purging process by having you create a 'Content Search'.\nOr maybe you'd like to do something different?\n\n\n'1': Start the search for emails\n'2': Purge emails using the search created in option 1\n'3': Block an email address\n\n'Syntax': Syntax guide for Content Search\n'firstrun': Use before running SWAIN for the first time\n\nWhat would you like to do? ")
      if Main_Query == "1":
          SWAIN_CSCT()
          print("Content search should take about 2 - 5 minutes")
          ProgressBar()
      elif Main_Query == "2":
          SWAIN()
          print("Purge started!\nIf you would like to see the status of your purge -- please use 'Get-ComplianceSearchAction <insert name here>_purge' (remember to include '_purge')")
      elif Main_Query == "3":
          SWAIN_block()
          time.sleep(2)
      elif Main_Query == "Syntax":
          print("\nhttps://github.com/TheSecurityAtlas/AtlasBlueSuite-SWAIN/blob/main/Syntax_Guide.txt\n\n\n\n")
          time.sleep(2)
      elif Main_Query == "firstrun":
          SWAIN_update()
      else:
          print("\nPlease enter a valid option")
          time.sleep(2.5)
    except KeyboardInterrupt:
      print("\nCtrl-C pressed, exiting...")
      exit()