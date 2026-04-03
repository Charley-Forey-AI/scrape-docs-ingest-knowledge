---
title: "Replacement Check Entry | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/employees/employee-entry/replacement-check-entry"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/employees/employee-entry/replacement-check-entry"
---

# Replacement Check Entry

Use this screen to re-issue a lost Payroll check, manual
 check, or auto-deposit check without having to manually void and re-enter a new check
 (provided a corresponding void entry does not already exist in the earnings history file for
 the same check number).
When you enter the original check number for the employee, the application automatically
 creates a voided check and assigns a new manual check number, so you do not need to copy any
 data from the original check. The software validates the employee and original check
 number with the Cash Management module (if installed) or the check reconciliation file in
 order to make sure the check has not been cashed or voided. The new check is flagged as a
 replacement check and will calculate exactly the same as the original check for gross pay,
 add-on amounts, deduction amounts, and tax amounts. Year-to-date totals will be current
 (updated) year-to-date totals.
For checks with add-on or deduction year-to-date balances, the application displays these balances on each check, even if there is no add-on or deduction on the current check. If there are more add-ons and deductions than will fit on the pay stub, the additional amounts are summarized under the classification of OTHER. Benefit totals are obtained from the Payroll Time Off Bank Log Table using the check date for 'YTD Earned'.
State Disability Insurance (SDI) and Resident Worker's Compensation amounts are listed separately on this report.
Important: Run the replacement check in its own
 payment cycle. If the replacement check is processed with other checks, it creates a
 combination of the previous week's auto deposit file and the current week's auto deposit
 amount in Cash Management, causing them to be out of balance.

## Information Flow

After the replacement check fields have been recorded, the Preview and Export buttons can be used
 to update to Pre-Time Card Entry. An Update to the Pre-Time Card Entry window allows you to
 Continue or Reprint (which
 returns you to the main screen and a Delete button becomes available).

- Manual replacement checks and their void counterpart time card
 lines are given a non-certified status, even if the original check was for certified
 work. This assures that only one check appears on the Certified Payroll Report for
 the work performed, even if the replacement check is issued with the same check date
 as the original, or is processed weeks or months later.

- When Void checks for auto-deposit checks are created in this
 screen, the Cash in bank G/L account
 code (specified in Payroll Installation or Cash Management
 Installation) is the Automatic deposit
 liability G/L account code (specified in Payroll Installation).

- If the Cash Management module is installed and the  Post payroll transactions checkbox is selected in Cash Management Installation, a Bank account field is available on
 this screen and the check number window displays based on the bank account entry
 instead of the default bank account. Note: If the Display
 accumulated balance on paycheck? option is selected in the [New/Edit Deduction/Add-on Code - Properties](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---properties) screen, the accumulated balance displays in the
 'Add-ons' and 'Deductions' boxes instead of in the Year To Date amounts.

Related information

- [Creating a Replacement Check](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/checks--auto-deposit-procedures/creating-a-replacement-check)

- [Worker's Compensation Limit Hierarchy](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/wage-code-file-maintenance/workers-compensation-limit-hierarchy)
