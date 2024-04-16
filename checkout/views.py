from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag you silly goose")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51P6EQ905xB0s6tsGaa5Ehy2EWScDYzhRuzDHtbmuPf9qrQNTRTBAeFmmdteyQK2U3caBMFoKnDsdsuOyepMAylSq00ZDeV3Duy',
        'client_secret': 'test'
    }

    return render(request, template, context)
