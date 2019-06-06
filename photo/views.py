from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Photo

#함수형 뷰
@login_required #decorator
def photo_list(request):
    photos = Photo.objects.all()
    return render(request,'photo/list.html',{'photos' : photos })

#클래스형 뷰
class PhotoUploadView(LoginRequiredMixin,CreateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/upload.html'

    def form_valid(self,form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form',form})

class PhotoDeleteView(LoginRequiredMixin,DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(LoginRequiredMixin,UpdateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'

class PhotoDetailView(LoginRequiredMixin,DetailView):
    model=Photo
    template_name='photo/detail.html'
