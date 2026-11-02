# Bug Report Log:
===============================================================================================================================

|Bug ID|Summary|Severity|Test Sheet|
-------------------------------------------------------------------------------------------------------------------------------
|M1-001|System is not transferred to OPEN state after LIMIT_OPEN is triggered|Critical|Smart Gate Test Sheet|
|M1-002|ledOpen is lit during the STOPPED state|Low|Smart Gate Test Sheet|
|M1-003|Timeout is absent during the OPENING state|High|Smart Gate Test Sheet|
|M1-004|Possible to switch between OPENING and CLOSING without stopping|Medium|Smart Gate Test Sheet|
|M1-005|The state can be switched from ERROR to STOPPED without resetting|Low|Smart Gate Test Sheet|
|M1-006|The state can be changed to STOPPED from CLOSED or OPEN|Low|Smart Gate Test Sheet|
|M1-007|The state can be changed to OPEN from almost any state|High|Smart Gate Test Sheet|
|M1-008|The state can be changed to CLOSE from almost any state|High|Smart Gate Test Sheet|
|M1-009|State is not set to ERROR after triggering LIMIT_OPEN and LIMIT_CLOSE at the same time|High|Smart Gate Test Sheet|
-------------------------------------------------------------------------------------------------------------------------------
|M2-001|Logical event is recorded during Noise Pulse|High|Button Bouncing Test Sheet|
-------------------------------------------------------------------------------------------------------------------------------
|M3-001|Error is not shown when using "set speed" command with 256 as the argument|Medium|UART_CLI Test Sheet|
|M3-002|Error is not shown when using th "set timeout" command with 0 as the argument|Medium|UART_CLI Test Sheet|
|M3-003|The "status" command is not case-sensitive|Low|UART_CLI Test Sheet|
|M3-004|Special characters are treated as valid input|Medium|UART_CLI Test Sheet|
|M3-005|Board is rebooted after CLI input limit is exceeded|High|UART_CLI Test Sheet|
|M3-006|Saved parameters are not kept after reset|High|UART_CLI Test Sheet|
|M3-007|Board resets when using an incomplete command in DIRTY state|High|UART_CLI Test Sheet|
-------------------------------------------------------------------------------------------------------------------------------
|M4-001|I2C connection is not recovered after FAULT|Critical|I2C Test Sheet|
-------------------------------------------------------------------------------------------------------------------------------
|M5-001|Deep Sleep ends after 0,5 seconds| High|Fault/Recovery Test Sheet|
|M5-002|No error is raised when the sensor is not connected|High|Fault/Recovery Test Sheet|
|M5-003|Relay remains on after watchdog reset|High|Fault/Recovery Test Sheet|
|M5-004|Mixed state after interrupt save|High|Fault/Recovery Test Sheet|
-------------------------------------------------------------------------------------------------------------------------------
|M6-001|Invalid JSON returned as response to “GET TEMP” command|High|Automation Test Sheet|
|M6-002|Invalid boundary settings configured for the “SET PWM” command|Medium|Automation Test Sheet|
|M6-003|Safe output state is not restored when using “RESET” after “SET LED ON”|High|Automation Test Sheet|
-------------------------------------------------------------------------------------------------------------------------------
|M7-001|Duplicates are sent during buffer flush when the connection is recovered|Medium|IoT Network Test Sheet|
|M7-002|Backoff interval does not increase after retries|High|IoT Network Test Sheet|
|M7-003|Memory leak occurs after heavy load|Critical|IoT Network Test Sheet|
|M7-004|Dropped messages are added to the buffer count in BACKOFF state|High|IoT Network Test Sheet|

