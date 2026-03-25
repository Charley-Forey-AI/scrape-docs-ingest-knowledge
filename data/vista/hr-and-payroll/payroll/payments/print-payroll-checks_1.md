---
title: "Print Payroll Checks | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/print-payroll-checks_1"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/print-payroll-checks_1"
---

# Print Payroll Checks

Use the PR Check Print form to print payroll checks.

- You must have specified the report onto which you will print the checks. For more information, see [Setting Payroll Payment Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information).

- The instructions on this page are for printing payroll checks. If needed, see [Printing Non-Negotiable Payroll Checks](/en/vista/vista/hr-and-payroll/payroll/payments/print-non-negotiable-payroll-checks).

For each Payroll Check Print task you initiate:

- The system completes this process in the background. During this time, the Background Jobs form displays the processing status. You may close the job queue while the system completes processing.Note: To open and view this and any other jobs in the queue, navigate to Main Menu > View > Display Job Queue.

- The system prevents other users from accessing the Pay Period record.

- Your username appears in the In Use By field in the PR Pay Period Control form, In Use By tab.

1. Enter the payroll group and the ending pay period date in the PR Group and Pay Period Ending Date fields, respectively. These fields default to the payroll group and ending pay period date that you accessed last.

1. Enter the date to pay checks in the Paid Date field. The Paid Month field defaults with the paid date's month and year.Note: Typically, the month should be the same in both the Paid Date and Paid Month fields. This is important for 941 Schedule B reporting. You can change the default in the Paid Month field as necessary.

1. Select a printing sort option from the Sort Checks by drop-down field. See [Sort Options and Restrictions for Printing Payroll Checks](/en/vista/vista/hr-and-payroll/payroll/payments/sort-options-and-restrictions-for-printing-payroll-checks) for more information.

1. If you want to restrict check printing to a specific payment sequence, check the Restrict by Payment Sequence # box and enter a payment sequence in the Payment Seq# field.

1. In the CM Account field, enter the CM account to use when making payments. This field defaults the CM account that you assigned to the PR group in PR Groups (CM Account field). If you enter a new account in this field, the system will update the CM Account field in PR Employee Pay Seq Control.

1. If you want to restrict check printing based on the setting in the Sort Checks by drop-down field, check the Restrict By... box that corresponds to the setting in the Sort Checks by field. Enter the specific restriction criteria in the additional fields that display once you check the box. See [Sort Options and Restrictions for Printing Checks](/en/vista/vista/hr-and-payroll/payroll/payments/sort-options-and-restrictions-for-printing-payroll-checks) for more information.

1. In the Comment field, enter a message that you would like to display on the check stubs, if necessary.

1. Enter a range of check numbers for printing in the Beginning Check # and Ending Check # fields.Note: The Beginning Check # field defaults to the next available check number. The Ending Check # field defaults to 999999999, although you can set this to another number. If the ending check number is reached before all eligible employee entries have been processed, those that received check numbers will print and a message displays informing you that additional check numbers are required. The cursor then returns to the beginning check number for input.

1. Click Print. A Printer dialog box displays and the system assigns the check numbers and paid date to each of the employees.

1. Select the appropriate printer and click OK.The system then prints the checks.


 When printing is finished, the system clears your username from the In Use By field and removes the task from the Background Jobs form.
You can now [process any EFT payments](/en/vista/vista/hr-and-payroll/payroll/payments/process-payroll-eft-payments) and [print direct deposit stubs](/en/vista/vista/hr-and-payroll/payroll/payments/print-direct-deposit-stubs) for your employees.Note:Once the checks and copies have been printed, the Check Print report closes. If the report fails, whether interrupted intentionally or not, check numbers and paid information may still exist in the system, even though a check was not actually printed. This, and other print problems, may result in one or more checks needing to be voided and reprinted. If this occurs, you can remove and/or void assigned check numbers from the Existing Checks tab on this form. See [Reprinting/Voiding Checks](/en/vista/vista/hr-and-payroll/payroll/payments/about-reprintingvoiding-checks) for more information. If printing is interrupted and the form closes prematurely, the pay period remains locked. To unlock the pay period, clear the In Use By field in the PR Pay Period Control form or reopen this form, void any non-printed checks, and re-run the check run (this clears the In Use By field). Only users displayed in the In Use By field can clear the field.

Related information

- [PR Check Print Form](/en/vista/vista/hr-and-payroll/payroll/payments/pr-check-print-form)

- [About the PR EFT Payments Form](/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-eft-payments-form)

- [About the PR Ledger Update Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-ledger-update-form)
