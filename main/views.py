from django.shortcuts import render, redirect
from Users.forms import UserProfileForm, UserForm
from Users.models import UserProfile
from .forms import OrderForm

# Create your views here.


def main_view(request):
    working_process = [
        {'image': 'img/We bring back.svg', 'title': 'Bag up your dirty laundry'},
        {'image': 'img/scadul.svg', 'title': 'Schedule a free pick up'},
        {'image': 'img/packup.png', 'title': 'We pick up your dirty clothes'},
        {'image': 'img/wash.png', 'title': 'We wash and dry. Fresh and clean'},
        {'image': 'img/fold and sort.svg', 'title': 'We fold and sort for you'},
        {'image': 'img/bring back.png', 'title': 'We bring back your fresh laundry'},
    ]
    final_steps = [
        {'number': '1', 'title': 'Place Order'},
        {'number': '2', 'title': 'Pick Up'},
        {'number': '3', 'title': 'Dry Cleaning'},
        {'number': '4', 'title': 'Delivery'},
    ]
    return render(request, 'main/main.html', {'working_process': working_process, 'final_steps': final_steps})
def hawitwork(request):
    return render(request, 'main/hawitwork.html')

# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order
from django.shortcuts import render, get_object_or_404


@login_required
def profile_view(request):
    orders = Order.objects.filter(user=request.user)
    for order in orders:
        order.update_status()

    user_profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'orders': orders,
        'user_profile': user_profile
    }
    
    return render(request, 'main/profile.html', context)



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required
@csrf_exempt
def update_order_status(request):
    if request.method == 'POST':
        orders = Order.objects.filter(user=request.user)
        updated_orders = []
        for order in orders:
            order.update_status()
            updated_orders.append({
                'id': order.id,
                'status': order.status,
                'time_remaining': order.time_remaining(),
                'scheduled_date': order.scheduled_date,
                'scheduled_time': order.scheduled_time,
            })
        return JsonResponse({'orders': updated_orders})





@login_required
def manage_profile_or_order(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # Create form instances
        order_form = OrderForm(request.POST)
        user_profile_form = UserProfileForm(request.POST, instance=user_profile)
        
        # Validate both forms
        if order_form.is_valid() and user_profile_form.is_valid():
            # Save both forms
            order = order_form.save(commit=False)
            order.user = request.user
            order.save()
            user_profile_form.save()
            return redirect('profile')  # Redirect to profile page after saving
        else:
            # Render the page with both forms and their errors
            context = {
                'order_form': order_form,
                'user_profile_form': user_profile_form,
                'user_profile_exists': created
            }
            return render(request, 'main/manage_profile_or_order.html', context)
    else:
        # Initial form instances
        order_form = OrderForm()
        user_profile_form = UserProfileForm(instance=user_profile)
    
    # Render the page with both forms
    context = {
        'order_form': order_form,
        'user_profile_form': user_profile_form,
        'user_profile_exists': created
    }
    return render(request, 'main/manage_profile_or_order.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'main/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



# views.py
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def charge(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        try:
            charge = stripe.Charge.create(
                amount=5000,  # Amount in cents
                currency='usd',
                description='Example charge',
                source=token,
            )
            return redirect('success')
        except stripe.error.CardError as e:
            return redirect('error')
    return render(request, 'main/payment.html')


import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY
def checkout_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        # التأكد من أن السعر ليس صفرًا
        if order.price <= 0:
            return HttpResponse("Invalid order amount.")

        # إنشاء جلسة Stripe
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f"Order {order.id}",
                    },
                    'unit_amount': int(order.price * 100),  # تحويل السعر إلى سنتات
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('payment_success', args=[order.id])),
            cancel_url=request.build_absolute_uri(reverse('payment_cancel', args=[order.id])),
        )
        return redirect(session.url, code=303)
    
    context = {
        'order': order,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'main/payment.html', context)

  
    



from django.http import HttpResponse

def payment_success_view(request, product_id):

    product = Order.objects.get(id=product_id)
    product.payment_status = True
    product.save()
    return render(request, 'payment/payment-success.html', {'product': product})

def payment_cancel_view(request, product_id):

    product = Order.objects.get(id=product_id)

    return render(request, 'payment/payment-failed.html', {'product': product})