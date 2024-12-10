from users.domain.entities import UserEntity
from users.domain.repositories import UserRepository
from users.application.exceptions import EmailAlreadyExistsException

class RegisterUserUseCase:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, data: dict) -> UserEntity:

        if self.user_repository.user_exists_by_email(email=data["email"]):
            raise EmailAlreadyExistsException("Este correo electrónico ya está en uso")

        user_entity = UserEntity(
            username=data["email"],
            email=data["email"],
            password=data["password"],
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            telephone=data.get("telephone", ""),
            country=data.get("country", "")
            )

        return self.user_repository.create_user(user_entity)