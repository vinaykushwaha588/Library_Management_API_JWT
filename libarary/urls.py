from django.urls import path

## define here urls - http//127.0.0.1:8000/libarary/

from .views import *

urlpatterns = [
    path('post/',library_view),
    path('update/<int:bid>/',library_update_delete),
]
