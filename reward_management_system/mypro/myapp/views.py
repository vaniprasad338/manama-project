from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *
import datetime
from django.contrib.auth.decorators import login_required

date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)


# Create your views here.
# def error404(request):
# return render(request, '404.html')


def index(request):
    return render(request, 'index.html')


''''def login(request):
    return render(request, 'login.html')'''


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def contactus(request):
    return render(request, 'contact-us.html')


def productdetails(request):
    val = Product_details.objects.all()
    for i in val:
        print(i.photo)
    id = 100
    return render(request, 'REWARD.html', {'val': val, 'id1': id})


def shop(request):
    amount = 10000
    var = Customer_details.objects.all()
    for i in var:
        today = datetime.datetime.now()
        xdate = datetime.datetime(today.year + 1, today.month, today.day)
        print(xdate)
        custid = '1'
        if i.customer_id == custid:
            print('working')
            date_time = datetime.datetime.now().strftime("%m/%d/%Y-%H:%M:%S")
            print("date and time:", date_time)
            g = Customers(cid=date_time, customer_id=i, edate=xdate, amount=amount, super_coin_detail=int(amount / 250))
            g.save()
    return render(request, 'shop.html')


def login(request):
    available_product.objects.all().delete()
    coin = 0
    list1 = []
    discounted_price = ''
    listoffer = []
    loginvar = Customer_details.objects.all()
    if request.method == 'GET':
        varobj = Customers.objects.all()
        slist = []
        var = scoin_form(request.GET)
        if var.is_valid():
            id1 = var.cleaned_data['customer_name']
            print(id1)
            for i in varobj:
                if i.customer_id.customer_name == id1:
                    slist.append(i)
            else:
                return render(request, 'new.html', {'Customer': slist})
        return render(request, 'login.html')
    if request.method == 'POST':
        var = login_form(request.POST)
        if var.is_valid():
            id1 = var.cleaned_data['customer_name']
            # uname = var.cleaned_data['uname']
            password = var.cleaned_data['password']
            for variable in loginvar:
                if variable.customer_name == id1 and variable.password == password:
                    client = Customers.objects.all()
                    id1 = variable.customer_id
                    for i in client:
                        if i.edate > datetime.datetime.now().date():
                            if i.customer_id.customer_id == id1:
                                coin += int(i.super_coin_detail)
                        else:
                            i.delete()
                    server = Product.objects.all()
                    for k in server:
                        if k.edate > datetime.datetime.now().date():
                            if k.pid == id1:
                                k.delete()
                    ofvar = Offer.objects.all()
                    for offer in ofvar:
                        if offer.scoin <= coin:
                            discounted_price = offer.price - round(offer.price * (offer.discount / 100))
                            listoffer.append(offer)
                            print(variable.customer_id)
                            h = Customer_details.objects.get(customer_id=int(variable.customer_id))
                            av = available_product(customer_id=h, offer_id=offer,
                                                   discounted_price=discounted_price)
                            av.save()
                    var1 = Offerproducts.objects.all()
                    for j in var1:
                        if j.scoin <= coin:
                            discounted_price = j.pid.price - round((j.pid.price) * (j.discount / 100))
                            j.discounted_price = discounted_price
                            list1.append(j)
                            h = Customer_details.objects.get(customer_id=int(variable.customer_id))
                            av = available_product(customer_id=h, Offerproduct_id=j,
                                                   discounted_price=discounted_price)
                            av.save()
                    return render(request, 'REWARD.html',
                                  {'value': list1, 'price': discounted_price, 'id': id1, 'value1': listoffer})
            else:
                return render(request, 'login.html', {'msg': 'Password and login not matching'})
    return render(request, 'login.html')


def scoin(request):
    if request.method == 'POST':
        var = scoin_form(request.POST)
        if var.is_valid():
            id1 = var.cleaned_data['customer_id']
            print(id1)
    return render(request, 'new.html')


