---
title: "Time Off Code Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/time-off-code-maintenance/time-off-code-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/time-off-code-maintenance/time-off-code-maintenance---field-descriptions"
---

# Time Off Code Maintenance - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Time off code
Enter the vacation, holiday or sick leave time off code and a description. For example, V1 for vacation hours of new employees on probation, V2 for salaried employees paid bi-monthly, V3 for carpenters paid weekly, S1 for sick leave accrual, and so forth. Note that these codes should be based on the frequency of the employee's pay period.

Pay type
Select the time off code type. The three pay type codes available to pay out from an employee's Time Off Bank balance are: Holiday (H), Vacation (V) and Sick (S).

Pay check label
After selecting a pay type, enter the corresponding label you want to appear on paychecks (for example, "PTO"), or accept the default.

Accrual method
Pay types included in hourly accrual
If Pay cycle is selected, the vacation, holiday, and sick hours will accrue according to the [Vacation, Holiday, Sick Pay Cycle Accrual Hierarchy](/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/vacation-holiday-sick-pay-cycle-accrual-hierarchy).
If Hourly is selected, you can select which pay types to include in the hourly accrual:

- Regular

- Overtime

- Double time

- Vacation

- Holiday

- Sick

Accrual details

Accrual rate
Enter the rate at which this benefit is accrued (Hourly or per Pay cycle). The rate should be the number of pay periods per year divided into the accrual limit. Accrual rates of up to 999.99999 are allowed.
For example, using the Pay cycle accrual method, for employees paid weekly who accrue two weeks (80 hours) of vacation per year, the accrual rate is 1.538 hours per week (80 hours¸ 52 weeks = 1.538 hrs/wk).

Limit per year
Enter the number of benefit hours representing the maximum that it is possible to accrue per calendar year. For example, in businesses with 40-hour work weeks, a one week vacation would equal a 40-hour limit. By setting this limit, it is assured that the employee will not accrue more hours than he or she is entitled to, even if an extra check run is processed (such as for a bonus) during the year. This limit applies to the Year-to-date earned field on the Employee Time Off Bank screen.

Accrual details

Set to zero anniversary? (use it or lose it)
Select this checkbox if the selected time off balance resets to zero at the employee's anniversary date (as entered in the Anniversary field on the Employee Time Off Bank screen).

Suspend accrual if balance over limit?
Select this checkbox to define the limit at which accruals stop accumulating. When this checkbox is selected the Balance limit field will display, allowing the Payroll Administrator to set the accrual limit. The accrual calculations performed during the Payroll cycle will be enhanced to cap earned amounts when the employee's 'Bank balance' exceeds the specified level.

Employment eligibility

# months for eligibility
Enter the number of months the employee must be employed (that is, the number of
 months from the Original hire
 date or the Latest rehire date field, whichever is later, on the
 Employee Main Properties screen) before becoming eligible for accrual of
 this benefit. For example, if the policy is that the new employee earns one
 week the first year but isn't allowed to take any vacation until after six
 months, the accrual should commence at once(in other words, this field
 should be set to zero) so that after one year, 40 hours will be earned.

Use only once?
If the time off code is to be used only once, select this checkbox. For example, if employees earn one week of vacation after six months of employment, and thereafter earn two weeks of vacation, the code assigned to the "one week after six months" condition would only be used once for each employee (for example, V1 in the above example). After that, the code for "two weeks after one year," which must also be defined in this screen, would be used to figure the employee's eligibility for vacation time. That code should be entered in the Next time off code field.
This option also requires that the limit is reached before changing to the next code.

Next time off code
Enter the next time off code to be used when the Use only once? checkbox is selected.
