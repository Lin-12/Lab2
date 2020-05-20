## Computer Process Organization
### Lab2

#### Title:
  Computational Process Organization Lab2,variant 6

#### List of group members:
  - Name:Huang Yanlin,  student number:192050222 
  - Name:Lin ningning,  student number:192050192

#### Laboratory work number:
   Lab2 variant 6
#### Description:
   variant 6: Regular expression

#### Synopsis:  
* Support special characters: \, ^, ., $, *, +, [ ], [^ ], { }.  
* Support functions: match, sub.
* Visualization as a finite state machine (state diagram or table).    

#### contribution
* contribution summary for each group member (should be checkable by git log and git blame);
   - r_e.py & regex_test:Lin ningning
   - shunting_yard & thompsons:Huang Yanlin

#### Explanation：  
 * shunting_yard.py  
 Uses Shunting Yard Algorithm to convert infix expression to postfix expression.

* thompsons.py  
Transform postfix expression into NFA.

* regular_expression.py  
Takes in a regular expression postfix notation, a string and a boolean for case insensitivity (default is false).  
If the regular expression have no '.' operator, will add the operator into it ( like "abcd" become "a.b.c.d").  
Matching the regular expression and the string (both case sensitive and insensitive).

* regex_test.py  
The unit testing script of the program.

#### Work demonstration 
* (how to use developed software, how to test it), should be repeatable by an instructor by given command-line examples:  
  - We write all files on Pycharm.
  - Use terminal to test the code. like 'python regex_test.py -v'.

#### Conclusion:  
  * We implement simple library for RE and demonstrate how it works.
  * Convert string from infix expression to suffix expression, and use regular expression to operate string
