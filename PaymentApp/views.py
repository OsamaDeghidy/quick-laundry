from django.shortcuts import render
from main.models import Order
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse

def CheckOut(request, product_id):

    product = Order.objects.get(id=product_id)

    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': product.price,
        'item_name': product.id,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment-success', kwargs = {'product_id': product.id})}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs = {'product_id': product.id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'product': product,
        'paypal': paypal_payment
    }

    return render(request, 'payment/checkout.html', context)

def PaymentSuccessful(request, product_id):

    product = Order.objects.get(id=product_id)
    product.payment_status = True
    product.save()

    return render(request, 'payment/payment-success.html', {'product': product})

def paymentFailed(request, product_id):

    product = Order.objects.get(id=product_id)

    return render(request, 'payment/payment-failed.html', {'product': product})