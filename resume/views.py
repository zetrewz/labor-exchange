from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, DeleteView, ListView

from resume.forms import ResumeCreateForm
from resume.models import Resume
from service.models import Application


class ResumeListView(View):
    template_name = 'resume/list.html'

    def get(self, request):
        try:
            resume = Resume.objects.get(user=request.user)
            context = {'resume': resume}
            return render(request, self.template_name, context)
        except Resume.DoesNotExist:
            return redirect('resume:create')


class ResumeDetailView(DetailView):
    template_name = 'resume/detail.html'
    model = Resume
    context_object_name = 'resume'


class ResumeCreateView(CreateView):
    template_name = 'resume/create.html'
    form_class = ResumeCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('resume:list')


class ResumeUpdateView(View):
    template_name = 'resume/update.html'

    def get(self, request, pk):
        resume = request.user.resume
        context = {'form': ResumeCreateForm(instance=resume)}

        return render(request, self.template_name, context)

    def post(self, request, pk):
        resume = request.user.resume
        form = ResumeCreateForm(request.POST, request.FILES, instance=resume)

        if form.is_valid():
            form.save()
            return redirect('resume:list')
        context = {'form': form}

        return render(request, self.template_name, context)


class ResumeDeleteView(DeleteView):
    template_name = 'resume/delete.html'
    model = Resume

    def get_success_url(self):
        return reverse_lazy('resume:create')


class ResumeResponsesView(View):
    template_name = 'resume/responses.html'

    def get(self, request):
        responses = Application.objects.filter(
            resume__user=request.user
        ).select_related('vacancy')
        context = {'responses': responses}

        return render(request, self.template_name, context)


class FavoritesResume(ListView):
    template_name = 'resume/favorites_resume.html'
    model = Resume
    context_object_name = 'favorites_resume'

    def get_queryset(self):
        return self.request.user.favorites_resume.all()

