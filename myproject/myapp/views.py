from django.shortcuts import render, get_object_or_404, redirect
from .GitLab_Function import create_gitlab_epic_hierarchy

from gc import get_objects

from django.template.defaultfilters import title

from .forms import LinearEquationForm, PostForm, ImageForm, MyForm

from django.http import HttpResponse, JsonResponse

from .models import Post, Image


# View showing my form
def get_variable_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name_value = form.cleaned_data['name'] # getting value name
            location_value = form.cleaned_data['location']
            # writing location value in the session
            request.session['location_value']=location_value

            # Run create gitlab hierarchy function
            try:
                create_gitlab_epic_hierarchy(group_path= location_value, TopLevel=name_value)
                return HttpResponse(f'PROJECT NAME: {name_value}\n, GITLAB GROUP LOCATION: {location_value}')
            except Exception as e:
                return HttpResponse(f'An error occurred : {str(e)}', status=500)
    else:
        form = MyForm()

    return render(request, 'form_template.html', {'form':form})





############################
def hello_world(request):
    #return HttpResponse('Hello World')
    return render(request,'hello_world.html')

def hello_name(request,name):
    #return HttpResponse(f'Hello {name}')
    return render(request, 'hello_name.html',{'name':name, 'klucz':'wartość'})

def add(request,a,b):
    result = a + b
    return render(request,'add.html',{'a':a,'b':b,'c':result})

def div(request,a,b):
    if b!=0:
        c = a / b
    else:
        c = None
    return render(request,'div.html',{'a':a, 'b':b, 'c':c })

def table(request):
    posts = [
        {'id':1,'title':'Pierwszy Post','content':'Tresc pierwszego posta','create at':"2025-05-19"},
        {'id':2,'title': '2 Post', 'content': 'Tresc 2 posta', 'create at': "2025-05-19"},
        {'id':3,'title': '3 Post', 'content': 'Tresc 3 posta', 'create at': "2025-05-19"},
    ]
    for post in posts:
        print(f"Lp.{post['id']}, Tytuł: {post['title']}, Tresc:{post['content']}, Data {post['create at']}")
    return render(request,'table.html')

def create_post(request):
    if request.method == "POST":
        # title = request.POST.get("title")
        # content = request.POST.get("content")
        # if title and content:
        #     Post.objects.create(title=title,content=content)
        # else:
        #     return HttpResponse("Nie wszystkie dane są podane")
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'myapp/post_form.html',{'form':form,'title':'Dodaj post'})

#
def delete_post(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST' and request.POST.get('_method') == 'DELETE':
        post.delete()
        return redirect("post_list")
    return render(request, 'myapp/delete_post.html', {"post":post})


def post_list(request):
    sort = request.GET.get('sort', 'id')
    posts = Post.objects.all().order_by(sort)
    return render(request, 'myapp/post_list.html', {'posts': posts})


def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if request.method == "POST" and form.is_valid():
        #post.title = request.POST.get("title")
        #post.content = request.POST.get("content")
        #post.save()
        form.save()
        return redirect("post_list")

    return render(request, 'myapp/post_form.html', {'form': form, 'title': 'Edytuj post'})


# def zero_point(request):
#     if request.method == 'POST':
#         form = LinearEquationForm(request.POST)
#         if form.is_valid():
#             a = form.cleaned_data['a']
#             b = form.cleaned_data['b']
#     form = LinearEquationForm()
#     return render(request, 'myapp/zero_point.html', {'form':form})
