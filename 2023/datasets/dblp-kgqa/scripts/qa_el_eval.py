import argparse
import json
import math
from collections import Counter
import sys
import os

def load_gold_stardard_el(gold_path):
    gold_answers = dict()
    with open(gold_path) as json_file:
        data = json.load(json_file)
    for ques in data:
        gold_answers[ques['id']] = ques['entities']
    print(f"\tgold answers: loaded {len(data)} questions!")
    return gold_answers


def load_system_answers_el(system_path):
    system_answers = dict()
    with open(system_path) as json_file:
        data = json.load(json_file)
    for ques in data:
        if 'entities' in ques:
            system_answers[ques['id']] = ques['entities']
        else:
            print(f"Missing entities: {ques['id']}")
    print(f"\tsystem answers: loaded {len(data)} questions!")
    return system_answers

def evaluate_dblp_el(gold_answers, system_answers):
    true_p,false_p,false_n=0,0,0
    for ques_id in gold_answers:
        gold_answer_set = set(gold_answers[ques_id])
        # if an answer is not provided to a question, we just move on
        if ques_id not in system_answers:
            system_answer_set = set([])
        else:
            system_answer_set= set(system_answers[ques_id])
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

def load_gold_stardard_qa(gold_path):
    gold_answers = dict()
    with open(gold_path) as json_file:
        data = json.load(json_file)
    for ques in data:
        gold_answers[ques['id']] = ques['answer']
    print(f"\tgold answers: loaded {len(data)} questions!")
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
    print(f"\tsystem answers: loaded {len(data)} questions!")
    return system_answers


def evaluate_dblp_qa(gold_answers, system_answers):
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
    gold_answers_qa = load_gold_stardard_qa(gt_path)
    system_answers_qa = load_system_answers_qa(system_path)
    precision_qa, recall_qa, f1_qa = evaluate_dblp_qa(gold_answers_qa, system_answers_qa)
    print(f"\nQA Results:\n\tPrecision: {round(precision_qa, 5)}\n\tRecall: {round(recall_qa, 5)}\n\tF1: {round(f1_qa, 5)}")
    
    gold_answers_el = load_gold_stardard_el(gt_path)
    system_answers_el = load_system_answers_el(system_path)
    precision_el, recall_el, f1_el = evaluate_dblp_el(gold_answers_el, system_answers_el)
    print(f"\nEL Results:\n\tPrecision: {round(precision_el, 5)}\n\tRecall: {round(recall_el, 5)}\n\tF1: {round(f1_el, 5)}")

if __name__ == "__main__":
    main(arg_parser())
