from django.http import JsonResponse

from prica.models import PricaModel


def get_num_of_unread_messages(request):
    unread_messages = PricaModel.objects.filter(reciever__id=int(request.user.id), is_read=False).count()
    return JsonResponse({"unread": unread_messages})
