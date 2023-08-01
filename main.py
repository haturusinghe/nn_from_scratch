# generate an example to demonstrate how zip works

# zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is
# paired together, and then the second item in each passed iterator are paired together etc.

# If the passed iterators have different lengths, the iterator with the least items decides the length of the new
# iterator. code example :
numberList1 = [1, 2, 3]
numberList2 = [10, 20, 30]
# Zip the two lists and display the zip object
print(zip(numberList1, numberList2))
# loop through the zip object and display the tuples
for i in zip(numberList1, numberList2):
    print(i)
# code example :
# Two separate lists
list1 = ['a', 'b', 'c']
# two-dimensional list
list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# loop through the zip object and display the tuples
for i in zip(list1, list2):
    print(i)
