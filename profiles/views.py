from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def profile(request):
    """ Display the user's profile
    Args:
        request: HTTP request
    Returns:
        The profile of the user and updates the
        profile if changes made
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Display the user order history
    Args:
        request: HTTP request object
        order_number: order number passed in
    Returns:
        Order history of the user if logged in
    """

    order = get_object_or_404(Order, order_number=order_number)
    if request.user.is_authenticated:
        messages.info(request, (
            f'This is a past confirmation for order number {order_number}. '
        ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
