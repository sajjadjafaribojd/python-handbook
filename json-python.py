import json

#Parse JSON - Convert from JSON to Python
user_request='{"name":"sajjad","family":"jabj","age":25}'

convert_to_dic=json.loads(user_request)
print(convert_to_dic)
print(convert_to_dic["name"])

#Convert from Python to JSON
mydic={"name":"sajjad","family":"jafari","age":25}

# convert into JSON:
response_user=json.dumps(mydic)

print(response_user)

print(json.dumps(31.76))

#print(json.dumps(x))
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
print(json.dumps(x, indent=4, separators=(", ", " = ")))