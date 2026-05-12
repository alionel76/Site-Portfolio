from django.urls import path
from blog import views
urlpatterns = [
    path('', views.BlogHomeView.as_view(), name='blog-home'),
    path('create/', views.BlogCreateView.as_view(), name='blog-create'),
    path('detail/<str:slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('update/<str:slug>/', views.BlogUpdateView.as_view(), name='blog-update'),
    path('delete/<str:slug>/', views.BlogDeleteView.as_view(), name='blog-delete'),

]
