from datetime import date
import random



# life class, includes birthdate for being born, deathdate for dying, winning and losing at life.
class Life: 

    # instantiate life with birthdate, 
    def __init__(self, name, country):
        self.name = name
        self.country = country

    # user is born introduce them to the world
    def begin_life(self):
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
        else:
            return self.begin_life()

    def risk_of_dying(self):
        final_wish = str(input(f'\n {self.name}, you have lived a great life living in {self.country}. Was it prosperous? Thats up to you. \n What is your final wish? :  '))
        return (print(f' \n That is a TERRIBLE FINAL WISH, Never Before has the game encountered someone who {final_wish}!!  \n Now you are at risk of dying {self.name} !'))




# class person inherits from life, using self.country and self.name provides method to age(by 20 years) and to set/move countires
class Adult(Life):
    # instantiate the inherited name and age
    def __init__(self, name, country, age = 0, career = 'none', ):
        super().__init__(name, country)
        # protect the age so its only modifiable in the subclass
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
                    return print(f'Dang {self.name}! You kinda messed up! $7/hr is kinda lame, oh well you are only {user_is_eighteen}, you are stuck now for the next 22 years but we will skip them for you good luck!')
                elif (users_job == 2):
                    self._career = 'Store Associate'
                    return print(f'Dang {self.name}! You kinda messed up! $8/hr is kinda lame, oh well you are only {user_is_eighteen}, you are stuck now for the next 22 years but we will skip them for you good luck!')
                elif (users_job == 3):
                    self._career = 'Trash Sorter'
                    return print(f'Dang {self.name}! You kinda messed up! $9/hr is kinda lame, oh well you are only {user_is_eighteen}, you are stuck now for the next 22 years but we will skip them for you good luck!')
                elif (users_job == 4):
                    self._career = 'University Student'
                    return print(f'Aye! Welcome to the Minor Leagues Freshmeat {self.name} you are now in debt by $115,000! Its ok! You are only {user_is_eighteen}! Also life has fast forwarded 22 years')
            elif (user_option.lower() == 'college'):
                self._career = 'University Student'
                print(f'Aye! Welcome to the Minor Leagues Freshmeat {self.name} you are now in debt by $115,000! Its ok! You are only {user_is_eighteen}! Also life has fast forwarded 22 years')
            else:
                print(f'Now that there is too bad, you want to do "{user_option}"!?! That is crazy talk you have something coming for you! \n \n ')
                user_is_eighteen = 40
                return self.move_country()

    def have_a_baby(self):
        baby_name = str(input(f'Hey Congrats on your new baby! What do you want to name them? : '))
        baby = Baby(self.name, baby_name, self.country, 0)
        self.children.append(baby)
        print(f' \n Achievement! {self.name} has a new baby named {baby_name} + 25 points! \n Now you cannot have a baby amd NOT have a house now can you? \n lets skip the next couple of years shall we? \n')
        return self.buy_a_house()

    def buy_a_house(self):
        house_buying_age = self.turn_forty(self._age)
        address = input(f" \n Congrats you are now {house_buying_age}! We call that House Buying Age! Whats your new address? : ")
        self.house.append(address)
        return Baby.baby_get_older(Baby)


class Baby(Adult):
    def __init__(self, parent_name, baby_name, baby_country, baby_age ):
        super().__init__(baby_name, baby_country, baby_age)
        self.parent_name = parent_name

    def baby_get_older(self):
        self.baby_age = 18
        return print(f'Wow {self.parent_name}, we are Proud of You! Your baby has turned {self.baby_age}! Way to go! +60 points!')

    def go_to_school(self):
        pass


class Life_is_going_bad():
    def __init__(self, name, country, age, situation):
        self.adult = Adult(name, country, age) #instantiateing the base
        self.situation = situation

    def series_of_unfortunate_event(self):
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
            self.adult.buy_a_house()
        else:
            print(f'{self.adult.name} died from a sudden heart attack in {self.adult.country} at the age of {self.adult._age}')
            return self.start_over()

    def start_over(self):
        print("\n \n \n \n \n \n \n \n")
        starting_over_question = int(input(f'Hey there {self.adult.name}... Sorry to see you go so soon. \n Life is FULL of choices and questions. Just remember to be yourself no matter what happens, good or bad. \n Do you want to play again? \n 1 = yes \n 2 = no : '))
        if (starting_over_question == 1):
            pass
        print(f"thank you for playing {self.adult.name}")
        quit



if __name__ == "__main__":

    test = Adult('Josh', 'USA', 0, True)

    # print(test.children)
    test.begin_life()
    test.start_a_career()
    # test_country = test.move_country()
    test_age = test.turn_forty(test)

    # testing_baby = Baby("Josh", "USA", test_age, "null")
    # # testing_baby.new_baby("Jared")
    # testing_baby.baby_get_older()

    # test_event = Life_is_going_bad(test.name, test.country, test_age, "car accident")
    # test_event.series_of_unfortunate_event()
# print(test.house)