def cust(request):
    a = Customers.objects.all()
    if request.method == 'POST':
        var = Customer_form(request.POST)
        if var.is_valid():
            id1 = var.cleaned_data['customer_id']
            amount = var.cleaned_data['amount']
            var = Customer_details.objects.all()
            for i in var:
                today = datetime.datetime.now()
                xdate = datetime.datetime(today.year + 1, today.month, today.day)
                if i.customer_id == id1:
                    print('working')
                    date_time = datetime.datetime.now().strftime("%m/%d/%Y-%H:%M:%S")
                    print("date and time:", date_time)
                    g = Customers(customer_id=i, edate=xdate, amount=amount,
                                  super_coin_detail=int(amount / 250))
                    g.save()
            return render(request, 'index.html')
        else:
            return render(request, 'scoin.html', {'msg': 'error'})
    return render(request, 'scoin.html')


def bynow(request):
    a = Customer_details.objects.all()
    if request.method == 'POST':
        var = cdetails_form(request.POST)
        if var.is_valid():
            name = var.cleaned_data['customer_name']
            address = var.cleaned_data['address']
            mobile = var.cleaned_data['mobile_number']
            email = var.cleaned_data['email_id']
            total = var.cleaned_data['grand_total']
            amount = var.cleaned_data['amount']
            scharge = var.cleaned_data['service_charge']
            discount = var.cleaned_data['discount']
    return render(request, 'bynow.html')


def purchase(request, count=0):
    coin = 0
    clientcoin = 0
    var = available_product.objects.all()
    list = []
    for i in var:
        list.append(i)
    if len(list) == 0:
        return render(request, 'valid.html')
    if request.method == 'POST' and 'btnform1' in request.POST:
        var1 = purchase_form(request.POST)
        if var1.is_valid():
            count = var1.cleaned_data['count']
            count = int(count)
            k = list[count - 1]
            det = purchased_product.objects.filter(customer_id=k.customer_id)
            client = Customers.objects.filter(customer_id=k.customer_id)
            for i in client:
                clientcoin += int(i.super_coin_detail)
            for i in det:
                if i.offer_id != None:
                    coin += int(i.offer_id.scoin)
                else:
                    coin += int(i.Offerproduct_id.scoin)
            print(coin)
            print(clientcoin)
            if coin > clientcoin:
                return render(request, 'error.html', {'msg': 'No more super coins'})
            g = purchased_product(customer_id=k.customer_id, offer_id=k.offer_id, Offerproduct_id=k.Offerproduct_id,
                                  discounted_price=k.discounted_price)
            g.save()
            if len(var) >= int(count):
                return render(request, 'valid.html')
            return render(request, 'purchase.html', {'count': str(int(count) + 1), 'detail': list[count]})
    if request.method == 'POST' and 'btnform2' in request.POST:
        var1 = purchase_form(request.POST)
        if var1.is_valid():
            count = var1.cleaned_data['count']
            count = int(count)
            if len(var) == int(count):
                return render(request, 'valid.html')
            return render(request, 'purchase.html', {'count': str(int(count) + 1), 'detail': list[count]})
    return render(request, 'purchase.html', {'count': str(int(count) + 1), 'detail': list[count]})


def validate(request, cid=0,status=0):
    coin = 0
    scoin = 0
    client = Customers.objects.filter(customer_id__customer_id=cid)
    for i in client:
        coin += int(i.super_coin_detail)
    offer = Cart_product.objects.filter(customer_id=int(cid))
    for j in offer:
        if j.offer_id is not None:
            scoin += j.offer_id.scoin
        else:
            scoin += j.Offerproduct_id.scoin
    list1 = []
    list2 = []
    dp=0
    price =0
    gst =0
    total =0
    if status == 2:
        if scoin > coin:
            value = Cart_product.objects.filter(customer_id=int(cid))
            for i in value:
                if i.offer_id is None:
                    list1.append(i)
                    price += i.Offerproduct_id.pid.price
                else:
                    list2.append(i)
                    price += i.offer_id.price
                dp += i.discounted_price
            bal = scoin - coin
            bal *= 250
            gst = round(price*(12/100))
            print(gst)
            total = bal+gst+dp
        customer = Customer_details.objects.get(customer_id=int(cid))
        return render(request, 'validation.html', {'customer': customer,'discounted_price':dp,'price':price,'gst':gst,'total':total,'scoin':scoin})
    else:
        if scoin > coin:
            value = Cart_product.objects.filter(customer_id=int(cid))
            for i in value:
                if i.offer_id is None:
                    list1.append(i)
                else:
                    list2.append(i)
            bal = scoin - coin
            bal *= 250
            return render(request, 'cart.html',
                          {'msg': 'You not have sufficient super coin for place order. You can place the order by paying on COD the amount is ,', 'value': list2, 'value1': list1,
                           'id': cid,'bal':bal,'msg1':'Continue','msg2':'Click on Continue button'})
        else:
            customer = Customer_details.objects.get(customer_id=int(cid))
            value = Cart_product.objects.filter(customer_id=int(cid))
            for i in value:
                if i.offer_id is None:
                    list1.append(i)
                    price += i.Offerproduct_id.pid.price
                else:
                    list2.append(i)
                    price += i.offer_id.price
                dp += i.discounted_price
            gst = round(price * (12 / 100))
            print(gst)
            total = gst + dp
            return render(request, 'validation.html',
                      {'customer': customer, 'discounted_price': dp, 'price': price, 'gst': gst, 'total': total,'scoin':scoin})

