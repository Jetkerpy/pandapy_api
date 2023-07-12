from django.urls import path
from . import views


urlpatterns = [
    path('sign_up/', views.UserSingUpApiView.as_view(), name = 'sign_up'),
    path('verify/', views.VerifyTokenApiView.as_view(), name = 'verify'),
    path('profile/<int:pk>/', views.ProfileApiView.as_view(), name = 'profile'),
    

]