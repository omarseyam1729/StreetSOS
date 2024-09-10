from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .models import UserProfile
from django.urls import reverse_lazy
from .forms import UserRegistrationForm  # Assuming you created this form

# User Profile Views
class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'users/profile_edit.html'
    fields = ['bio', 'profile_picture']
    success_url = reverse_lazy('profile-detail')

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

# Login View
class CustomLoginView(LoginView):
    template_name = 'users/login.html'

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(user=user)  # Create a UserProfile automatically
            login(request, user)  # Automatically log in the user after registration
            return redirect('profile-detail')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})
