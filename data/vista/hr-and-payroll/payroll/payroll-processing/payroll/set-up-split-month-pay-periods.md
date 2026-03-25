---
title: "Set Up Split-Month Pay Periods | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-split-month-pay-periods"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-split-month-pay-periods"
---

# Set Up Split-Month Pay Periods

You will use the PR Pay Period Control form to set up split-month pay periods.
Split-month pay periods cross over two accounting periods (months). When setting up a split-month pay period, you will need to specify the first and second months of the pay period, as well as a cut off date to indicate the last day of the first month.
You will create a pay period for each of your payroll groups. Multiple payroll groups cannot share a single pay period, so you must set up a different pay period for each group.
The following instructions detail how to set up a split-month pay period.

1. In the PR Group field, enter the payroll group number. Press F4 to see a list of valid payroll groups.

1. In the Pay Period Ending Date field, enter the last day in the pay period. Optionally, click the calendar button () to display a calendar and select the correct date.

1. Enter the first date of the pay period in the Beginning Date field. Optionally, you can click the calendar button to display a calendar and select the correct date.

1. Check the Expensed and/or Paid in More Than One Month box. This indicates that some expenses may be in the first or second month of the period, or all expenses occur in the first month and are being paid in the second month. 

1. In the 1st Month field, enter the month and year for the first month of the pay period in the MM/YY format. Note: This field defaults to the same month and year as the beginning date.

1. In the 2nd Month field, enter the month and year for the second month of the pay period in the MM/YY format. Note: This field defaults to the second month (the month specified in the Pay Period Ending Date field.

1. In the Cutoff Date field, enter the last date of the first month.

1. In the Limit Month field, enter the month that the system will use to apply monthly deduction and liability limits, using the MM/YY format.

1. Enter the total number of hours, days, and weeks for the pay period in the Standard Hours, Standard Days, and Standard Hours fields, respectively. Note: The system uses the amount in the Standard Hours field to calculate the rate per hour automatic earnings; the Standard Days field to calculate rate per day automatic earnings (if you checked the Posting to All box in PR Employees, Add'l Info tab) and rate per day deductions and liabilities; and the Standard Weeks field to update accumulations for state unemployment reporting.

1. If this is a weekly pay period, enter the maximum regular hours that employees can work for this pay period in the Maximum Regular Hours in Week 1 field. If this is a bi-weekly pay period, enter the maximum regular hours that employees can work for the first week in the pay period in the Maximum Regular Hours in Week 1 field, and enter the maximum number for the second week in the Maximum Regular Hours in Week 2 field.
You will typically adjust amounts in these fields when a holiday occurs during this pay period. See [Setting Holiday Week Overtime ](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-holiday-week-overtime) for more information.
Note: Both the Maximum Regular Hours in Week 1 and the Maximum Regular Hours in Week 2 fields are only enabled for weekly and bi-weekly pay periods.

1. Australian users: If you need to make more than one payment for this pay period, enter the number of payments in the Number of Payments Covered field. If you enter more than 1 in this field, the system will properly withhold tax for both payments and not withhold PAYG at a higher rate. For more information, see [Number of Payments Covered](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-pay-period-control-form/field-definitions-pr-pay-period-control-form#ID-00039a86--en).

1. [Set up the pay sequences for this pay period](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-payment-sequences-for-a-pay-period) on the Payment Seq tab.

1. [Set up the frequency codes for this pay period](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-setting-up-frequency-codes-for-a-pay-period) on the Active Frequency Codes tab.

1. [Set up any applicable holidays for the pay period](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-setting-holidays-for-pay-periods) on the Holidays tab.

1. Save the pay period record as normal. The system now displays an "Open" message next to the Pay Period Ending Date field and you can now [post time to the open pay period](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/processing-payroll/processing-a-payroll-period).

Related information

- [PR Pay Period Control Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-pay-period-control-form)

- [Interfacing Split-Month Pay Periods to GL](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-syncing-payroll-with-the-general-ledger/interfacing-split-month-pay-periods-to-gl)

- [Set Up Single-Month Pay Periods](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-single-month-pay-periods)

- [Processing Payroll](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/processing-payroll)
