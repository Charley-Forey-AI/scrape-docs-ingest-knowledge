---
title: "Canadian Vacation Pay - Add-on Code VACCRUE | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/canadian-vacation-pay/canadian-vacation-pay---add-on-code-vaccrue"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/canadian-vacation-pay/canadian-vacation-pay---add-on-code-vaccrue"
---

# Canadian Vacation Pay - Add-on Code VACCRUE

Setup in Deduction / Add-on Code Maintenance:
Properties Tab
Code = VACCRUE
Description = Accrue Vacation
Type = Add-on
Calculation method = % of gross by time card
Optional: 'Default rate', 'Frequency', 'Week numbers' fields
Optional: 'Clear employee balance at yearend', 'Davis-Bacon', 'Prevailing wage', 'Other jobs and non-jobs' checkboxes
Optional: Add-on entries in the 'Gross Pay Adjustments' sub-window
Tax Effects Tab
Empty listbox (no tax effects)
Add-ons Tab
Direct cost setup in 'Gross pay from time cards' box:
Select 'Non-direct cost' checkbox and non-direct G/L account:
00-8800 – Admin Vacation Expense
Select 'Job cost' checkbox and direct job G/L account:
00-5500 – Job Vacation Expense
Select 'Equipment cost' checkbox and direct equip G/L account:
00-6600 – Yard Vacation Expense
Select 'Work order cost' checkbox and direct W/O G/L account:
00-7700 – Service Vacation Expense
Leave 'Pay union benefits on this add-on' checkbox un-checked
'Payment options' box:
Leave 'Paid to employee on the paycheck' checkbox un-checked
Select 'Print on paycheck' checkbox
Non-cash G/L account = 00-2500 – Accrued Vacation Payable
Leave 'Is this for 'payout' from accrued benefit balance?' un-checked
See example.
Limits Tab and A/P Invoice Tab not applicable
Setup in Employee Recurring Deductions / Add-ons:
Code = VACCRUE
Status = Recurring
Percent = 4.00
