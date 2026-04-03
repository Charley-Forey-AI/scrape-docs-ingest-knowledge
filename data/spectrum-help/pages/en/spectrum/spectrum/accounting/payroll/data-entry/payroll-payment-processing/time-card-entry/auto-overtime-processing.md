---
title: "Auto-Overtime Processing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/auto-overtime-processing"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/auto-overtime-processing"
---

# Auto-Overtime Processing

There are a few key points that you will want to keep in mind when using auto-overtime.
To be eligible to be converted to overtime, the following rules are in place:

- Only Regular checks are eligible to be converted. Manual and Void checks are excluded from this process.

- R (Regular), ER
 (Equipment Regular), SR (Special Regular),
 O (Overtime) and EO
 (Equipment Overtime) pay types are included in auto-overtime processing.
 All other pay types will be ignored during the update. If the Exclude SR (special rate) pay type
 from calculations checkbox is selected, all pay types with
 SR pay rates will be added to the list of disqualifying time cards.

- Only time card records with a 'Work date' will be processed. Records that do not contain a date will be excluded.

- Time cards will be processed in 'Work date' order. When multiple time cards have been entered for the same 'Work date', the system will process these in the order that they were entered into the system.

- The software will keep track of regular hours worked within a seven-day period. The software can handle multi-week payrolls by restarting the week-to-date tally when encountering a time card dated later than the seven-day period. Overtime rates will be applied to the 'converted' hours during processing, plus double time rates for Saturday or Sunday, when applicable.

- The calculations and determination of overtime will be performed by 'Check sequence'. This means that each check stands alone in the daily and weekly calculations.

- When converting records to overtime, the overtime rate from the Wage Code, Union, Pay Group or Employee file will be used.

- A report is provided during the update process to allow you to review the changes the system is about to make. Pay close attention to the messages as they will indicate when records have been changed.

- If the Workflow module is serialized and you are using the Time Card Approval Workflow, the Auto-Overtime Update will convert (R)egular time to (O)vertime when the limits are reached. This occurs even when the Workflow has finished and the records are locked. By rule, (O)vertime records that are created as part of the update do not go through Workflow once again. The thought process here is that the employees hours were approved, not the rate of pay. Organizations that want to approve both the hours and rate of pay will want to perform the Auto-Overtime Update before the reviewers start to approve time.

## How to Use Auto-Overtime

1. Enter all time in using the R
 (Regular), ER (Equipment Regular) and
 SR (Special Regular) pay types.

1. After entering all time, click the Auto-OT option on the Command Bar. This option is available in both Pre-Time Card Entry and in Time Card Entry. In Pre-Time Card Entry, the user is prompted to select the appropriate Batch code to process.

1. Select whether to Exclude SR (special rate) pay type from calculations to add SR pay types to the list of disqualifying time cards.

1. Click Preview to see the [Auto Overtime Edit Listing](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/auto-overtime-edit-listing).

1. Review the Overtime Allocation
 column to see which records have been changed.

1. Click Continue to update the changes.

## Setting up Overtime Rules

Overtime rules are defined on the Federal and State/Province tax codes. While you can enter overtime rules on local tax codes, the system will not use these rules during the update.

1. Navigate to Payroll > Maintenance > [Tax Table Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance).

1. Enter your Federal tax code and click on the
 Overtime Rules tab.

1. Enter the number of hours in the Daily overtime
 starts after field. Blank is a valid answer.

1. Enter the number of hours in the Weekly
 overtime starts after field. Blank is a valid answer here as
 well.

1. Click OK to save your work.
Note: Perform steps 1-5 to enter the overtime rules for
 the States or Provinces your company performs work in.

Related information

- [Auto-Overtime Hierarchy](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/new-edit-tax-table---overtime-rules/auto-overtime-hierarchy)
