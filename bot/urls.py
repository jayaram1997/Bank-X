from django. urls import path
from bot import views

app_name = 'boturlhome'
urlpatterns=[
    path('',views.index1),
]