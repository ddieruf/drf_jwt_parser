from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from .models import Car
from django.conf import settings
import jwt
from .scraper import scraper
import time



class CarCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CarCreateSerializer
    


class CarUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CarUpdateSerializer
    
    def get_queryset(self):
        token = self.request.headers.get('Authorization').split()[1]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return Car.objects.filter(userid=payload.get('user_id'))  

class CarDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, )
    #serializer_class = CarCreateSerializer
    
    def get_queryset(self):
        token = self.request.headers.get('Authorization').split()[1]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return Car.objects.filter(userid=payload.get('user_id'))


class CarListView(generics.ListAPIView):
    serializer_class = CarDetailSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        token = self.request.headers.get('Authorization').split()[1]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        if self.request.user.is_staff:
            
            if self.request.GET.get('userid'):
                return Car.objects.filter(userid=self.request.GET.get('userid'))
            
            else:
                return Car.objects.filter(userid=payload.get('user_id'))    
        
        else:
            return Car.objects.filter(userid=payload.get('user_id'))
        
class CarScrapeView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        print(request.user.is_active)
        token = request.headers.get('Authorization').split()[1]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        userid = payload.get('user_id')

        user_cars = Car.objects.filter(userid=userid)
        data = []
        pages = request.GET.get('pages') or 0

        for i in user_cars:

            counter = 0
            while counter <= int(pages):
                scraped = scraper(
                    name=f'{i.brand} {i.model}',
                    page=counter
                )
                time.sleep(0.5)
                if scraped != []:
                    for j in scraped:
                        if j['la'] <= i.price:
                            data.append(j)
                    counter+=1
                else:
                    break
        
        return Response(data)
        
        
