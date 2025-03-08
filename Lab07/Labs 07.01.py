def  insertionSort(list, last):
    list = list(int(input()))
    last = int(input())
    element = 1
    for current in range(1, last + 1):
        hold = list[current]
        walker = current - 1
        while walker >= 0 and hold < list[current]:
            element += 1
            list[walker + 1] = list[walker]
            walker -= 1
        list[walker + 1] = hold
        print(list)
    print(element)
