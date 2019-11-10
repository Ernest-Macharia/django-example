from django.urls import path
from prediction import views

#TEMPLATE TAGGING
app_name = 'prediction'

urlpatterns = [
    path('register/',views.register, name ='register'),
    path('user_login/',views.user_login, name='user_login'),
    

]