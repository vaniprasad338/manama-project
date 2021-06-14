from django.db import models


# Create your models here.

class Customer_details(models.Model):
    customer_id = models.CharField(max_length=30, primary_key=True)
    customer_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    mobile_number = models.IntegerField()
    email_id = models.CharField(max_length=30)
    Joined_date = models.DateField()
    grand_total = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.customer_name + "   " + str(self.mobile_number)


class Login(models.Model):
    # uname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    customer_id = models.ForeignKey(Customer_details, on_delete=models.CASCADE, blank=True, null=True)


class Customers(models.Model):
    customer_id = models.ForeignKey(Customer_details, on_delete=models.CASCADE, blank=True, null=True)
    edate = models.DateField()
    amount = models.IntegerField()
    super_coin_detail = models.IntegerField()

    def __str__(self):
        return str(self.id) + "  " + str(self.customer_id) + "   " + str(self.edate)


class Supercoin(models.Model):
    cname = models.CharField(max_length=30)
    cid = models.ForeignKey(Customers, on_delete=models.CASCADE)
    scoin = models.IntegerField()
    edate = models.DateField()

    def __str__(self):
        return self.cname + "   " + str(self.cid)


class Product_details(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    created_date = models.DateField()
    expiry_date = models.DateField()
    brand_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='products')

    def __str__(self):
        return str(self.id) + "   " + self.name + "   " + str(self.price) + "   " + str(self.photo)


class Product(models.Model):
    pid = models.CharField(max_length=30, primary_key=True)
    pname = models.CharField(max_length=30)
    price = models.IntegerField()
    edate = models.DateField()

    def __str__(self):
        return self.pname + "   " + self.pid


class Offerproducts(models.Model):
    pid = models.ForeignKey(Product_details, on_delete=models.CASCADE)
    discount = models.IntegerField()
    scoin = models.IntegerField()
    edate = models.DateField()

    def __str__(self):
        return str(self.pid)


class Offer(models.Model):
    offers = models.CharField(max_length=100)
    offerid = models.CharField(max_length=30, primary_key=True)
    scoin = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    price = models.IntegerField()
    edate = models.DateField()
    photo = models.ImageField(upload_to='offers')

    def __str__(self):
        return self.offers + "   " + self.offerid


class Purchase(models.Model):
    cid = models.ForeignKey(Customers, on_delete=models.CASCADE)
    cname = models.CharField(max_length=30)
    scoin = models.IntegerField()
    pid = models.ForeignKey(Offerproducts, on_delete=models.CASCADE)
    pname = models.CharField(max_length=30)
    discount = models.IntegerField()
    offerid = models.CharField(max_length=30)
    offers = models.ForeignKey(Offer, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.cname + "   " + str(self.cid)


class available_product(models.Model):
    customer_id = models.ForeignKey(Customer_details, on_delete=models.CASCADE)
    offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)
    Offerproduct_id = models.ForeignKey(Offerproducts, on_delete=models.CASCADE, null=True, blank=True)
    discounted_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.customer_id


class purchased_product(models.Model):
    customer_id = models.ForeignKey(Customer_details, on_delete=models.CASCADE)
    offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)
    Offerproduct_id = models.ForeignKey(Offerproducts, on_delete=models.CASCADE, null=True, blank=True)
    discounted_price = models.IntegerField(null=True, blank=True)


class Cart(models.Model):
    Customer_details = models.ForeignKey(Customer_details, on_delete=models.CASCADE)
    Product_details = models.ForeignKey(Product_details, on_delete=models.CASCADE)


class Cart_product(models.Model):
    customer_id = models.ForeignKey(Customer_details, on_delete=models.CASCADE)
    offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)
    Offerproduct_id = models.ForeignKey(Offerproducts, on_delete=models.CASCADE, null=True, blank=True)
    discounted_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.customer_id)
