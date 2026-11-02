# Project Goals
Conduct Black Box testing on a number of projects that utilize Wokwi simulations as primary testing environment.

# System under test
    - Smart Gate project
    - Button Bouncing project
    - UART_CLI project
    - I2C project
    - Fault/Recovery project
    - Python automation project
    - IoT Network project

# Test strategy
Inputs:
    - sensors
    - CLI
    - Network
Outputs:
    - relay
    - MQTT
    - Logs
Interfaces:
    - UART
    - I2C
Critical Functions:
    - Controls
    - Recovery
    - Data storage
    - Reconnecting

# Environment & tools
- Wokwi
- VSCode
Projects:
    - Smart_Gate_BUGGY_VSCode_Wokwi
    - Button_Bounce_Buggy
    - Wokwi_UART_CLI_Homework_Buggy
    - Wokwi_I2C_BUGGY
    - Wokwi_States_BUGGY
    - Wokwi_Pytest_Homework_Buggy
    - Wokwi_IoT_Network_Homework_Buggy

# Bugs/findings
|M1-001|System is not transferred to OPEN state after LIMIT_OPEN is triggered|Critical|Smart Gate Test Sheet|
|M4-001|I2C connection is not recovered after FAULT|Critical|I2C Test Sheet|
|M7-003|Memory leak occurs after heavy load|Critical|IoT Network Test Sheet|

# Decisions made
NO-GO until critical and high severity bugs are fixed.