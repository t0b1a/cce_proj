from django.db import models

class Job(models.Model): #per interfacciarsi col db
    image = models.ImageField(upload_to='images/') # inside alla media folder che andremo a creare ci sarà una sottodir images
    title = models.CharField(max_length=200) #mettiamo un cap per lo spazio di testo
    description = models.CharField(max_length=200)
    url = models.URLField(max_length = 200)