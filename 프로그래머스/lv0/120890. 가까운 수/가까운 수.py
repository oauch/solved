def solution(array, n):
    array.sort()
    array_list = []
    for i in array:
        array_list.append(abs(i-n))
    return array[array_list.index(min(array_list))]