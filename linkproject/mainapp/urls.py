from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ReviewList, ReviewDetail

urlpatterns=[
    path('review/',ReviewList.as_view()),
    path('review/<int:pk>/',ReviewDetail.as_view()), #얘는 클래스형 뷰라 함..
]

urlpatterns=format_suffix_patterns(urlpatterns)