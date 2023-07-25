import argparse
import json
import math
from collections import Counter
import sys

def load_gold_stardard(gold_path):
    gold_answers = dict()
    with open(gold_path) as json_file:
        data = json.load(json_file)
    for ques in data:
        gold_answers[ques['id']] = ques['answer']
    print(f"\tgold answers: loaded {len(data)} questions!")
    return gold_answers


def load_system_answers(system_path):
    system_answers = dict()
    with open(system_path) as json_file:
        data = json.load(json_file)
    for ques in data:
        if 'answer' in ques:
            system_answers[ques['id']] = ques['answer']
        else:
            print(f"Missing questions: {ques['id']}")
    print(f"\tsystem answers: loaded {len(data)} questions!")
    return system_answers


def evaluate_dblp(gold_answers, system_answers):
    true_p,false_p,false_n=0,0,0
    for ques_id in gold_answers:
        gold_answer_set = set(gold_answers[ques_id])
        # if an answer is not provided to a question, we just move on
        if ques_id not in system_answers:
            system_answer_set = set([])        
        else:
            system_answer_set = set(system_answers[ques_id])
        for sysans in system_answer_set:
            if sysans in gold_answer_set:
                true_p += 1
            else:
                false_p += 1
        for goldans in gold_answer_set:
            if goldans not in system_answer_set:
                false_n += 1
    precision = true_p/(true_p+false_p+0.000001)
    recall = true_p/(true_p+false_n+0.000001)
    f1 = 0.0
    if precision+recall != 0:
        f1 = (2*precision*recall)/(precision+recall)

    return precision,recall,f1


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gt', type=str,
                        help='ground truth JSON file')
    parser.add_argument('--so', type=str,
                        help='system output JSON file')
    args = parser.parse_args()
    return args


def main(args):
    system_path = args.so
    gt_path = args.gt
    print(f"Config:\n\tGround truth: {gt_path}\n\tSystem path: {system_path}")
    gold_answers = load_gold_stardard(gt_path)
    system_answers = load_system_answers(system_path)
    precision, recall, f1 = evaluate_dblp(gold_answers, system_answers)

    print(f"\nResults:\n\tPrecision: {round(precision, 5)}\n\tRecall: {round(recall, 5)}\n\tF1: {round(f1, 5)}")


if __name__ == "__main__":
    main(arg_parser())
