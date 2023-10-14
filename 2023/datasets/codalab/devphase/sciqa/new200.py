import sys,os,json,random

discard = json.loads(open('reference/answer.txt').read())
discarddict = {}
for item in discard:
    discarddict[item['id']] = None

questions = []
questions_ = json.loads(open('questions.json').read())['questions']
for q in questions_:
    if q['id'] in discarddict:
        continue
    else:
        questions.append(q)

def select_random_items(input_list, num_items):
    if num_items > len(input_list):
        raise ValueError("Number of items to select is larger than the list size.")
    return random.sample(input_list, num_items)

questions200_  = select_random_items(questions, 200)
questions200 = [{'id':x['id'], 'question':x['question']['string']} for x in questions200_]

qids200 = [x['id'] for x in questions200]
print(qids200)
answers = json.loads(open('non_sparql_answers_1.json').read())

random200answers = [x  for x in answers if x['id'] in qids200]

print(len(random200answers))


f = open('final_phase_sciqa_200_questions_1.json','w')
f.write(json.dumps(questions200, indent=4))
f.close()

f = open('final_phase_sciqa_200_answers_1.json','w')
f.write(json.dumps(random200answers, indent=4))
f.close()

