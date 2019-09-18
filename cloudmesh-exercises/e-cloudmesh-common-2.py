
# fa19-516-160
# E.Cloudmesh.Common.2
# Task : Develop a program that demonstrates the use of dotdict.

# Imports
from cloudmesh.common.dotdict import dotdict

# Sample JSON data
data = [
  {
  "name": "Shreyans",
  "course": "e516",
    "address" : {
      "city": "Bloomington" ,
      "state": "IN"
    }
  },

{
  "name": "Ronak",
  "course": "e260",
    "address" : {
      "city": "Indianapolis",
      "state": "IL"
    }
  }
]

# Convert to dotdict and Print JSON data
data_1 = dotdict(data[1])
print(type(data_1))
print(data_1)

