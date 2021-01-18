class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):

    def __init__(self):
        # The call to super() in the initializer is recommended, but "not strictly required".
        super().__init__()
    
    def breathe(self):
        super().breathe()  # Inhale, exhale
        print("Doing this underwater")
    
    def swimm(self):
        print("Moving in water")


nemo = Fish()
nemo.swimm()
nemo.breathe()
print(nemo.num_eyes)
