def apk(actual, predicted, k=10):
    """Get Average Precision at k."""
    count_relevants = 0
    sum_of_precisions = 0.0
    
    for i in range(min(k, len(predicted))):
        currentk = i + 1.0
        
        if predicted[i] in actual:
            count_relevants += 1
        
        precision_at_k = count_relevants / currentk 
        sum_of_precisions += precision_at_k
        
    return sum_of_precisions / k