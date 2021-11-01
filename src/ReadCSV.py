import csv
import operator
from Package import Package
from ChainHash import ChainHash

all_package_values = ChainHash()
distance_dict = dict()

#Method to sort the distance per address to the other ones
#Time complexity: O(N)
def sort_row(row):
    distance_sorted_dict = dict()
    del row['DISTANCE']
    
    for key, value in row.items():
        row[key] = float(value)
        
        
    for item in sorted(row.items(), key=operator.itemgetter(1)):
        distance_sorted_dict.update({item[0]: item[1]})
    return distance_sorted_dict

#Method to calculate the distance between two addresses
#Time complexity: O(1)
def address_lookup(origin, dest):
    origin_list = distance_dict.get(origin)
    dist_to_dest = origin_list.get(dest)
    return dist_to_dest


#Method to read distance table and set distance dictionary
#Time complexity: O(N^2)
def read_distance_table():
    with open('../C950/input/DistanceData.csv', newline = '', encoding = 'utf-8-sig') as csvdistance:
        distance_data = csv.DictReader(csvdistance)


        for row in distance_data:
            distance_dict.update({row['DISTANCE']: sort_row(row)})
            
#Method to read package table and set package hash table
#Time complexity: O(N)
def read_package_table():
    with open('../C950/input/PackageData.csv', newline ='', encoding="utf-8-sig") as csvpackage:

        package_data = csv.reader(csvpackage, delimiter=',')

        for row in package_data:
            package = Package(row)
            if package.get_ID().isnumeric():
                all_package_values.insert(package.get_ID(), package)
    

