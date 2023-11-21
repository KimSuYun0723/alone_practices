from django.urls import path
from .views import *

app_name = 'acoounts'

urlpatterns = [
    path('login/', login),
    path('signup/', signup),
    path('logout/', logout)
]