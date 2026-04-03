---
title: "Canadian Vacation Pay - Add-on Code VPAYNOW | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/canadian-vacation-pay/canadian-vacation-pay---add-on-code-vpaynow"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/canadian-vacation-pay/canadian-vacation-pay---add-on-code-vpaynow"
---

# Canadian Vacation Pay - Add-on Code VPAYNOW

Setup in Deduction / Add-on Code Maintenance:
Properties Tab
Code = VPAYNOW
Description = Vacation Pay
Type = Add-on
Calculation method = % of gross by time card
Optional: 'Default rate', 'Frequency', 'Week numbers' fields
Optional: 'Clear employee balance at yearend', 'Davis-Bacon', 'Prevailing wage', 'Other jobs and non-jobs' checkboxes
Optional: Add-on entries in the 'Gross Pay Adjustments' sub-window
Tax Effects Tab
Add Federal tax code and set checkboxes to Taxable ('selected')
Add applicable Provincial tax codes and set checkboxes to Taxable
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
Optional: 'Pay union benefits on this add-on' checkbox
'Payment options' box:
Select 'Paid to employee on the paycheck' checkbox
Leave 'Is this for 'payout' from accrued benefit balance?' un-checked
Limits Tab and A/P Invoice Tab not applicable
See example.
Setup in Employee Recurring Deductions / Add-ons:
Code = VPAYNOW
Status = Recurring
Percent = 4.00
