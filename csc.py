
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














