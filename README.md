# mis203-basic-programming

**Name**: Fatıma Nur Yazıcı
**Student Number**: 2404109026
**Department**: Management Information Systems
**Course Name**: MIS203 Basic Programming

## WEEK01
# Development Notes

**AI Tool Used**: ChatGPT

**Prompt Used**: Help me create a simple Python student profile program using user input.

**What did you change?**
I reviewed the code, adjusted the wording, and made sure I understood how each part works.

## WEEK02
**AI Tool Used:** ChatGPT
**Prompt Used:** How can I calculate the average in Python? Can you show me a simple code example?
**What did you change?**
Actually I asked only average part because i forgetten how calculate average in Python. The most part of code i wrote myself.

**What does break do in your program?**
Break stops the loop when the user enters q.

**Explain Code**
The program asks for student names and scores. It gives a letter grade, counts the students, calculates the average score, and stops when the user enters q.



## WEEK03

**- AI Tool Used: ChatGPT**

**- Prompt Used:**
How can I write a simple cinema ticket program with percentage discounts?

**- What did you change?**
I changed the code according to the values and rules given in the homework. I also adjusted the age limits, ticket prices and discount percentages.

**- Tests:**
Age: 67, weekend, no -> 125.00 TRY (Senior)

Age: 11, weekend, yes -> 150.00 TRY (Child)

Age: 24, weekend, yes -> 175.00 TRY (Student)

**-Why does the order of the rules matter?:**

This code is important because it helped me understand how to use conditions, loops and user inputs together. It also showed me how a program can make different decisions according to the information entered by the user.


If we enter a 10-year-old student, the program gives the Child discount, not the Student discount.
This is because the Child rule comes before the Student rule.
For a weekday ticket:
200 TRY × 60% = 120 TRY
So the result will be:
120.00 TRY (Child)




## WEEK04
**- AI Tool Used: ChatGPT**

**- Prompt Used:**
What is a library in Python?
How can I import a library?
What do random and time do?
How does random.shuffle() work?
How can I make my program wait for one second?
**- What did you change?**
 changed one question in the quiz to a Python question. 
**Explain Code**
This code is a simple quiz game with 5 questions.
First, I imported two libraries, random and time. The random.shuffle() function changes the order of the questions, and time.sleep(1) makes the program wait for one second.
I used a list to store the questions and answers. The for loop asks each question, and input() gets the user's answer.
I used if and else to check if the answer is correct. If the answer is correct, the score increases by 1.
I also used .strip().lower() to remove extra spaces and make the answers lowercase.
At the end, the program shows the total score and uses if, elif, and else to display a message based on the result.
