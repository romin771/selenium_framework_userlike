# Selenium and Pytest Test Automation Framework

## Table of Contents

- [Introduction](#Introduction)
- [Project Structure](#project-structure)
- [Base Folder](#base-folder)
- [Page Objects](#page-objects)
- [Tests](#tests)
- [Project Purpose](#project-purpose)
- [How to Run](#how-to-run)
- [Future Improvements](#future-improvements)

## Introduction

Hey there! Welcome to my Selenium and Pytest-based Test Automation Framework. This is my playground where I'm showing off my skills in building automation stuff using Python.

Think of it like a cool recipe I've whipped up. It's all about creating a special kind of test automation framework, and I'm using a pattern called the Page Object Model (POM) to make it organized.

But here's the twist - I'm not keeping it all to myself. I'm going to keep improving it so that anyone else can use it and have fun while automating things. Let's learn and laugh together on this automation adventure! 😄🚀
## Project Folder

The framework follows a structured organization of directories and files, promoting modularity, reusability, and maintainability.
## Base Folder

The `base` folder contains two essential files:

- `basepage.py`: This file houses methods that are common to all pages throughout the application, promoting code reuse.

- `selenium_driver.py`: This file wraps Selenium WebDriver methods into custom methods for ease of use within the framework. Some of the functions include:
  - `getTitle`
  - `getCurrentUrl`
  - `getByType`
  - `getElement`
  - `elementClick`
  - `sendKeys`
  - `isElementPresent`
  - `isElementDisplayed`

## Page Objects

The `pages` directory is organized into subdirectories, such as `dashboard` and `home`. These contain Page Object classes:

- `website_widget_page.py` and `login_page.py`: These Page Object classes encapsulate page-related details, such as locators and actions on elements. This encapsulation shields tests from UI structure changes.

## Tests

The `tests` directory is organized into subdirectories, including `dashboard` and `home`. It contains test scripts:

- `test_website_widget.py` and `test_login.py`: These test scripts interact with the Page Object classes, promoting high-level abstractions of the page's functionality and maintaining separation of concerns.

- `conftest.py`: This file contains fixtures and configurations used by the test scripts.

## Project Purpose

The primary objective of this project is to demonstrate the structure of an automation framework using the Page Object Model (POM) design pattern. The framework emphasizes:

- Modularity: Each page/component is represented by a separate Page Object class, making it easy to maintain and update specific parts of the application without affecting others.

- Reusability: Common code and methods are encapsulated within base classes and utility classes.

- Error Handling: Effective error handling with clear error messages and robust mechanisms.

## How to Run

To run the project, ensure you have Python and Pytest installed on your machine. You can run tests in Firefox or Chrome using the following commands:

- To run in Firefox:

  pytest --browser firefox

- To run in Chrome:

  pytest --browser chrome


## Future Improvements

This project is a work in progress and will continue to evolve. Future enhancements may include adding more test cases, refining existing test scripts, and improving the overall framework architecture.

Enjoy exploring and learning from this example test automation framework! If you have any questions or suggestions, feel free to reach out.



