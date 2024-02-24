from django.http import JsonResponse

from prica.models import PricaModel


def get_num_of_unread_messages(request):
    if request.user.is_anonymous:
        return JsonResponse({"unread": 0})
    unread_messages = PricaModel.objects.filter(reciever__id=int(request.user.id), is_read=False).count()
    return JsonResponse({"unread": unread_messages})
