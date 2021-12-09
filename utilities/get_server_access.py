
# Josephat Mwakyusa, Dec 09 2021

async def get_user_name_and_password():
    DEST_BASE_URL=input("Enter server address: ")
    username = input("Enter your username: ")
    password =  input("Enter password: ")

    return {'username': username, 'password': password, 'url': DEST_BASE_URL}