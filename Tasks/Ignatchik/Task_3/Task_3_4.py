input_list = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61,
            -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 
            79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74,
            -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11,
            -26, -62, -84]

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        support_element = array[0]
        less_support_element = [i for i in array[1:] if i <= support_element]
        more_support_element = [i for i in array[1:] if i > support_element]
        return quick_sort(less_support_element) + [support_element] + quick_sort(more_support_element)

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:                  
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def sorting_by_simple_inserts(array):
    n = len(array)
    for i in range(1, n): 
        elem = array[i]  
        j = i
        while j >= 1 and array[j - 1] > elem: 
            array[j] = array[j - 1]
            j -= 1
        array[j] = elem
    return array

def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        i_max = array.index(max(array[:n - i]))
        array[i_max], array[-i-1] = array[-i-1], array[i_max]
    return array

if __name__ == "__main__":
    def second_number(enter):
        enter_1 = enter.copy()
        enter_2 = enter.copy()
        enter_3 = enter.copy()
        enter_4 = enter.copy()
        bubble = bubble_sort(enter_1)
        quick = quick_sort(enter_2)
        inserts = sorting_by_simple_inserts(enter_3)
        choice = selection_sort(enter_4)

        return bubble[-2], quick[-2], inserts[-2], choice[-2]
    
result = second_number(input_list)
print(*result)

