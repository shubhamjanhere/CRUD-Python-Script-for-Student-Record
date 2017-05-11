__author__ = "Shubham Jain"
"""
Implement a cache that on start-up would load data from a file into the cache. The cache would have an initial size of 20 
elements and upon reaching its limit, to add any new element it would remove the least recently accessed element. On shutdown 
it should store the cached data back to the file. The data should be stored in the cache according to a caching strategy. 
Provide options for cache CRUD. Testing Dataset : records of students. You need to create the test dataset. The student 
record would have data such as - their ID's, classes enrolled and marks obtained in them. The records should be cached 
in a sorted manner according to the student marks.

#Note - Initially, the cache is empty. You have to load data into cache, and maximum size of cache is 20

Reason for choosing list for implementing cache - 
    # Important thing about a list is that items in a list need not be of the same type.
    # There are a lot of ready-made methods available for list
    # Insertion and deletion node operations are easily implemented in a list.
    # There is no need to define an initial size for a linked list.
    # List can grow and shrink during run time.
    # Efficient memory utilization
    # Faster Access time
"""
import csv
# The limit of the cache is 20 and initially it is having 0 elements. YOu can add the elements as needed.
class student_marks(object):
    def __init__(self):
        self.cache_max_size = 20
        #Initialize cache with 20 elements
        self.marks_cache = []

    #For reading the data from a file
    def read_from_file(self,name = 'Marks.csv'):
        with open(name, 'r') as f:
            csv_file = csv.reader(f)
            data = list(csv_file)
        #Case1- When file has more than 20 elements or the size of cache, we replace the whole cache with first 20 elements of file
        if len(data) > self.cache_max_size:
            self.marks_cache = data[:self.cache_max_size]
        # Case2- When csv_file has less than 20 elements, we append elements on First Come First Serve basis
        elif len(data) < self.cache_max_size:
            self.marks_cache = self.marks_cache[0:len(data)]
            for row in data:
                self.marks_cache.append(row)
        #Sorting according to marks
        self.marks_cache.sort(key=lambda x: x[3])

   #For creating the data
    def create_data(self):
        print("Enter the data in format - USN (1RN13CS088), Name (Shubham), Class (CSE) and Marks out of 100 (78) that needs to be added")
        student_details = []
        for counter in range(4):
            student_details.append(input())
        if len(self.marks_cache)<self.cache_max_size:
            self.marks_cache.append(student_details)
        else:
            self.marks_cache.pop(0)
            self.marks_cache.append(student_details)
        self.marks_cache.sort(key=lambda x: x[3])

    def delete_data(self):
        print("Bellow is the list of USN in Cache")
        print(self.marks_cache)
        print("Enter the USN eg, '1RN13CS088' ie, roll no. that needs to be deleted")
        student_usn = input()
        for index in range(len(self.marks_cache)):
            if student_usn == self.marks_cache[index][0]:
                index_flag = index #Only one index will be there, since USN cannot be the same for any 2 students
        self.marks_cache = self.marks_cache[:index_flag] + self.marks_cache[index_flag+1:]
        self.marks_cache.sort(key=lambda x: x[3])

    def update_data(self):
        print("Bellow is the list of USN in Cache")
        print(self.marks_cache)
        print("Enter the USN, Name, Class and Marks,eg, '1RN13CS006', 'Naman', 'CSE', '74',that needs to be updated")
        student_detail = []
        for counter in range(4):
            student_detail.append(input())
        for index in range(len(self.marks_cache)):
            if student_detail[0] == self.marks_cache[index][0]:
                index_flag = index #Only one index will be there, since USN cannot be the same for 2 students
        self.marks_cache[index_flag] = student_detail
        print(self.marks_cache)
        self.marks_cache.sort(key=lambda x: x[3])

    # Reads the data from Cache
    def read_data(self):
        print("The data in the cache is as follows-")
        for student in self.marks_cache:
            print(', '.join(student))

    def save_before_exit(self,name = 'Marks.csv'):
        with open(name, 'r') as f:
            csv_file = csv.reader(f)
            data = list(csv_file)
        cache_index_list = []
        data = [x for x in data if x != []]
        for cache_element in self.marks_cache:
            cache_index = 0
            for data_element in data:
                if data_element[0]==cache_element[0] and data_element[1]==cache_element[1] and data_element[2]==cache_element[2] and data_element[3]==cache_element[3]:
                    cache_index_list.append(cache_index)
            if cache_index<self.cache_max_size:
                cache_index += 1
        for index in cache_index_list:
            del self.marks_cache[index]
        if cache_index != []:
            data.extend(self.marks_cache)
        for index in range(len(data)):
            data[index] = ','.join(data[index])
        with open(name, 'w') as myfile:
            wr = csv.writer(myfile,delimiter='\n')
            wr.writerow(data)

    def main_function(self):
        print("Following are the choices - \nEnter 1 for loading records from file to cache \nEnter 2 for adding new records "
              "\nEnter 3 for deleting data from cache \nEnter 4 for updating a record in cache \nEnter 5 for reading data from cache "
              "\nEnter 6 for saving all data from cache to disk \nEnter 7 for exit")
        key = None
        while (key != 7):
            try:
                key = int(input("Please press an option"))
            except:
                print("You have entered wrong")
            if key == 1:
                self.read_from_file()
            elif key == 2:
                self.create_data()
            elif key == 3:
                self.delete_data()
            elif key == 4:
                self.update_data()
            elif key == 5:
                self.read_data()
            elif key == 6:
                self.save_before_exit()
            elif key == 7:
                break

if __name__ == '__main__':
    obj = student_marks()
    obj.main_function()



