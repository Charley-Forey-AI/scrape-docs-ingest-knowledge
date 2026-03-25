---
title: "Field Definitions: PR Employee Leave Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-leave-form/field-definitions-pr-employee-leave-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-leave-form/field-definitions-pr-employee-leave-form"
---

# Field Definitions: PR Employee Leave Form

The following is a list of field descriptions for the PR
 Employee Leave form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Employee

The Employee field on the PR Employee Leave form.
Enter the employee for which to add or edit leave records. You may select an inactive employee; however, only active employees accrue leave units.

## Leave Balance Warning Level

The Leave Balance Warning Level field on the PR Employee Leave form, Info tab.
By setting alert options, you can identify and prevent employee timecard and leave usage issues that may occur if an employee exceeds a given available leave balance. This option determines how the system processes a leave entry batch.
Choose from one of the following alert options:

- Allowed w/Warning - If you select this option and the employee has a negative leave balance, with no other errors during batch validation, the system displays an error message on the HQ Batch Control Error List report; however, you can still post the batch.Important: These warnings are only accurate if you run PR Auto Leave Accrual/Usage after every payroll; if this is not part of your normal payroll workflow, we recommend leaving the field blank or setting it to Allowed w/o Warning.

- Allowed w/o Warning - If you select this option and the employee has a negative leave balance, with no other errors during batch validation, no error message is displayed on the HQ Batch Control Error List report and you can post the batch.

- Not Allowed - If you select this option and the employee has a negative leave balance, the system displays an error message on the HQ Batch Control Error List report and you will be unable to post the batch.

## Leave Code

The Leave Code field on the PR Employee Leave form.
Enter a valid, active leave code as set up in PR Leave Codes. The Leave Unit of Measure and Accrual Type display automatically on the form. If an employee/leave code combination is 'in use' by an unposted batch, you cannot make changes until the batch is posted, cleared, or the entry is deleted. If the entry is 'in use', a message displays indicating which batch currently has locked the record. Locking is required to ensure consistent updates to the Current Amounts table in PR Employee Leave.
Note: If you enter an inactive leave code, the description displays "Leave code is inactive" and you will be unable to save the record. If the leave code already exists for the employee, you cannot make any changes to the leave code information, nor can you activate the leave code for the employee in this form. You must reactivate the leave code in PR Leave Codes before reactivating it here.

## Eligible Date

The Eligible Date field on the PR Employee Leave form, Info tab.
Required.
Enter the date that the employee becomes eligible for this leave code. Automatic usage and accrual does not occur before this date.
Note: To inactivate a Leave Code for an employee, the Eligible Date must be dated in the future in PR Employee Leave or it may trigger leave warnings when validating or posting batches.

## Active

The Active checkbox on the PR Employee Leave form, Info tab.
This checkbox is automatically selected when assigning active leave codes to an employee.
You can deselect this checkbox if you are not ready to activate the leave code for this employee; however, you can still set up the leave code information.
Note: Leave codes are automatically deactivated for an employee when you deactivate a leave code in PR Leave Codes after it is assigned to the employee in this form or when you terminate the employee in PR Employees. Once deactivated, you can no longer edit the leave code record. For active employees, if you reactivate a leave code in PR Leave Codes, you must manually reactivate the leave code for the employee here.

## Fixed Accruals: Employee Override Amount

The Fixed Accruals: Employee Override Amount field on the PR Employee Leave form, Info tab.
For Fixed Basis leave codes only.
If you want to override the standard units defined in PR Leave Codes for this leave code (displayed to the left of this field), enter the units for this leave code/employee combination.
Leave this field blank to use the standard units for this employee/leave code.

## Fixed Accruals: Employee Override Frequency

The Fixed Accruals: Employee Override Frequency field on the PR Employee Leave form, Info tab.
For Fixed Basis leave codes only.
If you want to override the standard frequency defined in PR Leave Codes for this leave code (displayed to the left of this field), enter a valid frequency code to indicate how often the accrual units are calculated (such as, hourly, daily, monthly, or yearly) for this leave code/employee combination.
Leave this field blank to use the standard frequency for this employee/leave code.

## Accrual Limit #1: Last Date Reset

The Accrual Limit #1: Last Date Reset field on the PR Employee Leave form, Info tab.
This field is automatically maintained by the system; however, you can override the date (if needed).
When you enter a new employee leave code record in this form, this field defaults the employee's eligible date. Then, when performing accrual resets in PR Leave Code Reset (accessed via PR Leave Entry) for the specified leave code and frequency, the system automatically updates this field based on the specified reset date.
If you run an accrual reset for a frequency other than the standard or override frequency defined for this accrual limit, the system will not update this date during the reset process. For example, say the Accrual Limit #1 frequency is Weekly and the Accrual Limit #2 frequency is Yearly. When you run an accrual reset for the leave code, if you select a Frequency of Yearly, the system resets Accrual Limit #2 only, setting its Last Date Reset to the Reset Date specified in PR Leave Code Reset; no reset is performed for Accrual Limit #1.
Note: If you perform a leave code reset delete (via PR Leave Code Reset), the
 system updates this field to the last reset date or, if no prior reset was
 performed, the employee's eligible date.

## Accrual Limit #1: Employee Override Limit

The Accrual Limit #1: Employee Override Limit field on the PR Employee Leave form, Info tab.
If you want to override the standard limit defined in PR Leave Codes for this leave code (displayed to the left of this field), enter the maximum number of units allowed for this leave code/employee combination for this accumulator.
Leave this field blank to use the standard limit for this employee/leave code/accumulator.

##  Accrual Limit #1: Employee Override Frequency

