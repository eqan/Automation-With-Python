*** Settings ***
Documentation     Assigning variables.
Library           Collections

*** Keywords ***
What Does The Cat Say
    [Return]    Meow!

*** Tasks ***
Assign variables
    ${string}    Set Variable    Hello, world!    # ${string} = Hello, world!
    @{list}    Create List    a    b    c    # @{list} = [ a | b | c ]
    &{dict}    Create Dictionary    key1=val1    key2=val2    # &{dict} = { key1=val1 | key2=val2 }
    ${a}    ${b}    ${c}    Create List    a    b    c    # ${a} = a, ${b} = b, ${c} = c
    ${cat_says}    What Does The Cat Say    # ${cat_says} = Meow!
    ${evaluate}    Evaluate    datetime.date.today()    # ${evaluate} = 2020-09-08
    ${inline_evaluation}
    ...    Set Variable
    ...    ${{datetime.date.today() + datetime.timedelta(1)}}    # ${inline_evaluation} = 2020-09-09
