*** Settings ***
Documentation  Experimenting with while loop
Library  String

*** Keywords ***
Testing
    FOR    ${i}    IN RANGE    10
    	Log  ${i}
    END
    Log    Exited the loop.

*** Tasks  ***
Something
    Testing

