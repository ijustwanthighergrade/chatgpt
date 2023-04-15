from django.shortcuts import render,redirect
# Create your views here.s

from django.shortcuts import render, redirect
import requests

from booking.models import member
from booking.models import sign_in

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        if username==None or password==None:
            return render(request, 'login.html', {'error': '密碼錯誤'})
        # 檢查用戶是否存在，如果存在，則將其設置為已登錄的 session
        if member.objects.filter(account = username).exists():
            if member.objects.filter(password = password):
                request.session['account'] = username
                return redirect('home') 
            #要改成首頁
            else:
                return render(request, 'login.html', {'error': '密碼錯誤'})
        else:
            # 登錄失敗，顯示錯誤消息
            return render(request, 'register.html', {'error': '沒有此帳號，請註冊或是登入其他帳號'})
    else:
        # GET 請求顯示登錄表單
        return render(request, 'login.html')

def register(request):
    username=request.POST['username']
    password=request.POST['password']
    password=request.POST['password']
    password=request.POST['password']