def num(numbers: list) -> list:
    result = []
    for number in numbers:
        number = str(number)
        number = list(number)
        for i in range(len(number)):
            number[i] = int(number[i])
        result.append(sum(number))
    result.sort()
    return result


print(num([965, 582, 8, 23, 695210]))


def task_3(numbers: list) -> list:
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number//2)
    return result
