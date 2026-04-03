---
title: "Define Financial Report Columns - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/design-financial-reports/define-financial-report-columns/define-financial-report-columns---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/design-financial-reports/define-financial-report-columns/define-financial-report-columns---field-descriptions"
---

# Define Financial Report Columns - Field Descriptions

Use the table below for reference when completing the fields on this screen.
FieldDescription
Report IDEnter the ID of the report for which column information is being defined.
Column #Display only.
Start column positionEnter the number that represents the column in which the first character will display. The system defaults the first column to position one, and subsequent columns to a number that represents the ending position of the previous column plus two spaces. Press Enter to accept the default, or enter a new number that is greater than the ending position of the previous column.Important:

- Do not overlap non-numeric columns. For example, if Column 1 starts at position 20 and has a length of 10, then Column 2 must start after position 30.

- With the exception of Level columns, numeric columns may overlap if all parameters for overlapping columns are identical.

Tip: Phantom columnsEnter 0 if you want to use a phantom column - one which contains calculations or numbers referred to by other columns, but which does not appear on the printed report. In such cases, the Length and Display Code fields become display only.

LengthEnter the maximum number of characters that may print in this column.

Column typeSelect the code representing the type of information to be displayed in the column.

- A - Account number from the General Ledger Chart of Accounts

- N - Numeric informationNote:Entries the next six fields are relevant only when the column type is Numeric. For all other types, the next six fields are skipped.

- F - Formula calculation results

- FD - First 30 characters of the account code description in the Chart of Accounts

- AD - First 18 characters of the account code description in the Chart of Accounts


Column types A, AD, and FD print for detail type rows only. If needed, refer to [Define Financial Report Rows](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/design-financial-reports/define-financial-report-rows) for information on row types.

Period typeSelect the accounting period code to choose the type of information that will print in the column:


- P - Period

- Y - Year-to-date

- Q - Quarter-to-date

- Q1 - First quarter

- Q2 - Second quarter

- Q3 - Third quarter

- Q4 - Fourth quarter

YearEnter the code of the year from which the information is to be pulled: Current year, Last year, or Next year.

Offset periodsThis field and the next work in conjunction with the Year field to print the correct information in the column. For example, assume this column is to contain information from last year and the current period is period 4. The system needs to know from which period to pull the information to place in the report. If this column is to contain information from period 4, leave the field blank by pressing Enter. By pressing Enter, Spectrum takes the information from the same period as the current period, but the information is to come from the previous year.
To indicate to the software that information is needed from a period other than the current period, use the current period as the base period. Then add (+) or subtract (-) a certain number of periods to obtain the period needed. For example, the current period is period 4 and Last Year was entered in the "yr field". To print information from period 7 of last year, enter a +3 in this field. This tells the software to add 3 to the current period to determine the period from which the information is to be taken. To print information from period 1, 3 would be entered.
First select the plus or minus and press Enter, then enter the number and press Enter again.

Data typeThis field is skipped if Next year was selected in the Year field. Select the data type Actual or Budget to display in this column.

LevelLevel numbers are used in both the rows and columns to indicate to Spectrum which numbers to place in which columns, and how to total the columns in the report. Valid level numbers are 11 through 19. The level number entered here will correspond to level numbers entered in Define Financial Report Rows.
Each column may have a maximum of two level numbers.

Percent?Select if the column will be formatted to print data as a percentage.
DescriptionFor column types A#, AD, FD, and N, a description of the type of information in the field displays.
FormulaColumn Type F allows entry of a formula; the report will print the calculation results. Formulas are executed from left to right without regard for arithmetic precedence. They may reference only numeric columns and constants. A formula may refer to a column containing a formula provided that the column number being defined is greater than the number of the column referenced (that is, a column formula may reference other column formulas so long as the column being defined is to the right of the column(s) being referred to).
Formulas are entered as operand > operator > operand > operator > (and so on).
Operands may be any number 0 or greater or a column number from the report. If you use a column number in your formula, precede it with #.
Operators are addition (+), subtraction (-), multiplication (*), and division (/).
Formula Examples:
Important: Multiple operators in a formula must always be separated by an operand. For example, #2* 1 is not a valid formula.To total columns 2, 3, and 4
 #2 + #3 +#4

To average columns 2, 3, and 4
 #2 + #3 + #4 / 3

To create a variance percentage
 #2 - # 3 / #2 * 100


Display codeUse this field to tailor the type and format of numeric characters that print in the columns.
Enter a display code, which can be overwritten For example, if you do not want to display cents on the report, enter the display as ZZZ,ZZZ,ZZZ.
If a field length is changed after creating the report, the corresponding display code must also be changed.

A table of valid display codes.
