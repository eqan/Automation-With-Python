# Just for practicing different concepts in RobotFrameWork

*** Settings ***
Documentation       Robot Framework 4 syntax recipes cheat sheet robot.
...                 Demonstrates Robot Framework syntax in a concise format.
Library             SeleniumLibrary
Resource            robot_test_case.robot

*** Variables ***
${URL}  www.google.com
@{LIST}            this     list     is      quite    long     and
...                items in it can also be long


*** Tasks ***
# Empty parameters
Do something  ${EMPTY}
Do something  \

Example
    Do X    first argument    second argument    third argument
    ...    fourth argument    fifth argument    sixth argument
    ${var} =    Get X
    ...    first argument passed to this keyword is pretty long
    ...    second argument passed to this keyword is long too
