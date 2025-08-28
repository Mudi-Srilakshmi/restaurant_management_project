# Email backend (for development use console backend)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# If you want real email sending, configure SMTP like this:
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = "yourgmail.com"
# EMAIL_HOST_PASSWORD = "yourpassword"

DEFAULT_FROM_EMAIL = "yourgmail@gmail.com" # sender email
RESTAURANT_EMAIL = "restaurant@example.com" # restaurant receiving email



