from django.shortcuts import render, get_object_or_404, redirect
from .GitLab_Function import create_gitlab_epic_hierarchy

from gc import get_objects

from django.template.defaultfilters import title

from .forms import  MyForm

from django.http import HttpResponse, JsonResponse




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





# def hello_name(request,name):
#     #return HttpResponse(f'Hello {name}')
#     return render(request, 'hello_name.html',{'name':name, 'klucz':'wartość'})
#





