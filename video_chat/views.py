from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from api.v1.bookings.models import Booking
from api.v1.users.models import Doctor, Patient, User
from video_chat.forms import RecordForm, VideoForm
from .utils import get_access_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class JoinRoom(View):

    def get(self, request, ref):
        print(ref)
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

@method_decorator(csrf_exempt, name='dispatch')
class RoomView(View):
    def get(self, request, room_name):
        room_data = request.session['room_data']
        participant_data = request.session['participant_data']
        patient_id = request.session['patient_id']
        doctor_id = request.session['doctor_id']
        booking_id = request.session['booking_id']
        is_doctor = request.session['is_doctor']


        record_form = RecordForm()

        context = {
            "context": {
                'room_name': room_name,
                'room_sid': room_data['room_sid'],
                'participant_token': participant_data['token'],
                'doctor': doctor_id,
                'patient': patient_id,
                'booking': booking_id,
                'is_doctor': 'true' if is_doctor else 'false',
            },
            'record_form': record_form
        }

        return render(request, 'video_chat/room.html', context)

    def post(self, request, room_name):
        medical_form = RecordForm(request.POST)
        booking_id = request.session['booking_id']
        patient_id = request.session['patient_id']
        doctor_id = request.session['doctor_id']

        booking = Booking.objects.get(id=booking_id)
        doctor = Doctor.objects.get(id=doctor_id)
        patient = Patient.objects.get(id=patient_id)
        room_data = request.session['room_data']
        room_sid = room_data['room_sid']

        if medical_form.is_valid():
            medical_record = medical_form.save(commit=False)
            medical_record.booking_id = booking
            medical_record.doctor = doctor
            medical_record.patient = patient
            medical_record.save()

            return redirect('video_chat:end-room', room_sid)

