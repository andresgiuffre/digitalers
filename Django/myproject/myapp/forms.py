from django import forms
from .models import Curso, Comentario, Calificacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('id', 'nombre', 'inscripciones', 'turno')
        labels = {
            'nombre': 'Nombre',
            'inscripciones': 'Inscripciones',
            'turno': 'Turnos'
        }

        nombre = forms.CharField(max_length=128)
        inscripciones = forms.IntegerField()
        turno = forms.ChoiceField()
        
        #fecha_inicio = forms.DateField(
        #    label="Fecha de Inicio",
            #input_formats=["%d/%m/%Y"] # ---> dd/mm/AAAA
        #    widget=forms.DateInput(attrs={"type": "date"})
        #)


class FormularioPelicula(forms.Form):
    nombre = forms.CharField(label="Nombre de la Película", max_length=128)
    fecha_estreno = forms.DateField(
        label="Fecha de Estreno",
        widget=forms.DateInput(attrs={"type": "date"})
    )
    edad_minima = forms.IntegerField(label="Apta para Mayores de ...")
    preventa_online = forms.BooleanField(
        label="¿Con Preventa Online?",
        required=False
    )


class RegistrarUsuario(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    nombre = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}))
    apellido = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su apellido'}))

    class Meta:
        model: User
        fields = ('username', 'nombre', 'apellido', 'email', 'password1', 'password2')


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']


class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['puntaje']
        labels = {'puntaje': 'Puntaje (Entre 0 y 5)'}


    def clean_puntaje(self):
        puntaje = self.cleaned_data.get('puntaje')
        if puntaje < 0 or puntaje > 5:
            raise forms.ValidationError("El puntaje debe estar entre 0 y 5")
        return puntaje