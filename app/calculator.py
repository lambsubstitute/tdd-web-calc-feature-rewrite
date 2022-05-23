class Calculator:
    """
    This is the main class to implement the Calculator
    """

    def __init__(self):
        self.value = 0

    def parse(self, calculation):
        """
        parse is a function that takes a list of numbers and operators and
        sets the value to the resulting calculation
        """

        print(f"Parsing calculation: {calculation}")

        # First pass reduce the numbers
        self.calculation = []
        temp_value = None

        # Iterate over all items in the calculation
        for item in calculation:
            if isinstance(item, int):
                if temp_value == None:
                    temp_value = item
                else:
                    temp_value = int(str(temp_value) + str(item))
            else:
                ## Item is an operator
                if temp_value != None:
                    self.calculation.append(temp_value)

                self.calculation.append(item)
                temp_value = None

        print(f"Reduces to: {self.calculation}")

        # Recurse over calculation and workout answer
        self.value = self.calculate(self.calculation)

        # Answer is now available in self.value
        print(f"Answer is: {self.value}")

    def calculate(self, calculation):
        """
        Calculate the result of a list of numbers and operators.
        This is a recursive function
        """
        # Work out the inputs
        if len(calculation) > 0:
            first_item = calculation[0]
        if len(calculation) > 1:
            second_item = calculation[1]
        if len(calculation) > 2:
            third_item = calculation[2]
        if len(calculation) > 3:
            remainder = calculation[3:]

        if second_item == "+":
            # Addition
            sum = first_item + third_item

            if len(calculation) > 3:
                remainder.insert(0, sum)
                print(remainder)
                return self.calculate(remainder)
            else:
                return sum

        if second_item == "=":
            return first_item
