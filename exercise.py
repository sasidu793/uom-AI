## override the statistics. median function to compute the moving of a list of numbers
def moving_median(data, window_size):
    if window_size <= 0:
        raise ValueError("Window size must be positive")
    if not data:
        return []

    medians = []
    for i in range(len(data)):
        start_index = max(0, i - window_size + 1)
        window = data[start_index:i + 1]
        sorted_window = sorted(window)
        n = len(sorted_window)
        mid = n // 2
        if n % 2 == 0:
            median = (sorted_window[mid - 1] + sorted_window[mid]) / 2
        else:
            median = sorted_window[mid]
        medians.append(median)
    
    return medians  
print(moving_median([1, 3, 2, 5, 4], 3))  # Example usage
