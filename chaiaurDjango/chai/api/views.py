from chai.models import chaiVarity
from chai.api.serializers import chaiVaritySerializer
from rest_framework import viewsets

class chaiVarityViewSet(viewsets.ModelViewSet):
    queryset = chaiVarity.objects.all()
    serializer_class = chaiVaritySerializer