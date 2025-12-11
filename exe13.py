class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers
        
    def get(self):
        return self.numbers
    
    def change_original_value(self, func: lambda x: x*2):
        new_numbers = []
        for num in self.numbers:
            new_numbers.append(func(num))
        # self.numbers = new_numbers
        return new_numbers
    
    def filter_values(self, func: lambda x: x%2 == 0):
        filtered_numbers = []
        for num in self.numbers:
            if func(num):
                filtered_numbers.append(num)
        return filtered_numbers
    
    def compound_numbers(self, func: lambda x,y: x+y):
        result = 0
        for num in self.numbers:
            result = func(result, num)
        return result
    
    def sort(self):
        return sorted(self.numbers)
    
if __name__ == "__main__":
    numbers = [2, 5, 1, 66, 22, 11, 10]
    
    n1 = Numbers(numbers)
    
    # Get original numbers
    print("Numbers : ",n1.get())   
        
    # Get new numbers after applying lambda function
    print("New Numbers : ", n1.change_original_value(lambda x: x * 2))

    # Get filtered numbers after applying lambda function
    print("Filtered Numbers : ", n1.filter_values(lambda x: x%2 == 0))
    
    # Get compounded result after applying lambda function
    print("Compounded Values : ", n1.compound_numbers(lambda x,y : x + y))
    
    # Get sorted numbers
    print("Sorted Numbers : ", n1.sort())