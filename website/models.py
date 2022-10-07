from django.db import models

class Pastes(models.Model):
	uuid = models.CharField(max_length = 100)
	data = models.CharField(max_length = 10000)

	def __str__(self):
		return self.uuid + ': ' + str(len(self.data))
