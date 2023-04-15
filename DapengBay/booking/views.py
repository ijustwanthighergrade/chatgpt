<<<<<<< HEAD
from django.shortcuts import render,redirect
# Create your views here.s

from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from booking.models import member
from booking.models import sign_in
from booking.models import travel
from booking.models import breakfast
from booking.models import Dinner
from .models import participate

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
        return render(request, 'login.html')

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
    else:
        return render(request, 'register.html')



def add_person(request):
    if 'account' in request.session:
        if participate.objects.count() >= 6:
            return render(request, 'exceed.html')
        if request.method == "GET":
                message = ''
                name = request.GET.get('name')
                mid = request.GET.get('mid')
                birth = request.GET.get('birthday')
                insurance = request.GET.get('insurance_status')
                if participate.objects.filter(MID=mid).exists():
                    message = '身分證已存在，請輸入不同的身分證。'
                    return redirect('list_persons')
                else:
                    new_person = participate(Name=name, MID=mid, insurance_status=insurance,birthday=birth)
                    new_person.save()
                persons = participate.objects.all()
                num=participate.objects.count()
        return render(request, 'list_persons.html',locals())
    else:
        return render(request, 'login.html')

def complete(request):
    if 'account' in request.session:
        prob = participate.objects.filter(booking_number=0)
        prob_list =list(prob.values())
        if request.method == "GET":
            id = request.GET.get('id')
        return render(request, 'complete.html',locals())
    else:
        return render(request, 'login.html',{'prob_list':prob_list})

def list_persons(request):
    if 'account' in request.session:
        persons = participate.objects.all()
        num=persons.count()
        return render(request, 'list_persons.html', {'persons': persons,'num':num})
    else:
        return render(request, 'login.html')

def delete_person(request, person_id):
    person = participate.objects.get(id=person_id)
    person.delete()
    return redirect('list_persons')
def update_person(request):
    if request.method == "GET":
        name = request.GET.get('name')
        mid = request.GET.get('mid')
        birthday = request.GET.get('birthday')
        insurance_status = request.GET.get('insurance_status')

        person = participate.objects.get(MID=mid)
        person.Name = name
        person.MID = mid
        person.birthday = birthday
        person.insurance_status = insurance_status
        person.save()

    return redirect('list_persons')


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
    
def edit1(request):
    amember=""
    atravel=""
    aparticipate=""
    if 'account' in request.session:
        id = request.session['account']
        if request.method == "GET":
            amember = member.objects.get(Email=id)
            atravel = travel.objects.all()
            aparticipate = participate.objects.all()
            num=participate.objects.count()

        return render(request, 'edit.html', {'amember': amember,'atravel': atravel,'aparticipate':aparticipate,'num':num})
    else:
        return render(request, 'login.html')
def delete_edit(request):
    person = participate.objects.all()
    person.delete()
    travel_de = travel.objects.all()
    travel_de.delete()
    breakfast_de = breakfast.objects.all()
    breakfast_de.delete()
    dinner_de = Dinner.objects.all()
    dinner_de.delete()
    return redirect('edit')
=======
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
from django.shortcuts import render,redirect
# Create your views here.s

from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from booking.models import member
from booking.models import sign_in
from booking.models import travel
from booking.models import breakfast
from booking.models import Dinner
from .models import participate
from datetime import datetime

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
    else:
        return render(request, 'register.html')



def add_person(request):
    if 'account' in request.session:
        if participate.objects.count() >= 6:
            return render(request, 'exceed.html')
        if request.method == "GET":
                message = ''
                name = request.GET.get('name')
                mid = request.GET.get('mid')
                birth = request.GET.get('birthday')
                insurance = request.GET.get('insurance_status')
                if participate.objects.filter(MID=mid).exists():
                    message = '身分證已存在，請輸入不同的身分證。'
                    return redirect('list_persons')
                else:
                    new_person = participate(Name=name, MID=mid, insurance_status=insurance,birthday=birth)
                    new_person.save()
                persons = participate.objects.all()
                num=participate.objects.count()
        return render(request, 'list_persons.html',locals())
    else:
        return render(request, 'login.html')

def complete(request):
    if 'account' in request.session:
        prob = participate.objects.filter(booking_number=0)
        prob_list =list(prob.values())
        if request.method == "GET":
            id = request.GET.get('id')
        return render(request, 'complete.html',locals())
    else:
        return render(request, 'login.html',{'prob_list':prob_list})

def list_persons(request):
    if 'account' in request.session:
        persons = participate.objects.all()
        num=persons.count()
        return render(request, 'list_persons.html', {'persons': persons,'num':num})
    else:
        return render(request, 'login.html')

