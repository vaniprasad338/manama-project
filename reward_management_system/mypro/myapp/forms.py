from django import forms


class Customer_form(forms.Form):
    customer_id = forms.CharField(max_length=30)
    amount = forms.IntegerField()


class search_form(forms.Form):
    cid = forms.CharField(max_length=30)


class login_form(forms.Form):
    customer_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


class scoin_form(forms.Form):
    customer_id = forms.CharField(max_length=30)


class cdetails_form(forms.Form):
    customer_name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=100)
    mobile_number = forms.CharField(max_length=30)
    email_id = forms.CharField(max_length=30)
    service_charge = forms.CharField(max_length=30)
    grand_total = forms.CharField(max_length=30)
    amount = forms.CharField(max_length=30)
    discount = forms.CharField(max_length=30)


class offer_purchase(forms.Form):
    offer_id = forms.CharField(max_length=20)


class purchase_form(forms.Form):
    count = forms.CharField(max_length=20)
