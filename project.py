a = input("Введите последовательность чисел через пробел:")
element = int(input("Введите число:"))
array = list(a.split())
array = list(map(int, array))
#array = [2, 3, 55, 4, 6, 17, 19, 8, 7]
print(array)
a = len(array) - 1

for i in range(len(array)):
    idx_min = i
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j

    if i != idx_min:
        array[i], array[idx_min] = array[idx_min], array[i]

print(array)
a = len(array) - 1
while array[a] < element:
    element = int(input("Введите другое число:"))
def binary_search(array, element, left, right):
    if left > right:
        return False
    #if array[a] < element:
      #  return False
    if left == right:
        if array[left] > element:
            return ((left - 1) + 1)
        elif array[left] < element:
            return left + 1
    elif left == (len(array) - 1):
        return ((left - 1) + 1)
    elif array[a] < element:
        return False
    #else :
      #  return ((binary_search(array, element, 0, len(array))) -1)
    middle = (right+left) // 2
    if array[middle] == element:
        return middle
    elif element < int(array[middle]):

        return binary_search(array, element, left, middle-1)


    else: # иначе в правой
        return binary_search(array, element, middle+1, right)

#element = int(input())
#array = [i for i in range(1,100)] # 1,2,3,4,...
a = len(array) - 1
# запускаем алгоритм на левой и правой границе
if array[a] < element:
    print("Выберите другое число")
else:
    print((binary_search(array, element, 0, len(array))) -1)

#element = int(input())







