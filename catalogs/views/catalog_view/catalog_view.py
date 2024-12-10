from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from catalogs.application.repositories import DjangoCatalogRepository
from catalogs.application.serializer import CatalogSerializer
from catalogs.use_cases.create_catalog.catalog import CreateCatalogUseCase
from drf_yasg.utils import swagger_auto_schema
from catalogs.application.exceptions import CatalogAlreadyExistsException
from catalogs.use_cases.get_catalog_by_id.get_catalog_by_id import GetCatalogById
from catalogs.application.exceptions import CatalogNotFoundException

class CatalogView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        repository = DjangoCatalogRepository()
        self.repository = repository

    permission_classes = [IsAuthenticated]

    def get(self, request, catalog_id: None):
   
        if catalog_id is None:
            return Response({ "message": "Ingresa un id válido" }, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:

                get_catalog_by_id_use_case = GetCatalogById(self.repository)
                django_catalog = get_catalog_by_id_use_case.execute(catalog_id)
                serializer = CatalogSerializer(django_catalog)
                return Response({
                    "message": "cátalogo encontrado",
                    "data": serializer.data
                })
            except CatalogNotFoundException as e:
                return Response({
                    "message": str(e)
                }, status=status.HTTP_404_NOT_FOUND) 

    @swagger_auto_schema(
            operation_description="Crear un nuevo cátalogo",
            request_body=CatalogSerializer
    )
    def post(self, request):
        
        serializer = CatalogSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data

            create_catalog_use_case = CreateCatalogUseCase(self.repository)
            user = request.user
            
            try:
                catalog_entity = create_catalog_use_case.execute(validated_data, user.id)
                return Response(
                    {"message": f"Cátalogo {catalog_entity.name} creado", "catalog_id": catalog_entity.id},
                    status=status.HTTP_201_CREATED
                )
            except CatalogAlreadyExistsException as e:
                return Response({ "error": str(e) }, status=status.HTTP_400_BAD_REQUEST)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
