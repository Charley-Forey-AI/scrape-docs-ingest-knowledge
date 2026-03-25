---
title: "Field Definitions: PR Direct Deposit Print Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/pr-direct-deposit-print-form/field-definitions-pr-direct-deposit-print-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/pr-direct-deposit-print-form/field-definitions-pr-direct-deposit-print-form"
---

# Field Definitions: PR Direct Deposit Print Form

The following is a list of field descriptions for the PR Direct Deposit form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  PR Group

 Enter the PR group to process.

##  Pay Period Ending Date

 Enter the pay period ending date that, when combined with the PR Group, will identify an open pay period. Initially defaults the last accessed pay period for the current user.

## Sort Options

Sort options control the order in which direct deposit stubs are printed. When selecting an option, the restriction range inputs will change. The default sort option is Employee Sort Name.

- Employee SortName —Direct deposit stubs print in employee sort name order. You may select the beginning and ending sort names to restrict the range of direct deposit stubs printed.

- Employee #—Direct deposit stubs print in employee number order. You may select the beginning and ending employee numbers to restrict the range of direct deposit stubs printed.

- Job, Check Print Order and Employee #—Direct deposit stubs print in job order, then check print order (defined in PR Employees), then in employee number order. The job used for sorting is the current job assigned in the PR Employees form. Those with blank jobs will print first.

- Check Print Order and Employee #—Direct deposit stubs print in check print order and employee number order. The check print order is assigned in the PR Employees form. Those with no check print order assigned will print first.

- Crew, Check Print Order and Employee #—Direct deposit stubs print in order by crew, then check print order (assigned in PR Employees), then in employee number order. Those employees without a crew print first, sorted by check print order and employee number.

##  Restrict by Payment Sequence #

 Check this box if you want deposit stubs printed for a single payment sequence within the pay period. Leave the box unchecked if you want to print a deposit stub for each payment sequence paid by EFT for the employee.

##  Payment Seq#

 If you checked the Restrict By Payment Sequence # box, then enter a valid payment sequence.

##  Restrict by Employee Sort Name

 Check this box if you want to select beginning and ending sort names to restrict the range of direct deposit stubs printed.

##  Beginning Sort Name

 Enter the sort name where you would like to start printing direct deposit stubs.

##  Ending Sort Name

 Enter the sort name where you would like to stop printing direct deposit stubs.

##  Restrict by Employee #

 Check this box if you want to select beginning and ending employee numbers to restrict the range of direct deposit stubs printed.

##  Beginning Employee #

 Enter the employee number with which to start printing direct deposit stubs.

##  Ending Employee #

 Enter the Employee number with which to stop printing direct deposit stubs.

##  Restrict by Job and Employee #

 Check this box if you want to select beginning and ending JC Co, Job, and Employee numbers to restrict the range of direct deposit stubs printed.

##  Beginning JC Co#

 Enter the JC Co# with which to start printing direct deposit stubs.

##  Beginning Job

 Enter the job number with which to start printing direct deposit stubs.

##  Beginning Employee #

 Enter the employee number with which to start printing direct deposit stubs.

##  Ending JC Co#

 Enter the JC Co# with which to stop printing direct deposit stubs.

##  Ending Job

 Enter the job number with which to stop printing direct deposit stubs.

##  Ending Employee #

 Enter the employee number with which to stop printing direct deposit stubs.

##  Restrict by Check Print Order and Employee #

 Check this box if you want to select beginning and ending Check Print Orders and Employee numbers to restrict the range of direct deposit stubs printed.

##  Beginning Check Print Order

 Enter the check print order where you would like to start printing direct deposit stubs.

##  Beginning Employee #

 Enter the employee number with which to start printing direct deposit stubs.

##  Ending Check Print Order

 Enter the check print order where you would like to stop printing direct deposit stubs.

##  Ending Employee #

 Enter the employee number with which to stop printing direct deposit stubs.

##  Restrict by Crew and Employee #

 Check this box if you want to select the beginning and ending Crew and Employee numbers to restrict the range of direct deposit stubs printed.
 Do not check this box if you want direct deposit stubs printed for all employees.

##  Beginning Crew

 Enter the crew code with which to start printing direct deposit stubs.

##  Beginning Employee #

 Enter the employee number with which to start printing direct deposit stubs.

##  Ending Crew

 Enter the crew code with which to stop printing direct deposit stubs.

##  Ending Employee #

 Enter the employee number with which to stop printing direct deposit stubs.

##  Restrict by CM Reference #

 Check this box if you only want to print deposit stubs for a single CM Reference #.

##  CM Reference #

 If you checked the Restrict by CM Reference # box, then enter the CM Reference number, and only those employee payment sequences that have been assigned this number will be printed.

## Include employees notified by email on printed report

Check this box if you want to print direct deposit stubs for employees who have received an email notification of payment on the printed report. If you do not check this box, employees who received an email notification of payment will not be included.
Note: An employee will receive an email notification when
 you have selected either A-Email with attachment or E-Email as
 notification from the Method of Pay Stub Delivery field for the
 corresponding record in PR Employees. For more information on payment notifications, see
 [Sending Pay Stub Information by Email ](/en/vista/vista/hr-and-payroll/payroll/payments/send-pay-stub-information-by-email).

##  Comment

 Enter a comment, up to 180 characters, that will be printed on the deposit stub. Entry in this field is optional, and the default is null.
