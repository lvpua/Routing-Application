from datetime import datetime
import distance
import data

# Initiliazes the truck leave times and also the packages contained in each truck
truck_leave_times = ['08:00', '09:00', '10:20']
truck_1 = data.Truck(data.first_delivery, truck_leave_times[0])
truck_2 = data.Truck(data.second_delivery, truck_leave_times[1])
truck_3 = data.Truck(data.final_delivery, truck_leave_times[2])


#Updates the truck package status and determines how long the trucks will deliver all the packages.
def truck_delivery(truck, time_input):
    for package in truck.packages:
        package[8] = "Truck currently in Transit"
    truck.set_miles_at_time(time_input)
    while truck.total_miles < truck.miles_at_time:
        if len(truck.packages) == 0:
            break
        distance.nearest_distance(truck)


#Validates a time input from a user. This will ensure the leave time is accurate and if not, a package will not be loaded
#inside the truck. This also runs the delivery based on the the time input from the user.
def deliver_time(truck_time):
    if truck_time < datetime.combine(datetime.today().date(), datetime.strptime(truck_leave_times[0], '%H:%M').time()):
        return
    elif truck_time > datetime.combine(datetime.today().date(),
                                        datetime.strptime(truck_leave_times[2], '%H:%M').time()):
        truck_delivery(truck_1, truck_time)
        truck_delivery(truck_2, truck_time)
        truck_delivery(truck_3, truck_time)
        return
    elif truck_time < datetime.combine(datetime.today().date(),
                                        datetime.strptime(truck_leave_times[2], '%H:%M').time()):
        if truck_time < datetime.combine(datetime.today().date(),
                                        datetime.strptime(truck_leave_times[1], '%H:%M').time()):
            truck_delivery(truck_1, truck_time)
            return
        else:
            truck_delivery(truck_1, truck_time)
            truck_delivery(truck_2, truck_time)
            return



