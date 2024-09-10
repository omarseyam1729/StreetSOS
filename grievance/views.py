from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Grievance, UserGrievance
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect

class GrievanceListView(ListView):
    model = Grievance
    template_name = 'grievances/grievance_list.html'
    context_object_name = 'grievances'
    paginate_by = 10
    def get_queryset(self):
        return Grievance.objects.all().order_by('-created_at')

class GrievanceCreateView(LoginRequiredMixin, CreateView):
    model = Grievance
    template_name = 'grievances/grievance_form.html'
    fields = ['title', 'description', 'urgency', 'latitude', 'longitude']
    success_url = reverse_lazy('grievance-list')
    def form_valid(self, form):
        form.instance.user_profile = self.request.user.userprofile  # Set the user profile automatically
        return super().form_valid(form)

def save_grievance(request, grievance_id):
    grievance = get_object_or_404(Grievance, id=grievance_id)
    user_profile = request.user.userprofile
    user_grievance, created = UserGrievance.objects.get_or_create(user=user_profile, grievance=grievance)

    return redirect('grievance-list')
