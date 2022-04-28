from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, JsonResponse
from django.views import View
from rest_framework.response import Response

from api.v1.bookings.models import Booking
from api.v1.users.models import Doctor, Patient, User
from video_chat.forms import VideoForm
from .utils import get_access_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# after sending a post request to the join route and getting the token, what next
# add the token to the user's session rather
# get the name the person wants to use for the video call
# store room_name, room_id, person_information in session variable
# redirect to the room view page
# on room view get the room data and ther person's information from session variable
# pass the necessary content to the view and its context

# js vars can be retrieved from context

class JoinRoom(View):

    def get(self, request, ref):
        booking = get_object_or_404(Booking, booking_reference=ref)
        room_name = booking.room_name
        room_sid = booking.room_sid
        room_data = {
            'room_name': room_name,
            'room_sid': room_sid
        }
        patient_name = booking.patient.patient.first_name
        doctor_name = booking.doctor.doctor.first_name
        email_form = VideoForm()
        request.session['room_data'] = room_data
        context = {'room_name': room_data['room_name'], 
                    'room_sid': room_data['room_sid'], 
                    'patient_name': patient_name, 
                    'doctor_name': doctor_name, 
                    'form': email_form }
        return render(request, 'video_chat/join.html', context)


    def post(self, request, ref):
        booking = Booking.objects.get(booking_reference=ref)
        email_form = VideoForm(request.POST)
        if email_form.is_valid():
            user_email = email_form.cleaned_data['participant']
            if User.objects.filter(email = user_email).exists():            
                room_data = request.session['room_data']
                room_name = room_data['room_name']
                user_token = get_access_token(room_data['room_name'])
                user = User.objects.get(email = user_email)
                request.session['booking_id'] = booking.id
                request.session['patient_id'] = booking.patient.id
                request.session['doctor_id'] = booking.doctor.id
                request.session['user_id'] = user.id
                request.session['is_doctor'] = user.is_doctor
                request.session['participant_data'] = {'token': user_token.to_jwt()}
                return redirect('video_chat:room-view', room_name)
            else:
                return redirect('video_chat:join-room', ref)


def room_view(request, room_name):
    room_data = request.session['room_data']
    participant_data = request.session['participant_data']
    patient_id = request.session['patient_id']
    doctor_id = request.session['doctor_id']
    booking_id = request.session['booking_id']
    is_doctor = request.session['is_doctor']
    doctor = Doctor.objects.get(id=doctor_id)
    patient = Patient.objects.get(id=patient_id)
    booking = Booking.objects.get(id=booking_id)
    context = {
        "context": {
            'room_name': room_name,
            'room_sid': room_data['room_sid'],
            'participant_token': participant_data['token'],
            'doctor': doctor_id,
            'patient': booking_id,
            'booking': booking_id,
            'is_doctor': 'true' if is_doctor else 'false'
        }
    }

    return render(request, 'video_chat/room.html', context)

