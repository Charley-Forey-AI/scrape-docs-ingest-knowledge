---
title: "Build Payroll for Tax Reporting - Header Record - Import File Layout Specifications | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/build-payroll-for-tax-reporting/build-payroll-for-tax-reporting---header-record---import-file-layout-specifications"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/build-payroll-for-tax-reporting/build-payroll-for-tax-reporting---header-record---import-file-layout-specifications"
---

# Build Payroll for Tax Reporting - Header Record - Import File Layout Specifications

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
Header record

2
Entity
Alpha
10
No
Validate to Entity Table if non-blank
Not applicable unless EM is present and "entity tracking" is enabled.

3
Employee Code
Alpha
11
Yes
Validate to employee master
Any employee status is permitted

4
Start Date
Date
8
Yes
Format = MMDDYYYY

5
End Date
Date
8
Yes
Format = MMDDYYYY

6
Gross Earnings
Num
-12.2
No
This value will appear on the Payroll Taxes Register (report) in the 'Gross' column and will be used when validating 'Net Pay' during the import

7
Net Pay
Num
-12.2
No
Validate this amount = Gross minus FIT minus FICA minus Other Taxes* minus Deductions plus Add-ons (if paid to employee on the check)
* Other Taxes = Income taxes withheld + employee SDI tax deduction + Employee worker's compensation deduction (excluding Federal tax code)
This value will appear on the Payroll Taxes Register (report) in the 'net pay' column

8
Total Hours
Num
-12.2
No
This value will appear on the Payroll Taxes Register (report) in the 'Hours' column
