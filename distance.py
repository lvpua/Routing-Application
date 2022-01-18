import csv
import data
import datetime

#Reads the csv files(desinations) and creates a dictionary from raw data to unique IDs for usage on the algorithm below.
with open('csvfiles/destinations.csv') as destination_csv:
    destinations = list(csv.reader(destination_csv, delimiter=','))
    destination_dict = dict()
    for destination in destinations:
        destination_dict[f'{destination[2]}'] = destination[0]

#Reads the csv files(distance) and creates a dictionary from raw data to unique IDs for usage on the algorithm below.
with open('csvfiles/distance.csv') as distance_csv:
    distances = list(csv.reader(distance_csv, delimiter=','))
    distance_dict = dict()
    for col_index, distance in enumerate(distances):
        column = col_index
        if column == '27':
            break
        for row_index, distance2 in enumerate(distances):
            if distances[column][row_index] == '0.0':
                distance_dict[f'{column}{row_index}'] = '0.0'
                break
            else:
                distance_dict[f'{column}{row_index}'] = distances[column][row_index]
                distance_dict[f'{row_index}{column}'] = distances[column][row_index]


#*****Greedy Algorithm*****
#Below, a variation of Greedy Algorithm called "Nearest Neighbor" was implemented based on the dictionary created above
#to ensure that the best case space time complexity is used. This algorithm will compare the closest node to the
#current node and checks if the trucks are empty or not.

def nearest_distance(truck):
    min_distance = 10000000 # Arbitrary large number to ensure its bigger than all possible miles in the data given.
    package_to_remove = ''
    for package in truck.packages:
        if min_distance > float(distance_dict[f'{destination_dict[truck.current_location]}{destination_dict[package[1]]}']):
            min_distance = float(distance_dict[f'{destination_dict[truck.current_location]}{destination_dict[package[1]]}'])
            truck.destination = package[1]
            package_to_remove = package
    truck.current_location = truck.destination
    truck.total_miles = truck.total_miles + min_distance
    round(truck.total_miles, 2)
    round(truck.miles_at_time, 2)
    if truck.total_miles > truck.miles_at_time:
        return
    truck.last_delivery = truck.leave_times + datetime.timedelta(seconds=int((truck.total_miles*200)))
    data.package_table.return_package(package_to_remove[0])[8] = f'Delivered At: {truck.last_delivery}'
    truck.packages.remove(package_to_remove)
    round(truck.miles_at_time, 2)
    round(truck.total_miles, 2)
    if len(truck.packages) == 0:
        truck.destination = '4001 South 700 East'
        truck.total_miles = truck.total_miles + float(distance_dict[f'{destination_dict[truck.destination]}{destination_dict[truck.current_location]}'])
        truck.miles_at_time = truck.total_miles
    round(truck.miles_at_time, 2)
    round(truck.total_miles, 2)



