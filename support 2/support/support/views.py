from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket, TicketResponse
from .forms import TicketForm, ResponseForm

@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'support/ticket_list.html', {'tickets': tickets})

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'support/create_ticket.html', {'form': form})

@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.ticket = ticket
            response.user = request.user
            response.save()
            return redirect('ticket_detail', ticket_id=ticket_id)
    else:
        form = ResponseForm()
    return render(request, 'support/ticket_detail.html', {'ticket': ticket, 'form': form})

# Create your views here.

from django.core.mail import send_mail

# Trong view create_ticket
send_mail(
    'New Support Ticket Created',
    f'Your ticket "{ticket.subject}" has been received.',
    'noreply@gamehub.com',
    [request.user.email],
    fail_silently=False,
)