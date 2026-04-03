---
title: "New/Edit Deduction/Add-on Code - Add-ons - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---add-ons/newedit-deductionadd-on-code---add-ons---field-descriptions"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---add-ons/newedit-deductionadd-on-code---add-ons---field-descriptions"
---

# New/Edit Deduction/Add-on Code - Add-ons - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Direct cost
Select the direct cost type corresponding to the add-on type. This checkbox
 does not display if Payroll Installation is set to
 use pay groups in the current company.
Note: These options display as DISABLED when the Allocate across
 time cards? checkbox is selected on the New/Edit
 Deduction / Add-on Code Properties screen and calculation
 method is set to one of the 'by time card' options.

Gross pay from time cards
Note: This section does NOT display when the Allocate across time
 cards? checkbox is selected on the New/Edit
 Deduction / Add-on Code Properties screen and calculation
 method is set to one of the 'by time card' options.
This calculation method will add vacation pay to each time card line and distribute the vacation expense based on that time card line.This method especially relevant for Canadian employees who must be paid for vacation based on a statutory vacation rate that is either accrued or paid to the employees on their paychecks.
Specify which types of 'direct cost' time card lines to include in the distribution and the applicable 'G/L account code' to debit for each authorized type.

- Non-direct cost?

- Job cost?

- Equipment cost?

- Work order cost?

These checkboxes are selected by default and you are prompted to enter corresponding G/L accounts. The equipment and work order options will be disabled if the Equipment Control and Work Order modules are not installed.
View cost center information: If cost centers are being used, when the G/L
 accounts are specified, the software will assure the user has cost center
 security for the accounts and that the accounts are Active.

Pay union benefits on this add-on?
This flag controls whether union add-ons are taken for "% of gross by time card add-on" time card lines generated for vacation pay. This checkbox will NOT display if Payroll Installation is set to use pay groups in the current company.

Payment options

Paid to employee on this paycheck?
Select the checkbox if this add-on will be on employee paychecks, or leave clear if this is a non-cash add-on. For example, this can be used for accrual of the employer portion of 401(k) amounts.
Add-ons not paid to the employee on the paycheck do not affect subject to wages or the resulting tax computations. This field is not available for deductions.

Print on paycheck?
Select the checkbox if you want this add-on amount to appear on the employee's payroll check.

Post as union fringe to G/L by department?
Select this checkbox for codes not paid to the employee on the paycheck. When
 selected, the portion of the Payroll update that generate entries for
 General Ledger will derive the debit for the union add-on from the
 Department Expense Maintenance screen.

Is this computed as part of D-B/Prevailing wage employer benefit?
If this checkbox is selected, then the computed amount for the prevailing wage or Davis-Bacon jobs will be deducted from the prevailing wage adjustment time card lines and added to the Health & Welfare non-cash add-on code. In other words, the computed amount will be included as part of the employer benefits that have already been calculated in the check calculation for time card lines.
This checkbox displays for all non-cash add-ons only if the Calculate actual pension benefits for
 the D-B/Prevailing wage employer benefit credit checkbox is
 selected in the Payroll Installation > Defaults screen. This prompt is not available for Employer Health
 & Welfare Benefit, Prevailing Wage Adjustment, or Employer Non-stated
 Fringe Benefit calculation methods, or when the Allocate across
 time cards? checkbox is selected..
For an example of how this checkbox can affect calculations, refer to the [Example - Check Calculation for Davis-Bacon and Prevailing Wage Jobs](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults/example---check-calculation-for-davis-bacon-and-prevailing-wage-jobs) topic.

Non-cash G/L account
Enter the G/L account to credit instead of cash (for example, 401(k) payable).
Non-cash add-ons can be used to record employer matching for pension plans. The employee does not receive the cash, but a liability and expense for the employer are recorded in the General Ledger.

Is this for 'payout' from accrued benefit balance?
Select this checkbox if the payout is to come from an accrued benefit. After
 selecting this checkbox, a Related accrual add-on
 field displays an requires you to specify an add-on code from the time card
 file that will be used in the calculation.
