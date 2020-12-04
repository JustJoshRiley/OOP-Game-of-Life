from datetime import date
import random

# life class, includes birthdate for being born, deathdate for dying, winning and losing at life.
class Life: 

    # instantiate life with birthdate, deathdate, winner, loser 
    def __init__(self, name, country):
        self.name = name
        self.country = country

    # user is born introduce them to the world
    def user_is_born(self):
        start_dt = date.today().replace(day=1, month=1).toordinal()
        end_dt = date.today().toordinal()
        random_day = date.fromordinal(random.randint(start_dt, end_dt))
        
        # asking for the users first 'answer' or input to start the game
        answer_one = str(input('Would you like to begin the game of life...? ("yes" or "no") : '))

        if (answer_one.lower() == 'yes' or answer_one.lower() == 'y'):
            #altering the self.person attribute for the life class with input from prompt for user
            self.name = str(input('Hey there baby person! \n  Welcome, You get to choose a name! \n What do you want to be called...? ("Please enter a string") : ' ))
            self.country = str(input(f'Oi! Almost forgot! What Country are you from {self.name}...? ("Please enter a string) : '))
            return print(f'Wow! Its great to meet you {self.name}! welcome to life! You were born on {random_day} in {self.country}!')
        pass

# class person inherits from life, using self.country and self.name provides method to age(by 20 years) and to set/move countires
class Person(Life):
    # instantiate the inherited name and age
    def __init__(self, name, country, age = 0, career = 'none'):
        super().__init__(name, country)
        # protect the age so its only modifiable in the subclass
        self._age = age
        self._career = career

    def age_twenty_years(self, age):
        self._age += 20
        return self._age

    def turn_forty(self, age):
        self._age = 40
        return self._age 

    def move_country(self):
        self.age_twenty_years(self._age)
        new_country = str(input(f'Hey there {self.name}! You just turned {self._age}! \n You get to move countries if you would like. Right now you are in {self.country}, where would you like to move? ("Please enter a string") : '))
        self.country = new_country
        return print(f'Hey There! {self.name}! Welcome to {self.country}')

    def start_a_career(self):
        # decide on the career, job or college at 18
        while (self._age == 0):
            # make the user 18 just subtract two from the original 20
            user_is_eighteen = self.age_twenty_years(self._age) - 2
            user_option = str(input(f'Hey there {self.name}! Welcome to age {user_is_eighteen} Would you like to go to College or Get a Job? \n ("Please enter College or Job") : '))

            if (user_option.lower() == 'job'):
                # find out what the user wants to do for a career
                users_job = int(input(f'You Chose to get a JOB at the age of {user_is_eighteen}! What Job do you want? 1 = Chashier $7/hr  \n 2 = Store Associate $8/hr  \n 3 = Trash Sorter $9/hr \n 4 = Never Mind, go to college! $Unk/hr \n ("Please Enter a 1, 2, 3, or 4") : '))
                if (users_job == 1):
                    self._career = 'Cashier'
                    return print(f'Dang {self.name}! You kinda messed up! $7/hr is kinda lame, oh well you are only {user_is_eighteen}, you are stuck now for the next 20 years but we will skip them for you good luck!')
                elif (users_job == 2):
                    self._career = 'Store Associate'
                    return print(f'Dang {self.name}! You kinda messed up! $8/hr is kinda lame, oh well you are only {user_is_eighteen}, you are stuck now for the next 20 years but we will skip them for you good luck!')
                elif (users_job == 3):
                    self._career = 'Trash Sorter'
                    return print(f'Dang {self.name}! You kinda messed up! $9/hr is kinda lame, oh well you are only {user_is_eighteen}, you are stuck now for the next 20 years but we will skip them for you good luck!')
                elif (users_job == 4):
                    self._career = 'University Student'
                    return print(f'Aye! Welcome to the Minor Leagues Freshmeat {self.name} you are now in debt by $115,000! Its ok! You are only {user_is_eighteen}! Also life has fast forwarded 4 years')
                
            elif (user_option.lower() == 'college'):
                self._career = 'University Student'
                print(f'Aye! Welcome to the Minor Leagues Freshmeat {self.name} you are now in debt by $115,000! Its ok! You are only {user_is_eighteen}! Also life has fast forwarded 4 years')
            else:
                user_is_eighteen = 40
                print(user_is_eighteen)

class Baby(Person):
    def __init__(self, name, country, age, baby_name, baby_age = 0):
        super().__init__(name, country, age)
        self.baby_name = baby_name
        self.baby__age = baby_age

    # new_baby 
    def new_baby(self, baby_name):
        self.baby_name = str(input(f'Hey Congrats on your new baby! What do you want to name them? : '))
        return print(f'Achievement! {self.name} has a new baby named {self.baby_name} + 25 points')



test = Person('Josh', 'USA', 0, True)
test.user_is_born()
test.start_a_career()
test.move_country()
test.turn_forty(test)
testing_baby = Baby("Josh", "USA", 40, "null")
testing_baby.new_baby("Jared", 0)

