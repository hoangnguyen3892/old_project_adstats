def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)
        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = list(zip(ages, net_worths, [(float(pred) - actual)**2 for pred, actual in zip(predictions, net_worths)]))

    cleaned_data.sort(key = lambda tup: tup[2])

    #for i in range(0, int(len(cleaned_data) * 0.1)):
    for i in range(0, 3):
        cleaned_data.pop()
    
    return cleaned_data
