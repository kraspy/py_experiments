test_averages = {
    'Джанель': 98,
    'Сэм': 87,
    'Дженнифер': 92,
    'Томас': 74,
    'Салли': 89,
    'Зеб': 84,
}

high_scores = {k: v for k, v in test_averages.items() if v >= 90}

print(high_scores)
