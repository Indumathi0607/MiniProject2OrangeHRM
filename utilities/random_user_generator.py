import random
import string

import utilities.constants as const


class RandomUserGenerator:

    def auto_generate_username(self):
        prefix = "employee "
        random_suffix = "".join(random.choices(string.digits, k=4))
        username = prefix+random_suffix
        const.EMPLOYEE_USERNAME = username
        print(f"Username is {username} and new user name is {const.EMPLOYEE_USERNAME}")
        return username



