1-HOUR MEGA MASTERY TEST: SYNTAX & LOGIC REWRITE

Duration: 1 Hour

Total Marks: 100 (10% per function)

Status: ACTIVE
📋 CONCEPTS TESTED (ACTIVE POOL)

    Variables & Arithmetic

    Conditionals (if/elif/else)

    Loops (for/while)

    Strings & Lists

    Functions

    enumerate

    Basic Problem Solving

📜 INSTRUCTIONS

    Strictly No External Libraries: Do not import anything.

    No Logic Shortcuts: Do not use sum(), min(), max(), .reverse(), or [::-1]. Use Loops for these operations.

    Constraint: Every function must handle potential "Empty" inputs (None, "", or []) without crashing.

    Formatting: Maintain clean indentation. "Technical Debt" (redundant logic) will be penalized.

🛠️ THE CHALLENGE (10 FUNCTIONS)
Q1 - parity_accumulator(n)

Ensure the value n conforms to equal-distribution parity standards. Calculate the sum of all even integers from 0 up to and including n.

    Input: Integer n

    Output: Integer (Sum)

Q2 - linear_search_index(items, target)

Identify the positional placement of a specific target within a collection. You must use enumerate. If the target is not present, return -1.

    Input: List items, Any target

    Output: Integer (Index)

Q3 - string_sanitizer(text)

Process a string to remove all occurrences of the character '#'. You must build the new string manually using a loop.

    Input: String text

    Output: String (Sanitized)

Q4 - threshold_filter(data, limit)

Given a list of integers, return a new list containing only elements that strictly exceed the provided limit.

    Input: List data, Integer limit

    Output: List

Q5 - alternating_case(word)

Transform a string so that characters at even indices are Uppercase and characters at odd indices are Lowercase.

    Example: "hello" -> "HeLlO"

    Input: String word

    Output: String

Q6 - find_maximum_manual(numbers)

Determine the peak value in a list of numbers. Constraint: You are forbidden from using the max() built-in. Use a loop.

    Input: List numbers (may be empty)

    Output: Integer/Float or None if list is empty.

Q7 - vowel_frequency(phrase)

Calculate the total count of vowels (a, e, i, o, u) regardless of case.

    Input: String phrase

    Output: Integer

Q8 - multiplication_table(factor, limit)

Generate a list containing the multiplication table for a factor up to a specific limit (inclusive).

    Example: factor=3, limit=10 -> [3, 6, 9]

    Input: Two Integers

    Output: List

Q9 - list_integrity_check(data_stream)

Verify if a list is "Strictly Increasing." Return True if every element is larger than the previous one, otherwise False.

    Input: List data_stream

    Output: Boolean

Q10 - sentence_reconstructor(words)

Take a list of words and join them into a single string separated by a single space. Constraint: Do not use .join(). Use a loop.

    Input: List words

    Output: String