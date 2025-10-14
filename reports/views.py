from django.shortcuts import render, redirect, get_object_or_404
from .models import Report
from .forms import ReportForm, RegisterForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import login

def home(request):
    latest = Report.objects.all()[:6]
    return render(request, 'home.html', {'latest': latest})

def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)

    # Admin can mark report as reviewed
    if request.method == "POST" and request.user.is_staff:
        report.status = 'reviewed'
        report.save()
        messages.success(request, "Report marked as reviewed.")
        return redirect('report_detail', pk=report.pk)

    return render(request, 'report_detail.html', {'report': report})

@login_required
def report_create(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            report.save()
            messages.success(request, "Incident reported successfully.")
            return redirect('dashboard')
    else:
        form = ReportForm()
    return render(request, 'report_form.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
def dashboard(request):
    q = request.GET.get('q', '')
    reports = Report.objects.all()
    if q:
        reports = reports.filter(incident_description__icontains=q)
    return render(request, 'dashboard.html', {'reports': reports})
