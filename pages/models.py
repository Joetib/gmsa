from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.contenttypes.fields  import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
User = get_user_model()
# Create your models here.

class Configuration(models.Model):
    location = models.CharField(max_length=500)
    main_phone_number = models.CharField(max_length=13)
    office_phone_number = models.CharField(max_length=13)
    email_address = models.EmailField()
    about = models.TextField()

    # social links
    whatsapp_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)
    
    @classmethod
    def object(cls):
        return cls.objects.first()
    
    def save(self, *args, **kwargs):
        self.pk = 1
        self.id = 1
        super().save(*args, **kwargs)
        
class Image(models.Model):
    image = models.ImageField(upload_to="gallery/images/%Y/%m/")
    description = models.TextField(blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date_created",)
    
    @classmethod
    def for_model(cls,*,image, description, content_object: models.Model):
        _image = cls(image=image, description=description, content_object=content_object)
        _image.save()
        return _image

        

    
class ExecutiveRole(models.Model):
    name = models.CharField(max_length=100)
    core = models.BooleanField(default=True)
    duty = models.TextField()
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
        return reverse('executive-detail', kwargs={'pk': self.pk})


class Event(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to="events/%Y/%m/")
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.CharField(max_length=500)
    images = GenericRelation(Image, related_query_name="event")
    is_upcoming = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date", "date_created", "name")
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self) -> str:
        return reverse("event-detail",kwargs={"pk": self.pk} )


class Programme(models.Model):
    title = models.CharField(max_length=200)
    
    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("programme-detail", kwargs={"pk": self.pk})
    
    def get_courses(self):
        course_for_level = [
            {
            "level": "Level 100",
            "courses": self.get_level_100_courses()
            },
            {
            "level": "Level 200",
            "courses": self.get_level_200_courses()
            },
            {
            "level": "Level 300",
            "courses": self.get_level_300_courses()
            },
            {
            "level": "Level 400",
            "courses": self.get_level_400_courses()
            },
        ]
        courses = self.get_level_500_courses()
        if courses.exists:
            course_for_level.append({"level": "Level 500", "courses": courses})
        courses = self.get_level_600_courses()
        if courses.exists:
            course_for_level.append({"level": "Level 600", "courses": courses})
        return course_for_level
    
    def get_level_100_courses(self):
        return self.courses.filter(year=1)
    
    def get_level_200_courses(self):
        return self.courses.filter(year=2)
        
    def get_level_300_courses(self):
        return self.courses.filter(year=3)
        
    def get_level_400_courses(self):
        return self.courses.filter(year=4)
        
    def get_level_500_courses(self):
        return self.courses.filter(year=5)
        
    def get_level_600_courses(self):
        return self.courses.filter(year=6)

class Course(models.Model):
    YEAR_CHOICES = (
        (1, "Level 100"),
        (2, "Level 200"),
        (3, "Level 300"),
        (4, "Level 400"),
        (5, "Level 500"),
        (6, "Level 600"),
    )
    programme = models.ForeignKey(Programme, related_name="courses", on_delete=models.CASCADE)
    year = models.PositiveIntegerField(choices=YEAR_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ("year", "title")
    
    def __str__(self):
        return self.title

class Book(models.Model):
    course = models.ForeignKey(Course, related_name="books", on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    book = models.FileField(upload_to="books/%Y/")

    class Meta:
        ordering = ("course", "title")

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name + self.message[:20]
    

class Madarasah(models.Model):
    pass