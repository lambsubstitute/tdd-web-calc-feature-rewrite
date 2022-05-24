# Features

Feature files Cheat sheet:
Scenario: Name that scenario
  Given This is the past tense and everything that happened before
  When This is the present tense and what is going to happen right now
  Then What should happen in the future based on the past and present actions

---
Scenario: Turn calculator on
  When I turn on my calculator  
  Then it should initialise to 0

---
Scenario Outline: Enter and display digits
  Given I have an initialised the calculator  
  When I enter the the following characters "a" and "b"  
  Then they should display "concatinated_results" 
Examples:
  |a  |b  |concatinated_results|
  |1  |1  |11                  |
  |2  |3  |23                  |
  |a  |1  |Error               |

---
Scenario Outline: Can add two numbers together
  Given I have intialised calculator  
  When I add the two numbers "a" and "b" together
  Then The correct "addition_result" should be shown
Examples:
  |a  |b  |addition_result|
  |1  |1  |2              |
  |0.2|0.3|0.5            |
  |-2 |-3 |-5             |
  |1  |FF | Error         | ** Unless your calculator takes in hexadecimal numbers ;)
  

---
Given I have an intialised calculator  
When I enter 2 numbers with a minus between them  
Then I want these number to be subtracted  

---
Given I have an intialised calculator  
When I enter 2 numbers with a times between them  
Then I want these number to be multiplied  

---
Given I have an intialised calculator  
When I enter 2 numbers with a forward slash between them  
Then I want these number to be divided  
