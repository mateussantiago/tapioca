from collections import defaultdict


def frequency_queries(queries):
    memory = defaultdict(int)
    frequency = defaultdict(int)
    result = []

    for op, elem in queries:
        if op == 1:
            if memory[elem] > 0 and frequency[memory[elem]] > 0:
                frequency[memory[elem]] -= 1

            memory[elem] += 1
            frequency[memory[elem]] += 1

        elif op == 2:
            if memory[elem] > 0:
                freq = memory[elem]

                if freq > 0:
                    frequency[freq] -= 1
                    frequency[freq - 1] += 1

                memory[elem] -= 1

        else:
            if frequency[elem] > 0:
                result.append(1)

            else:
                result.append(0)

    return result
