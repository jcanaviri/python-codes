def factorial(number):
    """factorial receives an integer and returns its factorial
    a factorial is the result of the multiplication of the number 'til 1
    for example:
        factorial(5) = 5 * 4 * 3 * 2 * 1 = 120"""
    
    if number < 0:
        return None
    
    if number == 0 or number == 1:
        return 1
    
    return number * factorial(number-1)

print(factorial(5))  # 120
