from django.shortcuts import render

# Create your views here.

#  Home page view
def Home(request):
    # Renders the home page
    ctx = {}
    return render(request,"splitwise_app/index.html",ctx)