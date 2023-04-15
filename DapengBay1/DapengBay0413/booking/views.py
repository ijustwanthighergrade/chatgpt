from django.shortcuts import render,redirect
# Create your views here.
import datetime
from .models import travel,Order
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseBadRequest
from email.quoprimime import unquote
import json
from multiprocessing import context
from django.http import JsonResponse
from .models import breakfast_shop, dinner_shop
from django.utils import timezone
from django.db.models import Max






# def save_appointment(request):
#     if request.method == 'POST':
#         appointment = travel()
#         appointment.travel_date = request.POST['meeting-time']
#         appointment.save()
#         return render(request,'reserve.html',locals())
#     else:
#         return render(request,'news.html',locals())


# def appointment_success(request):
#     return render(request, 'reserve.html')

import random

from django.views.decorators.http import require_http_methods



def save_travel(request):
    if request.method == 'POST':
        date = request.POST.get('meeting-time')
            # Generate a random 3-digit booking number
        
        if travel.objects.filter(travel_date=date).exists():
            error_message = "The travel date you selected already exists. Please choose another date."
            return render(request, 'index.html', {'error': error_message})
          
            # Create a new Travel object and save it to the database
        # travel.objects.create(travel_date=date, booking_number=number)
        else:
             test=travel(travel_date=date)
             test.save()
             return redirect('book_c')
             
    
    else:
        return render(request,'index.html')

def reserve(request):
    return render(request,'reserve.html',locals())

def news(request):
    return render(request,'news.html',locals())

def index(request):
    return render(request,'index.html',locals())



@require_http_methods(['GET', 'POST'])
def checkout(request):
    if request.method == 'POST':
        # Handle payment form submission
        payment_method = request.POST.get('payment_method')
        # ...
        # Code to process payment goes here
        # ...
        return redirect('payment_success')
    else:
        # Display checkout page with reservation details
        reservation = {'datetime': '2023-04-07 19:30', 'num_people': 4, 'special_requests': 'No onions', 'notes': 'Table for 4'}
        return render(request, 'checkout.html', {'reservation': reservation})

# Create your views here.
def book_c(request):
    if request.method == 'POST':
        # 從表單數據中獲取 num_people
        num_people = request.POST.get('num_people', 1)
        # 檢查 num_people 是否為整數
        try:
            num_people = int(num_people)
        except ValueError:
            return HttpResponseBadRequest("Invalid num_people parameter")

        # 從表單數據中獲取 travel_id
       
        id = travel.objects.aggregate(Max('id'))['id__max']
        if id is None:
            id = 1
        else:
            id = id 

        # 更新旅遊預訂的人數
        travel.objects.filter(id=id).update(total_number=num_people)

        # 重定向到另一個頁面，例如成功提交的頁面
        return redirect('/part_d')

    # 如果是 GET 請求，渲染表單頁面
    return render(request, 'book_c.html')

# def start(request):
#     return render(request, 'start.html')


def part_d(request):
    num_people = request.GET.get('num-people', 1)
    try:
        num_people = int(num_people)
        if num_people <= 0:
            raise ValueError
    except ValueError:
        # 处理无效参数的情况
        return HttpResponseBadRequest("Invalid num-people parameter")

    person_info_array = [{'name': '', 'gender': '', 'id_number': ''} for i in range(num_people)]
    return render(request, 'part_d.html', {'num_people': num_people, 'person_info_array': person_info_array})


from booking.forms import ParticipateForm


def submit_form(request):
    if request.method == 'POST':
        form = ParticipateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/break/')  # 重定向到成功頁面
    else:
        form = ParticipateForm()
    return render(request, 'part_d.html', {'form': form})


from .models import travel


from django.shortcuts import render, redirect
from .models import travel


