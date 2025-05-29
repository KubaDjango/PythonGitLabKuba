from django.shortcuts import render, get_object_or_404, redirect
from .GitLab_Function import create_gitlab_epic_hierarchy

from gc import get_objects

from django.template.defaultfilters import title

from .forms import  MyForm

from django.http import HttpResponse, JsonResponse
from django.utils.html import format_html



# View showing my form
def get_variable_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name_value = form.cleaned_data['name'] # getting value name
            location_value = form.cleaned_data['location']
            # writing location value in the session
            request.session['location_value']=location_value

#           Run create gitlab hierarchy function
            try:
                create_gitlab_epic_hierarchy(group_path= location_value, TopLevel=name_value)
                gitlab_url = "https://gitlab.com/groups/analizy.badawcze-group/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=Initiative+Level::Top+Level"
                return HttpResponse(
                    f"PROJECT NAME: {name_value}<br>"
                    f"GITLAB GROUP LOCATION: {location_value}<br>"
                    f"Open: <a href='{gitlab_url}' target='_blank'>{gitlab_url}</a>"
                )
            except Exception as e:
                return HttpResponse(f'An error occurred : {str(e)}', status=500)
    else:
        form = MyForm()

    return render(request, 'form_template.html', {'form':form})





# def hello_name(request,name):
#     #return HttpResponse(f'Hello {name}')
#     return render(request, 'hello_name.html',{'name':name, 'klucz':'wartość'})
#





