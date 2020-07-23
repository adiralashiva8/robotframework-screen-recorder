*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
This Test Should Pass
    Open Browser   https://www.google.com   chrome
    Sleep   4s
    Close Browser

This Test Should Pass Once Again
    Open Browser   https://www.gmail.com   chrome
    Sleep   4s
    Close Browser