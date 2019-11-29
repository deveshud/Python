file = open('mydata','r') # file is opened for reading
#print(file.read()) # Reads all data
#print(file.readline()) # Reads single line
#print(file.readline()) # Reads single line
#print(file.readline()) # Reads single line

#file1 = open('mydata','a')
#file1.write('But I am trying my 20 %')

#copying data from 1 file to another

file1 = open('abc','w')

for data in file:
    file1.write(data)