from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Company
class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # When user is deleted, all records will be deleted too
    name = models.CharField(max_length=30)  # Only required field in the model to save the company to allow research later
    address = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    job_title = models.CharField(max_length=30, blank=True, null=True)  # E.g., frontend developer
    work_mode = models.CharField(
        max_length=6, 
        choices=[
            ('onsite', 'On-Site'),
            ('remote', 'Remote'),
            ('hybrid', 'Hybrid')
        ], 
        blank=True, null=True)
    notes = models.TextField(blank=True, null=True)  # For any additional information. If there are any repetitive info in multi records, I may add them as other fields later.
    culture_rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)
    mission_rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)
    support_rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)
    opportunity_rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)

    def __str__(self):
        return self.name
