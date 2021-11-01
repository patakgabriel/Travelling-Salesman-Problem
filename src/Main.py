#Gabriel Fernandez Patak 
#Student ID: 001534128

from Delivery import *

#Call methods to run the algorithm
first_truck_run()
second_truck_run()
third_truck_run()

#Variables to manage menu
package_list = {}


#Main menu to navigate through 4 different options
#Time complexity: O(N) + O(N^2) = O(N^3)
def main_menu():
    menu = True
    #Time complexity: O(N)
    while(menu):
        try:
            selection = int(input("\n1) View all packages \n" +
                              "2) Status between specific time \n" +
                              "3) View total distance \n" +
                              "4) Exit \n"+
                              "Choose: "))
            #It shows the whole list of delivered packages
            #Time complexity: O(N^2)   
            if selection == 1:
                print ("{:<5} {:<40} {:<10} {:<20} {:<10} {:<10} {:<10} {:<10}".format('ID','Address','Deadline','City','Zip Code','Weight','Status','Time Delivered'))
                for i in range(len(all_package_values.hash_table)):
                    for package in all_package_values.hash_table[i]:
                        
                        formatted_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(package.get_time_delivered() * 60, 60))
                        package_list[int(package.get_ID())] = "{:<5} {:<40} {:<10} {:<20} {:<10} {:<10} {:<10} {:<10}".format(package.get_ID(), package.get_address(), package.get_deadline(),
                                                                                                                              package.get_city(),package.get_zip(),package.get_weight(),package.get_status(), formatted_time)
                #Time complexity: O(N) 
                for key in sorted(package_list):
                    print(package_list[key])

            #It shows the packages status at certain time       
            #Time complexity: O(N)
            elif selection == 2:        
                invalid_time = True
                while(invalid_time):
                    try:
                        report_time = input('Enter time (HH:MM 24h format): ')
                        report_hour = int(report_time[0:2])
                        if report_hour >= 0 or report_hour < 24:
                            report_minute = int(report_time[3:5])
                            if report_minute >= 0 or report_minute < 60:
                                        invalid_time = False
                    except:
                        print('Invalid input')
                        
                report_time = report_hour + (report_minute * (1/60))

                print ("{:<5} {:<40} {:<10} {:<20} {:<10} {:<10} {:<20} {:<10}".format('ID','Address','Deadline','City','Zip Code','Weight','Status','Time Delivered'))
                #Time complexity: O(N^2)
                for i in range(len(all_package_values.hash_table)):
                    for package in all_package_values.hash_table[i]:
                        pack_time = package.get_time_delivered()
                        formatted_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(pack_time * 60, 60))
                        if package.get_ID() == '9' and report_time < 10.33:
                            package_list[int(package.get_ID())] = "{:<5} {:<40} {:<10} {:<20} {:<10} {:<10} {:<20}".format(package.get_ID(), '300 State St', package.get_deadline(),
                                                                                                                                 package.get_city(),'84103',package.get_weight(),'At hub')
                            break
                        if pack_time <= report_time:
                            package_list[int(package.get_ID())] = "{:<5} {:<40} {:<10} {:<20} {:<10} {:<10} {:<20} {:<10}".format(package.get_ID(), package.get_address(), package.get_deadline(),
                                                                                                                                  package.get_city(),package.get_zip(),package.get_weight(),package.get_status(), formatted_time)
                        elif (package.get_truck() == '1' and 8 <= report_time) or (package.get_truck() == '2' and 9.09 <= report_time) or (package.get_truck() == '3' and 10.33 <= report_time):
                            package_list[int(package.get_ID())] = "{:<5} {:<40} {:<10} {:<20} {:<10} {:<10} {:<20}".format(package.get_ID(), package.get_address(), package.get_deadline(),
                                                                                                                                  package.get_city(),package.get_zip(),package.get_weight(),'In Transit')
                        else:
                            package_list[int(package.get_ID())] = "{:<5} {:<40} {:<10} {:<20} {:<10} {:<10} {:<20}".format(package.get_ID(), package.get_address(), package.get_deadline(),
                                                                                                                                  package.get_city(),package.get_zip(),package.get_weight(),'At hub')
                #Time complexity: O(N)
                for key in sorted(package_list):
                    print(package_list[key])
            #It shows the total miles traveled by trucks
            elif selection == 3:
                print("\n" + str(get_total_distance()) + ' miles')
            #Exits menu    
            elif selection == 4:
                menu = False
            else:
                print("\nInvalid option.")
        except:
            print("\nInvalid option")



if __name__ == '__main__':
    main_menu()


