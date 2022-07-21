from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('create', views.CreateView.as_view(), name='create'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>', views.ReviewLike.as_view(), name='review_like'),
    path('funny/<slug:slug>', views.ReviewFunny.as_view(), name='review_funny'),
    path('insightful/<slug:slug>', views.ReviewInsightful.as_view(), name='review_insightful'),
]
