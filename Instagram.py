class Instagram:
    usernames = {}
    def __init__(self,name,username,age,gender):
        self.name = name
        self.username = username
        self.age = age
        self.gender = gender
        self.password = input("Enter your password: ")
        self.followers = 0
        self.following = 0
        self.friends_list = []
        self.logged = False
        Instagram.usernames[username] = self

    @classmethod
    def signup(cls):
        name = input("Enter your Name: ")
        while True:
            username = input("Enter your username: ")
            if username in Instagram.usernames.keys():
                print("Username already registered try another one")
                continue
            break
        age = input("Enter your age: ")
        gender = input("Enter your gender(Male/Female): ")
        return cls(name,username,age,gender)

    def login(self):
        if self.logged:
            print("Already logged in")
        else:
            user = input("Enter your username:")
            password = input("Enter your password:")
            if user == self.username and password == self.password:
                self.logged = True
                print("Logged in Successfully")
            else:
                print("Invalid Credentials")

    def logout(self):
        if self.logged:
            self.logged = False
            print("Logged out successfully")
        else:
            print("Already logged out")

    def follow(self,user):
        if self.logged:
            if user not in self.friends_list:
                self.following+=1
                user.followers+=1
                self.friends_list.append(user)
            else:
                print("User is already following")
        else:
            print("Not logged in")

    def unfollow(self,user):
        if self.logged:
            if user in self.friends_list:
                self.following-=1
                user.followers-=1
                self.friends_list.remove(user)
            else:
                print("User not Found")
        else:
            print("Not logged in")

    def profile(self):
        print(f"{self.name}'s Profile")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f'Following : {self.following}')
        print(f'Followers : {self.followers}')

    def friends_profile(self):
        if self.logged:
            for i,j in enumerate(self.friends_list):
                print(f"{i} : {j.name}")

            l = int(input("Enter your choice: "))
            self.friends_list[l].profile()
        else:
            print("Not logged in")


# i1 = Instagram("Cherry","Charan",23,"Male")
i1 = Instagram.signup()
# i2 = Instagram("MK","Murali",23,"Male")
i2 = Instagram.signup()
i3 = Instagram.signup()
i4 = Instagram.signup()
Instagram.login(i1)
i2.login()
i1.follow(i2)
i1.follow(i3)
i1.follow(i4)
i1.profile()
i1.friends_profile()
i2.unfollow(i1)
i3.follow(i2)
i3.friends_profile()