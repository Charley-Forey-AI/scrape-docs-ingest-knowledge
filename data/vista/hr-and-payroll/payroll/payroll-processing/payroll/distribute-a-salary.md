---
title: "Distribute a Salary | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/distribute-a-salary"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/distribute-a-salary"
---

# Distribute a Salary

You can use PR Salary Distribution to distribute an employee's salaried amounts to multiple jobs, pieces of equipment, or accounts by calculating an hourly wage based on the hours that you enter.
The following instructions detail how to distribute salaries.
Note: Before distributing a salary, make sure that the earnings
 code that you will use to post employee time has been set up for salary distribution. In
 PR Earnings Codes, select the Include in
 salary distribution calculations box for the correct earnings code and select A-Amount from the Method drop-down list. When using this code to post hours by job, equipment, or
 account, the salaried employee's pay rate and amount default to zero. When you process
 salary distribution with PR Salary Distribution, the system calculates the correct rate
 and amount, rounding any difference into the last timecard.

1. [Enter the hours worked by the employee](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/posting-timecards) per day for the current pay period in PR Timecard Entry. Note: When you enter the first timecard line for the employee,
 the Hours field will default to the standard number of hours for the pay
 period that you specified in PR Pay Period Control (Standard Hours field). As you adjust the hours and move to the next line, the
 system will default the remaining hours left in the pay period for each line. For
 example, if the standard hours are 40, the Hours field for the first timecard line defaults to 40. If you change
 this field to 8, and save the record, the system will default 32 in the
 Hours field for the next line.

1. At the end of
 the pay period, access the PR Salary Distribution form from the Main
 Menu. The Batch Selection form displays.

1. Enter the batch month, payroll group, payroll ending date, and payment sequence in the Batch Month, PR Group, PR End Date, and Pay Seq fields and click OK. The PR Salary Distribution form displays.

1. If you want to restrict salary distribution by a specific employee, check the Restrict by Employee box and enter the employee number in the Employee field. Press F4 from the Employee field to see a list of valid employees.

1. If you want to
 restrict salary distribution to a single payment sequence, check the
 Restrict posting to a single
 Payment Seq# box and enter the sequence in the
 Payment Seq#
 field.Note: If you do not choose to
 restrict salary distribution by specifying an employee or a
 payment sequence, the system will bring in all employees and
 sequences for the pay period.

1. Click Process. The system displays a confirmation message.

1. Click Close.  The employees matching the criteria display
 in the grid.

1. Select
 File > Process
 Batch. The PR Batch Process form displays.

1. [Process the batch](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/pr-batch-process-form). The system then divides the salary amount by the number of hours worked and distributes it over the jobs, equipment or accounts that you specified in PR Timecard Entry.
Tip: To see how the system distributed the salary, view the Batch
 List report from the PR Batch Process form after you validate the
 batch.
You can now [post automatic earnings](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-posting-automatic-earnings/post-automatic-earnings).

Related information

- [About the PR Salary Distribution Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-salary-distribution-form)

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)

- [PR Batch Process Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/pr-batch-process-form)

- [PR Pay Period Control Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-pay-period-control-form)

- [Processing Payroll](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/processing-payroll)
