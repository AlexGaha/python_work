


class User:
    def __init__(self, first_name, last_name, email, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name) 
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_reward_member)
        print(self.gold_card_points)
    def enroll(self):
        self.is_reward_member = True 
        self.gold_card_points = 200
        return self
    def spend_points(self,ammount): 
        self.gold_card_points - ammount
        return self
alex_info = User('alex','gahungu','alexgauhngu@iclod.com',42)
alex_info.enroll().spend_points().display_info()
