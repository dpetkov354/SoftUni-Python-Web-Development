from django.core import exceptions

MIN_LENGTH = 2
MAX_YEAR = 2049
MIN_YEAR = 1980


def validate_min_length(value):
    if len(value) < MIN_LENGTH:
        raise exceptions.ValidationError("The username must be a minimum of 2 chars")


def validate_year(value):
    if MIN_YEAR > value or value > MAX_YEAR:
        raise exceptions.ValidationError("Year must be between 1980 and 2049")
