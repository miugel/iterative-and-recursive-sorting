'''
61850
2350

linear (sequential) search
    going down a list one-by-one and checking to see if the value at the index is the value we are searching for

binary search
    data must be sorted
    start with the middle index (length of array divided by 2)
    if no match is found, you eliminate one side of the list depending on how the value compares to the middle index
    keep comparing the middle index until you find a match
    what if list has a an odd length?

algorithm - the steps to solve a problem
iterative algorithm - repeat one or many steps until a process is 'done'

insertion sort
    consider first item a sorted list of length 1
    add items one by one, sorting them as you go

selection sort
    search for smallest item and swap with first index
    you only search the unsorted items right?

bubble sort
    comparing pairs of items at a time, swap if left is bigger than the right
    after the first pass, the biggest item has 'bubbled' to the top
    if 1 or more swaps were performed, repeat process

as you implement these, ask yourself how these scale? how many more loops or processes need to happen?

time complexity (big-O)
    beautiful code is elegant and efficiently
    consise, easy to read, eady to understand, easy to maintain, easy to modify
    minimal CPU operations, minimal memory/storage requirements
    a way of determining efficiency of code
    input size
    o stands for order
    big theta is average case
    big o is worst case, but will usually say big o for average case
'''

# O(1), constant
def get_animals():
    n = 5 + 5
    n *= 5
    return animals

# O(n)
# for each animal we need to do one operation
# if we have one animal we need to do this process one time, if we have one hundred, we need to do this one hundred times
def count_animals():
    num_animals = 0
    for animal in animals:
        num_animals += 1
    return num_animals

# O(2n) => 0(n)
# ignore coefficient
# returns each animal with all letters lowercase
def get_lowercase_animal():
    lowercase_animals = list(animals)
    animal_index = 0
    for animal in animals:
        lowercase_animals[animal_index] = lowercase_animals[animal_index].index()
        animal_index...

# O(n^2)
# two layers
# logs scale very well
