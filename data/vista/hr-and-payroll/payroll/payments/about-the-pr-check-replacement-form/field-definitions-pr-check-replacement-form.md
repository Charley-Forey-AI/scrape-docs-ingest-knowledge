---
title: "Field Definitions: PR Check Replacement Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-check-replacement-form/field-definitions-pr-check-replacement-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-check-replacement-form/field-definitions-pr-check-replacement-form"
---

# Field Definitions: PR Check Replacement Form

The following is a list of field descriptions for the PR Check Replacement form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  PR Group

 Enter the PR group (from PR Groups) for the employee receiving this replacement check.

##  Pay Period Ending Date

 Specify a valid closed pay period (month must be open in subledgers and final GL interface already run). Press F4 for a list of valid closed pay periods (indicated by a Status of “1”).

## Employee

Specify the employee for whom this replacement
 check is being printed. A record for this employee must exist within the specified pay
 period and the employee must have been paid by EFT or Check (that is, cannot be pay method
 “X-No Pay”). Press F4 for a list of applicable employees for the specified pay period.

## Pay Seq #

Specify which payment sequence to process. Pay sequence must exist for the specified pay period and must have been paid by Check or EFT (that is, cannot be pay method “X-No Pay”).
Once the payment sequence is entered, the employee’s payment information is displayed (center of screen). Payment information includes the hours, earnings, deductions, and net pay, as well as the CM account and reference number, and the paid date and month.
Note: The paid month must still be open in both the PR and CM GL Company sub-ledgers, and the existing payment cannot be cleared or voided in CM.

##  Void Memo

 Enter a memo, up to 30 characters, to briefly describe the reason for this replacement check.

## Check Type

Specify the check type for this replacement check:

- Computer – New check is printed when the Update button is pressed.

- Manual – Check will be hand written.

##  CM Reference

 Enter the CM reference number, up to 10 characters. This will be the replacement check number; must be a valid, unique number when combined with the CM Reference Seq # entered to the right.

## CM Ref Seq #

Specify the sequence number of the CM Reference number. This allows you to reuse check numbers; however, the combination of the CM Reference entered in the previous field and this number must be unique.
For example, if you are reusing a check number and the check’s original sequence number was 1, you would enter 2 here.
