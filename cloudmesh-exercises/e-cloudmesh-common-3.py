# fa19-516-160
# E.Cloudmesh.Common.3
# Task : Develop a program that demonstrates the use of FlatDict.

# Imports
from cloudmesh.common.FlatDict import FlatDict # import FlatDict

# Sample data
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


# Conversion to FlatDict and Print  data
flat_data = FlatDict(data[0])
print(type(flat_data))
print(flat_data)


#Code reference Introduction to python : Gregor von Laszewski.: section 6.4.2