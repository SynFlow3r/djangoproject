from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from .models import Profile, CardPayment
from django.http import HttpResponse

def card_pay(request):
    if request.method == 'POST' and request.user.is_authenticated:
        card_name = request.POST.get('card-name')
        card_number = request.POST.get('card-number')
        expiry_date = request.POST.get('expiry-date')
        cvv = request.POST.get('cvv')
        product_name = request.POST.get('product-name')
        product_price = request.POST.get('product-price')

        # Process the payment or store the data
        # For example, you can print the values or save them to the database
        print(f"Card Name: {card_name}")
        print(f"Card Number: {card_number}")
        print(f"Expiry Date: {expiry_date}")
        print(f"CVV: {cvv}")
        print(f"Product Name: {product_name}")
        print(f"Product Price: {product_price}")
        card_payment = CardPayment.objects.create(
            user=request.user,
            product_name=product_name,
            product_price=float(product_price),
            card_number=card_number,
            name=card_name,
            card_cvv=int(cvv),
            expiry_date=expiry_date
        )
        card_payment.save()
        # Redirect to a success page or return a success response
        return HttpResponse("Payment processed successfully.")

    # Handle GET request
    product_name = request.GET.get('name')
    product_price = request.GET.get('price')

    context = {
        'product_name': product_name,
        'product_price': product_price,
    }
    return render(request, 'cardpay.html', context)



def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def login_register(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        context = {
            'user': request.user,
            'profile': profile,
        }
        return render(request, 'profile.html', context)
    if request.method == 'POST':
        if 'login' in request.POST:
            # Обработка логина
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                profile = Profile.objects.get(user=user)
                context = {
                    'user': request.user,
                    'profile': profile,
                }
                return render(request, 'profile.html', context)
            else:
                return render(request, 'logreg.html', {'login_error': 'Invalid username or password.', 'form': SignUpForm()})
        elif 'register' in request.POST:
            # Обработка регистрации
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                new_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'])
                login(request, new_user)
                profile = Profile.objects.get(user=new_user)
                context = {
                    'user': request.user,
                    'profile': profile,
                }
                return render(request, 'profile.html', context)
            else:
                return render(request, 'logreg.html', {'form': form})
    else:
        # GET запрос - просто отобразить форму
        form = SignUpForm()
    return render(request, 'logreg.html', {'form': form})