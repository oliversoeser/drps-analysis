import re

COURSE_ID_PATTERN = r"[A-Z]{4}[0-9]{5}"

def prereq(s):
    return [x.lower() for x in re.findall(COURSE_ID_PATTERN, s)]

