from django.shortcuts import render
from django.views import View
from .models import Transaction
from django.conf import settings

# Create your views here.


class TransactionView(View):
    template = "../templates/main.html"    

    def get(self, request, *args, **kwargs):    
        transactions=Transaction.objects.all()
        context = {
            "pending": False,
        }
        if len(transactions)>0:
            context["pendind"]=True
            context["reference"] = transactions[0].reference
            context["ammount_in_cents"] = int(transactions[0].ammount_in_cents)
            context["coin_type"] = transactions[0].coin_type
            context["signature_integrity"] = transactions[0].signature_integrity
            context["wompi_public_key"] = settings.WOMPI_PUBLIC_KEY

        return render(
            request,
            self.template,
            context
        )


class TransactionEventView(View): 

    def post(self, request, *args, **kwargs):    
        print(request.POST)
        return "ASDAS"
