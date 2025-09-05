from django.shortcuts import render

def privacy_policy(request):
    """
    Renders the hardcoded privacy policy page
    """
    return render(request, "orders/privacy.html")
    