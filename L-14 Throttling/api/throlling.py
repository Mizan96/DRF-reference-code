from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class StudentRateThrottle(UserRateThrottle):
    scope = 'student'
    
    
# class StudentRateThrottle(AnonRateThrottle):
#     scope = 'student'
    