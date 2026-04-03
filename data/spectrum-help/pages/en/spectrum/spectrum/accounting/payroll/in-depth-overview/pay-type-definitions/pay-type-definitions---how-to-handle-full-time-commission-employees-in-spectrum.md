---
title: "Pay Type Definitions - How to handle full-time commission employees in Spectrum | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/pay-type-definitions/pay-type-definitions---how-to-handle-full-time-commission-employees-in-spectrum"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/pay-type-definitions/pay-type-definitions---how-to-handle-full-time-commission-employees-in-spectrum"
---

# Pay Type Definitions - How to handle full-time commission employees in Spectrum

Follow the steps below to set up full-time commission
 employees.

1. Set up the employee with a pay type of Salary.

1. Enter 0 for the salary and hourly rates.

1. During Time Card Entry, enter the pay type as Regular. The hours entered here will be used in calculating the worker's compensation. When the cursor is at the "rate" column, enter the commission amount. The system will not try to calculate hours against this amount.When a transaction for pay type ER, EO, ED, or EU is added, the software will evaluate whether the equipment code assigned to the time card entry has any active attachments. If so, additional EU time cards will be generated automatically or the Attached Equipment window will display (based on the Automatically add transactions for attached equipment setting in the Equipment Control Installation - Properties screen).
Note: Employee Deductions with tax affects do not reduce the
 subject-to earnings correctly if there is a mixture of taxable and exempt
 earnings. Instead of using Pay types 1, 2, 3 or SA, use a new add-on code with
 appropriate tax effects.
