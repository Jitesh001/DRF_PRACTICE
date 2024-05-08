from rest_framework.throttling import UserRateThrottle

class DeveloperThrottle(UserRateThrottle):
    scope = 'developers'
    rate = '4/minute'