---
title: "Processing Payroll | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/processing-payroll"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/processing-payroll"
---

# Processing Payroll

This topic provides an overview to processing payroll in Vista™.
Each payroll group and its associated pay period is processed independently and all of the steps detailed below must be completed each time timecard information is entered or any other changes are made.
 Any number of payrolls may be running on your system at one time, each in varying stages of completion. The system tracks the status (open, current, and closed) of each payroll; however, keeping the number of open periods for each group down to a minimum reduces confusion and the potential for mistakes when processing.
Though the list below indicates each successive step, you may, as needed, back up to make changes and corrections or post additional earnings. The important thing to remember is that if you back up a few steps, you need to rerun the associated forms following the point at which you made the change. For instance, if you have already processed the payroll and then need to change time card details in PR Timecard Entry, then you must reprocess the payroll for those employees with changes.
The only point from which you are not allowed to back up is after the payroll period has been closed (in PR Pay Period Control). PR Pay Period Control includes many checks within it to help prevent you from closing before everything is ready (all employee earnings must be fully processed, accumulation files updated, and check numbers assigned to earnings, etc.). Should you close a payroll and then discover a problem, you can reopen it, but you will need to rerun final updates, even if no changes have been made.
The following instructions provide an overview to processing payroll. As you follow each of the steps, click the hyperlinks to get more information on completing the step. These links will take you to topics that will give you detailed information on completing each step in the payroll processing task.

1. Set up your pay period in PR Pay Period Control. Depending on how your pay period falls, you can set up either a [single-month pay period](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-single-month-pay-periods) or a [split-month pay period](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-split-month-pay-periods).

1. If you are using the crew feature, [enter time for your crew](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/using-crews-to-enter-employee-work-hours), approve crew timesheets, and [send crew timesheets](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/send-crew-timesheets) to a timecard batch.

1. If your employees are [entering their own timesheets](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/create-a-timesheet), make sure that the [timesheets are reviewed/approved](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/approving-timesheets), and then [sent to a timecard batch](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/send-timesheets).

1. [Post individual timecards manually](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/posting-timecards) in PR Timecard Entry.
 Note: If you are adding timecards to a batch containing records from crew timesheets or employee-entered timesheets, you can also review those timecards at this point as well.

1. [Post automatic overtime](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/post-automatic-overtime) using PR Auto Overtime, as necessary.
 Note: You can only process auto overtime if you have checked the Using automatic overtime box in PR Company Parameters (Info tab). If you did not check this box, the system displays a message when you attempt to post auto overtime and you will not be able to finish posting.

1. [Distribute employee salary amounts](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/distribute-a-salary) to jobs, equipment, or accounts with PR Salary Distribution, if required.

1. [Post automatic earnings for employees](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-posting-automatic-earnings/post-automatic-earnings) using PR Post Auto Earnings. Automatic earnings might include salary, subsistence, 401(k), etc.

1. Review the timecards by running the PR Timecard Entry report. This report prints one line per posted timecard and displays an earnings recap that summarizes earnings and hours for each employee. The grand total for all employees earnings and hours display at the end of the report.

1. [Process your pay periods](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/processing-payroll/processing-a-payroll-period) using PR Payroll Process.

1. Review the processed payroll. You can do this in one of two ways.

- Run the PR Payroll Register report. This report displays information that prints on employee checks such as the earnings, deductions, and liability amounts.

- [Review the processed payroll](/en/vista/vista/hr-and-payroll/payroll/payments/about-reviewing-processed-payrolls) by using the PR Employee Pay Seq Control form. This form displays the same information as the PR Payroll Register report, but you can use it to edit payment information if needed.

1. [Process employee leave](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-processing-employee-leave)

1. [Print checks](/en/vista/vista/hr-and-payroll/payroll/payments/print-payroll-checks) for your employees using PR Check Print.

1. [Process EFTs](/en/vista/vista/hr-and-payroll/payroll/payments/process-payroll-eft-payments) (PR EFT Payments form) and [print direct deposit stubs](/en/vista/vista/hr-and-payroll/payroll/payments/print-direct-deposit-stubs) (PR Direct Deposit Print form) for your employees.

1. Print the PR Check Register report to review the net amount for each employee in the pay period. The Payment Method Totals section at the bottom of the report displays the net amount for all payments, broken down by payment methods (i.e., computer check, prepaid check, or direct deposit).

1. Print any additional reports as needed. The following list provides some examples of reports that you might need.

- Certified reports (PR Certified Payroll Transcript, PR Certified Signature Page, etc.)

- PR Tax Report

- PR Federal Tax Deposit Liability

- Craft reports (PR Craft Report full or selective, PR Craft Weekly Hours, etc.)

- Insurance reports (PR Insurance Report, PR Insurance Report by Insurance Code, etc.)

1. [Close the pay period](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-closingopening-pay-periods) in PR Pay Period Control.

1. [Update ledgers](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/run-a-ledger-update) in PR Ledger Update. When updating ledgers, the system sends payroll information to the JC, EM, GL, and CM modules. Additionally, the system updates each employee's monthly accumulations of earnings, deductions, and liabilities.

1. [Update payroll information to the AP module](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/update-payroll-information-to-ap) (PR AP Update). This will create a batch of AP transactions based on a pay period's deduction and liability amounts, as well as any earnings codes [set for automatic updating](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-united-states/set-up-automatic-ap-updates-united-states).
 You are now finished processing your payroll.
