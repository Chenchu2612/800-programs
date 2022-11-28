# Serialization: the process of converting an object from python supported form into network supported or file supported form is called as serialization
# this conversion process by default considered as serializtion.
# import json

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


# Note: with open lo manam aliyas name istamu aa block motham aa aliyas name matrame vaaduthamu.

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

# separators yappudu tuple lo ivvali ledante ...error vastundi ... positional argument follows keyword arguments...

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
import json

'''
# Model : python to json

# 2. Write a Python program to convert Python object to JSON data.

# Exp: python dict_obj nunchi json_str (pd) json.dumps()....serialization to a json string.

python_obj = {
  "name": "David",
  "class":"I",
  "age": 6
}

import json
j_s = json.dumps(python_obj, indent=6, separators=("; ", "= "), sort_keys=True)

print(j_s)

'''
'''
# Model : python to json strings

# 3. Write a Python program to convert Python objects into JSON strings. Print all the values.

# Exp: pyhton object to json strings  (pd)...json.dumps().... serialization to a string.


python_dict =  {"name": "David", "age": 6, "class":"I"}
python_list =  ["Red", "Green", "Black"]
python_str =  "Python Json"
python_int =  (1234)
python_float =  (21.34)
python_T =  (True)
python_F =  (False)
python_N =  (None)

import json

json_dict = json.dumps(python_dict, indent=4, separators=("; ", ': '), sort_keys= False)
print(json_dict)
print(type(json_dict))

json_array = json.dumps(python_list, indent=2, separators=(":", "-"), sort_keys=False)
print(json_array)
print(type(json_array))

jsn_str = json.dumps(python_str, indent=4, separators=(", ",": "), sort_keys=False)
print(jsn_str)
print(type(jsn_str))


json_num = json.dumps(python_int, indent=4, separators=(": ", ", "), sort_keys=True)
print(json_num)
print(type(json_num))

json_fl = json.dumps(python_float, indent=4, separators=(",", ": "), sort_keys=True)
print(json_fl)
print(type(json_fl))

json_t = json.dumps(python_T, indent=4, separators=(': ', ', '), sort_keys=False)
print(json_t)
print(type(json_t))

# Note : in json True will become converts to true....capital true will becoms small true...

json_f = json.dumps(python_F, separators=(", ", ", "), sort_keys=False)

print(json_f)
print(type(json_f))

# Note: in json False will becomes false.... capital fall will becomes small false


json_n= json.dumps(python_N, separators=(", ",": "), sort_keys=True)

print(json_n)
print(type(json_n))

# Note: in json None will becomes null...

'''
'''
# Model: python to dict.

# 4. Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4

j_str = {'4': 5, '6': 7, '1': 3, '2': 4}

import json

js= json.dumps(j_str, indent=4, sort_keys=True)

print(js)

'''
'''
# Model : json to python

# 5. Write a Python program to convert JSON encoded data into Python objects.

# Exp : json to python mfjson load chestadu.... loads...json.loads()


jobj_dict =  '{"name": "David", "age": 6, "class": "I"}'
jobj_list =   '["Red", "Green", "Black"]'
jobj_string = '"Python Json"'
jobj_int = '1234'
jobj_float =  '21.34'


import json

python_dict=json.loads(jobj_dict)
print(python_dict)
print(type(python_dict))

for key, value in python_dict.items():
    print('{}:{}'.format(key, value))


python_list = json.loads(jobj_list)
print(python_list)
print(type(python_list))


pyton_str = json.loads(jobj_string)
print(pyton_str)
print(type(pyton_str))

python_int = json.loads(jobj_int)
print(python_int)
print(type(python_int))

python_fl = json.loads(jobj_float)
print(python_fl)
print(type(python_fl))

'''
'''
# Model : creating json from existing json.

# 6. Write a Python program to create a new JSON file from an existing JSON file.

# Exp : already existing file lo vunna json data ni tesukoni  new new json file lo create cheyyali.

# mundu existing data lo vunna json ni python object loki marchukoni tharuvata new file loki dump chesukovali.

with open('chenchu.json', 'r+') as f:
  data = json.load(f)

print(data)
print(type(data))




with open("new_files.json", 'w+') as f:
    json.dump(data, f, indent=4, separators=('; ', ': '), sort_keys=False)

'''
'''
# model: checking ccomplex or not

# 7. Write a Python program to check whether an instance is complex or not.

import json


def checking_complex(object):
    if isinstance(object, complex):
        return [object.real, object.imag]
    raise TypeError (repr(object)+"is not json serialized")


complex_obj =json.dumps(2, default=checking_complex)

print(complex_obj)


'''
'''

# New funcction ::: repr(objecct) >>>> ee function ichina objecct ni as it is ga string rupam lo print cheyyadaniki useavutundi.

a='chenchu_mahesh_ghattaneni'
print(repr(a))



#  8 is missing and it is difficult also


'''

'''
# Model :  accesing only unique key.

# 9. Write a Python program to access only unique key value of a Python object.

# Exp :  unique key value pair ni access cheyyali....ichindi json object danni python object ga convert cheste repeated key value anedi remove iepotundi.

python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print(type(python_obj))

import json

new= json.loads(python_obj)

print(new)

print(type(new))

'''