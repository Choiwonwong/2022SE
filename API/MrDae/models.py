from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class AccountManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
    
        user = self.model(
            email=email,)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        
        superuser.save(using=self._db)
        return superuser

class CustomerRank(models.Model):
    name = models.CharField(max_length=10)
    discount = models.IntegerField()
    condition = models.IntegerField()

class CustomerAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=256, null=True)
    phone_number = models.CharField(max_length=16, null=True)
    rank = models.ForeignKey(CustomerRank, db_column="rank", default = 0, on_delete=models.PROTECT)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'

class OrderState(models.Model):
    state_id = models.IntegerField(null=False)
    name = models.CharField(max_length=50)

class Style(models.Model):
    name = models.CharField(max_length=50)
    dish = models.CharField(max_length=50, null=False)
    napkin = models.CharField(max_length=50, null=False)
    cup = models.CharField(max_length=50, null=False)
    tray = models.CharField(max_length=50, null=False)

class Menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField() # ????????? ??????

class Dinner(models.Model): # ????????? ?????? ?????? ??????.
    dinner_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    style = models.ForeignKey(Style, on_delete=models.CASCADE, db_column="style", null = True)

class Order(models.Model): # ?????? id 
    customerid = models.ForeignKey(CustomerAccount, related_name='order', on_delete=models.CASCADE, db_column="customer_id") # ?????? id
    customer_orderid = models.IntegerField(default = 1, db_column="customer_order_id")
    state = models.ForeignKey(OrderState, db_column="state", on_delete=models.PROTECT, default=1)
    date = models.DateTimeField(auto_now_add = True)
    price = models.IntegerField() # ????????? ?????? ??????
    discount = models.IntegerField()

    # ?????? ??????
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16)
    address = models.CharField(max_length=256)
    class Meta:
        ordering = ('-date',)

class OrderDetail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_detail", db_column="order_id")
    dinner = models.ForeignKey(Dinner, default=1, on_delete=models.CASCADE, db_column="dinner") # ????????? ?????? ???????????? Null
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT, db_column="menu") # ?????? or ????????? ??????id
    count = models.IntegerField(null = False) # ????????? ??????

class Inventory(models.Model):
    name = models.CharField(max_length=50, null=False)
    count = models.IntegerField(null=False)
    class Meta:
        ordering = ('count',)

class Staff(models.Model):
    account = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
    authority = models.BooleanField(default=False) # ?????? ???????????? objects.filter ????????? ????????? ?????? ??????? -> ????????? ???????????? ????????? ???????????????.
    # ???????????? ??????????????? ???????????? ???????????? ?????? ????????? ?????????. -> ??????????????? ?????? ??????

