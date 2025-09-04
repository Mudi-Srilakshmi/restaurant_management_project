from django.shortcuts import render

# FAQ View
def faq(request):
    # Hardcoded FAQ content
    faqs = [
        {"question": "What are your opening hours?", "answer": "We are open from 9 AM to 10 PM daily."},
        {"question": "Do you offer home delivery?", "answer": "Yes, we offer free home delivery within 5 km."},
        {"question": "How can I book a table?", "answer": "You can book a table by calling our number: 123-456-7890."}
    ]
    return render(request, 'faq.html', {"faqs": faqs})
    