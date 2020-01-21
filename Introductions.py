class Person: 
    def __init__(self, name, age, sex, height, weight, ethnicity): # custom constructor // 'self' must be first arguement
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.ethnicity = ethnicity
        

    def introduce_self(self): # Must add additional arguement if function is within class
        print("My name is " + self.name + " and I'm " + self.age + " years old.") # this in Java
        print(" ")
        print("Sex: " + self.sex)
        print("Height: " + self.height)
        print("Weight: " + self.weight)
        print("Ethnicity: " + self.ethnicity)
        print(" ")
# When you add a custom constructor, the default one is unusable. So you must comment out the previous code block down below:

# p1 = Person()
# p1.name = 'Anthony Smith'
# p1.age = 20
# p1.height = '177cm'
# p1.weight = '65kg'

# p2 = Person()
# p2.name = 'Chouerlee Pierre-Victor'
# p2.age = 24
# p2.height = '176cm'
# p2.weight = '83kg'

p1 = Person('Anthony Smith', '20', 'Male', '177cm', '65kg', 'Black')
p2 = Person('Chouerlee Pierre-Victor', '24', 'Male', '176cm', '83kg', 'Black')

p1.introduce_self()
p2.introduce_self()
