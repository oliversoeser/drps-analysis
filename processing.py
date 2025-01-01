import re

COURSE_ID_PATTERN = r"[A-Z]{4}[0-9]{5}"
SCQF_PATTERN = r"SCQF Level (?P<level>\d+) \((Year (?P<year>\d) )?(?P<degree>Undergraduate|Postgraduate)\)"
SEMESTER_PATTERN = r"[Ss]em(ester)? (?P<semester>[12])"

def prereq(s):
    return [x.lower() for x in re.findall(COURSE_ID_PATTERN, s)]

def year(s):
    m = re.match(SCQF_PATTERN, s)
    year = m.groupdict()["year"]
    if year == None:
        return 999
    else:
        return year

def level(s):
    m = re.match(SCQF_PATTERN, s)
    return m.groupdict()["level"]

def degree(s):
    m = re.match(SCQF_PATTERN, s)
    return m.groupdict()["degree"]

def semester(s):
    m = re.match(SEMESTER_PATTERN, s)
    if m == None:
        return 1
    else:
        return m.groupdict()["semester"]

def list_order(l):
    return list(reversed(list(l)))