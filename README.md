# Automation_DealsDray
# Deals Dray Automation Testing

- This repository contains automation testing scripts for Deals Drat, utilizing the Behave framework for both UI and functional testing. The purpose of these tests is to ensure the accurate implementation of desired behaviors and to enhance collaboration among team members.

## Prerequisites

- Before running the automation tests, ensure you have the following dependencies installed:
  - *Python*: Ensure you have the latest version of Python installed.
    - bash
      # Install Python via the official website or package manager
      
  - *Behave*: Behave simplifies automation by translating human-readable specifications into executable tests.
    - bash
      pip install behave
      
  - *Selenium*: Selenium facilitates automation testing by enabling interactions with web browsers.
    - bash
      pip install selenium
      
  - *Requests*: The requests module is used for making HTTP requests, facilitating tasks like API testing and web scraping.
    - bash
      pip install requests
      

## Running UI Tests

- To run the UI tests, follow these steps:
  1. Navigate to the project directory.
  2. Execute the following command:
     - bash
       behave .\features\ui_testing\
  3. This command will execute the UI tests specified in the ui_testing directory.

## Running Functional Tests

- To run the functional tests, follow these steps:
  1. Navigate to the project directory.
  2. Execute the following command:
     - bash
       behave .\features\functional_testing\
  3. This command will execute the functional tests specified in the functional_testing directory.
