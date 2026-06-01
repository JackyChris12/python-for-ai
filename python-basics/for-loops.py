""" Sum 1 to 100: Write a function sum_100() that 
returns the sum using only a for loop. No sum() function. """

def sum_100():
    total =0
    for i in range(1, 101):
        total +=i
    return total
print(sum_100())

""" Filter strings: Write a function long_words(words) that takes a
list of strings and returns a new list containing only strings longer than 5 characters. """
def long_words(words):
    result= []
    for word in words:
        if len(word) >5:
            result.append(word)
    return result


sample_list = ["apple", "banana", "kiwi", "pineapple", "pear", "orange"]
print(long_words(sample_list))


""" Matrix traversal: Given matrix = [[1,2,3],[4,5,6],[7,8,9]], 
write nested for loops that prints each element. """
matrix = [[1,2,3],[4,5,6],[7,8,9]]

for row in matrix:
    for element in row:
        print(element)


""" Enumerate: Use enumerate() to print each element with its index.
Guess the syntax first. If wrong, fix it using only the docs. """
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row_index, row in enumerate(matrix):
    for col_index, element in enumerate(row):
        print(f"Index [{row_index}][{col_index}] = {element}")

