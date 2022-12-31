from django.shortcuts import render

# Create your views here.
def example_view(request):
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')

def variable_view(request):
    # my_var = {'first_name':'devanand', 
    #     'last_name':'yadav',
    #     'some_list':[1,2,3], 
    #     'user_logged_in': True
    # }

    return render(request, 'my_app/variable.html')