def delete_person(request, person_id):
    person = participate.objects.get(id=person_id)
    person.delete()
    return redirect('list_persons')
def update_person(request):
    if request.method == "GET":
        name = request.GET.get('name')
        mid = request.GET.get('mid')
        birthday = request.GET.get('birthday')
        insurance_status = request.GET.get('insurance_status')

        person = participate.objects.get(MID=mid)
        person.Name = name
        person.MID = mid
        person.birthday = birthday
        person.insurance_status = insurance_status
        person.save()

    return redirect('list_persons')


def home(request):
    if 'account' in request.session:
        if request.method == "GET":
            id = request.GET.get('id')
        return render(request, 'home.html',locals())
    else:
        return render(request, 'login.html')
def save_travel(request):
    # 讀取日期
    date_str = request.POST['date_input']
    # 將日期轉換為datetime物件
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    # 建立travel模型的實例
    travel_obj = travel()
    # 設定travel_date欄位的值
    travel_obj.travel_date = date_obj
    # 儲存travel模型
    travel_obj.save()


    
def logout(request):
    if 'account' in request.session:
        del request.session['account']
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def edit1(request):
    amember=""
    atravel=""
    if 'account' in request.session:
        id = request.session['account']
        if request.method == "GET":
            amember = member.objects.get(Email=id)
            atravel = travel.objects.get(id=0)
        return render(request, 'edit.html', {'amember': amember,'atravel': atravel})
    else:
        return render(request, 'login.html')
from django.shortcuts import render,redirect
# Create your views here.s

from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from booking.models import member
from booking.models import sign_in
from booking.models import travel
from booking.models import breakfast
from booking.models import Dinner
from .models import participate

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
    else:
        return render(request, 'register.html')



def add_person(request):
    if 'account' in request.session:
        if participate.objects.count() >= 6:
            return render(request, 'exceed.html')
        if request.method == "GET":
                message = ''
                name = request.GET.get('name')
                mid = request.GET.get('mid')
                birth = request.GET.get('birthday')
                insurance = request.GET.get('insurance_status')
                if participate.objects.filter(MID=mid).exists():
                    message = '身分證已存在，請輸入不同的身分證。'
                    return redirect('list_persons')
                else:
                    new_person = participate(Name=name, MID=mid, insurance_status=insurance,birthday=birth)
                    new_person.save()
                persons = participate.objects.all()
                num=participate.objects.count()
        return render(request, 'list_persons.html',locals())
    else:
        return render(request, 'login.html')

def complete(request):
    if 'account' in request.session:
        prob = participate.objects.filter(booking_number=0)
        prob_list =list(prob.values())
        if request.method == "GET":
            id = request.GET.get('id')
        return render(request, 'complete.html',locals())
    else:
        return render(request, 'login.html',{'prob_list':prob_list})

def list_persons(request):
    if 'account' in request.session:
        persons = participate.objects.all()
        num=persons.count()
        return render(request, 'list_persons.html', {'persons': persons,'num':num})
    else:
        return render(request, 'login.html')

def delete_person(request, person_id):
    person = participate.objects.get(id=person_id)
    person.delete()
    return redirect('list_persons')
def update_person(request):
    if request.method == "GET":
        name = request.GET.get('name')
        mid = request.GET.get('mid')
        birthday = request.GET.get('birthday')
        insurance_status = request.GET.get('insurance_status')

        person = participate.objects.get(MID=mid)
        person.Name = name
        person.MID = mid
        person.birthday = birthday
        person.insurance_status = insurance_status
        person.save()

    return redirect('list_persons')


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
    
def edit1(request):
    amember=""
    atravel=""
    aparticipate=""
    if 'account' in request.session:
        id = request.session['account']
        if request.method == "GET":
            amember = member.objects.get(Email=id)
            atravel = travel.objects.all()
            aparticipate = participate.objects.all()
            num=participate.objects.count()

        return render(request, 'edit.html', {'amember': amember,'atravel': atravel,'aparticipate':aparticipate,'num':num})
    else:
        return render(request, 'login.html')
def delete_edit(request):
    person = participate.objects.all()
    person.delete()
    travel_de = travel.objects.all()
    travel_de.delete()
    breakfast_de = breakfast.objects.all()
    breakfast_de.delete()
    dinner_de = Dinner.objects.all()
    dinner_de.delete()
    return redirect('edit')
>>>>>>> 7d6605a1793ed3a910c0552da53e317f250f990a
