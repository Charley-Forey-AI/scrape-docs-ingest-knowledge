---
title: "Build Payroll for Tax Reporting - Time Card - Import File Layout Specifications | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/build-payroll-for-tax-reporting/build-payroll-for-tax-reporting---time-card---import-file-layout-specifications"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/build-payroll-for-tax-reporting/build-payroll-for-tax-reporting---time-card---import-file-layout-specifications"
---

# Build Payroll for Tax Reporting - Time Card - Import File Layout Specifications

Use the table below for reference when completing the
 fields on this screen.
Field
Name
Type
Size
Req?
Field information

1
Record ID
Alpha
2
Yes
TC (time card) Record

2
Entity
Alpha
10
No
Validate to Entity table if non-blank.
This field is not applicable unless the Enterprise Management module is present and 'Entity tracking' is enabled.

3
Employee code
Alpha
11
Yes
Validate to employee master

4
Pay type
Alpha
1
Yes
Regular, Overtime, Double time, Vacation, Holiday or Sick time.

5
Hours
Num
-12.2
Yes
Must be non-zero (negative OK)
This value will appear on the Payroll Time Card History Report.

6
Union
Alpha
10
No
If the 'Default rate table' in Payroll Installation is set to 'Unions' or 'Wage code/unions', then validate to Union Table.
This field is not applicable when using pay groups.

7
Wage code
Alpha
10
No
If the 'Default rate table' in Payroll Installation is set to 'Unions' or 'Wage code/unions', then validate to Wage Code Table using union code specified in Field # 6.
This field is not applicable when using pay groups.

8
Pay group
Alpha
10
No
If the 'Default rate table' in Payroll Installation is set to 'Pay groups', then validate to Pay Group Table.
This field is not applicable when using unions or union/wage codes.

9
State
Alpha
10
Yes
Validate to Income Tax Table

10
County
Alpha
10
No
Validate to Income Tax Table

11
Local
Alpha
10
No
Validate to Income Tax Table

12
Message
Alpha
30
No
