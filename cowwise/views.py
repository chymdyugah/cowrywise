from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status
from .models import MyUuid
import uuid


@api_view(['GET'])
def getUUID(request, *args, **kwargs):
	try:
		import uuid, datetime
		MyUuid.objects.create()
		old = MyUuid.objects.all().order_by('-date_created')
		all = {}
		for a in old:
			all.update({str(a.date_created): a.val})

		return Response(all, status=status.HTTP_201_CREATED)
	except Exception as e:
		return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)