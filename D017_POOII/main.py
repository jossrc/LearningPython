class User:

    def __init__(self, user_id, username, followers):
        self.id = user_id
        self.username = username
        self.followers = 0
        print("new user being created...")


user_1 = User("001", "joss", 0)

print(user_1.username)

user_2 = User("002", "angela", 0)

print(user_2)
