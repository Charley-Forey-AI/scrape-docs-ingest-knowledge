---
title: "User Interface Elements | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/getting-started/spectrum-interface-faqs/user-interface-elements"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/getting-started/spectrum-interface-faqs/user-interface-elements"
---

# User Interface Elements

## Moving Around a Screen

To move from one field to the next, enter information at the desired field and press Enter. This automatically moves the cursor to the next field where information is to be entered. After responding to each entry field, the software takes the cursor to the next entry field, from there to the next, and so on through the screen.
If you are entering information and notice an error in the current field, the Back space key may be used to remove characters in error and then you may retype from that point. If an error is discovered in a previous field, you should press Shift + Tab to move back one field, and to each previous field until the cursor is in the field with the error. Otherwise, the mouse may be used instead of Shift + Tab to reposition the cursor at the desired field.
The Tab key may be used as a forward tab to move through a screen field by field. This may be helpful in screens where there are large blocks of information and the operator wishes to skip much of it. If the cursor tabs past a field where you intended to enter data, ARROWS may be used to get back to it. It is possible that the arrow keys may not always take the cursor to the expected field since the cursor moves to the closest physical location. Shift + Tab moves the cursor back to the prior logical field when moving back exactly one field.

## Alphanumeric Characters

Alphanumeric characters are letters, numbers, and special characters such as #, %, &, and *. If a field is designated as alphanumeric, any combination of these characters may be entered. These are generally left-justified input fields.

## Numeric

Numeric fields contain only the numbers 1 through 9 and 0.
There are some characteristics of numeric fields of which you should be aware:

- It is possible in some fields to enter more digits to the right of the decimal point than specified in the field characteristics. The additional digits will not display; however, they will be stored internally and used in calculations.

- The software may sometimes store more digits than it usually displays or prints. It stores up to six digits to the right of the decimal, but might only display or print two, as in the case of dollar amounts. Consequently, the number that displays or prints may be fractionally different from the number that is stored internally. Such discrepancies are called rounding differences and occur when the software rounds a number with six decimal places to fit into a two-decimal place format.

- Negative numbers may be entered into numeric fields. Although the minus sign may be entered either before or after the digits, the software will display and print the minus sign after the number, except on Crystal Reports.

## Phone Number Fields

Enter seven, ten, or eleven digits in these fields. Enter 11 digits to include the initial "1", area code and phone number; enter 10 digits for the area code and telephone number; enter only seven digits when an area code is not included. In all cases, enter the numbers only--no dashes or parentheses. After Enter is pressed, the software redisplays the phone number with the appropriate separators.

## Social Security Numbers

Social Security numbers are entered as nine digits without hyphens. After Enter is pressed, the software redisplays the number with the hyphens inserted automatically.

## SuperSelect Fields

A green asterisks signals that a field includes special selection capability
 called SuperSelect. Become familiar with the different selection types to be
 able to filter your data records quickly and efficiently.

For more about SuperSelect, see [About SuperSelect](/en/spectrum/spectrum/getting-started/reports--printing-overview/about-superselect).

## Dates

Dates are entered in the format MMDDYY. Enter two numbers for the month, two numbers for the day, and two numbers for the year, and press Enter. All six digits must be entered, including any zeroes.
How dates are entered into the software: In Spectrum, data entry is as quick and easy as possible. One way we do this is to make dates quick to enter. Most of the time, you don't have to enter the year at all: the software assumes the current year (for example, 915 will be interpreted as September 15 of the current year). If you need to enter in a date with a different year, you may enter the two-digit year (for example, 91500, which is September 15, 2000).
Any two-digit year below 60 is assumed to be in the 21st century; above 60 is assumed to be 20th century (for example, 97 is assumed to be 1997 and 02 is assumed to be 2002). If necessary, you may enter in the four-digit year (for example, if you have to enter in the year 2061, you would enter 2061). The one exception is for birth dates; if you type a birth date as six digits (DD/MM/YY), Spectrum will default the year to a past date. For example, if you type "02/02/50," the year will default to 1950 instead of 2050. If you enter a birth date earlier or later than the expected range, a warning message will display.
A convenient Date Calculator window is available at selected date fields throughout Spectrum. It allows the operator use the mouse to identify the desired date or simply view the calendar.

## Time

The time is entered in the format HHMMSS, without colons to separate hours from minutes or minutes from seconds. Time is entered on a 24-hour clock. Leading zeroes are entered for time up to 1000 hours (ten a.m.).

## Checkbox

A checkbox is used in the Graphical User Interface (GUI) environment to enable or disable one or more options on a list. When an option is selected, an X or a check mark appears in the box. The mouse can be used to toggle a checkbox on and off; the Spacebar on the keyboard may alternatively be used.

## Option Button

In the Graphical User Interface (GUI) environment, a radio button can be used to select from among several options. Unlike checkboxes, only one of the Options may be selected at any one time. Selecting one button will automatically deselect the previously selected button. An Option button is a small circle that when selected has a smaller filled circle inside it.
