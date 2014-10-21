from django.shortcuts import render
from django.http import HttpResponseRedirect
from chameleonRT import rtUtil, forms

def mytickets(request):
	rt = rtUtil.ChameleonRt()
	user_tickets = rt.getUserTickets(request.user.email)
	return render(request, 'ticketList.html', { 'user_tickets' : user_tickets})

def ticketdetail(request, ticketId):
	rt = rtUtil.ChameleonRt()
	ticket = rt.getTicket(ticketId)
	ticket_history = rt.getTicketHistory(ticketId)
	return render(request, 'ticketDetail.html', { 'ticket' : ticket, 'ticket_history' : ticket_history, 'ticket_id' : ticketId })

def ticketcreate(request):
	data = { 'email' : request.user.email, 'first_name' : request.user.first_name, 'last_name' : request.user.last_name}

	if request.method == 'POST':
		form = forms.TicketForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/chameleonRT/')
	else:
		form = forms.TicketForm(data)
	return render(request, 'ticketCreate.html', { 'form' : form }) 

def ticketreply(request, ticketId):
	print "Hello!"
	rt = rtUtil.ChameleonRt()
	ticket = rt.getTicket(ticketId)

	if request.method == 'POST':
		print "A new post!"
		form = forms.ReplyForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/chameleonRT/ticket/' + ticketId)

	else:
		form = forms.ReplyForm()
	return render(request, 'ticketReply.html', { 'ticket_id' : ticketId , 'ticket' : ticket, 'form' : form })
