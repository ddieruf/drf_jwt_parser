from rest_framework import serializers
from carsapi.models import Car
import jwt
from django.conf import settings

class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ('userid',)

class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
    
    def create(self, validated_data):
        request = self.context.get("request")
        token = request.headers.get('Authorization').split()[1]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        car = Car(
            userid = payload.get('user_id'),
            brand  = validated_data['brand'],
            model  = validated_data['model'],
            price  = validated_data['price'],
        )
        car.save()
        return car

class CarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ('userid','id')