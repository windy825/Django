from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("인덱스 뷰 함수 실행 완료")