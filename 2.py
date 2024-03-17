import ast


dictionary = {"name":"Иван Иванов","ids":[1,2,3],"balance":12345}

r = str(dictionary)
data = eval(r)

print(data)