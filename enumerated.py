import subprocess
import json

with open('Names.json', 'r') as names:
  namejson = json.load(names)
with open('Summaries.json', 'r') as summaries:
  summaryjson = json.load(summaries)
with open('categorynames.json', 'r') as category:
  categoryjson = json.load(category)

jsonout = {}
for x in range(len(namejson)):
	if type(namejson) != type([]):print(namejson)
	if type(summaryjson) != type([]):print(summaryjson)
	if type(categoryjson) != type([]):print(categoryjson)
	jsonout[f"Club {x}"] = {"Name": namejson[x], "Summary": summaryjson[x], "Categories": categoryjson[x]}

print(jsonout)