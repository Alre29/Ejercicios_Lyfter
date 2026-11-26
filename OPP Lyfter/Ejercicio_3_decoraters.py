from datetime import date
from functools import wraps

class User:
    def __init__(self, name: str, date_of_birth: date):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self) -> int:
        """Calculates current age in full completed years."""
        today = date.today()
        # Check if birthday has occurred this year
        birthday_passed = (today.month, today.day) >= (self.date_of_birth.month, self.date_of_birth.day)
        return today.year - self.date_of_birth.year - (0 if birthday_passed else 1)


def require_legal_age(func):
    @wraps(func)
    def wrapper(user: User, *args, **kwargs):
        # 1. Verify the first argument is a User instance
        if not isinstance(user, User):
            raise TypeError(f"Expected a User instance, but got {type(user).__name__}.")

        # 2. Check legal age via the age property
        if user.age < 18:
            raise ValueError(f"Access denied: {user.name} is {user.age} years old and must be at least 18.")

        # 3. Run function if the user is an adult
        return func(user, *args, **kwargs)

    return wrapper


# --- Testing ---
@require_legal_age
def grant_entry(user: User):
    return f"Welcome {user.name}, access granted!"

adult_user = User("Carlos", date(1995, 5, 20))
minor_user = User("Mateo", date(2012, 10, 15))

print(grant_entry(adult_user))

try:
    grant_entry(minor_user)
except ValueError as error:
    print(f"Caught error: {error}")