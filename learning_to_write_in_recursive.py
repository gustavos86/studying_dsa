def ch11_exercise1(lst):
    """
    Use recursion to write a function that accepts an array of strings and
    returns the total number of characters across all the strings. For example,
    if the input array is ["ab", "c", "def", "ghij"], the output should be 10 since there
    are 10 characters in total.
    """
    def count_chars(lst):
        if len(lst) == 1:
            return len(lst[0])
        else:
            return len(lst[0]) + count_chars(lst[1:])
    
    return count_chars(lst)

def ch11_exercise2(lst):
    """
    Use recursion to write a function that accepts an array of numbers and
    returns a new array containing just the even numbers.
    """
    def even_nums(lst, new_array=[]):        
        if len(lst) == 0:
            return new_array

        if lst[0] % 2 == 0:
            new_array.append(lst[0])
       
        return even_nums(lst[1:], new_array)
        
    return even_nums(lst)

def ch11_exercise3(num):
    """
    There is a numerical sequence known as “Triangular Numbers.” The
    pattern begins as 1, 3, 6, 10, 15, 21, and continues onward with the Nth
    number in the pattern, which is N plus the previous number. For example,
    the 7th number in the sequence is 28, since it's 7 (which is N) plus 21
    (the previous number in the sequence). Write a function that accepts a
    number for N and returns the correct number from the series. That is, if
    the function was passed the number 7, the function would return 28.
    """
    def triangular_numbers(num):
        if num == 1:
            return 1

        return num + triangular_numbers(num - 1)

    return triangular_numbers(num)

def ch11_exercise4(str):
    """
    Use recursion to write a function that accepts a string and returns the
    first index that contains the character "x." For example, the string,
    "abcdefghijklmnopqrstuvwxyz" has an "x" at index 23. To keep things simple,
    assume the string definitely has at least one "x."
    """
    def first_index_x(str, c=0):
        if str[0] == 'x':
            return c
        else:
            return first_index_x(str[1:], c+1)

    return first_index_x(str)