---
title: "PR Check Print Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/pr-check-print-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/pr-check-print-form"
---

# PR Check Print Form

Use this form to print paychecks with fully processed earnings for employees in a select payroll group and pay period.

The system will only print checks for employees who you have set up for printing checks in PR Employee Pay Seq Control (you selected C-Check from the Payment Method drop-down and C-Computer from the Check Type drop-down).
Employee Payment Sequences with 0.00 (0.00 earnings and 0.00 deductions) or negative net pay are skipped and must be handled manually in the PR Employee Pay Sequence Control form. For more information, see [Process Manual Checks](/en/vista/vista/hr-and-payroll/payroll/payments/process-manual-checks).
During the check processing procedure, check numbers are assigned, paid amounts recorded, and the system prepares information for printing. Once the check processing procedure is complete, a Crystal report is run to perform the actual check print based on the information in the Check Print tables. The report used for printing checks is determined by the report you specify in the Check Print Report Title field in PR Company Parameters (Info tab).

- A custom check print report may be substituted for
 the standard reports provided with Vista (PR Check Print, PR Check Print Stub). However,
 the custom report must contain the same input parameters as the standard reports
 (i.e. Company, PR Group, PR End Date, and Comment).

- If you do not have security to the report specified in the Check Print Report Title field, the system displays an error message and check processing does not occur.

 For more information about selecting the reports used for check printing, see [Set up Payment Report Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information).
For more information about using this form, see the articles below.
[Print Payroll Checks](/en/vista/vista/hr-and-payroll/payroll/payments/print-payroll-checks)
[Print Non-Negotiable Payroll Checks](/en/vista/vista/hr-and-payroll/payroll/payments/print-non-negotiable-payroll-checks)
[About Reprinting/Voiding Checks](/en/vista/vista/hr-and-payroll/payroll/payments/about-reprintingvoiding-checks)

Related information

- [About the PR Employee Pay Sequence Control Form](/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-employee-pay-sequence-control-form)
