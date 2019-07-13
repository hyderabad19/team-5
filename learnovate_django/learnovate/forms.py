class VideoForm(forms.ModelForm):
    class Meta:
        model= Resource
        fields= ["name" ,"file","description"]