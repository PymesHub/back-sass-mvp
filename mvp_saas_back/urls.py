from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import UserView

schema_view = get_schema_view(
    openapi.Info(
        title="Back End Saas",
        default_version="v1",
        description="Api documentation from saas"
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('api/register/', UserView.as_view(), name='user-registration')
]
