---
title: "Build Payroll for Tax Reporting - Tax Record - Import File Layout Specifications | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/build-payroll-for-tax-reporting/build-payroll-for-tax-reporting---tax-record---import-file-layout-specifications"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/build-payroll-for-tax-reporting/build-payroll-for-tax-reporting---tax-record---import-file-layout-specifications"
---

# Build Payroll for Tax Reporting - Tax Record - Import File Layout Specifications

Use the table below for reference when completing the
 fields on this screen.
Field
Name
Type
Size
Req?
Field Information

1
Record ID
Alpha
1
Yes
Tax record

2
Entity
Alpha
10
No
Validate to Entity Table if non-blank
Not applicable unless EM is present and 'entity tracking' is enabled.

3
Employee Code
Alpha
11
Yes
Validate to employee master

4
Tax Table Code
Alpha
10
Yes
Validate to Income Tax Table

5
Jurisdiction Type
Alpha
1
Yes
Federal, State, County or Local

6
Income Tax Subject-to
Num
-12.2
No

7
Income Tax Withheld
Num
-12.2
No
For the employee's Federal tax code, this value will appear on the Payroll Taxes Register (report) in the 'FIT' column and will be used when validating 'Net Pay' during the import
For all other tax codes, this value will be included in the employee's 'Other Taxes Paid' amount on the Payroll Taxes Register (report). It will also be used when validating 'Net Pay' during the import

8
Employee FICA Tax Subject-to
Num
-12.2
No
In Canada, this will be where CPP value is recorded for the Federal tax code
Note: Do not apply annual SS limit since this 'subject-to' amount applies to
 both Social Security and Medicare.

9
Employer FICA Tax Subject-to
Num
-12.2
No
In Canada, this will be where CPP value is recorded for the Federal tax code
Note: Do not apply annual SS limit since this 'subject-to' amount applies to
 both Social Security and Medicare

10
Employee Social Security Tax Deduction
Num
-12.2
No
For the employee's Federal tax code, this value will be included on the Payroll Taxes Register (report) in the 'FICA' column and will be used when validating 'Net Pay' during the import.
In Canada, this will be where CPP value is recorded for the Federal tax code, and will be used when validating 'Net Pay' during the import.
For all other tax codes, this field is not applicable.
Note to Programmer: User enters the amount for Social Security separate from Medicare (in field 12). During the import update, Spectrum will store the sum of these two values as FICA, and the Medicare amount will be stored separately.

11
Employer Social Security Tax Expense
Num
-12.2
No
This value will be included in the 'Employer Tax Summary' box on the Payroll Taxes Register (report).
In Canada, this will be where CPP value is recorded for the Federal tax code.

12
Employee Medicare Tax Deduction
Num
-12.2
No
For the employee's Federal tax code, this value will be included on the Payroll Taxes Register (report) in the 'FICA' column and will be used when validating 'Net Pay' during the import.
For all other tax codes, this field is not applicable. This field is also not applicable in Canada.

13
Employer Medicare Tax Expense
Num
-12.2
No
This value will be included in the 'Employer Tax Summary' box on the Payroll Taxes Register (report).
Not applicable in Canada.

14
Employee SDI Subject-to
Num
-12.2
No
In Canada, this will be where EI value is recorded for the Provincial tax code

15
Employee SDI Tax Deduction
Num
-12.2
No
This value will be included in the employee's 'Other Taxes Paid' amount on the Payroll Taxes Register (report) and will be used when validating 'Net Pay' during the import.
In Canada, this will be where EI value is recorded for the Provincial tax code.
Not applicable for the employee's Federal tax code.

16
Employer SDI Tax Subject-to
Num
-12.2
No
In Canada, this will be where EI value is recorded for the Provincial tax code.

17
Employer SDI Tax Expense
Num
-12.2
No
This value will be included in the 'Employer Tax Summary' box on the Payroll Taxes Register (report).
In Canada, this will be where EI value is recorded for the Provincial tax code.

18
Employer Unemployment Tax Subject-to
Num
-12.2
No
Not applicable in Canada.

19
Employer Unemployment Tax Expense
Num
-12.2
No
This value will be included in the 'Employer Tax Summary' box on the Payroll Taxes Register (report).
Not applicable in Canada.
