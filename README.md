# Week 3 Assignment: Conditions and Loops

- grade_reporter.py: Evaluates a list of scores against grading criteria, prints each student's grade, and calculates overall pass/fail counts and the class average.
- bug_hunt.py: Fixes syntax, logical range issues, and type concatenation errors in a script designed to sum numbers from 1 to 5.

The hardest bug to find in Part B was the logical loop condition (`count < 5` instead of `count <= 5`), because it produced no error message at all; the script ran successfully but incorrectly printed a sum of 10 instead of 15. I knew something was wrong when the output didn't match the expected total of 15 stated in the prompt, prompting me to trace the loop iterations.
