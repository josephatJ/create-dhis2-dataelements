
# Josephat Mwakyusa, Dec 09 2021


import csv

async def get_dataelements(file_path):
    data= []
    data_file = open(file_path)
    csv_arr_object = csv.reader(data_file)
    next(csv_arr_object)
    for data_row in csv_arr_object:
        data.append(data_row)
    return data

