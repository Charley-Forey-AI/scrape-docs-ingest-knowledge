---
title: "Field Definitions: PR Leave Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-codes-form/field-definitions-pr-leave-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-codes-form/field-definitions-pr-leave-codes-form"
---

# Field Definitions: PR Leave Codes Form

The following is a list of field descriptions for the PR
 Leave Codes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Leave Code

 Enter a unique 10-character alphanumeric code to identify a leave code. These codes identify leave types, such as vacation, sick, personal time.

##  Description

 Enter a description for this leave code, which will be used on forms and reports.
For Canadian users
If you want the descriptions on the pay stubs to appear in French and English, make sure that this field includes both French and English.
You should not create separate leave codes for French and English. Instead, create a bilingual description for the codes you want to use on the bilingual stubs.

##  Unit of Measure

 Enter a valid unit of measure (HQ Units of Measure) used to track accumulated units for this leave code. This field will typically be hours.

## Leave Balance Warning Level

Leave Balance Warning Level field on PR Leave Codes form
By setting alert options, you can identify and
 prevent employee timecard and leave usage issues that may occur if an employee exceeds a
 given available leave balance. This option determines how the system processes a leave
 entry batch. You can override this setting at the employee level by using the Leave Balance Warning
 Level field on the PR Employee Leave form.
Choose from one of the following alert options:

- Allowed w/Warning - If you select this option and the employee has a negative leave balance, with no other errors during batch validation, the system displays an error message on the HQ Batch Control Error List report, but you can then post the batch.
Important:

- These warnings are only accurate if you run PR Auto Leave Accrual/Usage after every payroll; if this is not part of your normal payroll workflow, we recommend leaving this field at its default setting of Allowed w/o Warning.

- Allowed w/o Warning - If you select this option and the employee has a negative leave balance, with no other errors during batch validation, the system does not display an error message on the HQ Batch Control Error List report and you can then post the batch.

- Not Allowed - If you select this option and the employee has a negative leave balance, the system displays an error message on the HQ Batch Control Error List report and then you will be unable to post the batch.

## Accrual Type

Indicate how accruals are calculated for this
 leave code.
Fixed Amount - Select
 this option if accruals are calculated for this leave code on a fixed basis, using the
 Fixed Accrual Units and Accrual Frequency specified below. Using this option means all
 employees with this leave code will accrue a fixed amount (typically hours) when the PR
 Auto Leave Accrual/Usage form is run. An example might be hours of vacation accrued
 annually. When the Auto Leave Accrual/Usage form is run for the “Annual” frequency, each
 employee assigned this leave code would have a leave detail entry created for the fixed
 amount of hours which will update their Accrual Limits #1, #2, and Available Balance (up to
 their limits).
Rate of Earnings or
 Hours – Select this option if accruals are calculated for this leave code on
 a rate of earnings or hours, using the Earn Codes, Basis, and Rates specified in the grid
 below. Only Earn codes identified as “Accrual” Types will be used.
Note: Leave Level overrides only apply to leave codes whose Accrual Type is set to
 Rate of Earnings or Hours. They do not apply to leave codes whose
 Accrual Type is set to Fixed Amount.

##  Fixed Accruals: Amount

 Enter the number of units that will be accrued for this leave code on a regular basis. For example, if an employee is to accrue 8.00 hours each month, enter 8.00 here. This field is disabled if the accrual type is rate based.

##  Fixed Accruals: Frequency

 Enter a valid frequency code to indicate how often the accrual units are calculated (e.g. hourly, daily, monthly, or yearly). This field is disabled if the Accrual Type is rate based.

## Accrual Limit # 1 & 2: Limit

These accrual limits allow you to track accruals for two different time frames, such as monthly and yearly.
For each accrual limit, enter the maximum number of units that can be accumulated during the time frame specified in the Reset Frequency field.

## Accrual Limit # 1 & 2: Reset Frequency

For each accrual limit, enter the frequency code that indicates how often the accumulated units should be reset to 0.00. Press F4 for a list of valid frequency codes
For example, if you are tracking monthly and yearly accruals, set the reset frequency to “Month” for accrual limit #1, and to “Year” for accrual limit #2.

