---
title: "Sample Report Calculations - Vacation, Holiday and Sick Accrual | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/human-resources/human-resource-module/spectrum-menus/data-entry-overview/vacholsick-gl-accrual-update/sample-report-calculations---vacation-holiday-and-sick-accrual"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/human-resources/human-resource-module/spectrum-menus/data-entry-overview/vacholsick-gl-accrual-update/sample-report-calculations---vacation-holiday-and-sick-accrual"
---

# Sample Report Calculations - Vacation, Holiday and Sick Accrual

The following table describes how each column is calculated on this report.
Column
Description

Hours bank balance
The Hourly banks balance (in Payroll Employee Maintenance  >  Properties) plus or minus balance changes after the accrual date display.

Pay rate
The employee default hourly pay rate (from Payroll Employee Maintenance  >  Financials) is used unless a home union is specified in Employee Maintenance. If this is the case, then the employee pay rate will be determined based on the Default pay rate selection on the Payroll Installation  >  Defaults screen as follows:

- If the installation Default pay rate option is set to Employee pay rate, the rate specified in Payroll Employee Maintenance  >  Financials is used unless it is not specified ($0.00). In this event, the wage/union code rate for the employee's default pay rate (or 1 if blank) will be used.

- If the installation Default pay rate option is set to Union/pay group rate, the wage/union code rate for the employee's default pay level (or 1 if blank) will be used unless it is not specified ($0.00). Then, the union code rate for the employee's default pay level (or 1 if blank) will be used unless it is $0.00. In this event, the employee's pay rate will be used.

- If the installation Default pay rate option is set to Higher of the two rates, the higher of the two rates (union/wage code or employee pay rate) as specified in Employee Maintenance will be used.

Payroll accrual
Hours bank balance multiplied by pay rate and then rounded to the nearest penny.

Burden accrual
Payroll accrual multiplied by the Payroll burden percentage (from the Vac/Hol/Sick G/L Accrual/Update starting screen) rounded to the nearest penny.

Total accrual
Payroll accrual plus burden accrual.

Previous date
Last accrual date stored in the Payroll Employee file.

Previous accrual
Last vac/hol/sick balance stored in the Payroll Employee file.

Net accrual
Total accrual minus previous accrual.
