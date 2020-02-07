from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from meeting.utils import get_unique_slug
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse


# Create your models here.

class Place_Of_Residence(models.Model):
    address = models.CharField(max_length=255)
    REGION = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    region = models.CharField(max_length=12, choices=REGION, default='1')

    def __str__(self):
        return self.address


class Appointment(models.Model):
    CHILDREN_NUMBER_CHOICES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),

    )
    MARITAL_STATUS = (
        ('single', 'single'),
        ('married', 'married'),
        ('divorced', 'divorced'),
        ('cohabitation', 'cohabitation'),
    )
    STATUS_CHOICES = (
        ('completed', 'completed'),
        ('pending', 'pending'),
        ('important', 'important'),
        ('follow up', 'follow up'),
    )
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=14, blank=True, unique=True)
    first_Name = models.CharField(max_length=255)
    last_Name = models.CharField(max_length=255)
    NIC = models.CharField(max_length=255)
    telephone = PhoneNumberField(blank=True)
    address = models.ForeignKey(Place_Of_Residence, on_delete=models.CASCADE)
    children = models.CharField(max_length=12, choices=CHILDREN_NUMBER_CHOICES, default='0')
    marital_Status = models.CharField(max_length=14, choices=MARITAL_STATUS, default='single')
    reasons = models.TextField()
    status = models.CharField(max_length=14, choices=STATUS_CHOICES, default='pending')
    published = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_Name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'NIC', 'slug')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('meeting-list', args=[str(self.slug)])
