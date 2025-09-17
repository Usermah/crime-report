from django.db import models
from django.contrib.auth.models import User

CRIME_CHOICES = [
    ('theft', 'Theft'),
    ('assault', 'Assault'),
    ('robbery', 'Robbery'),
    ('rape', 'Rape'),
    ('fraud', 'Fraud'),
    ('other', 'Other'),
]

STATUS_CHOICES = [
    ('new', 'New'),
    ('investigating', 'Investigating'),
    ('closed', 'Closed'),
]

class Report(models.Model):
    title = models.CharField(max_length=200)
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    crime_type = models.CharField(max_length=50, choices=CRIME_CHOICES, default='other')
    state = models.CharField(max_length=100, blank=True)
    lga = models.CharField("Location / LGA", max_length=150, blank=True)
    location_description = models.TextField(blank=True)
    incident_description = models.TextField()
    security_agency = models.CharField(max_length=150, blank=True)
    progress_notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    image = models.ImageField(upload_to='reports/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.get_crime_type_display()})"
