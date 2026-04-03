---
title: "Build Payroll for Tax Reporting - Deduction Record - Import File Layout Specifications | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/build-payroll-for-tax-reporting/build-payroll-for-tax-reporting---deduction-record---import-file-layout-specifications"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/build-payroll-for-tax-reporting/build-payroll-for-tax-reporting---deduction-record---import-file-layout-specifications"
---

# Build Payroll for Tax Reporting - Deduction Record - Import File Layout Specifications

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
Deduction record

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
Deduction Code
Alpha
10
Yes
Validate to Deduction/Add-on Table
Must be a Deduction Code

5
Deduction Amount
Num
-12.2
No
This value will be included in the employee's 'Deductions' amount on the Payroll Taxes Register (report) and will be used when validating 'Net Pay' during the import.
Positive value will reduce the amount paid to employee when calculating 'Net pay'.
