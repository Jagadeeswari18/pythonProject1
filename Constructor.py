#Constructors are generally used for instantiating an object.
#The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created.
#In Python the __init__() method is called the constructor and is always called when an object is created.
#Syntax of constructor declaration :
#def __init__(self):
#body of the constructor


class KLU:
    def __init__(self, name, id):  # Parameterized Constructor
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


obj1 = KLU("Feroz", 101)
obj2 = KLU("Khan", 102)
obj1.display()
obj2.display()