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