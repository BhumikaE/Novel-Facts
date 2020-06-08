# Fact-Check Bot

[![License](https://img.shields.io/badge/License-Apache2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) [![Slack](https://img.shields.io/badge/Join-Slack-blue)](https://callforcode.org/slack) [![Website](https://img.shields.io/badge/View-Website-blue)](https://code-and-response.github.io/Project-Sample/)

A solution to enable users of news websites and open/closed social platforms to request fact-checks directly from their browser or mobile app. 

## Contents

1. [Short description](#short-description)
1. [Demo video](#demo-video)
1. [The architecture](#the-architecture)
1. [Long description](#long-description)
1. [Project roadmap](#project-roadmap)
1. [Getting started](#getting-started)
1. [Running the tests](#running-the-tests)
1. [Live demo](#live-demo)
1. [Built with](#built-with)
1. [Contributing](#contributing)
1. [Versioning](#versioning)
1. [Authors](#authors)
1. [License](#license)
1. [Acknowledgments](#acknowledgments)

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

[![Watch the video](https://github.com/BhumikaE/Fact-Check-Bot/blob/master/src/Docs/NovelFacts.jpeg)](https://www.youtube.com/watch?v=Geq8aDdXgFY&rel=0)

## The architecture

![Novel Facts/Fake News Detection](https://github.com/BhumikaE/Fact-Check-Bot/blob/master/src/Docs/ArchitectureDiagram.png)

1. The user sends data (text/images/audio messages) for fact-checking via the Whatsapp chatbot or the browser.
2. Text similarity detection will be performed using BERT.
3. IBM Watson Speech to Text will be used for translating audio messages to text
4. Regional/foreign languages will be converted into English using Google Translate.
5. Image Processing techniques and open-cv will be used for Image Similarity Detection

## Long description

[More detail is available here](DESCRIPTION.md)

## Project roadmap

![Roadmap](https://github.com/BhumikaE/Fact-Check-Bot/blob/master/src/Docs/roadmap.PNG)

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```bash
dnf install wget
wget http://www.example.com/install.sh
bash install.sh
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be, for example

```bash
export TOKEN="fffd0923aa667c617a62f5A_fake_token754a2ad06cc9903543f1e85"
export EMAIL="jane@example.com"
dnf install npm
node samplefile.js
Server running at http://127.0.0.1:3000/
```

And repeat

```bash
curl localhost:3000
Thanks for looking at Code-and-Response!
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why, if you were using something like `mocha` for instnance

```bash
npm install mocha --save-dev
vi test/test.js
./node_modules/mocha/bin/mocha
```

### And coding style tests

Explain what these tests test and why, if you chose `eslint` for example

```bash
npm install eslint --save-dev
npx eslint --init
npx eslint sample-file.js
```

## Live demo

To connect with our Whatsapp bot, please send a WhatsApp message to +1 415 523 8886 with the code: join when-mental.

You can find a running system to test at [callforcode.mybluemix.net](http://callforcode.mybluemix.net/)

## Built with

* [IBM Cloudant](https://cloud.ibm.com/catalog?search=cloudant#search_results) - The NoSQL database used
* [IBM Cloud Functions](https://cloud.ibm.com/catalog?search=cloud%20functions#search_results) - The compute platform for handing logic
* [IBM API Connect](https://cloud.ibm.com/catalog?search=api%20connect#search_results) - The web framework used
* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds


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