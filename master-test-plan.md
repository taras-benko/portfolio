# Master Test Plan

## 1. Document Purpose
Master Test Plan for the practical tasks from the Embedded QA course. Presents an overview of the testing approach chosen during the course.

## 2. System Overview
- hardware: ESP32
- firmware:
    - Smart Gate project
    - Button Bouncing project
    - UART_CLI project
    - I2C project
    - Fault/Recovery project
    - Python automation project
    - IoT Network project
- interfaces:
    - UART
    - I2C
- external dependencies:
    VSCode
    Wokwi
- critical data / actuators
    - Project simulations from the "wokwi" folder

## 3. Quality Objectives
Product passed validation and verification. All requirement are met.

## 4. Scope
- Firmware
- Interfaces
- Protocols
- Functional scenarios
- Critical states

## 5. Out of Scope
- Hardware
- Design/UI
- Cloud storage

## 6. Assumptions / Constraints
All the testing is done via Wokwi simulation. 

## 7. Quality Risks

| Risk ID | Risk | Impact | Probability | Priority | Mitigation / Test |
|Risk-01|Telemetry lost after network failure|High|Low|Medium|Scenario A|
|Risk-02|Watchdog does not reset the system after freeze|High|Medium|High|WDT hang scenario|
|Risk-03|System does not recover after I2C failure|High|Medium|High|I2C fault injection|
|Risk-04|Acutator remains on after reset|High|Low|Medium|Relay + WDT scenario|
|Risk-05|Memory leak|High|High|Critical|Scenario D|

## 8. Test Levels
- interface / protocol
- system
- recovery / fault injection
- network

## 9. Test Types
- functional
- boundary / negative
- protocol
- reliability
- recovery
- regression
- network stress
- memory stability
- automation

## 10. Test Environment
| Environment | Purpose | Tools |
| Wokwi | Firmware/system simulation | ESP32 simulator |
| Logic analysis | Protocol evidence | PulseView / analyzer |
| Host automation | Regression | Python / Pytest |

## 11. Entry Criteria
- Firmware build available
- Requirements detarmined

## 12. Exit Criteria
- All requirements are tested
- All bugs are fixed

## 13. Regression Strategy
- Use automation as much as possible
- Cover manually critical cases if not alreadyu covered by automation

## 14. Evidence Strategy
Save logs, traces, screenshots, JSON reports, pytest output, metrics a record videos whenever possible/relevant. Create bug reports for found issues and save wokwi projects.

## 15. Defect Management
Severity, reproducibility, evidence, retest.

## 16. Residual Risks
The functionality of the system on real hardware still remains untested and can be a risk.

## 17. Release Recommendation
NO-GO due to a lot of Critical and Major bugs found.
