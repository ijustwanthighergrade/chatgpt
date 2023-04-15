from django.shortcuts import render,redirect
# Create your views here.s

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from booking.models import 

def login(request):
    if request.method == 'POST':
        # 檢查用戶是否存在，如果存在，則將其設置為已登錄的 session
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            # 登錄失敗，顯示錯誤消息
            return render(request, 'register.html', {'error': '登入失敗，可以註冊'})
    else:
        # GET 請求顯示登錄表單
        return render(request, 'login.html')

