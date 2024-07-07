from enum import Enum

class CourseStates(Enum):
    ACTIVE = 'ACTIVE'
    PROVISIONED = 'PROVISIONED'
    ARCHIVED = 'ARCHIVED'
    DECLINED = 'DECLINED'
    SUSPENDED = 'SUSPENDED'


COURSES_API_ENDPOINT = 'https://classroom.googleapis.com/v1/courses'
JSON_KEY = 'json_key.json'
SCOPES = [
    'https://www.googleapis.com/auth/classroom.courses',
    'https://www.googleapis.com/auth/classroom.courses.readonly',
    'https://www.googleapis.com/auth/classroom.rosters',
    'https://www.googleapis.com/auth/classroom.rosters.readonly',
    'https://www.googleapis.com/auth/classroom.profile.emails',
    'https://www.googleapis.com/auth/classroom.profile.photos'
]
