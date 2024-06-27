def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except TypeError:
        print("Error: Invalid data types for division.")
    finally:
        print("Opp!")


result1 = divide_numbers(10, 2)
print(result1)  # Output: 5.0

result2 = divide_numbers(8, 0)  # Raises ZeroDivisionError
result3 = divide_numbers("hello", 5)  # Raises TypeError