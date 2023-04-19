from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HumanSerializer, TrackSerializer
from .models import Human, Track
from datetime import datetime

@api_view(["POST"])
def register_user(request):
    data = {"phone": request.data["phone"], "days": request.data["days"]}

    serializer = HumanSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "success"})

    else:
        return Response({"message": "failed"})


@api_view(["POST"])
def record(request):
    user = Human.objects.get(phone=request.data["phone"])
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d-%m-%Y")
    data = {
        "human": user.id,
        "date_taken": formatted_date,
        "achieved": request.data["status"],
        "note": request.data["note"],
    }

    track = Track.objects.filter(date_taken=formatted_date)

    if len(track) == 0:

        serializer = TrackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"})
        else:
            print(serializer.errors)
            return Response({"message": "failed"})
    else:
        return Response({"message": "You have already registered today"})


@api_view(["POST"])
def retrieve(request):
    user = Human.objects.get(phone=request.data["phone"])
    results = []
    tracks = Track.objects.filter(human=user)

    for track in tracks:
        if track.achieved:
            results.append({"date": track.date_taken, "count": 5, "note": track.note})
        else:
            results.append({"date": track.date_taken, "count": 0, "note": track.note})

    return Response({"message": "success", "data": results})
