from django.db import models

class Job(models.Model): #per interfacciarsi col db
    image = models.ImageField(upload_to='images/') # inside alla media folder che andremo a creare ci sarà una sottodir images
    title = models.CharField(max_length=200) #mettiamo un cap per lo spazio di testo
    placeholder = models.CharField(max_length=200)
    button_text = models.CharField(max_length=200)
    description = models.CharField(max_length=200)