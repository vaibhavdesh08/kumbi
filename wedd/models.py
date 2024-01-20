# from django.db import models

# class kumbi(models.Model):
#     gender_choices = (
#         ('male', 'Male'),
#         ('female', 'Female'),
#         ('other', 'Other'),
#     )

#     full_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)  # Note: In a production environment, use a hashed password field
#     confirmPassword = models.CharField(max_length=100)
#     dob = models.DateField()
#     gender = models.CharField(choices=gender_choices,max_length=120)
#     # Add more fields as needed, such as address, education, occupation, etc.

#     # You might want to add additional fields for verification purposes (e.g., is_verified, verification_code, etc.)

#     def __str__(self):
#         return self.

# models.py

from django.db import models

class MatrimonialProfile(models.Model):
    # Section 1: Profile Pics
    profile_pics = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # Section 2: Basic Details
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    height = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    birth_time = models.TimeField()
    birth_place = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=20, choices=[('single', 'Single'), ('married', 'Married')])
    caste = models.CharField(max_length=50, default='Wandekar Kunbi')
    country_living = models.CharField(max_length=50)
    state_living = models.CharField(max_length=50)
    city_living = models.CharField(max_length=50)
    permanent_address = models.TextField()

    # Section 3: About Me
    bio = models.TextField()
    profile_created_by = models.CharField(max_length=50)
    languages_spoken = models.CharField(max_length=100)
    disability = models.BooleanField(default=False)

    # Section 4: Education
    about_education = models.TextField()
    highest_education = models.CharField(max_length=100)
    pg_degree = models.CharField(max_length=100)
    pg_college = models.CharField(max_length=100)
    ug_degree = models.CharField(max_length=100)
    ug_college = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)

    # Section 5: Career
    about_career = models.TextField()
    employed_in = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    organization_name = models.CharField(max_length=100)

    # Section 6: Family
    about_family = models.TextField()
    father_occupation = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    brothers = models.PositiveIntegerField()
    sisters = models.PositiveIntegerField()
    married_sisters = models.PositiveIntegerField()
    family_income = models.PositiveIntegerField()
    living_with_parents = models.BooleanField(default=False)
    family_based_city = models.CharField(max_length=50)
    maternal_uncles_name = models.CharField(max_length=100)
    

    # Section 7: Contact Details
    email_id = models.EmailField()
    phone_no = models.CharField(max_length=15)

    # Section 8: Lifestyle
    lifestyle = models.TextField()
    drinking_habits = models.BooleanField(default=False)
    smoking_habits = models.BooleanField(default=False)

    # section 9 : Document upload
    document = models.FileField(upload_to='uploads/', null=True, blank=True)


    def __str__(self):
        return self.name


    
