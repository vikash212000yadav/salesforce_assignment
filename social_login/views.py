from urllib import request

from django.shortcuts import render
from allauth.socialaccount.providers.salesforce.views import SalesforceOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


class SalesforceLogin(SocialLoginView):
    authentication_classes = []  # disable authentication
    adapter_class = SalesforceOAuth2Adapter
    callback_url = "http://localhost:3000"
    client_class = OAuth2Client


"""@csrf_exempt
def salesforce_token():
    if "code" not in request.body.decode():
        from rest_framework_simplejwt.settings import api_settings as jwt_settings
        from rest_framework_simplejwt.views import TokenRefreshView

        class RefreshNuxtAuth(TokenRefreshView):
            def post(self, request, *args, **kwargs):
                request.data._mutable = True
                request.data["refresh"] = request.data.get("refresh_token")
                request.data._mutable = False
                response = super().post(request, *args, **kwargs)
                response.data['refresh_token'] = response.data['refresh']
                response.data['access_token'] = response.data['access']
                return response

        return RefreshNuxtAuth

    else:
        return SalesforceLogin"""
