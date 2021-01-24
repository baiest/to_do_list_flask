from flask_login import UserMixin

class UserData:

    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserModel(UserMixin):
    """
    :param user_data: UserData
    """
    def __init__(self, user_data):
        self.id = user_data.username
        self.password = user_data.password

