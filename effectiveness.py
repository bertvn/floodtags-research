import json

with open("annotated.json", encoding="utf8") as anno:
	data = json.load(anno)["tags"]

annotations = {}
	
for tweet in data:
	if tweet["annotation"] not in annotations:
		annotations[tweet["annotation"]] = 1
	else:
		annotations[tweet["annotation"]] += 1

for key in annotations.keys():
	print(key, " : ", annotations[key])
	
print("-" * 79)
score = {}
results = []
files =["top 10.txt","top 15.txt","top 20.txt"]

for file in files:
	with open(file, encoding="utf8") as result:
		results = result.readlines()
	results = [s[:-1] for s in results]
	for res in results:
		found = False
		for tweet in data:
			if res in tweet["text"]:
				if tweet["annotation"] not in score:
					score[tweet["annotation"]] = 1
				else:
					score[tweet["annotation"]] += 1
				found = True
				break
		if not found:
			print("string not found:")
			try:
				print(res)
			except:
				print("bloody emoji")
	print("-" * 79)
	print(file)
	print("-" * 79)
	for key in score.keys():
		print(key, " : ", score[key])
	print("-" * 79)
