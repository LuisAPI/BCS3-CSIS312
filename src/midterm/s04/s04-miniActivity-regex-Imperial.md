Luis Anton P. Imperial  
BCS32

-----

Type: Discussion
Max score: 100
Category: Enabling Asssessment
Start: Sep 23, 11:00 am
Due: Sep 23, 3:00 pm **(<t:1727074800:R>)**

Allow late submissions: ✅

-----

Write the correct regular expression for the following questions. Screen shot your answer and submit it to the given link

- Write a regex pattern to match any string that starts with a digit and ends with a letter.
 - ^\d.*[a-zA-Z]$
- Create a regex to validate standard email addresses (e.g., user@example.com).
 - ^[a-ZA-Z0-9._+-]@[a-ZA-Z0-9.-]+\.[a-zA-Z]{2,}$
- Write a regex pattern that matches US phone numbers in the format (123) 456-7890.
 - ^\(\d{3}\) \d{3}-\d{4}$
- How would you write a regex to extract dates in the format DD/MM/YYYY from a text?
 - \d{2}/\d{2}/\d{4}
-  Write a regex that replaces multiple spaces in a string with a single space.
 - \s+
- Create a regex to match filenames that end with .jpg, .jpeg, or .png.
 - ^.*\.(jpg|jpeg|png)$
-  How can you use capturing groups in regex to extract both the area code and the number from a phone number like (123) 456-7890?
 - ^\((\d{3})\) (\d{3}-\d{4})$
- Write a regex to find all occurrences of the word "cat" in a sentence, ensuring it only matches as a whole word (not as part of another word).
 - \bcat\b
- Construct a regex pattern that matches a string containing a sequence of digits followed by either a hyphen or a space, and then a sequence of letters.
 - \d+[- ]+[a-zA-Z]+
- How would you use regex to sanitize a string by removing all non-alphanumeric characters (keeping only letters and numbers)?
 - [^a-ZA-Z0-9]+