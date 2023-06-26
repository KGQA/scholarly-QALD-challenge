import sys,os,json

d = json.loads(open(sys.argv[1]).read())["questions"]
newarr = []
for item in d:
    newarr.append({"id":item['id'], "entities":item['entities']})

f = open(sys.argv[2],'w')
f.write(json.dumps(newarr,indent=4))
f.close()
