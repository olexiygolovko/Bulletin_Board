from django import forms
from .models import Post, Response


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {'title': forms.TextInput(attrs={'size': '100'})}
        fields = ('category', 'title', 'text',)

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['category'].label = "Category:"
        self.fields['title'].label = "Heading"
        self.fields['text'].label = "Announcement text:"


class RespondForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super(RespondForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = "Response text:"


class ResponsesFilterForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(ResponsesFilterForm, self).__init__(*args, **kwargs)
        self.fields['title'] = forms.ModelChoiceField(
            label='Announcement',
            queryset=Post.objects.filter(author_id=user.id).order_by('-dateCreation').values_list('title', flat=True),
            empty_label="All",
            required=False
        )
