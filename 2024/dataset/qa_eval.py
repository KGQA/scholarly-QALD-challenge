import argparse
import json
import math
import sys
import os
import subprocess
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("nltk")
import nltk
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

nltk.download('wordnet')

# Initialize WordNet
nltk.download('punkt')  # Ensure you have punkt tokenizer downloaded


def load_gold_standard_qa(gold_path):
    gold_answers = dict()
    with open(gold_path) as json_file:
        data = json.load(json_file)
    for ques in data:
        gold_answers[ques['id']] = ques['answer']
    print(f"\tGold answers: loaded {len(data)} questions!")
    return gold_answers

def load_system_answers_qa(system_path):
    system_answers = dict()
    with open(system_path) as json_file:
        data = json.load(json_file)
    for ques in data:
        if 'answer' in ques:
            system_answers[ques['id']] = ques['answer']
        else:
            print(f"Missing questions: {ques['id']}")
    print(f"\tSystem answers: loaded {len(data)} questions!")
    return system_answers

def evaluate_qa(gold_answers, system_answers):
    total_questions = len(gold_answers)
    exact_match_count = 0
    bleu_scores = []
    smoothie = SmoothingFunction().method4

    for ques_id in gold_answers:
        gold_answer = gold_answers[ques_id]
        system_answer = system_answers.get(ques_id, "")

        # Calculate exact match
        if gold_answer == system_answer:
            exact_match_count += 1

        # Tokenize the answers
        gold_sentences = nltk.word_tokenize(gold_answer)
        tokenized_sysans = nltk.word_tokenize(system_answer)
        
        # Calculate BLEU for each answer
        bleu_scores.append(sentence_bleu([gold_sentences], tokenized_sysans, smoothing_function=smoothie))

    # Calculate exact match accuracy
    exact_match_accuracy = exact_match_count / total_questions if total_questions > 0 else 0.0

    # Calculate BLEU score
    avg_bleu = sum(bleu_scores) / len(bleu_scores) if bleu_scores else 0.0

    return exact_match_accuracy, avg_bleu

def main():
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    gt_path = os.path.join(os.path.join(input_dir, 'ref'), 'answer.txt')
    system_path = os.path.join(os.path.join(input_dir, 'res'), 'answer.txt')
    print(f"Config:\n\tGround truth: {gt_path}\n\tSystem path: {system_path}")

    gold_answers_qa = load_gold_standard_qa(gt_path)
    system_answers_qa = load_system_answers_qa(system_path)
    exact_match_accuracy, avg_bleu_qa = evaluate_qa(gold_answers_qa, system_answers_qa)
    print(f"\nQA Results:\n\tExact Match Accuracy: {round(exact_match_accuracy * 100, 2)}%\n\tBLEU: {round(avg_bleu_qa, 5)}")
    
    with open(os.path.join(output_dir, 'scores.txt'), 'w') as f:
        f.write(f"EM: %f\n"%(exact_match_accuracy))
        f.write(f"BLEU: %f\n"%(avg_bleu_qa))

if __name__ == "__main__":
    main()

