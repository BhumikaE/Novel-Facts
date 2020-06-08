from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from web_scraping import Web
from bert_models import Model
import emoji
import country_codes
import flag
from image_processing import ImageProcessing
import time
from googletrans import Translator
import re
from voice_chat import VoiceChat

app = Flask(__name__)


def get_key(val):
    for key, value in country_codes.ISO3166.items():
        if val == value:
            return key


def is_greeting(sentence):
    greeting_inputs = (
        "hello",
        "hi",
        "greetings",
        "sup",
        "what's up",
        "hey",
        "good morning",
    )

    for word in sentence.split():
        if word.lower() in greeting_inputs:
            return True


def format_response(row, match):
    beware = emoji.emojize(":warning: This news is fake")
    exclamation = emoji.emojize(
        ":exclamation_mark: Please check below information for details -"
    )

    sample_flag = ""

    if row["Country"].values[0].strip() is not "":
        country_code = get_key(row["Country"].values[0])
        if country_code is not None:
            sample_flag = flag.flag(country_code)

    match_percent = round((match * 100), 2)
    response = f"""{beware}

*[{match_percent}% Match]*: {row['FakeNews'].values[0]} 

{exclamation}

*Explanation*: {row['Explanation'].values[0].strip()}

{row['Url'].values[0]}

{sample_flag} {row['Country'].values[0]}
"""
    return response


def format_image_response(response):
    regex = (
        r"(?P<Claim>[A-Za-z].*)\n"
        r"(?P<Explanation>[A-Za-z ].*)\n"
        r"(?P<Url>.*)"
    )

    match = re.search(regex, response)

    beware = emoji.emojize(":warning: This claim associated with this image is fake")
    formatted_response = f'''{beware}

*Claim*: {match['Claim']} 

*Explanation*: {match['Explanation']}

{match['Url']}
'''
    return formatted_response


def translate_text(text, target="en"):
    translator = Translator()
    translated = translator.translate(text)
    return translated.text


def detect_text(text):
    translator = Translator()
    detected = translator.detect(text)
    return detected


@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if incoming_msg:

        if incoming_msg and is_greeting(incoming_msg):
            output = emoji.emojize(
                "Hello, welcome to our COVID-19 fact-checking bot. Please enter the message you want to verify."
            )
            msg.body(output)
            responded = True
        else:

            if detect_text(incoming_msg) == "en":
                print("en")
            else:
                translated_text = translate_text(incoming_msg)

            results = bert_model.is_fake_news(translated_text)
            row = test.get_full_news_data(results)
            match = results[0][1]

            if match > 0.6:
                formatted_message = format_response(row, match)
                msg.body(formatted_message)
                responded = True
            else:
                msg.body("No Match Found. Please try some other query")
                responded = True

    try:
        if request.values["NumMedia"] != "0":
            req = request.values
            print(request.values['MediaUrl0'])
            print(request.values['NumMedia'])

            if(request.values['MediaContentType0'] == 'audio/mpeg'):
                filename = request.values["MessageSid"] + ".mp3"
                filepath = "./Images"

                full_path = filepath + "/" + filename
                with open("{}/{}".format(filepath, filename), "wb") as f:
                    audio_url = request.values["MediaUrl0"]
                    f.write(requests.get(audio_url).content)

                text = voice_chat.translate_media_to_text(full_path)
                print(text)

            else:
                # Use the message SID as a filename.
                filename = request.values["MessageSid"] + ".png"
                filepath = "./Images"

                full_path = filepath + "/" + filename
                with open("{}/{}".format(filepath, filename), "wb") as f:
                    image_url = request.values["MediaUrl0"]
                    f.write(requests.get(image_url).content)

                start = time.time()  # What in other posts is described is
                temp = imageprocessing.is_fake_image(full_path)
                end = time.time()
                stopWatch(end - start)

                s = format_image_response(temp)
                print(s)
                msg.body(s)
                # msg.media()
                responded = True

    except:
        print("Tried to load image from UI, failed")

    if not responded:
        msg.body("Please try again with a different message")

    print(str(resp))

    return str(resp)


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


if __name__ == "__main__":
    test = Web()
    fake_news_data_set = test.get_saved_news_data()
    bert_model = Model()
    bert_model.create_corpus_embeddings(fake_news_data_set)

    imageprocessing = ImageProcessing()
    voice_chat = VoiceChat()
    app.run(debug=True)
