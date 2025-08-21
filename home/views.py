from django.shortcuts import render, redirect
from .forms import FeedbackForm

# View to handle feedback form
def feedback_view(request):
    if request.method == 'POST': # If form is submitted
        form = FeedbackForm(request.POST)
        if form.is_valid(): # Validate form
            form.save() # Save feedback to database
            return redirect('feedback') # Redirect to same page after submit

    else:
        form = FeedbackForm() # Empty form for GET request

    return render(request, 'home/feedback.html', {'form': form})
    
