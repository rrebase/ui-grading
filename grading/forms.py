from django.forms import ModelForm


class ProfileSettingsForm(ModelForm):

    class Meta:
        # model = Student
        fields = ("allow_seen_in_stats", "is_email_public")

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields["allow_seen_in_stats"].widget.attrs["class"] = "form-check-input"
        self.fields["is_email_public"].widget.attrs["class"] = "form-check-input"
