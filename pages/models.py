from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Configuration(models.Model):
    location = models.CharField(max_length=500)
    main_phone_number = models.CharField(max_length=13)
    office_phone_number = models.CharField(max_length=13)
    email_address = models.EmailField()
    about = models.TextField()

    @classmethod
    def object(cls):
        return cls.objects.first()
    
    def save(self, *args, **kwargs):
        self.pk = 1
        self.id = 1
        super().save(*args, **kwargs)

class ExecutiveRole(models.Model):
    name = models.CharField(max_length=100)
    core = models.BooleanField(default=True)
    class Meta:
        ordering = ("core", 'name')
    
    def __str__(self) -> str:
        return self.name

class Executive(models.Model):
    executive_role = models.ForeignKey(ExecutiveRole, related_name="executives", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=150)
    about = models.TextField()
    picture = models.ImageField(upload_to='executives/images/%Y/')
    is_active = models.BooleanField(True)
    date_started = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("-is_active", "executive_role", "date_created")
    
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return ''


class Event(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to="events/%Y/%m/")
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.CharField(max_length=500)
    is_upcoming = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date", "date_created", "name")
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self) -> str:
        return ''
