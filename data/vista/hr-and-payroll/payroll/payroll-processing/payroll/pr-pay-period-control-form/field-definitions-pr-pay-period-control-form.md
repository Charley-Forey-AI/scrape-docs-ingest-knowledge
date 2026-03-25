---
title: "Field Definitions: PR Pay Period Control Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-pay-period-control-form/field-definitions-pr-pay-period-control-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-pay-period-control-form/field-definitions-pr-pay-period-control-form"
---

# Field Definitions: PR Pay Period Control Form

The following is a list of field descriptions for the PR Pay
 Period Control form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## PR Group

Enter the payroll group that you are setting
 up the pay period for. Press F4 for a list of valid groups from PR
 Groups.

## Pay Period Ending Date

Initially defaults the last accessed pay period for the current user.
Enter the date that will be used to identify this pay period for the PR Group. Generally this is the last day of the pay period.

## Beginning Date

Enter the first date of the pay period; the date
 must be equal to or earlier than the date that you enter in the Pay Period Ending
 Date field. A warning displays for timecards posted to this pay period
 that fall outside this range of dates.

## Expensed and/or Paid in More Than One Month

Check this box if this pay period’s expenses and/or payments will be posted in more than a single month. For example, if the end of a month falls in the middle of a week, you may have earnings from the first part of the week expensed to Job Cost in the first month and earnings from the remainder of the week expensed in the second month.
Do not check this box if this pay period's
 expenses and/or payments will be posted in one month. When unchecked, all earnings and
 payments will be posted in the first Month, and the system disables the 2nd Month,
 Cutoff
 Date, and Limit Month fields.

[](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-split-month-pay-periods)Setting Up a Split-Month Pay Period

## 1st Month

Enter a month that is open in the PR GL company. All timecard batches posted to this pay period must use this month, unless this is a split-month pay period where earnings may be expensed in both the first and second months. Payments may use either the first or second month. This field cannot be changed if non-interfaced payments exist for the pay period.

## 2nd Month

For split-month pay periods only. The system
 displays this field when you check the Expensed and/or Paid in More Than One
 Month box.
Enter the second month in which expenses or
 payments will be posted for this pay period. The month must be open in the PR GL company,
 and must be one month later than the date in the 1st Month field.
It is important to correctly identify the month the checks are paid in since this determines the month the Employee Accumulations are updated. The date of the check should be posted to the calendar month paid to comply with IRS regulations. This affects the month reported on Quarterly taxes.

## Cutoff Date

For split-month pay periods only. The system
 enables this box when you check the Expensed and/or Paid in More Than One
 Month box.
Enter the last day to include in the first
 accounting month. This date will be compared to the timecard date when determining to which
 month expenses or payments will be posted. For example, if you entered 03/02/XX in the
 Pay Period
 Ending Date field, 02/24/XX in the Beginning Date field, and 02/28/XX in the
 Cutoff
 Date field, all expenses posted on or before 02/28/XX will be posted to
 month 02/XX. All expenses posted after 02/28/XX will be posted to month 03/XX. If you enter
 a cutoff date that is prior to the beginning date (e.g., 02/23/XX), all expenses posted on
 or after 02/24/XX will be posted to month 03/XX. The expenses posted to the first month
 will include the wage and burden expenses for the hours worked through the cut off
 date.

## Limit Month

Enter the month to be used when applying monthly deduction and liability limits. If this is a single-month pay period, this field defaults the first month and cannot be changed. If this is a split-month pay period, this field defaults the second month, which can be overridden.
Note: Monthly limits are applied using amounts from the current pay period and sequence, earlier sequences within the same pay period, and previous pay periods that used the same limit month. Monthly limits are not applied based on employee accumulations.

## Standard Hours

Enter the total number of straight time hours in the Pay Period. Typically, this value is 40 for weekly and 80 for biweekly. This field is used to calculate rate per hour Automatic Earnings and for tracking unemployment hours (as required in a few states).

## Standard Days

