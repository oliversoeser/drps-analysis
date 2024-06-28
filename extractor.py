from bs4 import BeautifulSoup

def extract(html: str):
    f = open("keys.txt", "r")
    keys_text = f.read()
    f.close()

    keys_list = [line.split(",") for line in keys_text.split("\n")]
    keys = {key[0]: key[1] for key in keys_list}

    html = BeautifulSoup(html, features="lxml")

    page = {}

    html = html.find_all("table")[2]

    page["title"] = html.find("h1").decode_contents()

    for table in html.find_all("table"):
        caption = table.find("caption")
        if caption != None:
            title = caption.text
            if title in keys.keys():
                section = keys[title]
                page[section] = {}
                
                for row in table.find_all("tr"):
                    key = ""
                    for data in row.find_all("td"):
                        if data.text in keys.keys():
                            key = keys[data.text]
                        if key != "":
                            text = data.text
                            text = "\n".join([line.strip() for line in text.split("\n")])
                            text = "\n".join([line for line in text.split("\n") if line.strip() != ""])
                            page[section][key] = text

    return page