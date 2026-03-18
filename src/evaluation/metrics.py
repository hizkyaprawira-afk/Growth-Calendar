def accuracy(preds, labels):
    """
    Computes the accuracy of predictions against the true labels.

    Args:
        preds (list): A list of predicted labels.
        labels (list): A list of true labels.

    Returns:
        float: The accuracy of the predictions.
    """
    correct = sum(p == l for p, l in zip(preds, labels))
    total = len(labels)
    return correct / total if total > 0 else 0.0

def precision(preds, labels):
    """
    Computes the precision of predictions against the true labels.

    Args:
        preds (list): A list of predicted labels.
        labels (list): A list of true labels.

    Returns:
        float: The precision of the predictions.
    """
    true_positive = sum(p == l == 1 for p, l in zip(preds, labels))
    false_positive = sum(p == 1 and l == 0 for p, l in zip(preds, labels))
    return true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0.0

def recall(preds, labels):
    """
    Computes the recall of predictions against the true labels.

    Args:
        preds (list): A list of predicted labels.
        labels (list): A list of true labels.

    Returns:
        float: The recall of the predictions.
    """
    true_positive = sum(p == l == 1 for p, l in zip(preds, labels))
    false_negative = sum(p == 0 and l == 1 for p, l in zip(preds, labels))
    return true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0.0

def f1_score(preds, labels):
    """
    Computes the F1 score of predictions against the true labels.

    Args:
        preds (list): A list of predicted labels.
        labels (list): A list of true labels.

    Returns:
        float: The F1 score of the predictions.
    """
    prec = precision(preds, labels)
    rec = recall(preds, labels)
    return 2 * (prec * rec) / (prec + rec) if (prec + rec) > 0 else 0.0

