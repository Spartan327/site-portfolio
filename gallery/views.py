from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import VectorDrawingForm
from .models import VectorDrawing, Tag


class GalleryView(ListView):
    template_name = 'gallery/index.html'
    model = VectorDrawing
    context_object_name = 'images'
    paginate_by = 6


class GalleryByTagView(ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'images'
    paginate_by = 6

    def get_queryset(self):
        return VectorDrawing.objects.filter(tags__title=self.kwargs['tag'])


class VectorDrawingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'gallery/add.html'
    form_class = VectorDrawingForm
    success_url = reverse_lazy('gallery:index')
    login_url = "/login"
    permission_required = ('gallery.add_vectordrawing')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        if not self.request.POST.get('new_tags') == '':
            t = []
            new_tag_list = self.request.POST.get('new_tags').split(';')
            if new_tag_list:
                for tag in new_tag_list:
                    t.append(Tag.objects.create(title=tag))
                for tag in t:
                    if not tag in self.object.tags.all():
                        self.object.tags.add(tag)
        return redirect(self.success_url)


def image_id(request, pk):
    success_url = reverse_lazy('gallery:index')
    if request.method == 'POST':
        if not 'delete_image' in request.POST:
            image = VectorDrawing.objects.get(id=pk)
            image.title = request.POST.get('title')
            image.description = request.POST.get('description')
            tag_list = []
            for tag in request.POST.getlist('tags'):
                tag_list.append(Tag.objects.get(title=tag))
            for tag in request.POST.getlist('new_tags'):
                tag_list.append(Tag.objects.get(title=tag))
            image.tags.set(tag_list)
            image.save()
            return redirect(image_id, pk)
        image = VectorDrawing.objects.get(id=pk)
        for tag in image.tags.all():
            if tag.entries.all().count() == 1:
                tag.delete()
        image.delete()
        return redirect(success_url)
    image = VectorDrawing.objects.get(id=pk)
    tags = Tag.objects.all()
    context = {
        'image': image,
        'tags': tags,
    }
    return render(request, 'gallery/image_id.html', context)
