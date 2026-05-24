with open("movies.json", "rb") as f:
    data = f.read()

with open("movies_utf8.json", "wb") as f:
    f.write(data.decode("utf-16").encode("utf-8"))