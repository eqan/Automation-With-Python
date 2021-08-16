# Putting comments here for the sake of testing 
*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${HOMEPAGE}       https://robotsparebinindustries.com/
${BROWSER}        Firefox

*** Keywords ***
Launch Browser
    open browser    ${HOMEPAGE}    ${BROWSER}
    Maximize Browser Window

Log In
    Input Text    username    maria
    Input Password    password    thoushallnotpass
    Submit Form

*** Tasks ***
Launch browser and log in
    Launch Browser
    Log In
