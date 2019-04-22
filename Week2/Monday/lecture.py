

# myList = [1, 2, 3, 4]
# myList[2]

# myDictionary = {

#     "first_name" : "Veronica",
#     "last_name" : "Lino",
#     "isInstructor": True,
#     "isStudent": False
# }



# result = myDictionary.get("isStudent")

# print(result)

# if result != None:
#     print(f"key was found {result}")
# else:
#     print(f"key was not found")


# myDictionary["student"]

# result = myDictionary["isInstructor"]

# print(result)

# print(myDictionary["isInstructor"])


# my_dictionary = {
#     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
# }


# results = my_dictionary.items()

# print(results)

# for value in my_dictionary.items():
#     print(f"{value[1]}")
    # print(key)
    # print(value)

# dict_items([(key, value), (), ()])

# print(my_dictionary)
# del my_dictionary["hello"]
# print(my_dictionary)

# results = my_dictionary.values()
# print(results)

# for i in results:
#     print(i)

# results = my_dictionary.keys()

# print(results)

# for result in results:
#     print(result)

# print(my_dictionary)

# my_dictionary["hello"] = "Digital Crafts"

# print(my_dictionary)

# my_dictionary["school"] = "Digital Crafts"

# print(my_dictionary)

# isItThere = "hello" in my_dictionary
# # print(isItThere)

# if "wat" in my_dictionary:
#     print("found")
# else:
#     print("not found")

# contactList = [{},{},{}]

# contactList = [{
#     "first_name" : "Sabrina",
#     "last_name" : "Goldfarb",
#     "email": "sabrina@sabrina.com",
#     "phone": {
#         "work": "123-222-3333",
#         "cell": "222-222-2222"
#     }
# }, {

#     "first_name" : "Garrett",
#     "last_name" : "Weaver",
#     "email": "garrett@garrett.com",
#     "phone": {
#         "work": "333-333-3333",
#         "cell": "444-444-4444"
#     }
# }, {

#     "first_name" : "Alfie",
#     "last_name" : "Santos",
#     "email": "alfie@alfie.com",
#     "phone": {
#         "work": "555-555-5555",
#         "cell": "666-666-6666"
#     }
# }]


# result = contactList[0]["first_name"]
# result = contactList[1]["last_name"]
# result = contactList[2]["phone"]["cell"]

# contactList[3][""]

# print(result)

# while True:
#     try:
#         x = int(input("enter in a number >>"))
#         break
    
#     except ValueError:
#         print('oops try again')


# while True:
#     if True
#         try: 
#             x = int(input("enter in a number >>"))
#             break
#         except ValueError:
#             print('oops')
        
#     else:
#         print('oops')
#         break

# x = 10

# if x > 5:
#     raise Exception('this is custom error')


import pickle

# data = {'name': 'Paul'}

# with open('data.pickle', 'wb') as fh:
#   pickle.dump(data, fh)


with open('data.pickle', 'rb') as fh:
  data = pickle.load(fh)
#   print(data)

print(data["name"])