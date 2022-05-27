from django import forms

from recipes.web.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Recipe
        fields = ('title', 'image', 'description', 'ingredients', 'time')
        labels = {
            'image': 'Image URL',
            'time': 'Time (Minutes)',
        }


class EditRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Recipe
        fields = ('title', 'image', 'description', 'ingredients', 'time')
        labels = {
            'image': 'Image URL',
            'time': 'Time (Minutes)',
        }


class DeleteRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Recipe
        fields = ('title', 'image', 'description', 'ingredients', 'time')
        labels = {
            'image': 'Image URL',
            'time': 'Time (Minutes)',
        }