The Accrual Limit #1: Employee Override Frequency field on the PR Employee Leave form, Info tab.
If you want to override the standard frequency defined in PR Leave Codes for this leave code (displayed to the left of this field), enter a valid frequency code to indicate how often the accumulated units should be reset to 0.00 for this leave code/employee combination.
Leave this field blank to use the standard frequency for this employee/leave code/accumulator.

## Accrual Limit #2: Last Date Reset

The Accrual Limit #2: Last Date Reset field on the PR Employee Leave form, Info tab.
This field is automatically maintained by the system; however, you can override the date (if needed).
When you enter a new employee leave code record in this form, this field defaults the employee's eligible date. Then, when performing accrual resets in PR Leave Code Reset (accessed via PR Leave Entry) for the specified leave code and frequency, the system automatically updates this field based on the specified reset date.
If you run an accrual reset for a frequency other than the standard or override frequency defined for this accrual limit, the system will not update this date during the reset process. For example, say the Accrual Limit #1 frequency is Weekly and the Accrual Limit #2 frequency is Yearly. When you run an accrual reset for the leave code, if you select a Frequency of Weekly, the system resets Accrual Limit #1 only, setting its Last Date Reset to the Reset Date specified in PR Leave Code Reset; no reset is performed for Accrual Limit #2.
Note: If you perform a leave code reset delete (via PR Leave Code
 Reset), the system updates this field to the last reset date or, if no prior reset
 was performed, the employee's eligible date.

## Accrual Limit #2: Employee Override Limit

The Accrual Limit #2: Employee Override Limit field on the PR Employee Leave form, Info tab.
If you want to override the standard limit defined in PR Leave Codes for this leave code (displayed to the left of this field), enter the maximum number of units allowed for this leave code/employee combination for this accumulator.
Leave this field blank to use the standard limit for this employee/leave code/accumulator.

## Accrual Limit #2: Employee Override Frequency

The Accrual Limit #2: Employee Override Frequency field on the PR Employee Leave form, Info tab.
If you want to override the standard frequency defined in PR Leave Codes for this leave code (displayed to the left of this field), enter a valid frequency code to indicate how often the accumulated units should be reset to 0.00 for this leave code/employee combination.
Leave this field blank to use the standard frequency for this employee/leave code/accumulator.

## Balance: Last Date Reset

The Balance: Last Date Reset field on the PR Employee Leave form, Info tab.
This field is automatically maintained by the system; however, you can override the date (if needed).
When you enter a new employee leave record in this form, this field defaults the employee's eligible date. Then, when performing available balance resets in PR Leave Code Reset (accessed via PR Leave Entry) for the specified leave code and frequency, the system automatically updates this field based on the specified reset date.
If you run an available balance reset for a frequency other than the standard or override frequency defined for this employee/leave code, the system will not reset the limit and update this date during the reset process. For example, if the leave code frequency is Yearly, and you run an available balance reset for all leave codes, specifying a frequency of Semi-Annual, the system only updates those leave codes with a Semi-Annual frequency; all leave codes with a frequency of Yearly are skipped.
Note: If you perform a leave code reset delete (via PR Leave Code Reset), the
 system updates this field to the last reset date or, if no prior reset was
 performed, the employee's eligible date.

## Balance: Employee Override Limit

The Balance: Employee Override Limit field on the PR Employee Leave form, Info tab.
If you want to override the standard limit defined in PR Leave Codes for this leave code (displayed to the left of this field), enter the maximum number of units allowed for this leave code/employee combination at any one time.
Leave this field blank to use the standard limit for this employee/leave code.

## Balance: Employee Override Frequency

The Balance: Employee Override Frequency field on the PR Employee Leave form, Info tab.
If you want to override the standard frequency defined in PR Leave Codes for this leave code (displayed to the left of this field), enter a valid frequency code to indicate how often the accumulated units should be reset to 0.00 for this leave code/employee combination.
Leave this field blank to use the standard frequency for this employee/leave code.

##  Balance: Employee Override Carryover

The Balance: Employee Override Carryover field on the PR Employee Leave form, Info tab.
If you want to override the standard carryover limit defined in PR Leave Codes for this leave code (displayed to the left of this field), enter the maximum number of units that can be carried over when the available balance is reset for this leave code/employee combination. Set to 0.00 if no carryover is allowed.
Leave this field blank to use the standard carryover limit for this employee/leave code.

## Earn Code

The Earn Code field on the PR Employee Leave form, Accrual/Usage Override tab.
Specify the earnings code to override. This earnings code is used to calculate accruals on rate-based leave codes or to track leave code usage for this leave code/employee combination. All of the standard earnings code information is used when processing automatic accrual and usage updates unless overridden here.

## Type

The Type field on the PR Employee Leave form, Accrual/Usage Override tab.
Defaults the type for this earnings code as specified for the leave code in PR Leave Codes; may be overridden.

- A-Accrual

- U-Usage

Note: If you are tracking both accrual and usage for an earnings code, you can set up both 'accrual' and 'usage' overrides for an earnings code; however, only earnings codes with an Accrual Type of 'Rate of Earnings or Hours' can be set up in this grid as an Accrual.

## Basis

The Basis field on the PR Employee Leave form, Accrual/Usage Override tab.
Defaults the basis for this earnings code as specified for the leave code in PR Leave Codes; may be overridden.

- A-Amount – Select this option if calculations are based on earnings amount

- H-Hours – Select this option if calculations are based on hours.

## Rate

The Rate field on the PR Employee Leave form, Accrual/Usage Override tab.
Enter the override rate of calculation for accrual or usage. For usage type accruals, this is typically 1.0.
