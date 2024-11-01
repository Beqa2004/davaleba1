class PlatformAccount:
    def __init__(self, username, membership_type):
        self.username = username
        self.membership_type = membership_type
        self.view_limit = self.set_view_limit()
        self.views = 0 

    def set_view_limit(self):
        if self.membership_type == "Basic":
            return 3
        elif self.membership_type == "Premium":
            return 5
        elif self.membership_type == "VIP":
            return 10
        else:
            raise ValueError("Invalid membership type")

    def watch_video(self):
        if self.views < self.view_limit:
            self.views += 1
            print(f"{self.username} watched a video. Remaining views: {self.view_limit - self.views}")
        else:
            print(f"{self.username} has reached the viewing limit.")

    def add_view_limit(self, additional_views):
        self.view_limit += additional_views
        print(f"{self.username}'s view limit increased to {self.view_limit}.")


class BasicAccount(PlatformAccount):
    def __init__(self, username):
        super().__init__(username, "Basic")


class PremiumAccount(PlatformAccount):
    def __init__(self, username):
        super().__init__(username, "Premium")


class VIPAccount(PlatformAccount):
    def __init__(self, username):
        super().__init__(username, "VIP")


class PlatformCard:
    def __init__(self, cardholder_name, card_type, user_account):
        self.cardholder_name = cardholder_name
        self.card_type = card_type
        self.user_account = user_account

    def get_card_info(self):
        print(f"Cardholder Name: {self.cardholder_name}\nCard Type: {self.card_type}\nAccount Username: {self.user_account.username}\nMembership Type: {self.user_account.membership_type}\nView Limit: {self.user_account.view_limit}\nRemaining Views: {self.user_account.view_limit - self.user_account.views}")
    
user1 = BasicAccount("beqa")
user1.watch_video()
user1.watch_video()


user1_card = PlatformCard("Beqa", "Digital", user1)
print(user1_card.get_card_info())
