---
title: "New/Edit Electronic File Table - Detail | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/newedit-electronic-file-table---detail"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/newedit-electronic-file-table---detail"
---

# New/Edit Electronic File Table - Detail

Use this tab to enter detail information for the new electronic file.
Fields/Buttons
Descriptions

Variable type
Select the variable type: Single, Multiple, Constant, or Formula.

- If Single is selected, the Search File Variables window opens and displays all of the available variables in Payroll.

-  If Multiple is selected, the Concatenate Multiple Variables window displays. Use this window to combine the information from several fields into one field. For example, you might want to combine the City, State, and Zip fields into one concatenated "address" field.

- Select Constant if you want to use special plan numbers or other company information that is constant for all employees.

- If Formula is chosen, the Electronic File Formulas window displays. Select an appropriate formula code; this will default to the Descriptions field on the main screen.

 If you select Single or Formula, the Search File Variables window displays. Use this window to select the delimiter's source file. For Single and Formula variables, certain files offer different selections and selection type fields:
PR.INCTX, PR.STHIS
 Type = Federal (0), State (1), County (2), Local (3), and Blank (ALL)
Selection = Tax table code
PR.VDCTL, PR.EHVD
 Type = Add-on/deduction code, Category group
Selection = Code or group, as determined by Type
PR.WCCTL, PR.WCHIS
Type = N/A Selection = Worker's comp code

Descriptions
Enter a description that will display for the Constant variable type, for example: 'Employee Name'.
If the variable type is Single, Multiple, or Formula, press F4 or double-click on this field to display the corresponding search window or Details window.

Type
The file type defaults from the database. File types include Alphanumeric, Numeric, Date, and Key.
Note: You need to enter the Key field type if you want the sort
 variables (employee code, check number, and so forth) to display in the
 file; otherwise the information will still sort according to the setup in
 the Properties window, but the variables will not display.

Length
The length (number of characters) of the variable displays. This can either be the length in the database, or it can be defined here if the variable type is Constant or Multiple.

Round
Enter the number of decimal spaces that will appear after the decimal point.

Justification
Select the justification type: Default, Left, or Right.

Fill
If the file type is Numeric and right-justified, enter Zero to fill the leading spaces with zeros, or leave the fill type blank if you want the leading spaces to appear blank. You can also choose the character that will display for non-existent dates; for example, if you selected the character 0, the date would display as 00/00/0000, according to the display mask.

Display format
Use this field to determine a combination of mask characters (up to 20 characters).
Date formats might be set up as MM/DD/YY or MM/DD/YYYY (or any other user-defined arrangement).
Alpha-numeric formats can be set up to default as left or right-justified. Entering the character X causes the variable to be left-justified within the mask (for example, social security codes might be set up as XXX-XX-XXXX) and entering the character Y causes the variable to be right-justified within the mask. Likewise, X and Y are mutually exclusive within a single display mask. All other characters are displayed literally.
Numeric formats can be set up to use any combination of the following:
9 Digit 0-9 (when the position is blank a zero is stored),
Z Digit 0-9 (when the position is blank a blank is stored),
- Minus sign
, Comma
. Decimal (If you do not enter a decimal place, Spectrum will round to the nearest dollar.)

Period
Select the period: Current or Year-to-date. If this is not a check or check detail variable, the period should be blank.

Non-zero
Select this checkbox if you want to deselect this record if a given variable (for example, the hire date, social security number, or state earnings amount) is blank or zero. This feature is especially helpful if you do not want a record to appear in the file.

Selection
No entry is allowed.

Type
No entry is allowed.

File
The file corresponding to the sort variable displays.

Alternate name
No entry is allowed.

Descriptions
The tax table description displays in this field.
