from django.db import models

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Note: In a production environment, use a hashed password field
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    # Add more fields as needed, such as address, education, occupation, etc.

    # You might want to add additional fields for verification purposes (e.g., is_verified, verification_code, etc.)

    def __str__(self):
        return self.full_name
