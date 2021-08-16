*** Settings ***
Documentation     An example about for loops.

*** Variables ***
@{ROBOTS}        Bender    Johnny5    Terminator    Robocop

*** Tasks ***
Loop Over A List Of Items And Log Each Of Them
    FOR    ${robot}    IN    @{ROBOTS}
        Log    ${robot}
    END

Execute a for loop only three times
    FOR    ${robot}    IN    @{ROBOTS}
        Continue For Loop If    $robot == 'Terminator'
        Log    ${robot}
    END

Break out of the for loop on condition
    FOR    ${robot}    IN    @{ROBOTS}
        Exit For Loop If    $robot == 'Johnny5'
        Log    ${robot}
    END

Handle Table
    [Arguments]    @{table}
    FOR    ${row}    IN    @{table}
        FOR    ${cell}    IN    @{row}
            Handle Cell    ${cell}
        END
    END
