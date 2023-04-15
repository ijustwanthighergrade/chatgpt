from django.db import models
from django.utils import timezone

from django.shortcuts import render, redirect

# Create your models here.

class sign_in(models.Model):
    id = models.CharField(primary_key=True,default=0)
    account=models.CharField('帳號',max_length=20,null=False)
    password=models.CharField('密碼',max_length=20,null=False)

class member(models.Model):
    id = models.AutoField(primary_key=True,default=0)
    sign_in_type=models.CharField('類別',max_length=20,null=False)
    line_account=models.CharField('line帳號',max_length=20,null=True)
    fb_account=models.CharField('fb帳號',max_length=20,null=True)
    name=models.CharField('姓名',max_length=20,null=False,primary_key=True)
    phone=models.CharField('電話',max_length=20,null=False)
    Email=models.CharField('信箱',max_length=40,null=True)
    createdate=models.DateTimeField('創立日期',max_length=30,default=timezone.now)




class travel(models.Model):
    id = models.AutoField(primary_key=True,default=0)  # 添加自增主键字段
    #booking_number = models.ForeignKey(number,on_delete=models.CASCADE)  # 把 id 字段設置為可空
    total_number = models.IntegerField('人數', null=True,blank=True)
    travel_date=models.DateField('旅程時間',max_length=20,null=False,default=timezone.now())
    food_id=models.CharField('飲食訂單編號',max_length=10,null=True,default=000000)
    price=models.IntegerField('總價',default=15000,null=True) #每筆訂單的價格都是一樣的 餐點部分是自費需要額外列出
   

@classmethod
def create_travel(cls, total_number):
        travel = cls(total_number=total_number)
        travel.save()
        return travel
        

    
class breakfast(models.Model):
    breakfast_id=models.CharField('早餐訂單編號',max_length=10,null=False,primary_key=True,default=1)
    booking_number = models.ForeignKey(travel,on_delete=models.CASCADE,null=True) 
    breakfast_items=models.CharField('早餐品項',max_length=10,null=False)
    quality=models.IntegerField("數量",null=False)
    price=models.IntegerField("售價",null=False)
    def __str__(self):
        return self.breakfast_id

class Dinner(models.Model):
    dinner_id=models.CharField('晚餐訂單編號',max_length=20,null=False,primary_key=True,default=1)
    booking_number = models.ForeignKey(travel,on_delete=models.CASCADE,null=True) 
    dinner_items=models.CharField('晚餐品項',max_length=10,null=False)
    quality=models.IntegerField("數量",null=False)
    price=models.IntegerField("售價",null=False)
    def __str__(self):
        return self.dinner_id
    
class breakfast_shop(models.Model):
    breakfast_items=models.CharField('早餐品項',max_length=10,null=False,primary_key=True)
    breakfast_name=models.CharField('早餐名稱',max_length=10,null=False)
    sort=[
        ('小吃',"小吃"),
        ('麵飯',"麵飯"),
        ('湯',"湯"),
    ]
    breakfast_choices=models.CharField("類別",max_length=5,choices=sort,default="",null=False)
    breakfast_price=models.CharField('早餐價格',max_length=10,null=False)
    status=[
        ('停止銷售','停止銷售'),
        ('銷售中','銷售中'),
    ]
    breakfast_status=models.CharField('餐點狀態',max_length=4,default="",choices=status,null=False)
    def __str__(self):
        return self.breakfast_items

class dinner_shop(models.Model):
    dinner_items=models.CharField('晚餐品項',max_length=10,null=False,primary_key=True)
    dinner_name=models.CharField('晚餐名稱',max_length=10,null=False)
    size=[
        ('大',"大"),
        ('小',"小")
    ]
    dinner_size=models.CharField('尺寸',max_length=4,default="",choices=size,null=False)
    sort=[
        ('小吃',"小吃"),
        ('麵飯',"麵飯"),
        ('熱炒',"熱炒"),
    ]
    dinner_type=models.CharField('類別',max_length=5,default="",choices=sort,null=False)
    dinner_price=models.CharField('晚餐價格',max_length=10,null=False)
    status=[
        ('停止銷售','停止銷售'),
        ('銷售中','銷售中'),
    ]
    dinner_status=models.CharField('餐點狀態',max_length=4,default="",choices=status,null=False)
    

class participate(models.Model):
    booking_number = models.ForeignKey(travel,on_delete=models.CASCADE,null=True) 
    Name=models.CharField('參加人姓名',max_length=10,null=False)
    total_number=models.CharField('參加總人數',max_length=5,null=False)
    MID=models.CharField('身分證字號',max_length=10,null=False)
    birthday=models.DateField('出生年月日',max_length=20,null=False)
    status=[
        ('未投保',"未投保"),
        ('已投保',"已投保")
    ]
    insurance_status=models.CharField('保險狀態',max_length=5,default="",choices=status,null=False)


    def __str__(self):
        return self.id



from .models import participate
from .forms import ParticipateForm

#問趙子嘉 forms.py
def submit_form(request):
    if request.method == 'POST':
        form = ParticipateForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            name = form.cleaned_data['Name']
            mid = form.cleaned_data['MID']
            birthday = form.cleaned_data['birthday']
            insurance_status = form.cleaned_data['insurance_status']
            person = participate(id=id, Name=name, MID=mid, birthday=birthday, insurance_status=insurance_status)
            person.save()
            print(f"Successfully saved {id}, {name}, {mid}, {birthday}, {insurance_status} to database")
            return redirect('success')  # 重定向到成功頁面
    else:
        form = ParticipateForm()
    return render(request, 'part_d.html', {'form': form})

#把早餐、晚餐放在資料庫
class Order(models.Model):
    current_order_id = 1
    order_id = models.IntegerField()
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_quantity = models.IntegerField()
    total_price = models.IntegerField()
    order_time = models.DateTimeField()

#問趙子嘉 forms.py
def participate_form(request):
    if request.method == 'POST':
        num_people = request.POST.get('num_people')
        if num_people:
            try:
                num_people = int(num_people)
            except ValueError:
                return HttpResponseBadRequest("Invalid num_people parameter")

            # 创建旅行预订并保存到数据库中
            travel_obj = travel.objects.create(total_number=num_people)

            return redirect('part_d', id=travel_obj.id)
    else:
        return render(request, 'book_c.html')

