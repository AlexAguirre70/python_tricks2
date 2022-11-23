# Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.
# Unsorted list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] 
# Sorted list of tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

unsorted_tup = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] 

sorted_tup =sorted(unsorted_tup,key=lambda t: t[1])

print(sorted_tup)

# Write a lambda function to cube every element of a list.
# Original list: [3,6,9,2] List after lambda function: [27,216,729,8]
original_list=[3,6,9,2]

cubed=list(map(lambda x:x**3,original_list))
print(cubed)

# Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False.
# Input list: [3,6,9,2] List after lambda function and list comprehension: [False, True, False, True]
input_list=[3,6,9,2]

is_even_list=list(map(lambda x:x%2==0,input_list))
print(is_even_list)

is_odd_list= list(map( lambda x: x%2==1, input_list))
print(is_odd_list)
# Use a list comprehension to create a list of the numbers from 1 to 100 (including 100).
list_comp1 = [x for x in range(1,101)]
print(list_comp1)

# Use a dictionary comprehension to count the length of each word in a sentence.
# Input: "The quick brown fox jumped over the fence." 
# output: { {'The': 3, 'quick': 5, 'brown': 5, 'fox':3, 'jumped': 6, 'over': 4, 'the': 3, 'fence.': 6}
input_sent = "The quick brown fox jumped over the fence." 

list_dict={word:len(word) for word in input_sent.split()}
print(list_dict)