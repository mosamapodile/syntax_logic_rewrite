

def parity_accumulator(n):  
    """Q1: Calculate sum of even integers up to n."""
    # TODO: Implement logic using a loop
    sum_even = 0
    for number in range(0,n+1):
        if number %2 ==0:
            sum_even += number
    return sum_even

def linear_search_index(items, target):
    """Q2: Find index of target using enumerate."""
    # TODO: Implement logic. Return -1 if not found.
    if items == []:
        return None
    for index , number in enumerate(items):
        if number == target:
            return index
    return -1


def string_sanitizer(text):
    """Q3: Remove '#' without using .replace()."""
    # TODO: Build new string manually
    # ASCII
    result = []
    for char in text:
        if  'A' <= char <='Z':
            result.append(char)
        elif 'a' <= char <= 'z':
            result.append(char)
        else:
            continue
    return ''.join(result)
print(string_sanitizer("p#y#t#h#o#n"))


def threshold_filter(data, limit):
    """Q4: Return list of elements > limit."""
    # TODO: Use a loop and conditional
    result = []
    for number in data:
        if number > limit:
            result.append(number)
    return result
print(threshold_filter([1, 5, 10, 15],8))


def alternating_case(word):
    """Q5: Even index = Upper, Odd index = Lower."""
    # TODO: Use enumerate or index tracking
    result = []
    if word == '':
        return ''
    for index, char in enumerate(list(word)):
        if index %2 ==0:
            char = char.upper()
            result.append(char)
        else:
            char = char.lower()
            result.append(char)
    return ''.join(result)
print(alternating_case("test"))

def find_maximum_manual(numbers):
    """Q6: Find max value without using max()."""
    # TODO: Handle empty list case (None)
    if numbers == []:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
print(find_maximum_manual([1, 9, 3, 2]))

def vowel_frequency(phrase):
    """Q7: Count a, e, i, o, u (case-insensitive)."""
    # TODO: Use membership check
    # vowels = 'AEIOU'
    count = 0
    for char in phrase.lower():
        vowels = 'aeiou'
        if char in vowels:
            count += 1
        else:
            return 0
    return count
        
print(vowel_frequency("Aeiou"))


def multiplication_table(factor, limit):
    """Q8: Generate table up to limit."""
    # TODO: Use range or while loop
    result = []
    for number in range(1,limit +1):
        if number % factor == 0:
            result.append(number)
    return result
print(multiplication_table(5,20))


def list_integrity_check(data_stream):
    """Q9: Verify if list is strictly increasing."""
    # TODO: Compare current element to previous
    if len(data_stream) <= 1:
        return True
    for index in range(1,len(data_stream)):
        if data_stream[index] <= data_stream[index - 1]:
            return False
    return True
    # assert list_integrity_check([1, 5, 2]) == False
print(list_integrity_check([1, 2, 3, 10]))

def sentence_reconstructor(words):
    """Q10: Join list into string without .join()."""
    # TODO: Use loop and handle trailing space
    if not words:
        return ""
    
    reconstructed = ""
    i = 0
    
    while i < len(words):
        reconstructed += words[i]
        if i < len(words) - 1:
            reconstructed += " "
        i += 1
        
    return reconstructed
