from chai.models import chaiVarity
from rest_framework import serializers # type: ignore

class chaiVaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = chaiVarity
        fields = '__all__'