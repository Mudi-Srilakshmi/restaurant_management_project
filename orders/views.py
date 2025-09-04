from django.shortcuts import render
from datetime import datetime

def homepage(request):
    # Get the current date and time
    current_time = datetime.now()

    # Pass it to the template
    return render(request, 'home/homepage.html', {'current_time': current_time})
    