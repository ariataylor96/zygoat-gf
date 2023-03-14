import os
from loguru import logger as log
import requests

from urllib.parse import urljoin

_base_url = "https://www.toptal.com/developers/gitignore/api/"
_queries = [
    "python",
    "node",
    ("nextjs", "frontend"),
    ("django", "backend"),
]
_file_name = ".gitignore"


def inject_gitignores():
    for language in _queries:
        base_dir = "."

        if type(language) in [tuple, list]:
            language, base_dir = language

        url = urljoin(_base_url, language)
        response = requests.get(url)
        file_name = os.path.join(base_dir, _file_name)

        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        if not response.ok:
            log.warning(f"Could not find gitignore for {language}, skipping")
            continue

        with open(file_name, "a") as gitignore:
            log.info(f"Writing gitignore for {language}")
            gitignore.write(response.text + "\n")
