---
title: "Field Definitions: PR Leave Code Reset Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-code-reset-form/field-definitions-pr-leave-code-reset-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-code-reset-form/field-definitions-pr-leave-code-reset-form"
---

# Field Definitions: PR Leave Code Reset Form

The following is a list of field descriptions for the PR
 Leave Code Reset form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Reset Accrual Amounts to 0.00 hours for the next frequency period

The Reset Accrual Amounts to 0.00 hours for the next frequency period checkbox on the PR Leave Code Reset form.
Select this checkbox to reset amounts for the two accrual limits in PR Employee Leave to 0.00 for the next frequency period. You can only perform a reset if there are no open or unprocessed leave batches for the current PR
 Company.

##  Reset Available Balances to Carryover Limit

The Reset Available Balances to Carryover Limit checkbox on the PR Leave Code Reset form.

 Select this checkbox to reset available balance limits to the Carryover Limit specified in PR Leave Codes or the Carryover Employee Override specified in PR  Employee Leave. You can only perform a reset if there are no open or unprocessed Leave batches for the current PR
 Company.

Note: The system sets all negative leave balances to 0.00 during the reset process.

##  Reset Date

The Reset Date field on the PR Leave Code Reset form.
 Enter the reset date (must be greater than the Last Reset date in PR Employee Leave). All Leave History posted on or before this date is ignored when updating current balances and available amount.

##  Leave Code Option

The Leave Code option on the PR Leave Code Reset form.
This field is enabled once you select a Reset Type.

- All – Select this option to reset the Accrual Limits and/or Available Balance Limits for all leave codes.

- Leave Code – Select this option to reset the Accrual Limits and/or Available Balance
 Limit for a specific leave code (indicated to the right).

##  Leave Code

The Leave Code field on the PR Leave Code Reset form.
This field is enabled once you specify a Reset Type and then select the Leave Code option.

Enter the leave code for resetting the Accrual Limits and/or Available
 Balance Limits. Leave code must be set as Active in PR Leave Codes. If you enter an inactive leave code, an error displays and you must enter an active code before proceeding. Press F4 for a list of valid leave codes.Note: If you elected to perform a reset for all leave codes, the reset process will skip all inactive leave codes; that is, leave codes that are flagged as inactive in PR Leave Codes and/or PR Employee Leave.

## Frequency Option

The Frequency option on the PR Leave Code Reset form.
This field is enabled once you select a Reset Type.

- All - Select this option to reset the Accrual Limits and/or Available Balance Limits for all frequency codes.

- Frequency - Select this option to reset the Accrual Limits and/or Available Balance Limit for a specific frequency code (indicated to the right).

##  Frequency

The Frequency field on the PR Leave Code Reset form.
This field is enabled once you specify a Reset Type and then select the Frequency option.
Enter the frequency for resetting the Accrual Limits and/or Available Balance Limits. Press F4 for a list of valid frequencies.

## Employee Option

The Employee option on the PR Leave Code Reset form.
This field is enabled once you select a Reset Type.

- All –
 Select this option to reset the Accrual Limits and/or Available Balance
 Limits for all employees.

- Employee –
 Select this option to reset the Accrual Limits and/or Available Balance
 Limit for a specific employee (indicated to the right).

## Employee

The Employee field on the PR Leave Code Reset form.
This field is enabled once you specify a Reset Type and then select the Employee option.
Enter the employee for which you are resetting Accrual Limits and/or Available
 Balance Limits. Employee must be set as Active in PR Employees. Press F4 to select from a list of employees.

##  Delete any reset transactions currently posted to this date

The Delete any reset transactions currently posted to this date field on the PR Leave Code Reset form.

 Select this checkbox to 'reverse' leave reset transactions. The Reset Date
 specified above must match the Reset Date of the original reset
 transactions. The reset process pulls
 the previously reset transactions into a new batch and flags all of the
 transactions for deletion. When the batch is processed, all reset
 transactions in the batch are removed from the Leave History
 table, the 'Last Date Reset' (in PR Employee Leave) sets to null, and the
 Accrual Limits and Available Balance Limits are set to the previous
 values.

 If you are running a normal leave reset, do not select this checkbox.
Note: During the reset process, the system skips all previously posted reset transactions that reference an inactive leave code (that is, a leave code flagged as inactive in PR Leave Codes and/or PR Employee Leave).
