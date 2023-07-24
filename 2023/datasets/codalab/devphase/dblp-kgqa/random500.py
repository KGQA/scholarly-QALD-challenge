import sys,os,json,random

questions = json.loads(open('questions.json').read())['questions']

def select_random_items(input_list, num_items):
    if num_items > len(input_list):
        raise ValueError("Number of items to select is larger than the list size.")
    return random.sample(input_list, num_items)

questions500  = select_random_items(questions, 500)

qids500 = [x['id'] for x in questions500]
print(qids500)
answers = json.loads(open('non_sparql_answers2.json').read())

random500answers = [x  for x in answers if x['id'] in qids500]

print(len(random500answers))


f = open('random_test_500_questions_1.json','w')
f.write(json.dumps(questions500, indent=4))
f.close()

f = open('random_test_500_answers_1.json','w')
f.write(json.dumps(random500answers, indent=4))
f.close()

