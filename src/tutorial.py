import re
import itertools

def is_palindrome(text: str) -> bool:
    text_lower = text.lower().replace(" ", "")
    if text_lower == text_lower[::-1]:
        return True
    else:
        return False

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Argument value must not be negative")
    if n < 2:
        return n
    else:
        if n is None:
            print("none: ", n)
        n = fibonacci(n-1) + fibonacci(n-2)
    return n

def count_vowels(text: str) -> int:
    vowels = {'a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y'}
    vowel_count = 0
    for char in text:
        if char.lower() in vowels:
            vowel_count +=1
    return vowel_count
            
def calculate_discount(price: float, discount: float) -> float:
    if price <= 0:
        raise ValueError("Price cannot be negative!")
    if discount < 0 or discount > 1:
        raise ValueError("Discount must be between 0-1!")
    final_price = price - price*discount
    if final_price < 0:
        raise Exception("Something bad happend while calculating the price!")
    return final_price

def flatten_list(nested_list: list) -> list:
    flat_list = []    
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def word_frequencies(text: str) -> dict:
    word_regex = r"\w+"
    words = re.findall(word_regex, text) 
    words_lower = []
    for w in words:
        words_lower.append(w.casefold())
    word_counts = {}
    for word in words_lower:
        if not word in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    print(word_counts)
    return word_counts

def is_prime(n: int) -> bool:
    if type(n) != int:
        raise TypeError("Value should be an integer!")
    if n <= 1:
        return False
    else:
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        return is_prime