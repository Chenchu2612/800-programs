
# Q) What is csv files ?

# Ans)

# CSV = (Comma Separated Values)

# CSV is a simple file format used to store tabular data, such as spreadsheet or database.

#  A CSV file stores tabular data (numbers and text) in plain text.

#  Each line of the file is a data record(row). Each record consists of one or more fields(column), separated by commas.

#  The use of the comma as a field separator is the source of the name for this file format.

# if you want work with csv files in python you have to import csv module (import csv).

# THERE ARE TWO IMPORTANT CODES RELATES TO CSV FILE.

# a) WRITING DATA TO CSV FILE

# b)READING DATA FROM CSV FILE


# 1. WRITING DATA TO CSV FILE:

# 1. step.1 :- csv file open cheyyali with command tho and important eamiti ante ikkada newline = "" ani pettali ledante prathi row madhya lo ---
#              emepty spaces vastundi (blank lines)

# 2. step.2 :- creating csv writer object w_obj = csv.writer(filename)

# 3. step.3 :- writing the data => w_obj.writerow([***************]) manam data ni write row method lo enter chestamu...
#              first line vachi headding. prathi row manam list lo enter chestamu. comma saparated values tho.

"""
import csv

with open('chenchu.csv', 'w+', newline="") as f:
    writer_obj = csv.writer(f)  # initialize csv writer object
    print(writer_obj)   # for understanding purpose ..... it will returns the writer object <_csv.writer object at 0x000002204A2B4A00>
    writer_obj.writerow(['NAME', 'AGE'])  # writing rows
    n= int(input("ENter the number of employees :"))
    for i in range(n):
        name = input('ENter the name :')
        age= input("Enter the age :")
        writer_obj.writerow([name, age])
print("THE employee details are saved succesfully")

"""
import csv

"""
import csv

# b)READING DATA FROM CSV FILE

# step:-1 open the existing csv file. as read mode  a= open("filename","mode")

# step:- 2 reader object ni initialize cheyyali. red_obj = csv.reader(a)

# step :- 3 dentlo data manam list rupam lo ekkistamu kabatti prathi row manaki list rupam lo vuntundi ee list's ni anni inko list's lo tesukuntam
#           data = list(red_obj) >>> dentlo ippudu manaki nested list vastundi.



with open('csv file', 'r', newline = '') as f :
b = csv.reader(f, delimeter =",")   # initializing the reader object.

# delimiter: A one-character string used to separate fields. It defaults to ','.
  
print(b)       # >>>> it returns the reader object.
data = list(b)    # making list of all the records...

for row in data:    # accessing every row.
    for word in row: # accessing every field in the row.
        print(word, '\t', end=" ")
"""

# csv.reader() >>> to create reader object.

# csv.writer() >>>> to create writer object.

# for writer newline = "" is important .... for reader end="" is important
"""
file = open("chenchu.csv", 'r')

red_obj = csv.reader(file, delimiter ="," )

data = list(red_obj)

for row in data:
    for field in row:
        print(field, '\t', end="")
"""

# red_obj = csv.DictReader(open('filename')) >>> reader object ni create chestundi.... every row ni dictionary laga print chestundi...


"""
# 1. Write a Python program to read each row from a given csv file and print a list of strings
import csv

# Exp: join function will plays important rows here .... list lo vunna strings anni kalapa daniki join function vaadatharu.

with open("chenchu.csv", newline='',) as f :
    red= csv.reader(f)
    data = list(red)
    for row in data:
        print(','.join(row))
"""
"""
# Model: tab deimeter ga vunna csv files ni read cheyyali...

# delimeter ante each field saparete chesedi....ikkada tab saparate chestundi....

# 2. Write a Python program to read a given CSV file having tab delimiter.


# delimiter pycham lo radu manam type cheyyali..... spelling correct ga type cheyyali.

with open('filename.csv', newline="") as f:
    red = csv.reader(f, delimiter='\t')
    data = list(red)
    for row in data:
        print(','.join(row))

"""
"""
# Model : read csv file as list.

# 3. Write a Python program to read a given CSV file as a list.

# Exp: motham csv file ni list laga read cheyyamannadu ...okkoka row ni kaadu...entire in a list

import csv
with open('chenchu.csv', "r", newline="") as f:
    red = csv.reader(f)
    data = list(red)
print(data)

"""
"""
# Model : read csv as dict

# 4.Write a Python program to read a given CSV file as a dictionary.

# Exp: every row dict laga print avvali... 

# new func = csv.DictReader(open("filename")) >>>  returns each row as dicctionary.

import csv

red_obj = csv.DictReader(open("chenchu.csv"))  #>>> creating reader object... it always returns the readerobject...
print(red_obj)   #  for understanding purpose it prints reader object <csv.DictReader object at 0x0000021E8B042C10> ... 
for row in red_obj :  # object nunchi okkoka row ni print cheyyadaniki manam for loop vadathamu.
    print(row)

"""

