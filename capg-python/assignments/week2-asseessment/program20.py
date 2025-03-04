from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self, username, password):
        pass

    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self, username, password):
        print(f"GoogleAuth: User '{username}' logged in successfully.")

    def logout(self):
        print("GoogleAuth: User logged out successfully.")

class FacebookAuth(UserAuthentication):
    def login(self, username, password):
        print(f"FacebookAuth: User '{username}' logged in successfully.")

    def logout(self):
        print("FacebookAuth: User logged out successfully.")

google_auth = GoogleAuth()
facebook_auth = FacebookAuth()

google_auth.login("krutin", "asdfasdf")
google_auth.logout()

facebook_auth.login("rishi", "asdfasdf")
facebook_auth.logout()