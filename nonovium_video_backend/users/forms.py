from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from nonovium_video_backend.files.methods import is_nonoviumvideo_manager
from nonovium_video_backend.users.models import Channel

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class SignupForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")

    def signup(self, request, user):
        user.name = self.cleaned_data["name"]
        user.save()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "name",
            "description",
            "logo",
            "notification_on_comments",
            "is_featured",
            "advancedUser",
            "is_manager",
            "is_editor",
            # "allow_contact",
        )

    def clean_logo(self):
        image = self.cleaned_data.get("logo", False)
        if image:
            if image.size > 2 * 1024 * 1024:
                raise forms.ValidationError("Image file too large ( > 2mb )")
            return image
        else:
            raise forms.ValidationError("Please provide a logo")

    def __init__(self, user, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields.pop("is_featured")
        if not is_nonoviumvideo_manager(user):
            self.fields.pop("advancedUser")
            self.fields.pop("is_manager")
            self.fields.pop("is_editor")


class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ("banner_logo",)

    def clean_banner_logo(self):
        image = self.cleaned_data.get("banner_logo", False)
        if image:
            if image.size > 2 * 1024 * 1024:
                raise forms.ValidationError("Image file too large ( > 2mb )")
            return image
        else:
            raise forms.ValidationError("Please provide a banner")
