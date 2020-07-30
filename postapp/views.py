from django.shortcuts import render, redirect
from .forms import Postform
from .models import Post

# Create your views here.
def mainform(request):
    post = Post.objects.all().order_by('-id')
    return render(request,'mainform.html',{'post':post})

def newform(request):
    if request.method == "POST":
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Postform()
        return render(request, 'newform.html', {'form':form})