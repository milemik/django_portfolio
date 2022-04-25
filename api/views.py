# from django.contrib.sites.models import Site
from django.http import JsonResponse

from prica.models import PricaModel


def get_num_of_unread_messages(request, user_id):
    unread_messages = PricaModel.objects.filter(reciever__id=int(user_id), is_read=False).count()
    return JsonResponse({"unread": unread_messages})