Enter the total number of working days in the
 Pay Period. This field is used to calculate rate per day automatic earnings (if you checked
 the Posting to
 All box in PR Employees, Add'l Info tab) and rate per day deductions and
 liabilities.

## Standard Weeks

Enter the total number of weeks for the Pay Period. This field updates accumulations for state unemployment reporting.
Note: If you are tracking SUTA based on 'weeks worked', entry in this field must be greater than 0.

## Maximum Regular Hours in Week 1

This field is enabled for weekly and bi-weekly pay periods.
Enter the maximum number of regular hours for the week; this field initially defaults to 40.00 for U.S. and Australian users and to 0.00 for Canadian users.
You can use this field to compute automatic overtime pay for holiday weeks. For example, an employer might pay overtime based on 32 hours for the week; so, any additional hours are paid as overtime.

## Maximum Regular Hours in Week 2

This field is enabled for bi-weekly pay periods.
Enter the maximum number of regular hours for the week; this field initially defaults to 40.00 for U.S. and Australian users and to 0.00 for Canadian users.
You can use this field to compute automatic overtime pay for holiday weeks. For example, an employer might pay overtime based on 32 hours for the week; so, any additional hours are paid as overtime.

## Number of Payments Covered

This field appears for Australian companies only.
Enter the number of payments to be made during
 this pay period. This field initially defaults to 1, but you can change this field if you
 are paying employees more than once due to time off that crosses pay periods.
When you specify more than one payment, the system withholds the correct amount and prevents unwanted overstatement of PAYG withholding due to a higher payment for the pay period.
The value that you enter in this field
 defaults automatically for employee records in the Number of Payments Covered field in PR
 Employee Pay Seq Control, where you can override the value as necessary.

## In Use By

This field displays the user who is currently using the pay period during an update (PR Ledger Update and PR AP Update) or during a check print run (PR Check Print). When a user name displays here, no other user may access the pay period. The system clears this field once the update or check print is complete.
Note: To unlock the pay period, clear this field. Only the displayed user can clear this field.

## Pay Seq

When adding a new pay period, this field defaults to 1, and the Description field defaults to Sequence #1. You can override the Description field, but the sequence number cannot be changed.
Additional sequences may be added as necessary. Sequence numbers can be between 1 and 255. It is important to set up the proper sequence numbers here before processing a payroll because deductions and liabilities, automatic earnings, etc., can be limited to calculate on certain Payment Sequences.
Note: If tracking SUTA based on 'weeks worked', subject weeks are only reported for employees accruing under Pay Seq #1.

## Description

Enter a description of this payment sequence, to be used on reports (e.g., Regular Payroll, Layoff, Bonus, etc.). This field defaults to "Sequence #1" for the initial payment sequence.

## Bonus

The Bonus checkbox on the PR Pay Period Control form, Payment Sequence tab.
Select this checkbox if this is a bonus payment sequence.
For US users:You must have set up any associated deductions to calculate as a rate of gross for bonus sequences in PR Deductions and Liabilities (that is, selected the Calculate as Rate of Gross on Bonus Seq checkbox and entered a rate entered in the Bonus Rate field).For Canadian users:Selecting this checkbox triggers a special bonus tax routine during processing to calculate Federal and Provincial taxes. Therefore, in order for taxes to be calculated correctly on a bonus, it is necessary that you set up a separate payment sequence for the bonus (such as sequence #2) and select this checkbox for that pay sequence.Note: The system calculates bonus tax by taking the difference of the tax on (salary + previous bonuses / # of pay periods per year + current bonus) less the tax on (salary + previous bonuses / # of pay periods per year). The difference is then multiplied by the # of pay periods per year.

Related information

- [Set Up Payment Sequences for a Pay Period](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-payment-sequences-for-a-pay-period)

- [PR Pay Period Control Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-pay-period-control-form)

## OverrideDirDep

Check this box if you want to issue checks for all employees that normally receive direct deposits. Employees that already receive checks are unaffected by this selection.
Note: If you only want to override the direct deposit for a
 specific employee, override the payment method ain PR Employees (select the Not Used option
 from the Direct Deposit section, Direct Deposit tab).
Do not check this box if all employees will be paid by their regular payment method for this pay sequence.
Note: If you change the setting of this checkbox after timecards have been posted, a message displays as follows:

- If you check the box, and there are direct deposit employees for the pay period and pay sequence, the message displays as: "Change payment method to 'Check' on all unpaid earnings in this Pay Period and Sequence? Affected employees must be reprocessed."

- If you uncheck this box, the message displays as: "Change payment method back to employee’s default on all unpaid earnings in this Pay Period and Sequence? Affected employees must be reprocessed."

In both cases, the system updates the
 Payment
 Method field in PR Employee Pay Seq Control accordingly, and the system sets
 the sequence to not processed.

## Frequency

Enter a valid frequency code that will be active for the pay period. These codes identify which Automatic Earnings to post and which Employee-based deductions and liabilities to calculate. The description field is display only.
Adding or removing Frequency Codes from the grid after Automatic Earnings are posted or deductions and liabilities are calculated will have no effect, unless the PR Post Automatic Earnings or PR Payroll Process forms are rerun.

## Holiday

Enter a holiday date for automatic overtime calculations.
The holidays you specify here are used for overtime calculations when the overtime schedule indicates holiday pay is to be included.
Note: If an employee has a craft-type overtime schedule, the
 craft holidays will also be used (timecard must be posted to a craft, the employee must be
 assigned an overtime type of "Craft" (the Overtime field in PR Employees, Add'l
 Info tab, is set to C-Craft), and the craft must be assigned an overtime schedule).

## Apply to Craft

Check this box if all employees (craft and non-craft) should be paid
 overtime for the holiday (if worked). For craft employees, the holiday is paid in addition
 to any other holidays defined for the craft.
If you do not check this box, then only
 non-craft employees will be paid overtime for the holiday (if worked). Craft employees will
 only be paid overtime for the holiday if the holiday is defined for the employee's craft in
 PR Crafts.
Note: To set up a craft employee for this feature, select
 C-Craft from the Overtime field in PR Employees (Add'l
 Info tab). Employees with any other overtime method are considered 'non-craft'
 employees.
