---
title: "About Rolling up Employee Accumulations | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/about-rolling-up-employee-accumulations"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/about-rolling-up-employee-accumulations"
---

# About Rolling up Employee Accumulations

Rolling up accumulations reduces the volume of historical data while retaining potentially important payroll data.
When you rollup employee accumulations, the system consolidates a year's worth of data into a single line by keeping only the net sum for the year.
 The following table discusses the changes made when you rollup accumulations.
United StatesThe system makes the following changes in PR Employee Accumulations:

- For each combination of employee, month, type, EDL code, the system removes every instance of that combination

- For that same combination, the system creates a single entry (row) for the net sum of that type and EDL code

- Labels each row with a month value of 12/YY, where YY is the year being consolidated

CanadaThe following changes are made in PR Employee Accums Detail:

- For each combination of employee, month, type, EDL code, province, payroll program account, and Quebec file #, the system removes every instance of that combination

- For that same combination, the system creates a single entry (row) for the net sum of all instances.

- Labels each row with a month value of 12/YY, where YY is the year being consolidated

The system also makes the following changes in PR Employee Accumulations:

- Removes each instance of a given combination of employee, year, type, and EDL Code

- For that same combination, the system creates a single entry (row) for the net sum of that type and EDL code

- Labels each row with a month value of 12/YY, where YY is the year being consolidated

AustraliaThe following changes are made in PR Employee Accums Detail:

- For each combination of employee, month, type, EDL code, income stream type and income stream country, the system removes every instance of that combination

- For that same combination, the system creates a single entry (row) for the net sum of all instances

- Labels each row with a month value of 06/YY, where YY is the tax year being consolidated

The system also makes the following changes in PR Employee Accumulations:

- For each combination of employee, year, type, and EDL Code, the system removes each instance of that combination

- For that same combination, it creates a single entry (row) for the net sum of that type and EDL code

- Labels each row with a month value of 06/YY, where YY is the year being consolidated

For more information about rolling up employee accumulations, see [Rollup Employee Accumulations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/about-rolling-up-employee-accumulations/rollup-employee-accumulations).
