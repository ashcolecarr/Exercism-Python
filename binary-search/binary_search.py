def binary_search(list_of_numbers, number):
    start = 0
    end = len(list_of_numbers) - 1
    while start <= end:
        mid = start + ((end - start) // 2)

        if number == list_of_numbers[mid]:
            return mid

        # Get first half of list
        if number < list_of_numbers[mid]:
            end = mid - 1
        # Get back half of list
        else:
            start = mid + 1

    raise ValueError('Value is not in list.')
