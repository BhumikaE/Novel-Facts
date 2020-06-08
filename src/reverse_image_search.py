import argparse
import io
from bs4 import BeautifulSoup
from google.cloud import vision
from google.cloud.vision import types
from urllib.request import Request, urlopen


def annotate(path):
    """Returns web annotations given the path to an image."""
    client = vision.ImageAnnotatorClient()

    if path.startswith("http") or path.startswith("gs:"):
        image = types.Image()
        image.source.image_uri = path

    else:
        with io.open(path, "rb") as image_file:
            content = image_file.read()

        image = types.Image(content=content)

    web_detection = client.web_detection(image=image).web_detection

    return web_detection


def report(annotations):
    """Prints detected features in the provided web annotations."""
    if annotations.pages_with_matching_images:
        print(
            "\n{} Pages with matching images retrieved".format(
                len(annotations.pages_with_matching_images)
            )
        )

        for page in annotations.pages_with_matching_images:
            print("Url   : {}".format(page.url))
            # print(page)

    if annotations.full_matching_images:
        print("\n{} Full Matches found: ".format(len(annotations.full_matching_images)))

        for image in annotations.full_matching_images:
            print("Url  : {}".format(image.url))
            get_url_metadata(page.url)

    if annotations.partial_matching_images:
        print(
            "\n{} Partial Matches found: ".format(
                len(annotations.partial_matching_images)
            )
        )

        for image in annotations.partial_matching_images:
            print("Url  : {}".format(image.url))

    if annotations.web_entities:
        print("\n{} Web entities found: ".format(len(annotations.web_entities)))

        for entity in annotations.web_entities:
            print("Score      : {}".format(entity.score))
            print("Description: {}".format(entity.description))


def get_url_metadata(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, "html.parser")
    title = soup.title
    print(title)
    # print('Page number being scraped is:')

    pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    path_help = str(
        "The image to detect, can be web URI, "
        "Google Cloud Storage, or path to local file."
    )
    parser.add_argument("image_url", help=path_help)
    args = parser.parse_args()

    report(annotate(args.image_url))
