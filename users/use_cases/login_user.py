from users.domain.repositories import UserRepository
from django.contrib.auth.tokens import default_token_generator

class LoginUserCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str, password: str):

        user = self.user_repository.authenticate_user(email=email, password=password)

        if not user:
            raise ValueError("Correo electronico o contraseña incorrectos.")
        
        token = default_token_generator(user)

        return { "user": user, "token": token }