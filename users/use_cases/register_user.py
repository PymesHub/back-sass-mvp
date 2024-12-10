from users.domain.entities import UserEntity
from users.domain.repositories import UserRepository

class RegisterUserUseCase:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, data: dict) -> UserEntity:

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