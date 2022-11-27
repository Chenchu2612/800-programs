# Serialization: the process of converting an object from python supported form into network supported or file supported form is called as serialization
# this conversion process by default considered as serializtion.
import jsn

# Deserialization : the process of converting an object from file supported form or network supported form into python object is called as deserialization

# pickle module is used for serializing and deserializing.



# what is json ?

# ans):  json- java script object notation ... the most commonly used message formate for applications irrespective of language ...

# any programming language can understand json.

# json is similar to python dictionary objects ....jason contains group of key value pairs.

# i) The biggest specality of json is any programming language can understand the json

# ii) light weight and required less memory to store data

# There are mainly four functions in json :

# a)json.dumps(): converting an python dict object to the json string.  (serialization to a string (Here string is nothing but json string))

# coding : json.dumps(dict_obj, indent = num, separator = (", ", ": "), sort_keys = True/False)

# b) json.dump(): converting an python dict object to a json string and write that json to provided jason file. (serialization to a file)

# code : with open('emp.json', 'w+') as f :
#             json.dump(python_dict_object, f, indent=num, separator= (", ", ": "), sort_keys = True/False)

# kotha file okati open iyyi dantao json objecct save avutundi...

# manam koasari aliyas name ichinappudu aa entire code lo danne vadali...ex: f


# c) json.loads(): converting an json string to an python dict obj ... (deserialization from string)

# code : dict_obj=json.loads(json_str)

# for key, value in dict_obj.items():
#         print('{},{}'.format(key,value)

# d) json.load(): Reading json string from a file and converting to python dict_object (deserialization from a file)
# with open('emp.json', 'r+') as f:
#         dict_obj = json.load(f)

# for key, value in dict_obj.items():
#     print('{},{}'.format(key, value)


# json is a syntax for sorting and exchanging data, json text is written in Javascript object notation.


# if you want to work with json in python we have to import json module. (import json)

# python to json :- dumps ::: json.dump()

# json to python :- load ::: json.load()

# when you convert python to json  python objects are converted into json(javascript) objects.

# trick : mfjson load chestunnadu..... pd...


# json.dumps(python_obj, indent = num, separators = (". ", " = ") , sort_keys = True)


# indent = number of indentations.
# separators are used to separate each object and the each key value. default is (", ", ": ") it means each object is separated comma and space---
# and each key value pair is separated by colon (:) and space
# sort_keys is used to sort the keys (sort_keys= True or False) ...the sort_keys parameter to specify if the result should be sorted or not.


'''


# Questions:

# Model : JSON data to python object.

# 1. Write a Python program to convert JSON data to Python object.

# Exp: json string nunchi dictionary object ga marchali... so json loads.....(deserialization from string)

json_obj = '{ "Name":"David", "Class":"I", "Age":6 }'

import json

student_dict = json.loads(json_obj)

print(student_dict['Name'])
print(student_dict['Class'])

for key, value in student_dict.items():
    print(key, value)



# NOTE : nenu json file ni import chesnappudu attribute error vacchindi... endukante nenu python file json.py ane perutho create chesanu
# inbuild module json.py and nenu create chesina file json.py so error due to  circular import ani vastundi.

#  conclusion: python inbuilt names meeda manam eami create cheyyakudadu.

'''

# Model : python to json

# 2. Write a Python program to convert Python object to JSON data.

# Exp:

python_obj = {
  "name": "David",
  "class":"I",
  "age": 6
}





