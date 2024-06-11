class Priveleges:
    """A simple attempt to model admin privileges."""

    def __init__(self, priveleges=[]):
        """Initializes privileges attributes."""
        self.priveleges = priveleges

    def show_privileges(self):
        """Display admin privileges."""
        print("Admin priveleges:")
        for privilege in self.priveleges:
            print(f"- {privilege}")
