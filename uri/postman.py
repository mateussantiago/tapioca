def binary_search(elements: list, target: int) -> int:
    left, right = 0, len(elements) - 1

    while left <= right:
        mid = left + ((right - left) >> 1)

        if target < elements[mid]:
            right = mid - 1

        elif target > elements[mid]:
            left = mid + 1

        else:
            return mid

    return -1


def solution(n: int, m: int, house_numbers: list, order_deliveries: list):
    if m == 1 and house_numbers[0] == order_deliveries[0]:
        return 0

    total_time, last_position = 1, 1

    for h_number in order_deliveries:
        idx = binary_search(house_numbers, h_number)
        total_time += abs(idx - last_position)
        last_position = idx

    print(total_time)


n, m = input().split(" ")
house_numbers = input().split(" ")
order_deliveries = input().split(" ")
solution(
    int(n), int(m), list(map(int, house_numbers)), list(map(int, order_deliveries))
)
