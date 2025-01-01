import re

COURSE_ID_PATTERN = r"[A-Z]{4}[0-9]{5}"
SCQF_PATTERN = r"SCQF Level (\d+) \((Year (?P<year>\d) )?(Undergraduate|Postgraduate)\)"
SEMESTER_PATTERN = r"[Ss]em(ester)? (?P<semester>[12])"
START_TITLE_PATTERN = r"(Undergraduate|Postgraduate) Course: "
END_TITLE_PATTERN = r" \([A-Z]{4}[0-9]{5}\)"

def prereq(s):
    return [x.lower() for x in re.findall(COURSE_ID_PATTERN, s)]

def year(s):
    m = re.match(SCQF_PATTERN, s)
    year = m.groupdict()["year"]
    if year == None:
        return 7
    else:
        return year

def semester(s):
    m = re.match(SEMESTER_PATTERN, s)
    if m == None:
        return 1
    else:
        return m.groupdict()["semester"]

def title(s):
    s = re.sub(START_TITLE_PATTERN, "", s)
    return re.sub(END_TITLE_PATTERN, "", s)

def list_order(l):
    return list(reversed(list(l)))