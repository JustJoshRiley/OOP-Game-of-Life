from datetime import date
import random



# life class, includes birthdate for being born, deathdate for dying, winning and losing at life.
class Life: 

    # class attributes
    start_dt = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().toordinal()
    end_dt_death = end_dt
    random_day_birth = date.fromordinal(random.randint(start_dt, end_dt))
    random_day_death = date.fromordinal(random.randint(start_dt, end_dt_death))

    birth_date = random_day_birth
    death_date = random_day_death


    # instantiated attributes, 
    def __init__(self, name, country):
        self.name = name
        self.country = country

    # user is born introduce them to the world
    # start of the game
    def begin_life(self):
        answer_one = str(input('Would you like to begin the game of life...? ("yes" or "no") : '))
        if (answer_one.lower() == 'yes' or answer_one.lower() == 'y'):
            #altering the self.person attribute for the life class with input from prompt for user
            self.name = str(input('Hey there baby person! \n  Welcome, You get to choose a name! \n What do you want to be called...? ("Please enter a string") : ' ))
            self.country = str(input(f'Oi! Almost forgot! What Country are you from {self.name}...? ("Please enter a string) : '))
            return print(f'Wow! Its great to meet you {self.name}! welcome to life! You were born on {self.birth_date} in {self.country}!')
        else:
            print("Ok Run me again when you are ready!!")
            return quit

    def risk_of_dying(self):
        final_wish = str(input(f'\n {self.name}, you have lived a great life living in {self.country}. Was it prosperous? Thats up to you. \n What is your final wish? :  '))
        (print(f' \n That is a TERRIBLE FINAL WISH, Never Before has the game encountered someone who {final_wish}!!  \n Now you are at risk of dying {self.name} !'))
        return print(f'{self.name} lived a great life, supported {final_wish} for {self.country}. He was born on {self.birth_date} and died {self.death_date}')




# class person inherits from life, using self.country and self.name provides method to age(by 20 years) and to set/move countires
class Adult(Life):
    # instantiate the inherited name and age

    # class attributes
    has_house_insurance = False
    monthly_food_budget = 2,000


    # instance attributes
    def __init__(self, name, country, age = 0, career = 'none', ):
        super().__init__(name, country)
        # protect the age so its only modifiable in the subclass, each adult will have a unique age and career only accessible and mutable by them,
        self._age = age
        self._career = career
        self.children = []
        self.house = []

    def age_twenty_years(self, age):
        self._age = 20
        return self._age

    def turn_forty(self, age):
        self._age = 40
        return self._age

    def move_country(self):
        self.age_twenty_years(self._age)
        new_country = str(input(f'Hey there {self.name}! You just turned {self._age}! \n You get to move countries if you would like. Right now you are in {self.country}, where would you like to move? ("Please enter a string") : '))
        self.country = new_country
        print(f'Hey There! {self.name}! Welcome to {self.country}. \n You met someone and decided to stay and adopt a child!! \n \n ')
        return self.have_a_baby()

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
                    monthly_food_budget = 2800
                    print(f'Dang {self.name}! You kinda messed up! $7/hr is kinda lame, oh well you are only {user_is_eighteen}, you are stuck now for the next 22 years but we will skip them for you good luck! \n Your monthly food budget is ${monthly_food_budget} \n')
                    return self.have_a_baby()
                elif (users_job == 2):
                    self._career = 'Store Associate'
                    monthly_food_budget = 3000
                    print(f'Dang {self.name}! You kinda messed up! $8/hr is kinda lame, oh well you are only {user_is_eighteen}, you are stuck now for the next 22 years but we will skip them for you good luck! \n Your monthly food budget is ${monthly_food_budget} \n')
                    return self.have_a_baby()
                elif (users_job == 3):
                    self._career = 'Trash Sorter'
                    monthly_food_budget = 3200
                    print(f'Dang {self.name}! You kinda messed up! $9/hr is kinda lame, oh well you are only {user_is_eighteen}, you are stuck now for the next 22 years but we will skip them for you good luck! \n Your monthly food budget is ${monthly_food_budget} \n')
                    return self.have_a_baby()
                elif (users_job == 4):
                    self._career = 'University Student'
                    monthly_food_budget = 5000
                    print(f'Aye! Welcome to the Minor Leagues Freshmeat {self.name} you are now in debt by $115,000! \n Its ok! You are only {user_is_eighteen}! \n Your monthly food budget is ${monthly_food_budget} Also life has fast forwarded 22 years \n')
                    return self.move_country()
            elif (user_option.lower() == 'college'):
                self._career = 'University Student'
                monthly_food_budget = 5000
                print(f'Aye! Welcome to the Minor Leagues Freshmeat {self.name} you are now in debt by $115,000! Its ok! You are only {user_is_eighteen}! \n Your monthly food budget is ${monthly_food_budget} Also life has fast forwarded 22 years \n')
                return self.move_country()
            else:
                print(f'Now that there is too bad, you want to do "{user_option}"!?! That is crazy talk you have something coming for you! \n \n ')
                user_is_eighteen = 40
                return self.have_a_baby()

    def have_a_baby(self):
        baby_name = str(input(f'Hey Congrats on your new baby! What do you want to name them? : '))
        baby = Baby(self.name, baby_name, self.country, 0)
        self.children.append(baby)
        print(f' \n Achievement! {self.name} has a new baby named {baby_name} + 25 points! \n Now you cannot have a baby and NOT have a house now can you? \n lets skip the next couple of years shall we? \n')
        return self.buy_a_house()

    def buy_a_house(self):
        house_buying_age = self.turn_forty(self._age)
        address = input(f" \n Congrats you are now {house_buying_age}! We call that House Buying Age! Whats your new address? : ")
        self.house.append(address)
        has_house_insurance = True
        print(f'It is {has_house_insurance} that {address} now has house insurance under {self.name}, believe it {self.name} did not have any before \n ')
        start_over_instance = Life_is_going_bad(self.name, self._age, self.country, " ")
        return start_over_instance.series_of_unfortunate_event()

