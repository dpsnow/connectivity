from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.UserListView.as_view(), name='users'),
    re_path('^user/(?P<pk>\d+)$', views.UserDetailView.as_view(), name='user-data'),
]
