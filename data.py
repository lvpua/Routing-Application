from datetime import datetime
from hash_table import HashTable
import csv

# Referenced from C950 - Webinar 3 - How to Dijkstra : https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=aad71bd6-abf5-4cd4-8a78-ac7f01039c73
#Reads and extracts the raw data from the said csv files(package). The data is initalize into an empty delivery then
#later adds it to the hash table
with open('csvfiles/package.csv') as package_csv:
    data = csv.reader(package_csv, delimiter=',')
    package_table = HashTable()
    first_delivery = []
    second_delivery = []
    final_delivery = []
    for package in data:
        package_id = package[0]
        package_address = package[1]
        package_city = package[2]
        package_state = package[3]
        package_postal = package[4]
        package_deadline = package[5]
        package_weight = package[6]
        package_note = package[7]
        package_status = "AT THE HUB"
        package_delivery_start = ''
        package_key = package_id
        package_value = [package_id, package_address, package_city, package_state, package_postal, package_deadline,
                        package_weight, package_note, package_status]

        if 'EOD' not in package[5] and 'NA' in package[7]:
            first_delivery.append(package_value)
        if 'Must be' in package[7]:
            first_delivery.append(package_value)
        if 'Can only' in package[7] or 'Delayed on' in package[7]:
            second_delivery.append(package_value)
        if 'Wrong address' in package[7]:
            package[1] = '410 S State St'
            package[4] = '84111'
            final_delivery.append(package_value)
        if len(final_delivery) >= len(second_delivery) and package_value not in first_delivery and package_value not in second_delivery and package_value not in final_delivery:
            final_delivery.append(package_value)
        elif len(final_delivery) <= len(second_delivery) and package_value not in first_delivery and package_value not in second_delivery and package_value not in final_delivery:
            second_delivery.append(package_value)

        package_table.insert(package_key, package_value)


#Class that initializes the trucks with their respective leave times. Also, this will allow the code to keep track
#of the inventory and locations used. Algorithm is based on this class initialized.
class Truck:
    def __init__(self, packages, truck_leave_times):
        self.packages = packages
        self.speed = 18
        self.current_location = '4001 South 700 East'
        self.destination = ''
        self.total_miles = 0
        self.miles_at_time = '0'
        self.leave_times = datetime.combine(datetime.today().date(), datetime.strptime(truck_leave_times, '%H:%M').time())
        self.last_delivery = self.leave_times

# calculates the total possible miles the truck can travel in a given timeframe
    def set_miles_at_time(self, time):
        if time < self.leave_times:
            self.miles_at_time = 0
        self.miles_at_time = (int((time - self.leave_times).seconds / 60) * 18) / 60
        if self.miles_at_time < self.total_miles or len(self.packages) == 0:
            self.miles_at_time = self.total_miles
