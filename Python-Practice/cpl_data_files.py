# creates a empty file in the directory
import shelve
from cpl_classes import time
import pickle
out_file = open('mydata.txt', 'w')
# add lines to the file
out_file.write('Hello\n')
out_file.write('World!')
# writes the data temporarily in the file
out_file.flush()
# close the file
out_file.close()

# writing content to the file

out_file = open('mydata.txt', 'a')  # opening the file in append mode
weekends = ['\nSaturday', ' ,Sunday']
out_file.writelines(weekends)
out_file.close()


# reading the data from files

in_file = open('mydata.txt', 'r')
in_file.read()
in_file.tell()  # tell functions tell you where you are in the file
in_file.seek(0)  # changes the position to 0 byte
in_file.write('Hi ')  # reading and writing at he same time
print(in_file.readline())

print(in_file.readlines())

in_file.close()

# two other way of opening the file r+ and w+


in_file = open('mydata.txt', 'r+')
print(in_file.readline())
in_file.tell()  # tell functions tell you where you are in the file
in_file.seek(0)  # changes the position to 0 byte
in_file.write('Hi ')  # reading and writing at he same time
in_file.seek(0)
print(in_file.readline())
in_file.close()


# pickling and shelves
# pickling to string
myTime1 = time()
myTime1.set_time(1, 2, 3)
pickled_time = pickle.dumps(myTime1)
print(pickled_time)

unpickled_time = pickle.loads(pickled_time)
unpickled_time.print_time()

# pickling to a file
myTime1 = time()
myTime1.set_time(1, 2, 3)
out_file = open('data.txt', 'wb')
pickled_time = pickle.dump(myTime1, out_file)
out_file.close()

in_file = open('data.txt', 'rb')
# unpickling
unpickled_time = pickle.load(in_file)

unpickled_time.print_time()

# shelves
db_file = shelve.open('letters.txt', 'c')
db_file['vowels'] = ['a', 'e', 'i', 'o', 'u']
db_file['end'] = ['x', 'y', 'z']

print(list(db_file.keys()))
print("Original containing vowels:", 'vowels' in db_file)
del db_file['vowels']
print("After deleting vowels:", 'vowels' in db_file)
print(list(db_file.keys()))
db_file.close()
