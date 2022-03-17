from django.urls import path
from .views import *
urlpatterns = [
    path('create/', CarCreateView.as_view()),
    path('update/<int:pk>', CarUpdateView.as_view()),
    path('delete/<int:pk>', CarDeleteView.as_view()),
    path('all/', CarListView.as_view()),
    path('scrape/', CarScrapeView.as_view())
]
