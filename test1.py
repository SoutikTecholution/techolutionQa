# Violates Input Validation Against Vulnerabilities
def unsafe_sum(user_input):
    # Assumes user_input is a list of integers without validation
    return sum(user_input)

# Orphan Function (defined but never used)
def orphan_function():
    print("This function is never used.")

# Super Class misuse
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        # Super class not properly initialized
        # Missing super().__init__(name)
        self.breed = breed

# Example usage
user_data = input("Enter a list of numbers separated by commas: ")
user_data = eval(user_data)  # Unsafe: using eval on user input

result = unsafe_sum(user_data)
print("The sum is:", result)

# Creating a Dog instance without properly initializing Animal part
dog = Dog("Buddy", "Golden Retriever")
print("Dog name:", dog.name)
print("Dog breed:", dog.breed)
