f = open('D:\johns\csv.csv','a')
import json

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
result = json.dumps(thisdict)
f.write(result)
f.close()
f = open('D:\johns\csv.csv','r')
print(f.read())