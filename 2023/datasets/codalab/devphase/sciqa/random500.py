import sys,os,json,random

questions = json.loads(open('questions.json').read())['questions']

def select_random_items(input_list, num_items):
    if num_items > len(input_list):
        raise ValueError("Number of items to select is larger than the list size.")
    return random.sample(input_list, num_items)

questions200  = select_random_items(questions, 200)

qids200 = [x['id'] for x in questions200]
print(qids200)
answers = json.loads(open('non_sparql_answers_1.json').read())

random200answers = [x  for x in answers if x['id'] in qids200]

print(len(random200answers))


f = open('random_test_200_questions_1.json','w')
f.write(json.dumps(questions200, indent=4))
f.close()

f = open('random_test_200_answers_1.json','w')
f.write(json.dumps(random200answers, indent=4))
f.close()

