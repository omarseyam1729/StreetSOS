from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import Grievance, UserGrievance
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

class GrievanceListView(ListView):
    model = Grievance
    template_name = 'grievances/grievance_list.html'
    context_object_name = 'grievances'
    paginate_by = 10

    def get_queryset(self):
        return Grievance.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user_profile = self.request.user.userprofile
            saved_grievances = UserGrievance.objects.filter(user=user_profile).values_list('grievance_id', flat=True)
            context['saved_grievance_ids'] = list(saved_grievances)
        return context

class GrievanceCreateView(LoginRequiredMixin, CreateView):
    model = Grievance
    template_name = 'grievances/grievance_form.html'
    fields = ['title', 'description', 'urgency', 'latitude', 'longitude']
    success_url = reverse_lazy('grievance-list')

    def get_form(self):
        """
        Override the default form to add Bootstrap classes to the fields.
        """
        form = super().get_form()
        form.fields['title'].widget.attrs.update({'class': 'form-control'})
        form.fields['description'].widget.attrs.update({'class': 'form-control'})
        form.fields['urgency'].widget.attrs.update({'class': 'form-select'})  # Use form-select for dropdowns in Bootstrap
        form.fields['latitude'].widget.attrs.update({'class': 'form-control', 'readonly': 'readonly'})
        form.fields['longitude'].widget.attrs.update({'class': 'form-control', 'readonly': 'readonly'})
        return form

    def form_valid(self, form):
        # Set the user profile for the grievance before saving
        form.instance.user_profile = self.request.user.userprofile
        return super().form_valid(form)

def save_grievance(request, grievance_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Not authenticated'}, status=403)

    grievance = get_object_or_404(Grievance, id=grievance_id)
    user_profile = request.user.userprofile
    user_grievance, created = UserGrievance.objects.get_or_create(user=user_profile, grievance=grievance)

    if not created:
        return JsonResponse({'error': 'Already saved'}, status=400)

    return JsonResponse({'saved': True})

def delete_grievance(request, grievance_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Not authenticated'}, status=403)

    grievance = get_object_or_404(Grievance, id=grievance_id)
    user_profile = request.user.userprofile

    try:
        user_grievance = UserGrievance.objects.get(user=user_profile, grievance=grievance)
        user_grievance.delete()
        return JsonResponse({'deleted': True})
    except UserGrievance.DoesNotExist:
        return JsonResponse({'error': 'Grievance not saved by user'}, status=404)

class SavedGrievancesListView(LoginRequiredMixin, ListView):
    model = UserGrievance
    template_name = 'grievances/saved_grievances_list.html'
    context_object_name = 'saved_grievances'
    paginate_by = 10
    
    def get_queryset(self):
        return UserGrievance.objects.filter(user=self.request.user.userprofile).order_by('-saved_at')

class GrievanceDetailView(DetailView):
    model = Grievance
    template_name = 'grievances/grievance_detail.html'
    context_object_name = 'grievance'

class MyGrievancesListView(LoginRequiredMixin, ListView):
    model = Grievance
    template_name = 'grievances/my_grievances_list.html'  # Update with the actual template name
    context_object_name = 'grievances'
    paginate_by = 10

    def get_queryset(self):
        return Grievance.objects.filter(user_profile=self.request.user.userprofile).order_by('-created_at')
