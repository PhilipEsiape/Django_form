from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    #If the method is POST
    if request.method == 'POST':
        forms = PostForm(request.POST)
    
        # if the form is valid
        if forms.is_valid():
        
         #Yes,save
         forms.save()

         #Redirect to Home
         return HttpResponseRedirect('/')
       
        else:
            #No, Show Error
           return HttpResponse(forms.erros.as_json())

    # Get all posts, limit = 20
    post = Post.objects.all()[:20]


    #Show
    return render(request, 'post.html', 
                  {'posts': post})


def delete(request, post_id):
   post = Post.objects.get(id= post_id)
   post.delete()
  
   return HttpResponseRedirect("/")