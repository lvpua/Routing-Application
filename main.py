import data
import time
import truck
from datetime import datetime

#Lois Vernon A. Pua
#Student ID: 008443322 --> Will be removed once project passes.


#Main Program. Will ask for user's input and will return data based on the user's input.(On the command line)
def main():
    print("*****WGU C950 Delivery Program*****")
    print("")
    print("")
    option = input("Select from the following options:\n1. To view by Package ID\n2. To view all packages\n3. To exit the program\n")
    if option == '1':
        package_id = input("Please enter a valid Package ID(1-40)\n")
        time_input = input("Please enter a time in the format HH:MM(Ex: 08:30 or 15:10).\n")
        time_input = datetime.combine(datetime.today().date(), datetime.strptime(time_input, '%H:%M').time())
        truck.deliver_time(time_input)
        print_package(package_id)
    if option == '2':
        time_input = input("Please enter a time in the format of HH:MM(Ex: 08:30 or 15:10).\n")
        time_input = datetime.combine(datetime.today().date(), datetime.strptime(time_input, '%H:%M').time())
        truck.deliver_time(time_input)
        print_status(time_input)
    if option == '3':
        return
    if option != '1' and option != '2' and option != '3':
        print("Option selected is invalid!\nRestarting...\n")
        time.sleep(0)
        main()


def print_status(time_input):
    print(f'PACKAGES STATUS AS OF: {time_input.time()}')
    print(
        f'Total Truck Distance Traveled: {float(truck.truck_1.miles_at_time) + float(truck.truck_2.miles_at_time) + float(truck.truck_3.miles_at_time)}' + " " + "miles")
    for bucket in data.package_table.return_all_package():
        for pair in bucket:
            print(f' Package ID: {pair[1][0]} || Package Address: {pair[1][1]} || City: {pair[1][2]} || Package Zip: {pair[1][4]} ||'
                  f' Package Deadline: {pair[1][5]} || Package Weight: {pair[1][6]} ||  Package Status: {pair[1][8]}')


def print_package(package_id):
    package = data.package_table.return_package(package_id)
    print(f' Package ID: {package[0]} || Package Address: {package[1]} || City: {package[2]} || Package Zip: {package[4]} ||'
          f' Package Deadline: {package[5]} || Package Weight: {package[6]} || Package Status: {package[8]}')


main()
