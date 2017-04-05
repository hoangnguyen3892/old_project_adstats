def outlierCleaner(predictions, x, y):
    """
        Clean away 3 points that have the largest
        residual errors (different between the prediction
        and the actual)

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (x, y, error)
    """
    
    cleaned_data = list(zip(x, y, [(float(pred) - actual)**2 for pred, actual in zip(predictions, y)]))

    cleaned_data.sort(key = lambda tup: tup[2])

    #for i in range(0, int(len(cleaned_data) * 0.1)):
    cleaned_list = []
    for i in range(0, 5):
        cleaned_list.append(cleaned_data[-1][0])
        cleaned_data.pop()
    return cleaned_data, cleaned_list
