# INTRODUCTION:
The leap year and time conversion utility is a simple python project designed to demonstrate decision making, functions, input validation, arithmetic calculations, and modular programming. The user enter a year, the program determines whether it is a leap year , and then converts the numbers of days in that year into hours, minutes, and seconds.
# OBJECTIVE :
1. check whether an entered year is a leap year.
2. determine whether the year contains 365 or 366 days.
3.  calculate total hours, minutes, and seconds.
4.  validate user input and handle invalid values.
5.  demonstrate [python functions, conditions, arithmetic operators, and modular design.
# FUNCTIONAL REQUIREMENTS :
The project contains these major modules:
module 1 - input & validations : accept the year and verifies that it is positive integer.
module 2 - leap-year checker : applies the standard leap-year rule: divisible by 400, or divisible by 4 but not by 100.
module 3 - time calculator & report : converts days into hours, minutes, and seconds and displays a formatted result.
# NON-FUNCTIONAL REQUIREMENTS :
1. usability : simple command line interaction.
2. performance : calculations complete immediately for normal input.
3. reliability : uses clear validation and deterministic calculations.
4. maintainability : functions are maintained by responsibility.
5. Error handling : non-integer and non-positive input are rejected with a useful message.
# STYSTEM ACHITECTURE :
Input → Validation → leap-year logic → days calculation → time conversion → result display.
the system uses a simple layered flow . No database is required because the utility calculates result from the current input and does not need persistent storage.
# FLOWCHART :
                                          start

                                            ↓
                                        input year
                                            ↓
                                   valid positive integer ?  → no → show error → input again
                                            ↓ yes
                                        leap year ? → yes → days = 366
                                                    → no → days = 365
                                            ↓
                                      hours = days * 24
                                     minutes = hours * 60
                                     seconds = minutes * 60
                                            ↓
                                      display report
                                            ↓
                                          Stop
# DATABASE :
Not applicable. The project is a calculation utility and does not require a database or persistent storage.
# DESIGN DECISIONS & RATIONALE :
The program is divided into functions so each function has one clear responsibility. The leap-rule is implemented directly using conditional logic. Time conversion uses fixed relationship: 1 day = 24 hours, 1 hour = 60 minutes, and 1 minute = 60 seconds.
# IMPLEMENTATION DETAILS :
The implementation uses python's input handling, integer conversion, if/else conditions, boolean return values, functions, arithmetic operators, and formatted output.
# TESTING APPROACH :
Test cases should include ordinary years, leap years, century years, and a year divisible by 400. Invalid inputs such as zero, negative values, and non-numeric text should also be tested.
# CHALLENGES FACED :
1. Applying the leap-year rule correctly for century years.
2. Handling invalid user input.
3. Keeping calculations modular and easy to understand.
4. Formatting the final output clearly.
# FUTURE ENHANCEMENTS :
1. Add a graphical user interface (GUI).
2. Add a date/day-of-week calculator.
3. allow repeated calculations without restarting.
4. Export results to a text or CSVreport.
5. Add automated unit tests.
# CONCLUSIONS :
The leap year & time conversion utility is a compact python project that solves a practical calculation problem while demonstrating core programming concepts. It can be expanded into a more complete date and time utility in future versions.                                          
