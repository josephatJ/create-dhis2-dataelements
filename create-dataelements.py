import asyncio
import json
# Josephat Mwakyusa, Dec 09 2021
import os

# import utilities
from utilities.get_server_access import get_user_name_and_password
from utilities.get_dataelements_from_csv import get_dataelements
from utilities.dataelement import create_dataElement

# Addresses
DEST_BASE_URL = ''

# authentication
username = ''
password = ''

headers = {
'Content-type': 'application/json'
}

async def main():
    # Get credentials
    server_access = await get_user_name_and_password()
    DEST_BASE_URL = server_access['url']
    username = server_access['username']
    password = server_access['password']

    # Get file name from user
    file_name =  input("Enter csv file name: ")

    current_directory = os.getcwd()

    # get data elements
    dataelements_from_csv = await get_dataelements(current_directory + "/dataelements/" + file_name)
    for element in dataelements_from_csv:
        dataelement = {
            "name": element[0],
            "shortName": element[3],
            "formName": element[5],
            "domainType": element[6],
            "valueType": element[7],
            "aggregationType": element[8],
            "zeroIsSignificant": False
        }
        print(json.dumps(dataelement))
        response = await create_dataElement(dataelement, DEST_BASE_URL, username, password, headers)
        


asyncio.run(main())