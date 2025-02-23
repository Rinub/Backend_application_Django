from django.urls import path
from .views import get_persons, get_persons_FREE, add_person_to_excel

urlpatterns = [
    path('persons/', get_persons, name='get_persons'),
    path('persons_free/', get_persons_FREE, name='get_persons_FREE'),
    path('add_person/', add_person_to_excel, name='add_person_to_excel'),
]
