from django.urls import path

from . import views


urlpatterns = [
    path('', views.InfoListView.as_view(), name='index'),
    path('unsorted', views.UnsortedListView.as_view(), name='unsorted'),
    path('<int:id>', views.one_item_detail, name='detail'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]
