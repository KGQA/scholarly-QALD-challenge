import sys,os,json,copy

d0 = json.loads(open(sys.argv[1]).read())["questions"]
sepidxs = []
for item in d0:
    if 'separator' in item['query']['sparql']:
        sepidxs.append(item['id'])

d = json.loads(open(sys.argv[2]).read())
newarr = []
for item in d:
    citem = copy.deepcopy(item)
    if type(citem['answer']) is not list:
        citem['answer'] = [citem['answer']]
    elif item['id'] in sepidxs:
        print(item)
        newans = []
        for ans in item['answer']:
            for an in ans.split(', '):
                newans.append(an)
        citem['answer'] = newans
        print(citem)
        print("..............")
    newarr.append(citem)

f = open(sys.argv[3],'w')
f.write(json.dumps(newarr, indent=4))
f.close()
