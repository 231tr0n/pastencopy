from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
import uuid
from website.models import Pastes

# Create your views here.
def index(req):
	if req.method == 'GET':
		return render(req, 'index.html')
	elif req.method == 'POST':
		if req.POST['data']:
			if len(req.POST['data']) <= 10000:
				temp_uuid = str(uuid.uuid4())
				p1 = Pastes(uuid = temp_uuid, data = req.POST['data'])
				p1.save()
				return HttpResponseRedirect('/link/' + temp_uuid)
		raise PermissionDenied

def paste(req, uuid):
	try:
		p1 = Pastes.objects.get(uuid = uuid)
		return render(req, 'paste.html', context = {
			'data': p1.data
		})
	except:
		return HttpResponseNotFound()
