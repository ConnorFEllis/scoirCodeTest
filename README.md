# csv-filter-challenge-public


# How-To
   1. Press the WINDOWS button and type 'cmd'.
   2. Type 'python' into the cmd line.
   3. This should bring you to the windows store where you can install the newest version of python for free. After installiation, exit the window.
   4. Type 'pip3 install wheel' into the cmd line.
   5. After the install in complete type 'pip3 install pandas' into the cmd line.
   6. Navigate to the directory containing the program (ScoirCodeTest.py) and the CSV file (file.csv). You can do this by typing 'cd Desktop' if your files are on the desktop.
   7. type 'ScoirCodeTest.py' into the cmd line.
   8. Follow the prompts!

# Assumptions
   1. CSV file name is File.csv
   2. CSV file is in the same directory as our program
   3. The user wants the whole record(s) to be returned as a result of the filter they choose


# Instructions
1. Click "Use this template" to create a copy of this repository in your personal github account.  
1. Using technology of your choice, complete assignment listed below.
1. Update the README in your new repo with:
    * a `How-To` section containing any instructions needed to execute your program.
    * an `Assumptions` section containing documentation on any assumptions made while interpreting the requirements.
1. Send an email to Scoir (andrew@scoir.com) with a link to your newly created repo containing the completed exercise.

## Expectations
1. This exercise is meant to drive a conversation. 
1. Please invest only enough time needed to demonstrate your approach to problem solving, code design, etc.
1. Within reason, treat your solution as if it would become a production system.

## Assignment
Create a command line application that parses a CSV file and filters the data per user input.

The CSV will contain three fields: `first_name`, `last_name`, and `dob`. The `dob` field will be a date in YYYYMMDD format.

The user should be prompted to filter by `first_name`, `last_name`, or birth year. The application should then accept a name or year and return all records that match the value for the provided filter. 

Example input:
```
first_name,last_name,dob
Bobby,Tables,19700101
Ken,Thompson,19430204
Rob,Pike,19560101
Robert,Griesemer,19640609
```
