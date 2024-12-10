from users.domain.repositories import UserRepository
from utils.generatetoken import generate_token


class LoginUserCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str, password: str):

        user = self.user_repository.authenticate_user(email=email, password=password)

        if not user:
            raise ValueError("Correo electronico o contraseña incorrectos.")
        
        token = generate_token(user)

        return { "user": user, "token": token }