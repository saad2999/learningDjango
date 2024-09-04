from django.urls import path, include
from chai.api.views import chaiVarityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud', chaiVarityViewSet, basename='chai')

urlpatterns = [
    path('', include(router.urls)),
    
]
