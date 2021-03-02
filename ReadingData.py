#Import

from csv import reader

with open("C:\\Users\Jonathan\Downloads\FantasyLabs_NBAProjections_3_1_2021.csv", 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
    print(list_of_rows)