class Baby(Adult):
    # class attributes
    birth_certificate = False
    grade_in_school = 'A'

    # instance attributes
    def __init__(self, parent_name, name, country, age ):
        super().__init__(name, country, age)
        self.parent_name = parent_name

    def baby_get_older(self):
        self.baby_age = 18
        self.birth_certificate = True
        print(f'Wow {self.name}, we are Proud of You! Your baby has turned {self._age}! Way to go! +60 points!')
        return self.start_a_career()

    def go_to_school(self):
        print(f'{self.name} is going to school for {self.baby_age} years.')
        return self.baby_get_older()

    def report_card(self):
        return print(f'this is your current grade in school {self.grade_in_school}')

class Life_is_going_bad():
    # class attributes
    is_struggling = True
    is_dead = False

    # instance attributes
    def __init__(self, name, country, age, situation):
        self.adult = Adult(name, country, age) #instantantiating the base
        self.situation = situation

    def series_of_unfortunate_event(self):
        if (self.adult._age == 40):
            start_series = str(input((f'Uh Oh! {self.situation} just happened to {self.adult.name} in {self.adult.country} at {self.adult._age} years old! \n Will you be ok? : ("Please answer yes or no") ')))
            if (start_series.lower() == 'yes' or start_series.lower == 'y'):
                new_age = self.adult.age_twenty_years(self.adult._age) - 16
                print(f'Well Since your ok, we decided that you are resilient, Here is your new age {new_age}')
                continue_series = str(input(f'would you like the next event? : ("Please answer yes or no") '))
                if (continue_series.lower() == 'yes' or continue_series.lower == 'y'):
                    print(f'The Most unfortunate thing happened to {self.adult.name}! You got deported from {self.adult.country} for no reason! \n')
                    deporting_you_to_where = str(input(f'Where do you think {self.adult.country} is deporting you to? : '))
                    print(f'{self.adult.name} got deported to {deporting_you_to_where}')
                    pass
                self.start_over()
            else:
                print(f'{self.adult.name} died from a sudden heart attack in {self.adult.country} at the age of {self.adult._age}')
                return self.start_over()

    def start_over(self):
        print("\n \n")
        starting_over_question = int(input(f'Hey there {self.adult.name}... Sorry to see you go so soon. \n Life is FULL of choices and questions. Just remember to be yourself no matter what happens, good or bad. \n Do you want to play again? \n 1 = yes \n 2 = no : '))
        if (starting_over_question == 1):
            return self.adult.begin_life()
        self.is_dead = True
        self.is_struggling = False
        print(f"thank you for playing {self.adult.name}")


if __name__ == "__main__":

    
    # instantiate life
    # life_test = Life('Jarden', 'France')
    # life_test.risk_of_dying()
    # instantiate Adult
    adult_test = Adult('Josh', 'USA', 0, True)
    adult_test.begin_life()
    adult_test.start_a_career()
    test_age = adult_test.turn_forty(adult_test)
    # instantiate baby
    # testing_baby = Baby("", "USA", test_age, "null")
    adult_test.have_a_baby()
    child = adult_test.children[0]
    child.baby_get_older()
    # instantiate Life is going bad
    test_event = Life_is_going_bad(adult_test.name, adult_test.country, 40, "car accident")
    test_event.series_of_unfortunate_event()

