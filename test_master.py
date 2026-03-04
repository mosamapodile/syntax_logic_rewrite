import pytest
from master import *

def test_q1_parity():
    assert parity_accumulator(10) == 30
    assert parity_accumulator(0) == 0
    assert parity_accumulator(-2) == 0

def test_q2_search():
    assert linear_search_index([10, 20, 30], 20) == 1
    assert linear_search_index(["a", "b"], "z") == -1

def test_q3_sanitizer():
    assert string_sanitizer("p#y#t#h#o#n") == "python"
    assert string_sanitizer("###") == ""

def test_q4_filter():
    assert threshold_filter([1, 5, 10, 15], 8) == [10, 15]
    assert threshold_filter([], 10) == []

def test_q5_case():
    assert alternating_case("test") == "TeSt"
    assert alternating_case("") == ""

def test_q6_max():
    assert find_maximum_manual([1, 9, 3, 2]) == 9
    assert find_maximum_manual([]) == None

def test_q7_vowels():
    assert vowel_frequency("Aeiou") == 5
    assert vowel_frequency("xyz") == 0

def test_q8_table():
    assert multiplication_table(5, 20) == [5, 10, 15, 20]
    assert multiplication_table(10, 5) == []

def test_q9_integrity():
    assert list_integrity_check([1, 2, 3, 10]) == True
    assert list_integrity_check([1, 5, 2]) == False

def test_q10_reconstructor():
    assert sentence_reconstructor(["We", "Think", "Code"]) == "We Think Code"
    assert sentence_reconstructor([]) == ""