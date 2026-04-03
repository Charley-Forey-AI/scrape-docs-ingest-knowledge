---
title: "Vac/Hol/Sick Accruals and Payroll Burden - Report Calculations | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/human-resources/human-resource-module/hr-specific-topics/vacholsick-accruals-and-payroll-burden/vacholsick-accruals-and-payroll-burden---report-calculations"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/human-resources/human-resource-module/hr-specific-topics/vacholsick-accruals-and-payroll-burden/vacholsick-accruals-and-payroll-burden---report-calculations"
---

# Vac/Hol/Sick Accruals and Payroll Burden - Report Calculations

Use the following table to determine how payroll and burden accruals are calculated.
Report Column
How Calculated

Hours bank balance
The hours bank balance is calculated using the Payroll Current Processing Date. For example, if a user runs the accrual on 4/16/20, and the payroll current processing date is 4/16/20, even if they entered March dates on the update start screen, all hours through 4/16/20 will be included.
Users can obtain hours as of 3/31/20 by temporarily changing the Payroll Current Processing Date to 3/31/20.

Pay Rate
The default hourly pay rate comes from Employee Maintenance and will be used unless a home union is specified for the employee.
When a home union is specified, the employee pay rate will be determined based on the Payroll Installation – Defaults tab prompt for the Default pay rate (Union/pay group rate, Employee pay rate, Higher of the two rates):
Employee pay rate: When the installation prompt is set to Employee pay rate, the Employee Maintenance rate will be used unless it is $0.00. In this case, the 'wage code/union code' rate for the employee's default pay level (or '1' if blank) will be used.
Union/pay group rate: When the installation prompt is set to Union/pay group rate, the 'wage code / union code' rate for the employee's default pay level (or '1' if blank) will be used unless it is $0.00. Then, the 'union code' rate for the employee's default pay level (or '1' if blank) will be used unless it is $0.00. Otherwise, when the union rate is $0.00, the employee's pay rate will be used.
Higher of the two rates: When the installation prompt is set to Higher of the two rates, the higher of the Employee Maintenance rate and the 'wage code / union code' rate will be used.

Payroll Accrual
The Hours bank balance is multiplied by the Pay rate and is rounded to the nearest penny.

Burden Accrual
The Payroll accrual is multiplied by the Payroll burden % (from the starting screen or employee override), and is rounded to the nearest penny.

Total Accrual
The Payroll accrual is added to the Burden accrual.

Previous Date
The last accrual date stored.

Previous Accrual
The last vacation, holiday, or sick balance.

Net Accrual
The Total accrual amount minus the Previous accrual amount.
