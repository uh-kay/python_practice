from user import User
from privileges import Priveleges


class Admin(User):
    """An attempt to model an admin user."""

    def __init__(self, first_name, last_name, age, address, priveleges=[],
                 login_attempts=0):
        """
        Initializes atrributes of the parent class.
        Then initializes attributes specific to admin.
        """
        super().__init__(first_name, last_name, age, address, login_attempts=0)
        self.priveleges = Priveleges(priveleges)
