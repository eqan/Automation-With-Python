*** Settings ***
Documentation  Just medddling with some things mostly different variables

*** Variables ***
${STRING}           cute cat
${INT_AS_STRING}    1
${INT_AS_INT}       ${1}
${FLOAT}            ${3.14}
@{LIST}             one    two    three
&{DICTIONARY}       string=cat    int=${1}    list=@{LIST}
${ENVIRONMENT}      %{PATH}

*** Tasks ***
Log Variables
   Log Many
    ...    ${STRING} 
    ...    ${INT_AS_STRING}
    ...    ${INT_AS_INT}
    ...    ${FLOAT}
    ...    ${LIST}
    ...    ${LIST}[0]
    ...    ${LIST}[1:]
    ...    ${DICTIONARY}
    ...    ${DICTIONARY}[string]
    ...    ${DICTIONARY.int}
    ...    ${DICTIONARY}[list][0]
    ...    ${ENVIRONMENT}
