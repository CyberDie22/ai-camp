#!/usr/bin/python3
import sys, os, json
from serpapi import GoogleSearch
import requests

def get_google_images(query, page):
    params = {
        "api_key": "f0923f75eb336758c72dc0205648c08ca0d0a3fddcc05eeb014ff29a9368f911",
        "engine": "google",
        "q": f"{str(query)}",
        "tbm": "isch",
        "safe": "active",
        "ijn": int(page)
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    print(json.dumps(results["images_results"], indent=2, ensure_ascii=False))
    
    if not os.path.exists(f"./images/{query}-{page}"):
        os.makedirs(f"./images/{query}-{page}")

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36"
    }

    for index, image in enumerate(results["images_results"]):
        try:
            print(f"Downloading {index} image...")

            filepath = os.path.join(f"./images/{query}-{page}", params["q"] + str(index) + ".jpg")

            response = requests.get(image['original'], headers=headers).content
            with open(filepath, "wb") as f:
                f.write(response)

        except Exception as e:
            print(e)
            print(f"Error downloading {index} image. Error = ", e)

get_google_images(sys.argv[1], sys.argv[2])

# vim:tabstop=4
# vim:shiftwidth=4
# vim:expandtab
