from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import requests
import urllib.request as ur
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import time


def stopWatch(value):
    """From seconds to Days;Hours:Minutes;Seconds"""

    valueD = ((value / 365) / 24) / 60
    Days = int(valueD)

    valueH = (valueD - Days) * 365
    Hours = int(valueH)

    valueM = (valueH - Hours) * 24
    Minutes = int(valueM)

    valueS = (valueM - Minutes) * 60
    Seconds = int(valueS)

    print(Days, ";", Hours, ":", Minutes, ";", Seconds)


class ImageProcessing:
    def __init__(self):
        # scraping the image_url and details
        self.url = "http://joyojeet.people.si.umich.edu/an-archive-of-covid-19-related-fake-news-in-india/"
        req = Request(self.url, headers={"User-Agent": "Mozilla/5.0"})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, "html.parser")
        news = soup.find_all("table", {"class": "c18"})
        claim = news[1].find_all("td", {"class": "c15"})
        fact = news[1].find_all("td", {"class": "c6"})

        images = soup.find_all("a", {"href": re.compile(".png")})
        self.img = []
        self.img_list = []
        for image in images:
            self.img.append(image["href"])
        self.len_dataSet = len(claim)

        for i in range(1, self.len_dataSet):
            string = claim[i].text + "\n" + fact[i].text + "\n" + self.img[i - 1]
            self.img_list.append(string)

        print("Data load complete")

    # print(img_list)

    # mean square error
    def mse(self, imageA, imageB):
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])
        return err

    def compare_images(self, imageA, imageB):
        m = self.mse(imageA, imageB)
        s = ssim(imageA, imageB)
        return m, s

    # converting image_url to image
    def url_to_image(self, url):
        resp = ur.urlopen(url)
        image_new = np.asarray(bytearray(resp.read()), dtype="uint8")
        image_new = cv2.imdecode(image_new, cv2.IMREAD_COLOR)
        return image_new

    def is_fake_image(self, filename):
        start_full = time.time()

        max_mse = None
        min_ssim = None
        index = None
        # loading the images
        # image from the url for loop
        for i in range(-1, self.len_dataSet):
            print(f"{i}")
            url = self.img[i]
            start_img = time.time()
            saved_img = self.url_to_image(url)
            end_img = time.time()
            print(stopWatch(end_img - start_img))
            # image from the user
            # filename="image16.png"
            contrast = cv2.imread(filename)

            # convert the images to grayscale
            original = cv2.cvtColor(saved_img, cv2.COLOR_BGR2GRAY)
            contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)

            # convert both of them into the same size
            dim = (original.shape[1], original.shape[0])
            resized = cv2.resize(contrast, dim)

            # comparing the image
            m, s = self.compare_images(original, resized)

            if max_mse is None and min_ssim is None and index is None:
                max_mse = m
                min_ssim = s
                index = i
            if max_mse > m or min_ssim < s:
                max_mse = m
                min_ssim = s
                index = i

            # print(compare_images(original, resized))

            if m >= 0 and m <= 0.2 or s >= 0.8 and s <= 1.2:
                print(self.img[index])
                print(self.img_list[index])
                print(f"({m},{s})")
                return self.img_list[i]

        return (
            "We could not find a match for this image. Please try with a different one"
        )
        end_time = time.time()
        print(stopWatch(end_time - start_full))
