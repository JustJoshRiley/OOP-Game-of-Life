from adult import Adult


class Baby(Adult):
    def __init__(self, name, country, age, baby_name, baby_age = 0):
        super().__init__(name, country, age)
        self.baby_name = baby_name
        self.baby_age = baby_age

    # new_baby 
    def new_baby(self, baby_name):
        
        self.baby_name = str(input(f'Hey Congrats on your new baby! What do you want to name them? : '))
        return print(f'Achievement! {self.name} has a new baby named {self.baby_name} + 25 points')

    def baby_get_older(self):
        self.baby_age = 18
        return print(f'Wow {self.name}, we are Proud of You! Your baby has turned {self.baby_age}! Way to go! +60 points!')