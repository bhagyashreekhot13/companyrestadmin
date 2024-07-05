from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model): # company account
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    # def __str__(self):
    #     return self.name

# class UserProfile(models.Model):
#     username = models.OneToOneField(User, on_delete=models.CASCADE)
#     userfirstName = models.OneToOneField(User, on_delete=models.CASCADE)
#     # userlastName = models.OneToOneField(User, on_delete=models.CASCADE)
#     email = models.EmailField()
#
#     account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='users')

    # def __str__(self):
    #     return self.user.username

class Organization(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name

class Invoice(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    payment_status = models.CharField(max_length=255)
    # def __str__(self):
    #     return f"Invoice {self.id} - {self.amount}"

class Role(models.Model):
    rolename = models.CharField(max_length=255)
    roleDescription = models.CharField(max_length=255)

class UserAccount(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    accountId = models.ForeignKey(Account, on_delete=models.CASCADE)
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE)
