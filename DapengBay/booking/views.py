from django.shortcuts import render,redirect
# Create your views here.s

from django.shortcuts import render, redirect
import requests

from booking.models import member
from booking.models import sign_in
from .models import participate,dinner_shop

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        if username==None or password==None:
            return render(request, 'login.html', {'error': '密碼錯誤'})
        # 檢查用戶是否存在，如果存在，則將其設置為已登錄的 session
        if sign_in.objects.filter(account = username).exists():
            if sign_in.objects.filter(password = password):
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
        return render(request, 'complete.html')

def register(request):
    error=""
    if request.method == 'POST':
        username=request.POST['name']
        password=request.POST['password']
        phone=request.POST['phone']
        email=request.POST['email']
        if username==None or password==None or phone==None or email==None:
            return render(request, 'register.html', {'error': '請填寫完整'})
        else:
            if member.objects.filter(Email=email).exists():
                return render(request, 'register.html', {'error': '已有此帳號'})
            else:
                sign_in.objects.create(account=email,password=password)
                member.objects.create(Email=email,phone=phone,name=username)
                return render(request, 'login.html')



def add_person(request):
    if participate.objects.count() >= 6:
        return render(request, 'exceed.html')
    if request.method == "GET":
            name = request.GET.get('name')
            mid = request.GET.get('mid')
            birth = request.GET.get('birthday')
            insurance = request.GET.get('insurance_status')
            new_person = participate(Name=name, MID=mid, insurance_status=insurance,birthday=birth)
            new_person.save()
            persons = participate.objects.all()
            num=participate.objects.count()
    return render(request, 'list_persons.html',locals())

def complete(request):
    if 'account' in request.session:
        if request.method == "GET":
            id = request.GET.get('id')
        return render(request, 'complete.html',locals())
    else:
        return render(request, 'login.html')

def list_persons(request):
    persons = participate.objects.all()
    return render(request, 'list_persons.html', {'persons': persons})

def delete_person(request, person_id):
    person = participate.objects.get(id=person_id)
    person.delete()
    return redirect('list_persons')

def edit1(request):
    member = member.objects.get(account=id)
    return render(request, 'edit.html', {'member': member})

def home(request):
    if 'account' in request.session:
        if request.method == "GET":
            id = request.GET.get('id')
        return render(request, 'home.html',locals())
    else:
        return render(request, 'login.html')
    
def logout(request):
    if 'account' in request.session:
        del request.session['account']
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    


def dinner(request):
    items = dinner_shop.objects.all()
    return render(request, 'dinner.html', {'items': items})















def break_view(request):
    return render(request, 'break.html')



def breakfast_items(request):
    items = breakfast_shop.objects.all()
    return render(request, 'break.html', {'items':items})



def order(request):
    if request.method == 'POST':
        items = []
        total_price = 0
        counter=0
        for i in range(1, counter+1):
            item_name = request.POST.get('breakfast_items')
            item_price = request.POST.get('price' + str(i))
            item_quantity = request.POST.get('quantity' + str(i))
            item_total = int(item_price) * int(item_quantity)
            total_price += item_total
            items.append({
                'name': item_name,
                'price': item_price,
                'quantity': item_quantity,
                'total': item_total
            })
        # 將訂單儲存到資料庫中
        # ...
        # 將總金額傳遞給HTML模板
        return render(request, 'order.html', {'items': items, 'total_price': total_price})