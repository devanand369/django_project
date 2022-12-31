from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView
from django.urls import reverse, reverse_lazy

from classroom.forms import ContactForm
from classroom.models import Teacher

# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # success URL? URL NOT a template.html
    success_url = reverse_lazy('classroom:thank_you')

    # what to do with form?
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')

class TeacherListView(ListView):
    # model_list.html
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')

    context_object_name = "teacher_list"

class TeacherDetailView(DetailView):
    # RETURN ONLY ONE MODEL ENTRY PK
    # model_detail.html
    model = Teacher
    # PK --> {{teacher}}

class TeacherUpdateView(UpdateView):
    # SHARE model_form.html --> PK
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher')


