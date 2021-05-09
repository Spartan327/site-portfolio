from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import VectorDrawingForm
from .models import VectorDrawing, Tag


def index(request):
    images = VectorDrawing.objects.all()
    context = {
        'images': images
    }
    return render(request, 'gallery/index.html', context)


def by_tag(request, tag):
    images = VectorDrawing.objects.filter(tags__title=tag)
    context = {
        'images': images
    }
    return render(request, 'gallery/index.html', context)


class VectorDrawingCreateView(CreateView):
    template_name = 'gallery/add.html'
    form_class = VectorDrawingForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        t = []
        new_tag_list = self.request.POST.get('new_tags').split('; ')
        if new_tag_list:
            for tag in new_tag_list:
                t.append(Tag.objects.create(title=tag))
            for tag in t:
                if not tag in self.object.tags.all():
                    self.object.tags.add(tag)
        return redirect(index)


def image_id(request, pk):
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
            print(tag.title)
            print(tag.entries.all().count())
            if tag.entries.all().count() == 1:
                tag.delete()
        image.delete()
        return redirect(index)
    else:
        image = VectorDrawing.objects.get(id=pk)
        tags = Tag.objects.all()
        context = {
            'image': image,
            'tags': tags,
        }
        return render(request, 'gallery/image_id.html', context)
