### Task 1 – Input from the user

User input is an important part of any program. Remember, programs need to take input, store the data, process the information, and output data to a file or display. Python has a simple way to get information from the user’s keyboard. The input command is used to pull information, as a string, into a variable.

Open the Python 3.10 Integrated Development Learning Environment (IDLE) and create a new project named, IDinput.

Let’s start off by adding your StudentID to the program, then asking the user for their birth date:

```python
print("<Your StudentID>")
birthdate = input("What is your birthdate (MM/DD/YYYY)? ")
```

No deliverables for Task 1.

---

### Task 2 – Write the program

In this task you will use the input statement to pull data from the user while the program is running.

Open the Python 3.10 Integrated Development Learning Environment (IDLE) and create a new project named, Birthday.

Let’s start off by adding your StudentID to the program, then asking the user for their birth date:

```python
print("<Your StudentID>")
birthdate = input("What is your birthdate (MM/DD/YYYY)? ")
```

Now let’s print out their birthdate to the screen:

```python
print(birthdate)
```

Run the program and make sure you can enter a date which is then printed out to the screen.
Try running the program again but enter something else (not a date). What happens? Please answer this in your Lab Report.

Let’s split out the MM, DD, and YYYY from what the user input. Type:

```python
month, day, year = birthdate.split("/")
```

This will split the birthday into month, day, and year.
Add the following statement so we can check that everything is working:

```python
print(month, day, year)
```

Now you are going to convert your month, day, and year into a date number your computer can recognize. To do this we must first import the module datetime into the program. Add the following statements to the program:

```python
bdate = datetime.datetime(int(year), int(month), int(day))
print(bdate)
```

Unfortunately, that doesn’t work because we haven’t imported the datetime module. At the top of the program add:

```python
import datetime
```

Your program should now run and show you the date and time for the entered birthday.

Now you can do the math to determine the user’s age. Enter the following statements:

```python
todays_date = datetime.datetime.now()
age = todays_date - bdate
print(age.days)
```

This will give you the number of days old you are.

Finally, you are going to convert the number of days to years by typing the following:

```python
print("You are " + str(age.days/365.25) + " years old")
```

We are dividing the total number of seconds by 365.25 which is the total number of days in a year. Take a screenshot of your current program for the Lab Report. Your screen shot should resemble the one below.