# Critical Bugs:
==========================================================================================================================================================================
Bug ID          ||M1-001                                                                                                                                                  |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Summary         ||System is not transferred to OPEN state after LIMIT_OPEN is triggered                                                                                   |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Requirement     ||R6                                                                                                                                                      |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Precondition    ||State=OPENING                                                                                                                                           |     
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Description     ||System is not transferred to OPEN state after LIMIT_OPEN is triggered. Open relay remains ON. Multiple "OPEN LIMIT DETECTED" messages are sent to logs  |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Steps           ||1. Make sure the state is set to OPENING and the OPEN relay is active                                                                                   |
                ||2. Trigger LIMIT_OPEN                                                                                                                                   | 
                ||3. Pay attention to the OPEN relay and the logs                                                                                                         |     
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Expected        ||System is transferred to OPEN state                                                                                                                     | 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Actual          ||System state does not change after LIMIT_OPEN is triggered                                                                                              |     
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Severity        ||Critical                                                                                                                                                | 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Reproducibility ||5/5                                                                                                                                                     | 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Environment     ||Smart_Gate_BUGGY_VSCode_Wokwi                                                                                                                           | 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Evidence        ||  COMMAND: O                                                                                                                                            | 
                ||  STATE: STOPPED -> OPENING                                                                                                                             | 
                ||  OPEN LIMIT DETECTED                                                                                                                                   |
                ||  OPEN LIMIT DETECTED                                                                                                                                   | 
==========================================================================================================================================================================

==========================================================================================================================================================================
Bug ID          ||M4-001                                                                                                                                                  |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Summary         ||I2C connection is not recovered after FAULT                                                                                                             |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Requirement     ||R8                                                                                                                                                      |  
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Description     ||I2C connection is not recovered after FAULT. No retries are attempted. The system does not recover after the FAULT is gone.                             |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Steps           ||1. Reboot the board                                                                                                                                     |
                ||2. Wait a few seconds for transaction to pass                                                                                                           |
                ||3. Turn on FAULT                                                                                                                                        | 
                ||4. Turn off FAULT                                                                                                                                       |
                ||5. Wait 5 seconds                                                                                                                                       |
                ||6. Pay attention to the terminal                                                                                                                        |  
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Expected        ||Retries are sent, and the system recovers                                                                                                               | 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Actual          ||I2C connection does not recover after FAULT                                                                                                             |     
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Severity        ||Critical                                                                                                                                                | 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Reproducibility ||5/5                                                                                                                                                     | 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Environment     ||Wokwi_I2C_BUGGY                                                                                                                                         | 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Evidence        || <Screenshots>                                                                                                                                          | 
==========================================================================================================================================================================

==========================================================================================================================================================================
Bug ID          ||M7-003                                                                                                                                                  |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Summary         ||Memory leak occurs after heavy load                                                                                                                     |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Requirement     ||R7                                                                                                                                                      |   
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Description     ||A significant memory leak occurs after heavy load. About 8000 bytes are lost every 100 messages.                                                        |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Steps           ||1. "RESET STATS"                                                                                                                                        |
                ||2. Send "STRESS 100" 10 times                                                                                                                           |
                ||3. "STATUS"                                                                                                                                             |
                ||4. Pay attention to the free heap in the terminal                                                                                                       |     
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Expected        ||No steady decrease in free heap, no matter how many messages are sent                                                                                   | 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Actual          ||Memory leak occurs after heavy load                                                                                                                     |     
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Severity        ||Critical                                                                                                                                                | 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Reproducibility ||5/5                                                                                                                                                     | 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Environment     ||Wokwi_IoT_Network_Homework_Buggy                                                                                                                        | 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Evidence        ||  Start: {"net":"CONNECTED","broker":true,"buffer":0,"capacity":8,"sent":0,"dropped":0,"duplicates":0,"reconnect_attempts":0,"heap":350868}             |
                ||  Please refer to the memory stability log and the graph below.                                                                                         |
                ||  <graph>                                                                                                                                               |
                ||  End:                                                                                                                                                  |
                ||  {"net":"CONNECTED","broker":true,"buffer":0,"capacity":8,"sent":1000,"dropped":0,"duplicates":0,"reconnect_attempts":0,"heap":270600}                 |
==========================================================================================================================================================================