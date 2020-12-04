from life import Life

# class person inherits from life, using self.country and self.name provides method to age(by 20 years) and to set/move countires
class Adult(Life):
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
                user_is_eighteen = 40