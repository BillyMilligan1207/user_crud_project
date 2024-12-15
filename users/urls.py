from django.urls import path
from .views import UserView

urlpatterns = [
    path('', UserView.as_view(), name='home'),
    path('api/users/', UserView.as_view(), name='user_list'),
    path('api/users/<int:user_id>/', UserView.as_view(), name='user_detail'),
]
