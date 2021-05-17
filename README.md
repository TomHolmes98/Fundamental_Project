# Dream Team


## Contents
* [Introduction](#introduction)
    * [Objective](#objective)
    * [Proposal](#proposal)
* [Architecture](#architecture)
    * [Entity-Relationship Diagram(ERD)](#entity-relationship-diagram(erd))
    * [Risk Assessment](#risk-assessment)
    * [Trello](#trello)
    * [Continuous Integration](#continuous-integration)
* [Development](#development)
    * [Testing](#testing)
        * [Unit Testing](#unit-testing)
* [Working Product](#working-product)

* [Footer](#footer)

## Introduction

### Objective

The objective for this project was to produce a CRUD application (Create, Read, Update and Delete) using tools that have been taught to us throughout this course;
* Use the AGILE planning method.
* Create a database containing a 1 to many relationship.
* Use Python te create a fuctional CRUD application.
* Integrate the use of both a VCS and a CI server.
* Provide coverage for the app using testing.
* Deploy the app using a cloud-based VM, GCP in this case.

### Proposal

In order to meet the requirements set out within the objectives and the brief, I decided to begin designing an app where you can enter a team name and list of players in order to form your dream football team. In creating a team you will be entering:
* A team name.
* The team league.
* A player name.
* The player nationality.
* The player position.

This proposal showed potential to be able to execute the proposed CRUD functionality and therefore I decided to carry out the application idea.

## Architecture

### Entity-Relationship Diagram(ERD)

The ERD that I created for my project shows the relationship between both teams and players and shows how a team can have many diferent players and for this to work in terms of using a primary key and a foreign key, the foreign key must be stored within the players table.

[![Image from Gyazo](https://i.gyazo.com/ef515549cd5f4b0ffa164bce5196e63f.png)](https://gyazo.com/ef515549cd5f4b0ffa164bce5196e63f)

### Risk Assessment

Below are 2 versions of my risk assessment, the first one being an initial risk assessment and the 2nd being a follow up in which the impact levels and likeliness have been edited to show the impact having a risk assessment has made in ensuring that I am cautious of any potential risks.

[![Image from Gyazo](https://i.gyazo.com/a8a85131aa668b1dc3170ba66db138b0.png)](https://gyazo.com/a8a85131aa668b1dc3170ba66db138b0)

[![Image from Gyazo](https://i.gyazo.com/976cc7a085e013f6dc1093f93d8eddf9.png)](https://gyazo.com/976cc7a085e013f6dc1093f93d8eddf9)

### Trello

I used Trello in order to track my project, in terms of using the AGILE planning method, Trello was very useful in keeping me on schedule and it also allowed me to refine my objectives over time and branch them out into more detailed sub classes within the Trello. Using Trello to track my project allowed me to identify what the project required each step of the way.

[![Image from Gyazo](https://i.gyazo.com/ecc276c01173ef36e81b431bb4d3930d.png)](https://gyazo.com/ecc276c01173ef36e81b431bb4d3930d)

### Continuous Integration

Jenkins is used within my project in order for continuous integration to occur. A webhook has been set up which means that any changes made within the GitHub repository are then mirrored in the Jenkins program. Jenkins runs automated tests within the program and has been set up in order to proivde coverage reports of the application.

Below are the instructions I have given to Jenkins in order to create a virtual environment, followed by installing the needed requirements and then Jenkins is issued with instructions to both unit test and integration test and then provide a coverage report as aforementioned.

```

#!/bin/bash

sudo apt update 
sudo apt install python3 python3-pytest python3-pip python3-venv chromium-browser wget unzip -y
wget https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip -d /usr/bin
rm chromedriver_linux64.zip

python3 -m venv venv

source venv/bin/activate
pip install pytest-cov
pip3 install -r requirements.txt
pip3 install -r requirements2.txt
export DATABASE_URI
export SECRET

python3 -m pytest --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html

```


## Development

### Testing

#### Unit Testing

Unit testing was carried out to ensure that the routes contained within the application were efficiently practicing the CRUD functionality and specifically that, under different circumstances, the routes would not fail. Examples of the unit testing that I carried out within this project are shown below.

#### Integration Testing

Integration testing was also carried out within this project, this testing focused upon testing the functionality of the entire application build, meaning the database, frontend and backend. Currently my integration tests cover the homepage and what should show up there, I also wrote tests querying the add-player section of my app and also the add-team section of my app.

[![Image from Gyazo](https://i.gyazo.com/f2aca0c02274095da9b4780d9a32fbe3.png)](https://gyazo.com/f2aca0c02274095da9b4780d9a32fbe3)

[![Image from Gyazo](https://i.gyazo.com/460dd31e3a896590e8b39b2d2e4b4be2.png)](https://gyazo.com/460dd31e3a896590e8b39b2d2e4b4be2)

## Working Product

[![Image from Gyazo](https://i.gyazo.com/24e50119722435e6a036da520dca8312.png)](https://gyazo.com/24e50119722435e6a036da520dca8312)

[![Image from Gyazo](https://i.gyazo.com/abb5b36bf16c8396106cb170b203493d.png)](https://gyazo.com/abb5b36bf16c8396106cb170b203493d)

[![Image from Gyazo](https://i.gyazo.com/8efe87d0e2406e533a309da7ae89d6a0.png)](https://gyazo.com/8efe87d0e2406e533a309da7ae89d6a0)












