from django import forms


class JoinRoomForm(forms.Form):
    room_id = forms.CharField(max_length=100)
