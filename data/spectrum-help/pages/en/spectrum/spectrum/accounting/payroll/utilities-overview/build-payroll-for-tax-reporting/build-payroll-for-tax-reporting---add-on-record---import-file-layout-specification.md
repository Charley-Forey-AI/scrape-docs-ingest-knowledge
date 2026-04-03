---
title: "Build Payroll for Tax Reporting - Add-on Record - Import File Layout Specification | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/build-payroll-for-tax-reporting/build-payroll-for-tax-reporting---add-on-record---import-file-layout-specification"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/build-payroll-for-tax-reporting/build-payroll-for-tax-reporting---add-on-record---import-file-layout-specification"
---

# Build Payroll for Tax Reporting - Add-on Record - Import File Layout Specification

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
Add-on record

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
Add-on Code
Alpha
10
Yes
Validate to Deduction/Add-on Table
Must be an Add-on Code

5
Add-on Amount
Num
-12.2
No
This value will be included in the employee's 'Add-ons' amount on the Payroll Taxes Register (report) when the code is flagged as 'paid to employee on pay check', and will be used when validating 'Net Pay' during the import.
Positive value will increase the amount paid to employee when calculating 'Net pay' (if the code is flagged as 'paid to employee on pay check').
