import sys,os,json


skip = ['HQ0081','HQ0097','HQ0043''HQ0085','HQ0078','HQ0026','HQ0032','HQ0017','HQ0027','HQ0068']

d = json.loads(open(sys.argv[1]).read())["answers"]
newarr = []
for item in d:
    newanswer = []
    answer = item["answer"]
    if 'results' in answer:
        if 'bindings' in answer['results']:
            for ans in answer['results']['bindings']:
                for k,v in ans.items():
                    newanswer.append(ans[k]["value"])
            newarr.append({"id":item["id"], "answer":newanswer})
    elif 'boolean' in answer:
        newarr.append({"id":item["id"], "answer":answer['boolean']})
    else:
        newarr.append({"id":item["id"], "answer":[]})


f = open(sys.argv[2],'w')
f.write(json.dumps(newarr,indent=4))
f.close()