##  Limit

 Enter the maximum number of units allowed for this leave code at any one time. Enter 0.00 if there is no limit.

##  Reset Frequency

 Enter a valid frequency code to indicate how often the available balance should be reset. Leave this field blank if no reset is to occur.

##  Carryover Limit

 Enter the maximum number of units that can be carried over when the available balance is reset. For example, if a maximum of 40 hours of vacation can be carried over annually, then set the Carryover Limit to 40. When the annual reset is run, employees having more than 40 hours of vacation available will have their balance reduced to 40. Those with less than 40 hours will be unchanged. Set to 0.00 if no carryover is allowed.

## Active

The Active checkbox on the PR Leave Codes form, Info tab.
This checkbox is automatically selected when adding a new leave code.
You can deselect this checkbox if you are not ready to activate the leave code; however, you must activate the leave code before you can assign it to employees in PR Employee Leave.
If this is an existing code, you can deselect this checkbox to deactivate the leave code. If there are active employees associated the leave code (in PR Employee Leave), a message displays alerting you to the number of active employees and prompting you to deactivate the employee leave codes. If you select OK, the system deactivates the leave code for all applicable employees.
Note: If you later reactivate the leave code, you must manually reactivate the leave code for any associated employees in PR Employee Leave.

##  Earn Code

 Enter a valid earnings code that will be used as a basis to calculate accruals on rate-based leave codes or to track leave code usage.

## Type

Specify whether the earnings code is an (A)ccrual or (U)sage type. For instance, regular earnings might be set up as an accrual type with a rate of .1 hours earned for one basis hour worked. A vacation earnings code might then be set up as a usage type with a rate of 1.0 hour’s usage for each 1.0 hour posted.
Note: If you want to track both accrual and usage for an earnings code, you can set up the earnings code with both Accrual and Usage entries in the grid; however, only earnings codes with an Accrual Type of 'Rate of Earnings or Hours' can be set up in this grid as an Accrual.

## Basis

Enter the basis for usage or accrual calculations.

- A-Amount – Calculations will be based on the earnings amount.

- H-Hours – Calculations will be based on hours.

##  Rate

 Enter the rate at which to calculate accrual or usage. Typically, the rate for usage will be 1.00.

## Earn Code

Earn Code field in the PR Leave Codes form, Leave Level Overrides tab
Enter an Earnings Code that you want to assign a different leave rate to. Press F4 to select from a list.
In conjunction with your entry in the Leave
 Level field, and when the Leave Level
 code is inserted at the job/project level (PR Info tab on either
 PM Projects or JC Jobs form), that job/project can refer to the
 value you enter in the Rate
 field.
Note: Leave Level overrides only apply to leave codes whose Accrual Type is set to Rate of Earnings or Hours. They do not apply to leave codes whose Accrual Type is set to Fixed Amount.

## Leave Level

Leave Level field in the PR Leave Codes form, Leave Level Overrides tab
Enter the Leave Level code that you want to associate to this earnings code. Press F4 to select from a list.
In conjunction with your entry in the Earn
 Code field, and when this Leave Level
 code is inserted at the job/project level (PR Info tab on either
 PM Projects or JC Jobs form), that job/project can refer to the
 value you enter in the Rate
 field.
When you process PR Auto Leave, the system compares the following two rates and uses the highest of the two in leave accrual calculations:

- the rate set for the employee in the PR Employee Leave form, or if there is not one there, the PR Leave Codes form

- the rate associated with the leave level code (as set in the PR Leave Codes form, Leave Level Overrides tab)

If the job leave rate happens to be the highest of the two, the amount of leave accrued by the employee is also based on how much they worked on the job. Note: Job-specific Leave Level overrides affect only *accruals* . These accruals cannot override limits, nor do they impact frequencies or usage.

## Basis

Basis field in the PR Leave Codes form, Leave Level Overrides tab
Enter the basis for accrual calculations.

- A-Amount – Calculations are based on the earnings amount.

- H-Hours – Calculations are based on hours.

## Rate

Rate field in the PR Leave Codes form, Leave Level Overrides tab

 Enter the rate the system should use to calculate leave accrual for this Leave Level code.
