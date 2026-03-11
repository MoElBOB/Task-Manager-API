from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# إعداد swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Task Manager API",
      default_version='v1',
      description="API documentation for Task Manager project",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/', include('tasks.urls')),

    path('api/token/', TokenObtainPairView.as_view()),

    path('api/token/refresh/', TokenRefreshView.as_view()),

    # swagger documentation
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]