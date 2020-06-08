# NovelFacts 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A solution to enable users of news websites and open/closed social platforms to request fact-checks directly from their browser or mobile app. 

## Contents

1. [Short description](#short-description)
1. [Demo video](#demo-video)
1. [The architecture](#the-architecture)
1. [IBM Services Used](#ibm-services-used)
1. [Long description](#long-description)
1. [Project roadmap](#project-roadmap)
1. [Getting started](#getting-started)
1. [Live demo](#live-demo)
1. [Built with](#built-with)
1. [Authors](#authors)
1. [License](#license)
1. [Sources](#sources)

## Short description

### What's the problem?

The spread of deliberate misinformation and hoaxes through social media, primarily WhatsApp, has increased manifold during the coronavirus crisis. Rumours about the origin and transmission of the virus, number of affected people, areas of contamination, and treatments have gone viral. Distinguishing factual information from false reports is difficult, and very few mechanisms are available for fact-checking.

### How can technology help?

In age of social media we receive news through various sources such as Whatsapp,Facebook and Twitter.
Technology can be a boon to mankind if used properly, but it can also cause destruction.
With proper use of technology, we can help curb the spread of misinformation through the different channels, either through text or media.
By sourcing news data from trusted goverment sites, we can 
leverage latest machine learning techniques to verify the false information and help user identify if the news is fact or fake.

It's important to develop open source tools which will help to validate the information we receive to avoid unnecessary panic
and also guide us to proper channels in the times of crises,such as COVID-19 pandemic.

### The idea

We aim to develop a solution to enable users of news websites and open/closed social platforms to request fact-checks directly from their browser or mobile app. These fact-checks will be performed directly against multiple government-verified data sources, and falsified information could be readily identified.

With our product - NovelFacts, we are providing open source tools in two forms - Whatsapp ChatBot and Websites - which will enable users to validate information.

## Demo video

[![Watch the video](https://github.com/BhumikaE/Novel-Facts/blob/master/src/Docs/NovelFacts.jpeg)](https://www.youtube.com/watch?v=Geq8aDdXgFY&rel=0)

## The architecture

![Novel Facts/Fake News Detection](https://github.com/BhumikaE/Novel-Facts/blob/master/src/Docs/ArchitectureDiagram.png)

1. The user sends data (text/images/audio messages) for fact-checking via the Whatsapp chatbot or the browser.
2. Text similarity detection will be performed using BERT.
3. IBM Watson Speech to Text will be used for translating audio messages to text
4. Regional/foreign languages will be converted into English using Google Translate.
5. Image Processing techniques and open-cv will be used for Image Similarity Detection


## IBM Services Used

- [Watson Speech to Text](https://www.ibm.com/in-en/cloud/watson-speech-to-text)

  This service was used to translate the incoming messages from the users which were in audio format.
  We have currently added support for 'mpeg' format, and we will further extend it to include 'ogg'(Whatsapp voice notes         format)
  
## Long description

[More detail is available here](DESCRIPTION.md)

## Project roadmap

![Roadmap](https://github.com/BhumikaE/Novel-Facts/blob/master/src/Docs/roadmap.PNG)

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Have python3.7 installed on your system and run the following command -

```bash
pip install -r requirements.txt
```

### Installing
From the project directory run the following commands -

```bash
cd src
python bot.py
```

```bash
cd src
streamlit run app.py
```
## Live demo

To connect with our Whatsapp bot, please send a WhatsApp message to +1 415 523 8886 with the code: join when-mental.

We have currently hosted our UI locally (Could not deploy app on IBM cloud due to 256MB restriction on memory for the free VM)
We plant to deploy this app on IBM cloud in the future. To test the working of the UI for now please use the above installation step to host the UI locally when testing. Alternatively, we will keep adding the updated IPs in the comments.

## Built with

* [BERT](https://arxiv.org/abs/1810.04805) - State-of-the-Art Pre-training for Natural Language Processing
* [Watson Speech to Text](https://www.ibm.com/in-en/cloud/watson-speech-to-text) - Convert audio and voice into written text for quick understanding of content
* [OpenCV](https://opencv.org/) - Library of programming functions mainly aimed at real-time computer vision
* [Google Translate](https://translate.google.co.in/) - multilingual statistical and neural machine translation service developed by Google
* [Twilio](https://www.twilio.com/) - Twilio allows software developers to programmatically make and receive phone calls, send and receive text/whatsapp messages
* [Streamlit](https://www.streamlit.io/) - Open-source app framework to build visualizations using Python


## Authors

* **Bhumika Ekbote** 
* **Shilpa Redeej** 
* **Jaya Singh** 
* **Neha Awate** 
* **Preeti Bahuguna** 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details


## Sources

* [The CoronaVirusFacts/DatosCoronaVirus Alliance Database](https://www.poynter.org/ifcn-covid-19-misinformation/).
* [Content patterns in COVID-19 related digital misinformation in India](http://joyojeet.people.si.umich.edu/an-archive-of-covid-19-related-fake-news-in-india/).
