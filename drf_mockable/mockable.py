from django.http import JsonResponse

from rest_framework.views import APIView

class MockableView(APIView):
    """
    This is the class which will allow you to build Mockable APIs
    """

    def initial(self, request, *args, **kwargs):
        """
        Runs anything that needs to occur prior to calling the method handler.
        """
        self.format_kwarg = self.get_format_suffix(**kwargs)

        # Perform content negotiation and store the accepted info on the request
        neg = self.perform_content_negotiation(request)
        request.accepted_renderer, request.accepted_media_type = neg

        # Determine the API version, if versioning is in use.
        version, scheme = self.determine_version(request, *args, **kwargs)
        request.version, request.versioning_scheme = version, scheme

        # Ensure that the incoming request is permitted
        self.perform_authentication(request)
        self.check_permissions(request)
        self.check_throttles(request)
        self.check_mockable(request)


    def check_mockable(self, request):
        """
        """
        try:
            if str(request.META.get('HTTP_MOCKABLE', "")).lower() == 'yes':
                return JSONResponse(self.mock_response)
        except Exception as e:
            print(repr(e))
            exit()