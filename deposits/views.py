from django.shortcuts import render
from django.views. generic import View, ListView
from deposits.models import Deposit


class DepositListView(ListView):
    model = Deposit
    template_name = 'deposit_list.html'

class AddDepositView(View):

    def get(self, request):

        return render(
            template_name='add_deposit.html',
            request=request,
        )
    def post (self, request):

        deposit = Deposit(
            deposit=request.POST['deposit'],
            term=request.POST['term'],
            rate=request.POST['rate'],
            interest=request.POST['interest'],
        )

        deposit.save()

        context = {
            'deposit': deposit.deposit,
            'term': deposit.term,
            'rate': deposit.rate,
        }

        return render (
            template_name='deposit_list.html',
            request=request,
            context=context,
        )
