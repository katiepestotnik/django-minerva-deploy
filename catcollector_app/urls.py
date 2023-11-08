from django.urls import path
from . import views

urlpatterns = [
    ## WEB PAGES ##
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),

    ## CAT URLS ##
    path('cats/', views.cats_index, name="index"),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    ## feeding url
    path('cats/<int:pk>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('cats/<int:pk>/assoc_toy/<int:toy_pk>/', views.assoc_toy, name='assoc_toy'),

    ## TOY URLS ##
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('cats/<int:pk>/assoc_delete/<int:toy_pk>/', views.assoc_delete, name='assoc_delete'),
    ## url to add photo
    path('cats/<int:cat_id>/add_photo/', views.add_photo, name='add_photo'),
    # sign up route follows accounts/ pattern
    path('accounts/signup', views.signup, name='signup'),
]