#This classes allows us to create package objects
class Package(object):
    #Default constructor of the class. It sets initial values from a list argument.
    #Time complexity: O(1)
    def __init__(self, package):
        self.ID = package[0]
        self.address = package[1]
        self.city = package[2]
        self.zip = package[4]
        self.deadline = package[5]
        self.weight = package[6]
        self.notes = package[7]
        self.delivery_status = 'At Hub'
        self.time_delivered = None
        self.truck = None
        
    #Method to set package address
    #Time complexity: O(1)
    def set_address(self, address):
        self.address = address
    
    #Method to get package address
    #Time complexity: O(1)
    def get_address(self):
        return self.address

    #Method to get package ID
    #Time complexity: O(1)
    def get_ID(self):
        return self.ID
    
    #Method to get package city
    #Time complexity: O(1)
    def get_city(self):
        return self.city
    
    #Method to get package zip code
    #Time complexity: O(1)
    def get_zip(self):
        return self.zip
    
    #Method to set package zip code
    #Time complexity: O(1)
    def set_zip(self, zip):
        self.zip = zip
    
    #Method to get package deadline
    #Time complexity: O(1)
    def get_deadline(self):
        return self.deadline
    
    #Method to get package status
    #Time complexity: O(1)
    def get_status(self):
        return self.delivery_status
    
    #Method to set package status
    #Time complexity: O(1)
    def set_status(self, new_status):
        self.delivery_status = new_status
    
    #Method to set time delivered
    #Time complexity: O(1)
    def set_time_delivered(self, time):
        self.time_delivered = time
    
    #Method to get time delivered
    #Time complexity: O(1)
    def get_time_delivered(self):
        return self.time_delivered
    
    #Method to get package notes
    #Time complexity: O(1)
    def get_notes(self):
        return self.notes
    
    #Method to get package weight
    #Time complexity: O(1)
    def get_weight(self):
        return self.weight
    
    #Method to set the assigned truck for the package
    #Time complexity: O(1)
    def set_truck(self, truck):
        self.truck = truck
        
    #Method to get the assigned truck for the package
    #Time complexity: O(1)
    def get_truck(self):
        return self.truck
