import sys,os,json


def load_data(gold_answers_path, system_answers_path):
    gold_data = json.loads(open(gold_answers_path).read())
    pred_data = json.loads(open(system_answers_path).read())
    gold_answers = {item['id']: str(item['answer']).strip() for item in gold_data}
    predictions = {item['id']: str(item['answer']).strip() for item in pred_data}

    gold_list = []
    pred_list = []

    for qid, answer in gold_answers.items():
        if qid in predictions:
            gold_list.append(answer)
            pred_list.append(predictions[qid])

    return gold_list, pred_list


def calculate_exact_match(reference, hypothesis):
    return int(reference == hypothesis)


def calculate_f_score(references, hypotheses):
    precision_recall_f1_list = []

    for ref, hyp in zip(references, hypotheses):
        ref_tokens = ref.split()
        hyp_tokens = hyp.split()

        common_tokens = set(ref_tokens) & set(hyp_tokens)
        precision = len(common_tokens) / len(hyp_tokens) if hyp_tokens else 0
        recall = len(common_tokens) / len(ref_tokens) if ref_tokens else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        precision_recall_f1_list.append((precision, recall, f1_score))

    avg_precision = sum(pr[0] for pr in precision_recall_f1_list) / len(precision_recall_f1_list)
    avg_recall = sum(pr[1] for pr in precision_recall_f1_list) / len(precision_recall_f1_list)
    avg_f1_score = sum(pr[2] for pr in precision_recall_f1_list) / len(precision_recall_f1_list)

    return avg_precision, avg_recall, avg_f1_score


def evaluate(gold_answers_path, system_answers_path):
    gold_answers, predictions = load_data(gold_answers_path, system_answers_path)
    exact_matches = [calculate_exact_match(ref, hyp) for ref, hyp in zip(gold_answers, predictions)]
    precision, recall, f1_score = calculate_f_score(gold_answers, predictions)
    exact_match_score = sum(exact_matches) / len(exact_matches) if exact_matches else 0

    return  exact_match_score,  precision, recall, f1_score

def main():
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    gt_path = os.path.join(os.path.join(input_dir, 'ref'), 'answers2.txt')
    system_path = os.path.join(os.path.join(input_dir, 'res'), 'answers2.txt')
    print(f"Config:\n\tGround truth: {gt_path}\n\tSystem path: {system_path}")

    exact_match_accuracy, precision, recall, f1 = evaluate(gt_path, system_path)
    print(f"\nQA Results:\n\tExact Match Accuracy: {round(exact_match_accuracy * 100, 2)}%\n\tPrecision: {round(precision, 5)}\n\tRecall: {round(recall, 5)}\n\tF1: {round(f1, 5)}")

    with open(os.path.join(output_dir, 'scores.txt'), 'w') as f:
        f.write(f"ExactMatch: %f\n" % (exact_match_accuracy))
        f.write(f"Precision: %f\n" % (precision))
        f.write(f"Recall: %f\n" % (recall))
        f.write(f"F1: %f\n" % (f1))


if __name__ == "__main__":
    main()

