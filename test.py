from collections import deque
def reverse_pop_until_key(stack, key):
    d = stack
    while d:
        front_element = d.pop()
        print(f"Popped: {front_element}")  # Optional: print the popped element
        if front_element == key:
            print(f"Key {key} found. Stopping.")
            return front_element
    print("Key not found in the stack.")
    return None

# Example usage
stack = [1, 2, 3, 4, 5]
stack = deque(stack)
key = 3

result = reverse_pop_until_key(stack, key)
print(f"Result: {result}")
print(f"Stack after operation: {stack}")