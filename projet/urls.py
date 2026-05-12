from django.urls import path
from projet import views
urlpatterns = [
    path('', views.ProjetHomeView.as_view(), name='projet-home'),
    path('create/', views.ProjetCreateView.as_view(), name='projet-create'),
    path('detail/<str:slug>/', views.ProjetDetailView.as_view(), name='projet-detail'),
    path('update/<str:slug>/', views.ProjetUpdateView.as_view(), name='projet-update'),
    path('delete/<str:slug>/', views.ProjetDeleteView.as_view(), name='projet-delete'),

]
