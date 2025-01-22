# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page on success
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save()
        # Optional: Automatically log the user in immediately after register
        # login(self.request, user)
        return redirect(self.success_url)

def home_view(request):
    return render(request, 'home.html')

# We'll define the picks view in the picks app, but here's an example if it was in accounts:
# @login_required
# def picks_view(request):
#     return render(request, 'picks.html')


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')
