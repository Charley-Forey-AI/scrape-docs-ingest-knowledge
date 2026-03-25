---
title: "Processing a Payroll Period | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/processing-payroll/processing-a-payroll-period"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/processing-payroll/processing-a-payroll-period"
---

# Processing a Payroll Period

You will use PR Payroll Process to process payroll periods.
When processing pay periods, you must process each one individually, so you may need to run through this process multiple times.
You may process a pay period as often as you wish. Any employee already assigned a check number can be reprocessed and the system recalculates the deductions, liabilities, and earnings; however, the system does not adjust the check amount.
Note: If payroll payment sequences are not processed in order, a limit might be exceeded. This typically occurs when processing bonus checks. If a bonus check is processed before regular checks, a limit might be reached in the bonus sequence (e.g., FICA). To avoid this problem, post and process the regular payroll before processing the bonus check sequence. Optionally, put the bonus checks in a separate, one-day pay period with a week ending date less than the normal payroll.
The following instructions detail how to process your payroll.

1. Enter the payroll group number in the PR Group field. Press F4 for a list of valid payroll groups.

1. Enter the last date of the pay period on the Pay Period Ending Date field.

1. Select the correct processing option in the Processing Option section of the form:

- All Employees - Select this option only if changes for the current pay period have been made to the basic setup information that the system uses to apply add-on earnings or calculate deductions and liabilities. Click [here](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-payroll-process-form/field-definitions-pr-payroll-process-form#ID-0003a2eb--en) for more information on this option

- Employees with changed earnings or overrides - This is the recommended method to use at all times- even when processing payroll for the first time. Using this option processes all employees with new and changes records and never processes those without any changes.

- Select Employee - Select this option if you want to process an individual employee.

1. If you selected the Select Employee option, enter the employee number in the Employee field. Press F4 for a list of valid employees.

1. If you want to restrict payroll period posting to a single payment sequence, check the Restrict by Payment Seq # box and enter the sequence in the Payment Seq # field. Note: If you do not choose to restrict payroll period posting by specifying a payment sequence, the system will bring in all sequences for the pay period.

1. Click Process. A confirmation message displays.

1. Click Close. Note: If the system could not process a pay record, the system will display the employee in the grid, along with the specific batch number(s). This might happen when a timecard is in a batch that has not been posted. In this case you could post the timecard batch and then reprocess the payroll period.

1. Repeat steps 1-8 for any additional pay periods that require processing.

1. Run the PR Payroll Register report to review the deduction and liability calculations that the system made. If you need to [make adjustments for an employee](/en/vista/vista/hr-and-payroll/payroll/payments/about-reviewing-processed-payrolls), you can use the PR Employee Pay Seq Control form. If you do not need to make any adjustments, you can now [process employee leave](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-processing-employee-leave).

Related information

- [About the PR Payroll Process Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-payroll-process-form)

- [About the PR Employee Pay Sequence Control Form](/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-employee-pay-sequence-control-form)

- [Processing Payroll](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/processing-payroll)
