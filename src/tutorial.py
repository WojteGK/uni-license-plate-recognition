def is_palindrome(text: str) -> bool:
    if text == text[::-1]:
        return True
    else:
        return False

def fibonacci(n: int) -> int:
    if n < 2:
        return n
    else:
        n = fibonacci(n-1) + fibonacci(n-2)

def count_vowels(text: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
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
    pass

def word_frequencies(text: str) -> dict:
    pass

def is_prime(n: int) -> bool:
    pass