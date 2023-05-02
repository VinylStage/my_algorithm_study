from collections import Counter

array = [1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]

counter = Counter(array)
mode_count = max(counter.values())
mode = [k for k, v in counter.items() if v == mode_count]
print(mode[0] if len(mode) == 1 else -1)
