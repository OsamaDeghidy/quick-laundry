from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import  UserProfileForm, UserForm
from .models import DeliveryAgent
from .forms import DeliveryAgentSignUpForm, DeliveryAgentProfileForm
from main.models import Order

@login_required
def profilee(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    context = {
        'form': form,
    }

    return render(request, 'users/profile.html', context)



def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('mainview')  # أو الصفحة التي تريد إعادة التوجيه إليها بعد التسجيل الناجح
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'users/Signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



# views.py

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'users/Login.html'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)

    def get_success_url(self):
        if self.request.user.groups.filter(name='delivery_agents').exists():
            return reverse_lazy('available_orders')
        else:
            return reverse_lazy('mainview')








from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import DeliveryAgent
from main.models import Order
from .forms import DeliveryAgentSignUpForm, DeliveryAgentProfileForm

def is_delivery_agent(user):
    return DeliveryAgent.objects.filter(user=user, is_approved=True).exists()

def delivery_agent_signup(request):
    if request.method == 'POST':
        user_form = DeliveryAgentSignUpForm(request.POST)
        profile_form = DeliveryAgentProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = DeliveryAgentSignUpForm()
        profile_form = DeliveryAgentProfileForm()
    return render(request, 'users/representative/delivery_agent_signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
@user_passes_test(is_delivery_agent)
def available_orders(request):
    orders = Order.objects.filter(status='pending')
    return render(request, 'users/representative/available_orders.html', {'orders': orders})

@login_required
@user_passes_test(is_delivery_agent)
def claim_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.status == 'pending':
        order.status = 'claimed'
        order.delivery_agent = request.user.deliveryagent
        order.save()
    return redirect('personal_orders')

@login_required
@user_passes_test(is_delivery_agent)
def personal_orders(request):
    orders = Order.objects.filter(status='claimed', delivery_agent=request.user.deliveryagent)
    return render(request, 'users/representative/personal_orders.html', {'orders': orders})

@login_required
@user_passes_test(is_delivery_agent)
def add_notes(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        notes = request.POST.get('notes')
        order.notes = notes
        order.save()
        return redirect('personal_orders')
    return render(request, 'users/representative/add_notes.html', {'order': order})

@login_required
@user_passes_test(is_delivery_agent)
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'users/representative/order_details.html', {'order': order})