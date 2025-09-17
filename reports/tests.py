from django.test import TestCase
from django.contrib.auth.models import User
from .models import Report

class ReportModelTest(TestCase):
    def test_create_report(self):
        r = Report.objects.create(title="Test", incident_description="desc")
        self.assertEqual(str(r), "Test (Other)" if r.get_crime_type_display()=="Other" else r.title)
