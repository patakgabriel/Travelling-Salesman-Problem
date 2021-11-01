from ReadCSV import *

#Call functions to populate tables
read_distance_table()
read_package_table()

#Manually load the trucks
first_truck_packages = ['15','1','13','14','16','20','19','29','30','34','37','40','2','35','33','31']
second_truck_packages = ['6', '25', '28', '32', '3', '18', '36', '38']
third_truck_packages = ['4','5','7','8','9','10','11','12','17','21','22','23','24','26','39','27']

#Fix wrong address
all_package_values.lookup(9).set_address('410 S State St')
all_package_values.lookup(9).set_zip('84111')

#Tracks sum of all trucks
total_distance = 0

#Method to return total distance
#Time Complexity: O(1)
def get_total_distance():
    return total_distance

#Method to start the Nearest Neighbor algorithm for truck 1.
#It loops through each package and calculates the distance to each other package on ther truck.
#It will save the lowest distance and package ID until the loop is completed
#The time and distance effort are calculated, and the package is removed from the truck.
#The address of the package we removed will become our current address to start the loop again.
#If there are no packages left, set destination back to HUB.
#Time complexity: O(N) + O(N) + O(N^2) = O(N^4)
def first_truck_run():
    global total_distance
    distance = 0
    origin_location = 'HUB'
    lowest_distance = 200
    first_truck_time = 8
    for i in range(len(first_truck_packages)):#Time complexity: O(N)
        for package in first_truck_packages:  #Time complexity: O(N)
            dest_location = all_package_values.lookup(int(package)).get_address() #Time complexity: O(N^2)
            distance = address_lookup(origin_location,dest_location)
            if distance < lowest_distance:
                lowest_distance = distance
                current_package = package


        all_package_values.lookup(int(current_package)).set_truck('1')
        first_truck_time += lowest_distance/18
        dest_location = all_package_values.lookup(int(current_package)).get_address()
        total_distance += address_lookup(origin_location,dest_location)
        all_package_values.lookup(int(current_package)).set_status('Delivered')
        all_package_values.lookup(int(current_package)).set_time_delivered(first_truck_time)
        origin_location = dest_location
        first_truck_packages.remove(current_package)
        lowest_distance = 200
        if len(first_truck_packages) == 0:
            distance = address_lookup(origin_location,'HUB')
            first_truck_time += distance/18
            total_distance += distance
            
        
#Method to start the Nearest Neighbor algorithm for truck 2.
#It loops through each package and calculates the distance to each other package on ther truck.
#It will save the lowest distance and package ID until the loop is completed
#The time and distance effort are calculated, and the package is removed from the truck.
#The address of the package we removed will become our current address to start the loop again.
#If there are no packages left, set destination back to HUB.
#Time complexity: O(N) + O(N) + O(N^2) = O(N^4)
def second_truck_run():
    global total_distance
    distance = 0
    origin_location = 'HUB'
    lowest_distance = 200
    second_truck_time = 9.09
    for i in range(len(second_truck_packages)): #Time complexity: O(N)
        for package in second_truck_packages:   #Time complexity: O(N)
            dest_location = all_package_values.lookup(int(package)).get_address()   #Time complexity: O(N^2
            distance = address_lookup(origin_location,dest_location)
            if distance < lowest_distance:
                lowest_distance = distance
                current_package = package


        all_package_values.lookup(int(current_package)).set_truck('2')
        second_truck_time += lowest_distance/18
        dest_location = all_package_values.lookup(int(current_package)).get_address()
        total_distance += address_lookup(origin_location,dest_location)
        all_package_values.lookup(int(current_package)).set_status('Delivered')
        all_package_values.lookup(int(current_package)).set_time_delivered(second_truck_time)
        origin_location = dest_location
        second_truck_packages.remove(current_package)
        lowest_distance = 200
        if len(second_truck_packages) == 0:
            distance = address_lookup(origin_location,'HUB')
            second_truck_time += distance/18
            total_distance += distance
            
#Method to start the Nearest Neighbor algorithm for truck 3.
#It loops through each package and calculates the distance to each other package on ther truck.
#It will save the lowest distance and package ID until the loop is completed
#The time and distance effort are calculated, and the package is removed from the truck.
#The address of the package we removed will become our current address to start the loop again.
#If there are no packages left, set destination back to HUB.
#Time complexity: O(N) + O(N) + O(N^2) = O(N^4)
def third_truck_run():
    global total_distance
    distance = 0
    origin_location = 'HUB'
    lowest_distance = 200
    third_truck_time = 10.33
    for i in range(len(third_truck_packages)):  #Time complexity: O(N)
        for package in third_truck_packages:    #Time complexity: O(N)
            dest_location = all_package_values.lookup(int(package)).get_address()   #Time complexity: O(N^2
            distance = address_lookup(origin_location,dest_location)
            if distance < lowest_distance:
                lowest_distance = distance
                current_package = package


        all_package_values.lookup(int(current_package)).set_truck('3')
        third_truck_time += lowest_distance/18
        dest_location = all_package_values.lookup(int(current_package)).get_address()
        total_distance += address_lookup(origin_location,dest_location)
        all_package_values.lookup(int(current_package)).set_status('Delivered')
        all_package_values.lookup(int(current_package)).set_time_delivered(third_truck_time)
        origin_location = dest_location
        third_truck_packages.remove(current_package)
        lowest_distance = 200
        if len(third_truck_packages) == 0:
            distance = address_lookup(origin_location,'HUB')
            third_truck_time += distance/18
            total_distance += distance
