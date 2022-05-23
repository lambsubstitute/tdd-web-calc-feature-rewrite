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
