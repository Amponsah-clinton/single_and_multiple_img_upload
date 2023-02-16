from django.shortcuts import render
from .models import User, Multiple
from .forms import UserForm

# one to one view
def index(request):
    obj = User.objects.all()
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = UserForm()
    return render(request, 'index.html', {'form': form, 'obj': obj})



# multiple images views
def upload(request):
    if request.method == 'POST':
        images  = request.FILES.getlist('images')
        for img in images:
            Multiple.objects.create(images=img)
    images = Multiple.objects.all()
    return render(request, 'upload.html', {'images':images})
            
