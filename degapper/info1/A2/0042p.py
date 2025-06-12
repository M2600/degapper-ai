langs = ["EN", "GE", "JP"]
with open("sample.txt") as f:
    text = f.read()
    for la in langs:
        print(la, text.count(la))
    