from django.shortcuts import render
from rest_framework import views

class Info(views.APIView):
    def get(self, request):
        context = {
            "project_info": {
                "name": "KADChan (Kiss Anime Downloader Chan)",
                "version": "1.0.0.0",  # Major.Minor.Feature.BugFix
                "version_release_phase": "development",  # "alpha | beta | charlie | development"
                "author": "Dean Van Greunen",
                "email": "deanvg9000@gmail.com",
                "license": "GNU v3",
                "license_url": "https://github.com/DeanVanGreunen/KADChan/blob/master/LICENSE",
                "repo": "https://www.github.com/DeanVanGreunen/KADChan",
                "social": {
                    "Keybase": "https://www.keybase.io/DeanVanGreunen",
                    "Facebook": "https://www.facebook.com/TheDeanVanGreunen"
                }
            }
        }
        return render(request, "info-get.html", context)
