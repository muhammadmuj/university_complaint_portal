from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

# from django.db import models
# from django.contrib.auth.models import User

# class Complaint(models.Model):
#     USER_TYPE_CHOICES = (
#         ('teacher', 'Teacher'),
#         ('student', 'Student'),
#     )

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
#     complaint_text = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} ({self.user_type}) - {self.timestamp}"


