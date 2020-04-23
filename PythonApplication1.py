import requests
import json
import argparse
import getpass

#username = input("Enter Username: ")
#password = getpass.getpass()


with open("namelist.json", "r") as f:
   namelist = json.load(f)


with open("config.json", "r") as f:
   config = json.load(f)


   for name in namelist:
         current_config = config["FamilyNames"].copy()
         current_config["PetName"] = name

         print(current_config)

   
   

