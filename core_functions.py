def hello_world():
    print("Hello this is the hello world function")

def add(a,b):
    return a + b
def subtract(a,b):
    return a-b

def find_largest_number_builtin(numbers):
  """
  Finds the largest number in a list using the built-in max() function.

  Args:
    numbers: A list of numbers (integers or floats).

  Returns:
    The largest number in the list.
  """
  if not numbers:
    # Handles the edge case of an empty list
    return None
  return max(numbers)

def binaryToDecimal(b):
    d, p = 0, 0
    while b:
        d += (b % 10) * (2 ** p)
        b //= 10
        p += 1
    print(d)

def remove_all_spaces(input_string):
  """
  Removes all space characters (' ') from a string.
  """
  return input_string.replace(" ", "")