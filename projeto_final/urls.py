from django.urls import path, include
from rest_framework import routers

from cadastro.views import CadastroViewSet

router = routers.DefaultRouter()
router.register("cadastro", viewset=CadastroViewSet)

urlpatterns = [
    path('', include(router.urls))
]
