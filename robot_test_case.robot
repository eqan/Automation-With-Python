*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${HOMEPAGE}       http://google.com
${BROWSER}        Firefox

*** Test Cases ***
Sample Test
    Launch Browser
    Check Title
    [Teardown]    Close Browser


*** Keywords ***
Launch Browser
    open browser    ${HOMEPAGE}    ${BROWSER}
    Maximize Browser Window

Check Title
    Title Should Be    Google