def participate_form(request):
    if request.method == 'POST':
        # 從表單數據中獲取 num_people
        num_people = request.POST.get('num_people', 1)

        # 檢查 num_people 是否為整數
        try:
            num_people = int(num_people)
        except ValueError:
            return HttpResponseBadRequest("Invalid num_people parameter")

        # 創建一個旅遊預訂
        new_travel = travel.objects.create(total_number=num_people)

        # 重定向到另一個頁面，例如成功提交的頁面
        return redirect('submit_success')
    else:
        return render(request, 'submit_form.html', {'total_number': total_number})






    

def show_breakfast(request):
    menu_items = breakfast_shop.objects.order_by('breakfast_items')
    return render(request, 'breakfast.html', {'menu_items': menu_items})

def show_break(request):
    menu_items = breakfast_shop.objects.order_by('breakfast_items')
    return render(request, 'break.html', {'menu_items': menu_items})


def show_dinner(request):
    menu_items = dinner_shop.objects.order_by('dinner_items')
    return render(request, 'dinner.html', {'menu_items': menu_items})

def show_dinner_snacks(request):
    menu_items = dinner_shop.objects.filter(dinner_type='小吃').order_by('dinner_items')
    return render(request, 'snacks.html', {'menu_items': menu_items})

def show_dinner_noodles(request):
    menu_items = dinner_shop.objects.filter(dinner_type='麵飯').order_by('dinner_items')
    return render(request, 'noodles.html', {'menu_items': menu_items})

def show_dinner_hotdishes(request):
    menu_items = dinner_shop.objects.filter(dinner_type='熱炒').order_by('dinner_items')
    return render(request, 'hotdishes.html', {'menu_items': menu_items})

def submit_order(request):
    if request.method == 'POST':
        order_items = request.POST.get('order_items')
        order_items = json.loads(order_items)
        total_price = request.POST.get('total_price')
        print('order_items:', order_items)
        print('total_price:', total_price)

        # 產生一組編號 order_id
        max_order_id = Order.objects.aggregate(Max('order_id'))['order_id__max']
        if max_order_id is None:
            order_id = 1
        else:
            order_id = max_order_id + 1

        # 轉換成 Order 的對象
        order_objects = []
        for item_name, item_data in order_items.items():
            item_price = item_data['item_price']
            item_quantity = item_data['item_quantity']
            total_price_item = float(item_price) * int(item_quantity)
            order_objects.append(Order(
                order_id=order_id,
                item_name=item_name,
                item_price=item_price,
                item_quantity=item_quantity,
                total_price=total_price_item,
                order_time=timezone.now()
            ))

        # 批量創建 Order 對象
        Order.objects.bulk_create(order_objects)

        # 返回訂單編號和儲存狀態
        return JsonResponse({'order_id': order_id, 'success': True})

    return redirect('dinner')

def submit_order2(request):
    if request.method == 'POST':
        order_items = request.POST.get('order_items')
        order_items = json.loads(order_items)
        total_price = request.POST.get('total_price')
        print('order_items:', order_items)
        print('total_price:', total_price)

        # 產生一組編號 order_id
        max_order_id = Order.objects.aggregate(Max('order_id'))['order_id__max']
     
        if max_order_id is None:
            order_id = 1
        else:
            order_id = max_order_id

        # 轉換成 Order 的對象
        order_objects = []
        for item_name, item_data in order_items.items():
            item_price = item_data['item_price']
            item_quantity = item_data['item_quantity']
            total_price_item = float(item_price) * int(item_quantity)
            order_objects.append(Order(
                order_id=order_id,
                item_name=item_name,
                item_price=item_price,
                item_quantity=item_quantity,
                total_price=total_price_item,
                order_time=timezone.now()
            ))

        # 批量創建 Order 對象
        Order.objects.bulk_create(order_objects)
        travel.objects.filter(id=id).update(food_id=max_order_id)

        # 返回訂單編號和儲存狀態
        return JsonResponse({'order_id': order_id, 'success': True})

    return redirect('dinner')
