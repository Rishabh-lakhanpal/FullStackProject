from .models import WebsiteSetting


def getWebSetting():
    try:
        web_setting = WebsiteSetting.objects.get(id=1)
        return web_setting
    except WebsiteSetting.DoesNotExist:
        return []