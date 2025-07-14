# Class
# You can call multile functions with single parameter 
# Set of functions
class Math: # 5
    def __init__(self, a): # 5
        self.a = a # 5

    def subraction(self):
        a = self.a - 2
        return a
    def addition(self):
        return self.a + 2 # 5 * 2 

    def multiplication(self):
        a = self.a * 2
        return a
c = Math(5)


print("Subtraction:" , c.subraction())
print("Multiplicaiton:" , c.multiplication())
print("Addtion:", c.addition())