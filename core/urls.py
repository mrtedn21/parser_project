from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from parser.views import BillViewSet
from parser.views import BillsFileViewSet

router = DefaultRouter()
router.register(r'bills', BillViewSet)
router.register(r'bills_file', BillsFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
