class Endpoints:
    def __init__(self, base: str = ""):
        self.USERS = f"{base}/users"
        self.USER_BY_ID = f"{base}/users/{{id}}"
        self.LOGIN = f"{base}/login"
        self.REGISTER = f"{base}/register"


endpoints = Endpoints()
