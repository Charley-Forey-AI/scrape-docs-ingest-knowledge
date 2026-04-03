---
title: "Canadian Vacation Pay - Add-on Code VPAYOUT | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/canadian-vacation-pay/canadian-vacation-pay---add-on-code-vpayout"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/canadian-vacation-pay/canadian-vacation-pay---add-on-code-vpayout"
---

# Canadian Vacation Pay - Add-on Code VPAYOUT

Setup in Deduction / Add-on Code Maintenance:
Properties Tab
Code = VPAYOUT
Description = Vacation Pay
Type = Add-on
Calculation method = Fixed Amount
Optional: 'Default rate', 'Frequency', 'Week numbers' fields
G/L account = 00-8800 – Admin Vacation Expense
Optional: 'Clear employee balance at yearend' checkbox
Tax Effects Tab
Add Federal tax code and set checkboxes to Taxable ('selected')
Add applicable Provincial tax codes and set checkboxes to Taxable
Add-ons Tab
'Direct cost' radio group:
Select 'Non-direct cost' option
'Payment options' box:
Select 'Paid to employee on the paycheck' checkbox
Select 'Is this for 'payout' from accrued benefit balance?' checkbox
Related accrual code = VACCRUE
See example.
Limits Tab
Optional
A/P Invoice Tab not applicable
Setup in Employee Recurring Deductions / Add-ons:
Not applicable for VPAYOUT
Add line in Time Card Entry
Pay type = VPAYOUT
Department = ADMIN (a non-direct payroll department)
Rate = Dollar amount of vacation pay taken
Optional: Other fields, including union code
