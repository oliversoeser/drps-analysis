from bs4 import BeautifulSoup

# Read data keys
with open("keys.txt", "r") as keyfile:
    keys_text = keyfile.read()

keys = {key[0]: key[1] for key in [line.split(",") for line in keys_text.split("\n")]}

# Data extraction
def extract(html: str):
    html = BeautifulSoup(html, features="lxml")
    tables = html.find_all("table")

    # Detect 404s
    if len(tables) < 3:
        return {}

    html = tables[2]

    page = {}
    page["title"] = html.find("h1").decode_contents()

    for table in html.find_all("table"):
        caption = table.find("caption")
        if caption == None:
            continue
        title = caption.text
        if title not in keys.keys():
            continue
        section = keys[title]
        page[section] = {}
        for row in table.find_all("tr"):
            key = ""
            for data in row.find_all("td"):
                text = data.text
                # Remove trailing and leading whitespace, as well as empty lines
                text = "\n".join([line.strip() for line in text.split("\n") if line.strip() != ""])
                if section in ["outcomes", "reading"]:
                    page[section] = text
                elif text in keys.keys():
                    key = keys[text]
                elif key != "":
                    page[section][key] = text
    
    return page