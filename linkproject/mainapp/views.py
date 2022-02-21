from multiprocessing import managers
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .serializers import ReviewSerializer
from .models import Review
# Create your views here.

class ReviewList(APIView):
    def get(self, request): #리스트 보여줄때
        reviews=Review.objects.all() #객체 싹다 가져와서
        serializer=ReviewSerializer(reviews, many=True) #가져온 여러개 객체 serialize 여러개 쓰려면 many=True
        return Response(serializer.data)
    def post(self,request):
        serializer=ReviewSerializer(data=request.data) #request.data는 사용자가 입력한 데이터
        if serializer.is_valid():
            serializer.save() #유효하면 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED) #유효할때 반환
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #유효하지 않을 때 반환

class ReviewDetail(APIView):
    def get_object(self,pk): 
        try:
            return Review.objects.get(pk=pk) #리뷰 객체 가져오기
        except Review.DoesNotExist:
            raise Http404 
    def get(self,request,pk,format=None):
        review=self.get_object(pk) #이 클래스 안에 있는 함수 이용한다는 뜻
        serializer=ReviewSerializer(review)
        return Response(serializer.data)
    def put(self,request,pk,format=None):
        review=self.get_object(pk) #이 클래스 안에 있는 함수 이용한다는 뜻
        serializer=ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        review=self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)