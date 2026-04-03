---
title: "Define Financial Report Rows - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/design-financial-reports/define-financial-report-rows/define-financial-report-rows---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/design-financial-reports/define-financial-report-rows/define-financial-report-rows---field-descriptions"
---

# Define Financial Report Rows - Field Descriptions

Use the table below for reference when defining the rows in your financial report.
FieldDescription
Report IDEnter the ID of the report whose rows you want to view.
LineDisplay only.
Row type

- Header rows contain descriptive text that is not specifically associated with a dollar value, and can be positioned anywhere on the financial report.

- Detail rows print one line for each General Ledger account code that falls within the account number range you specify.

- Total rows print a sum of all accounts within the specified range and associated text.

- Inclusion rows are used to include an additional account or range of accounts outside the start and end account number range. An Inclusion row is used in conjunction with a total line and must directly follow the total line it is associated with.

- Exclusion rows are used to exclude a portion of the account within the range of accounts being totaled. An Exclusion row is used in conjunction with a total line and must directly follow the total line it is associated with.

Start accountHeader rows automatically skip this field and proceed to the Top of Form field.
For detail rows, enter the first General Ledger account number you want to print information for.
For Total, Inclusion, and Exclusion rows, enter the account number that begins the range of values to be totaled.
Whichever checkbox is selected for this report in the Design Financial Reports screen dictates how much of the GL code you should enter here:

- Cost center report - enter the complete G/L code.

- Department report - enter the applicable truncated G/L code.Note: If this is a departmental report, do not enter the part of the General Ledger account code that contains the department number.

End accountFor Detail, Total, Inclusion, and Exclusion rows, enter the General Ledger account number that ends the range.
Whichever checkbox is selected for this report in the Design Financial Reports screen dictates how much of the GL code you should enter here:

- Cost center report - enter the complete G/L code.

- Department report - enter the applicable truncated G/L code.Note: If this is a departmental report, do not enter the part of the General Ledger account code that contains the department number.

LevelSpectrum identifies each line by the combination of the ending account number with the level number. There can never be multiple lines ending with the same ending account number/level number combination.
Detail lines are automatically assigned level 10.
The column definitions of the report include percentage columns, so each line is calculated as a percentage of total revenue. The level number entered in this field tells Spectrum which denominator to use in the percentage calculation.

Reverse sign?For Detail and Total rows, select this checkbox if the values will be printed with the reverse sign, for example, positive numbers as negative numbers, and vice versa. For example, since liability and capital accounts are "negative", selecting this checkbox will cause these amounts to print on a balance sheet report as positive numbers.

New page?For Header, Detail, and Total rows, select this checkbox if this row should print at the top of the next screen.
Press Enter to leave the field blank if you want the rows to print successively until the next screen break.
Leave this checkbox clear if you do not want a new screen.

End account % basisThe End account % basis and Level fields are only used when a percentage has been indicated during Column Entry. It is used to indicate the relationship between the value of the row being entered with a different row. It is also used to link header rows to their corresponding detail and total rows.
Enter the ending account number from which the percentage should be calculated. To enter the final account number of a range being totaled, enter the appropriate account number. In the Cost example, if Total Sales adds the values of accounts 501 through 542, enter "542" as the ending account number.
Whichever checkbox is selected for this report in the Design Financial Reports screen dictates how much of the GL code you should enter here:

- Cost center report - enter the complete G/L code.

- Department report - enter the applicable truncated G/L code.Note: If this is a departmental report, do not enter the part of the General Ledger account code that contains the department number.

Level % basisFor Total rows, enter the level number associated with this total line.
Lines beforeFor header, Detail, and Total rows, enter the number of carriage returns to print between the previously printed row and the current row. For example, if 1 is entered, the current row prints directly beneath the previous row. If 2 is entered, there is one blank line between the current row and the previous row. There are two occasions when 0 may be entered:


- The first row may have a value of zero regardless of the row type since there is no previous row.

- Header rows may have a value of zero, which causes the text of the current row to be printed on the same line as the previous row.

Start column positionFor Header and Total rows, enter the beginning position of the text, press Enter, then enter the text and Enter a second time.

Heading or total labelChoose the character you want the system to use to create the underline which appears just above the total row: -, =, or _.
If you don't want an underline, leave this field blank.
This field appears only in conjunction with Total rows.
Warning: Underscores cause errors with Crystal reports, and must only be used for Standard reports. If you're working with a Crystal report, you must use a hyphen (-) or minus(-).
