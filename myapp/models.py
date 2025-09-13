from tkinter import CASCADE
from django.db import models

# Contact model
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    des = models.TextField(max_length=100)

    def __str__(self):
        return self.name

# Login model
class login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

# Company model
class company(models.Model):
    com_id = models.CharField(max_length=10, unique=True)
    cname = models.CharField(max_length=40)

    def __str__(self):
        return self.cname

# Employee model
COM_INFO = [
    ('01', 'SAF'),
    ('02', 'FFA'),
    ('03', 'SSA'),
]

class employee_info(models.Model):
    em_Id = models.CharField(max_length=10)
    em_Name = models.CharField(max_length=40)
    em_Mobile = models.CharField(max_length=14)
    em_Salary = models.CharField(max_length=10)
    em_Email = models.EmailField(max_length=40)
    em_Birth_Date = models.DateTimeField()
    em_Join_Date = models.DateTimeField()
    em_Desin = models.CharField(max_length=20)
    em_Dept = models.CharField(max_length=20)
    com_Id = models.CharField(max_length=2, choices=COM_INFO, default='01')

    def __str__(self):
        return f"{self.em_Name} ({self.get_com_Id_display()})"

# Hotel model
class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Budget(models.Model):
    b_id =models.CharField(max_length=20)
    subcode=models.CharField(max_length=20)
    amount =models.IntegerField()
    com_id = models.ForeignKey( 'Company',  on_delete=models.CASCADE
)

    
    def __str__(self):
        return f"{self.subcode} ({ self.amount})"