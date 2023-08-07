import sys,os,json,random,copy

questions = json.loads(open('random_test_500_questions_1.json').read())
answers = json.loads(open('random_test_500_answers_1.json').read())
q = {}
a = []
for question in questions:
    q[question['id']] = question
for answer in answers:
    citem = copy.deepcopy(answer)
    citem['entities'] = q[answer['id']]['entities']
    a.append(citem)

f = open('random_test_500_answers_2.json','w')
f.write(json.dumps(a, indent=4))
f.close()