"""
# Model : skipping initial spaces.

# 5. Write a Python program to read a given CSV files with initial spaces after a delimiter and remove those initial spaces
import csv

with open('chenchu.csv', 'r') as f:
    red= csv.reader(f, skipinitialspace=False) # with initial spaces after delimeter.
    for data in red:
        print(data)
        

with open('chenchu.csv', 'r') as f:
    red = csv.reader(f, skipinitalspace=True) # without initial spaces.
    for data in red:
        print(data)

"""
"""
# not understanding

# 6. Write a Python program that reads a CSV file and remove initial spaces, quotes around each entry and the delimiter.

import csv

csv.register_dialect('csv_dialect', delimiter='|', skipinitailspace=True, quoting=csv.QUOTE_ALL)

# not understanding

"""
"""
# Model: Reading csv file and printing onlly specified columns.

# 7. Write a Python program to read specific columns of a given CSV file and print the content of the columns.

# Exp: manam csv file lo specific fields matrame kavali.


# Exp: ikkada DictReader object ni create cheyyali....dantlo manaki eadi kavalo manam dictionary key method dwara get chesukovocchunu.

import csv

with open('chenchu.csv', 'r') as f:
    red = csv.DictReader(f)
    for row in red:
        print(row['department_name'])

"""

"""
# Model : 1. skipping headder of the file
#         2. print number of rows and field names.

# 8. Write a Python program that reads each row of a given csv file and skip the header of the file. Also print the number of rows and the field names.

# For skipping the headder file : fields = next(red)

# number of rows = readerobj.line_num  .... Our csv_reader_object has a method called line_num that returns the number of lines in our CSV.
# NOte :- idi last line yokka number ni return chestundi.....

#

import csv

with open('chenchu.csv', newline='') as f:
    reader_obj = csv.reader(f)
    fields = next(reader_obj)     # its like a pop function in removes the headding part and returns it
    for data in reader_obj:
        print(','.join(data))

    print('no of lines :', reader_obj.line_num)  # idi manam enno line lo vunnamo return chestundi.
    print('field names:',  ','.join(fields))

"""
"""
# Model : create writer object , write, print it .

# 9. Write a Python program to create an object for writing and iterate over the rows to print the values


import csv

with open ('chenchu.csv', 'w+', newline="") as f:
    wrt = csv.writer(f)
    wrt.writerow(('s.no', 'date', 'event'))
    for i in range(5):
        s_no = i+1
        date = input("Enter the date :")
        event = input('Enter the event :')
        wrt.writerow((s_no, date, event))

with open('chenchu.csv', newline="") as f:
    red = csv.reader(f)
    for data in red:
        print(', '.join(data))

"""

"""
# Model : writing list of list to a csv file (nested_lists) and read those csv file.

# 10. Write a Python program to write a Python list of lists to a csv file. After writing the CSV file read the CSV file and display the content.


# Exp: python lo csv file lo prathi row manaki list rupam lo chupistundi and motham data kalipi oka list rupam lo cupistundi...so list lopala ---

#     every row oka nested list's  list lopala nested lists.

import csv

data = [[10, 'a1', 1], [12, 'a2', 3], [14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]

with open('chenchu.csv', 'w+', newline='') as f:
    wrt = csv.writer(f, delimiter=',')
    wrt.writerows(data)   # csv lo prathi row oka list and motham data kalipi oka list lo vuntundi ... so list lopla nested lists

with open('chenchu.csv', newline="") as f:
    red = csv.reader(f)
    for data in red:            # for loop can be used to extract values from the iterator object
        print(', '.join(data))

"""

"""
# Model : dict data ni csv loki marchali. and ela read cheyyali.

# 11. Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the conten

# Exp: oka dict data ni csv loki marchali ante mundu column names field names initialize cheyyali....

# tharuvatha column names or field names ni initialize cheyyali....


# csv.DictReader() is used to create csv dict reader object for reading data as dictionary from csv file


# csv.DictWriter() is used to create  csv DictWriter ..this writer object is used to write dict data to the csv file ... 

# keys are filed names ...we have to initialize this first.... and them write rows...

csv_columns = ['id', 'Column1', 'Column2', 'Column3', 'Column4', 'Column5']
dict_data = {'id': ['1', '2', '3'], 'Column1': [33, 25, 56], 'Column2': [35, 30, 30], 'Column3': [21, 40, 55], 'Column4': [71, 25, 55], 'Column5': [10, 10, 40]}

import csv 

try:
    with open('chenchu.csv', 'w+') as f:
        wrt = csv.DictWriter(f, fieldnames=csv_columns)   # dict writer object ni initialize cheyyali...
        wrt.writeheader()    # heading ni rayali. (field names)
        for data in dict_data:
            print(data)  # only keys it will prints.
            wrt.writerow(dict_data)
except IOError:
    print('I/O error')


data = csv.DictReader(open('chenchu.csv'))   # reading data from csv as dict
for dat in data:
    print(dat)

"""















