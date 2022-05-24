# Features

Feature files Cheat sheet:

Scenario: Name that scenario <br>
- Given This is the past tense and everything that happened before <br>
- When This is the present tense and what is going to happen right now <br>
- Then What should happen in the future based on the past and present actions <br>

---
Scenario: Turn calculator on <br>
- When I turn on my calculator  <br>
- Then it should initialise to 0  <br>

---
Scenario Outline: Enter and display digits  <br>
- Given I have an initialised the calculator  <br>
- When I enter the the following characters "a" and "b"   <br>
- Then they should display "concatinated_results" <br>
Examples: <br>
  - |a  |b  |concatinated_results|  <br>
  - |1  |1  |11                  |  <br>
  - |2  |3  |23                  |  <br>
  - |a  |1  |Error               |  <br>

---
Scenario Outline: Can add two numbers together <br>
- Given I have intialised calculator  <br>
- When I add the two numbers "a" and "b" together  <br>
- Then The correct "addition_result" should be shown  <br>
Examples:  <br>
   - |a  |b  |addition_result|  <br>
   - |1  |1  |2              |  <br>
   - |0.2|0.3|0.5            |  <br>
   - |-2 |-3 |-5             |  <br>
   - |1  |FF | Error         | ** Unless your calculator takes in hexadecimal numbers ;)  <br>
  

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
