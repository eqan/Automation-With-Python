*** Settings ***
Documentation     Using variables for readability and flexibility.
Library           SeleniumLibrary

*** Variables ***
${I_FEEL_LUCKY_SEARCH_BUTTON}    css:.FPdoLc > center:nth-child(1) > input:nth-child(2)
${SEARCH_URL}     https://www.google.com/search?q=cute cat
${BROWSER}        Firefox

*** Tasks ***
Search using hard-coded search URL and term
    open browser      https://www.google.com/search?q=    Firefox

*** Tasks ***
Search using variables
    open browser      ${SEARCH_URL}  ${BROWSER} 

*** Tasks ***
Search using environment variables
    open browser      %{SEARCH_URL}  %{BROWSER}

*** Tasks ***
Search using local variables
    ${search_url}     Set Variable    https://duckduckgo.com/?q=Robocorp
    open browser    ${search_url}   ${BROWSER} 

*** Tasks ***
Click an element using a hard-to-understand locator
    Launch Browser
    Click Element     css:.FPdoLc > center:nth-child(1) > input:nth-child(2)

*** Tasks ***
Click an element using a well-named locator variable
    Launch Browser
    Click Element     ${I_FEEL_LUCKY_SEARCH_BUTTON}

*** Keywords ***
Launch Browser
    open browser    ${SEARCH_URL}    ${BROWSER}
    Maximize Browser Window
