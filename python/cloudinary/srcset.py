'''
This script takes in a json file with a list of objects. Each object contains a key called "url". From this key, string manipulation is perform to create a key:value scrset within the value.

The end product is a new json file which has a list of objects with those objets having a new key:value
'''
import json

# reading the data from the file
with open('wyghost.json') as f:
    data = f.read()


      
# reconstructing the data as a dictionary
js = json.loads(data)
for i in js["photo"]:
    url = i["url"]
    searchword = "upload/"
    searchwordafter = "/fortydegreewaters"

    searchwordindex = url.find(searchword) + len(searchword)
    searchwordafterindex = url.find(searchwordafter)

    srcsetsmall = url[:searchwordindex] + "c_scale,h_200,w_330" + url[searchwordafterindex:]
    srcsetmedium = url[:searchwordindex] + "c_scale,h_450,w_640" + url[searchwordafterindex:]
    srcset = srcsetmedium + " 640w, " + srcsetsmall + " 320w"

    i["srcset"] = srcset

    # a = i["url"].find('upload/')
    # b = i["url"].find(searchwordafter)
    # print(str(a) + "\t" + str(i["url"][a + len(searchword)]))
    # c = i["url"][:a + len(searchword)] + "Asdfadsf" + i["url"][b:]
    # print(i["url"][:a + len(searchword)])
    # print(c)
    # print(i)
    print()
  
# Serializing json
json_object = json.dumps(js, indent=4)
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)


# f = open("./wyghost.js", "r")
# print(f.read())
