from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.use_cases.login_user import LoginUserCase
from users.application.repositories import DjangoUserRepository
from users.application.serializer import LoginSerializer
from drf_yasg.utils import swagger_auto_schema

class LoginView(APIView):

    @swagger_auto_schema(
            operation_description="Iniciar sesion",
            request_body=LoginSerializer,
            responses={ 200: "Login éxitoso", 400: 'Invalid request data', 500: 'Internal server error' }
    )
    def post(self, request, *args, **kwargs):

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():

            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user_repository = DjangoUserRepository()
            login_user_use_case = LoginUserCase(user_repository)

            try: 
                result = login_user_use_case.execute(email=email, password=password)
                return Response({ "message": "Inicio de sesión éxitoso", "token": result['token'] })
        
            except ValueError as e:
                return Response({ "error": str(e)}, status=status.HTTP_400_BAD_REQUEST )
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)