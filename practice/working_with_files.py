import io
import json

# file = open('./requirements.txt', 'rb')  # not recommend

with open('./requirements.txt', 'rb') as req:
    res = req.read()
    print(res)

with open('./to_write.txt', 'wb') as writer:
    stream = io.BytesIO(res)
    # io.TextIOBase()
    # io.FileIO()
    writer.write(stream.read())

data = {
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}


DATA_PATH = './data.json'
with open(DATA_PATH, 'w') as writer:
    writer.write(json.dumps(data))


with open(DATA_PATH, 'r') as req:
    res = json.loads(req.read())
    print(res)


