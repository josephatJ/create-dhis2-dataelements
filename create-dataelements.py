import asyncio
#import json
from requests.auth import HTTPBasicAuth
#import requests
from time import sleep

# Josephat Mwakyusa, Dec 09 2021
import csv
import os

# import utilities
from utilities.get_server_access import get_user_name_and_password

# Addresses
DEST_BASE_URL = ''

# authentication
username = ''
password = ''

headers = {
'Content-type': 'application/json'
}

async def main():
    server_access = await get_user_name_and_password()
    DEST_BASE_URL = server_access['url']
    username = server_access['username']
    password = server_access['password']

    # Get file name from user
    users_file_name =  input("Enter csv file name: ")

    current_directory = os.getcwd()


asyncio.run(main())