def product_add_to_cart(request, cid=0, id=0, discounted_price=0):
    h = Customer_details.objects.get(customer_id=int(cid))
    p = Offerproducts.objects.get(id=int(id))
    val = Cart_product.objects.filter(customer_id=int(cid)).filter(Offerproduct_id=int(id))
    list1 = []
    list2 = []
    if len(val) != 0:
        value = Cart_product.objects.filter(customer_id=int(cid))
        for i in value:
            print(i.offer_id)
            print(i.Offerproduct_id)
            if i.offer_id is None:
                list1.append(i)
            else:
                list2.append(i)
        return render(request, 'cart.html',
                      {'msg': ' The product is already Added to cart', 'value': list2, 'value1': list1, 'id': cid})
    else:
        g = Cart_product(customer_id=h, Offerproduct_id=p, discounted_price=discounted_price)
        g.save()
        value = Cart_product.objects.filter(customer_id=int(cid))
        for i in value:
            print(i.offer_id)
            print(i.Offerproduct_id)
            if i.offer_id is None:
                list1.append(i)
            else:
                list2.append(i)
    return render(request, 'cart.html', {'value': list2, 'value1': list1, 'id': cid})


def offer_add_to_cart(request, cid=0, id=0, discount=0):
    h = Customer_details.objects.get(customer_id=int(cid))
    p = Offer.objects.get(offerid=int(id))
    val = Cart_product.objects.filter(customer_id=int(cid)).filter(offer_id=int(id))
    list1 = []
    list2 = []
    if len(val) != 0:
        value = Cart_product.objects.filter(customer_id=int(cid))
        for i in value:
            print(i.offer_id)
            print(i.Offerproduct_id)
            if i.Offerproduct_id is None:
                list2.append(i)
            else:
                list1.append(i)
        return render(request, 'cart.html',
                      {'msg': ' The product is already Added to cart', 'value': list2, 'value1': list1, 'id': cid})
    else:
        g = Cart_product(customer_id=h, offer_id=p, discounted_price=discount)
        g.save()
        value = Cart_product.objects.filter(customer_id=int(cid))
        for i in value:
            print(i.offer_id)
            print(i.Offerproduct_id)
            if i.Offerproduct_id is None:
                list2.append(i)
            else:
                list1.append(i)
    return render(request, 'cart.html', {'value': list2, 'value1': list1, 'id': cid})


def finish_purchase(request,coin=0,cid=0):
    amt = 0
    client = Customers.objects.filter(customer_id__customer_id=int(cid)).order_by('edate')
    value = Cart_product.objects.filter(customer_id=int(cid))
    for k in value:
        k.delete()
    for i in client:
        print(i.super_coin_detail)
        if i.super_coin_detail <= coin:
            coin -= i.super_coin_detail
            i.delete()
        else:
            g = Customers.objects.filter(customer_id=i.customer_id).order_by('edate').first()
            amt =g.super_coin_detail-coin
            print(amt)
            var = Customers(customer_id=g.customer_id,edate=g.edate,amount=g.amount,super_coin_detail=amt)
            g.delete()
            var.save()
            print(g.customer_id)
            '''edate = models.DateField()
            amount = models.IntegerField()
            super_coin_detail'''
            print(coin)
    return render(request, 'valid.html')
