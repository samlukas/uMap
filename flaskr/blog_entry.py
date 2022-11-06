import json


def create_blog_entry(name: str, title: str, text: str, date: str, latitude: float, longitude: float, file_path: str) -> str:
    """Returns a JSON Document String for a blog entry with the given parameters
    """

    entry = {
        "name": name,
        "title": title,
        "text": text,
        "date": date,
        "latitude": latitude,
        "longitutde": longitude,
        "file_path": file_path  # for images
    }

    return json.dumps(entry)
