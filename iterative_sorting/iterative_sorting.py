'''
selection sort
- loop through list
- compare current index with smallest index, reducing the range each iteration
- if current index is smaller, replace smallest index with current index
- at the end of iteration, swap the current index and the smallest index in the list
'''

def selection_sort(list):
    for i in range(0, len(list)-1):
        smallest_index = i

        for j in range(i, len(list)):
            if list[j] < list[smallest_index]:
                smallest_index = j

        placeholder = list[i]
        list[i] = list[smallest_index]
        list[smallest_index] = placeholder
    
    return list

# why did the boilerplate come with len(list)-1 in range?
# what happens with duplicates?
list = [1, 2, 0, 3, 9, 2, 3, 4, 9, 0, 5]
selection_sort(list)
print(list)

# bubble sort
# not using list directly, but range
def bubble_sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                placeholder = list[j]
                list[j] = list[j+1]
                list[j+1] = placeholder

    # return list
    return list

list2 = [1, 2, 0, 3, 9, 2, 3, 4, 9, 0, 5]
bubble_sort(list2)
print(list2)

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr