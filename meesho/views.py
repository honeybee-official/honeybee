from django.shortcuts import redirect, render
from meesho.form import ContactForm, UserRegisterForm
from meesho.models import Category, Product
# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def category(request):
    return render(request, 'pages/category.html')


def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {'form': form}
    return render(request, 'pages/register.html', context)

def login(request):
    return render(request, 'pages/login.html')


def success(request):
    return render(request, 'pages/success.html')

# Define the contact_view function to handle the contact form
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    context = {'form':form}
    return render(request, 'pages/contactForm.html', context)

# Define the contact_success_view function to handle the success page
def contact_success_view(request):
    return render(request, 'pages/success.html' )