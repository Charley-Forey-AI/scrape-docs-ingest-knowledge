---
title: "Field Definitions: PR Employee Pay Sequence Control Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-employee-pay-sequence-control-form/field-definitions-pr-employee-pay-sequence-control-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-employee-pay-sequence-control-form/field-definitions-pr-employee-pay-sequence-control-form"
---

# Field Definitions: PR Employee Pay Sequence Control Form

The following is a list of field descriptions for the PR
 Employee Pay Seqeuence Control form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  PR Group

 Enter the PR Group for the employees whose payment records are to be accessed.

##  Pay Period Ending Date

 Enter a Pay Period Ending Date that, when combined with the PR Group, identifies an open Pay Period. Initially defaults the last accessed pay period for the current user.

##  Employee

 Enter an active Employee who is currently assigned to the PR Group.

##  Pay Seq#

 Enter an existing Payment Sequence set up for this Pay Period.

##  Payment Method

 Indicate how this payment is to be made by selecting either “C” (check), “E” (EFT direct deposit), or “X” (no pay). This field is initialized as “C” unless the Employee has an active direct deposit, in which case it is initialized as “E.” This field can only be changed if the CM Reference is blank. Payment method “X” may be used when the net pay is zero, and no check is needed. This is typically used if the payment sequence is a correction of a prior pay period and did not affect the net pay. If “X” is selected, then no payment is made on this Employee and Pay Sequence, no entry is recorded in either CM or PR Payment History, and it is only valid if the net pay equals 0.00.

##  Check Type

 Select “C” for computer generated checks or “M” for manual checks. This field is null and disabled if payment method is “E.” This field is initialized as “C” for all checks.

## CM Co#

### Computer Checks, EFTs, and No Pays

Defaults the CM Company specified for the
 payroll group (in PR Groups). This is the CM company from which the payment is issued
 and that is updated with the CM detail; cannot be overridden.

### Manual Checks

Defaults the CM Company specified for the
 payroll group (in PR Groups). May be overridden during initial entry; however, once you
 have entered and saved the payment information (i.e. CM Reference, CM Ref Seq#, Paid
 Date, and Paid Month), this field is disabled.

## CM Account

### Computer Checks, EFTs, and No Pays

Defaults the CM account specified for the
 payroll group (in PR Groups). This is the bank account that is used to issue payment,
 and when updating CM and determining the Cash account to credit; cannot be overridden.


### Manual Checks

Defaults the CM account specified for the
 payroll group (in PR Groups). May be overridden during initial entry; however, once you
 have entered and saved the payment information (CM Reference, CM Ref Seq#, Paid Date,
 and Paid Month), this field is disabled.

## CM Reference

The CM Reference field is blank until the Employee Payment Sequence has been paid. It represents the check number or EFT# based on the Payment Method.

- Computer Check—The CM Reference number is assigned by the PR Check Print form and cannot be entered here.

- Manual Check—A CM Reference number can be entered only if the current value is blank. When a check number is assigned, the paid totals are set equal to the calculated totals displayed on the lower tab. If the Employee’s earnings require processing, use the Update Amounts option after running the PR Payroll Process form to correct the payment totals.

- Direct Deposit—If paid through an EFT, the CM Reference number and EFT Seq# will be assigned by the PR Direct Deposit Download form.

An existing CM Reference number can only be changed by deleting it using the Void Payment option.

##  CM Ref Seq#

 The CM Reference Sequence number allows for the reuse of a check number. The default is 0 for all checks and EFTs. This field can be entered for manual check information, but cannot be changed on existing computer checks or EFTs.
 If correcting entries have been posted to an Employee resulting in negative net pay, you may want to reuse the original CM Reference number and assign a new Reference Seq#. Both will be updated to CM and PR Payment History, and both can be cleared.

##  EFT Seq#

 The EFT Seq# denotes an individual payment for the Employee and Pay Seq# within an EFT. This field must be 0 for all checks and is assigned for EFTs through the PR Direct Deposit Download form.

##  Paid Date

 The Paid Date is the actual date that the payment was made and is used to determine the month accumulations are updated.
 Entry in this field is required for manual checks or ‘No Pays’; cannot be changed on existing computer checks, EFTs, or manual checks with a CM reference number assigned.

##  Paid Month

 The Paid Month updates CM and GL when this payment is interfaced.
 Entry in this field is required with manual checks or ‘No Pays’; cannot be changed on existing computer checks, EFTs, or manual checks with a CM reference number assigned.

##  Post to All - use Pay Period's standard number of days

 This field indicates whether rate per day deductions calculated for this Employee and Pay Sequence should use the standard number of days for the Pay Period or the true number of days posted on timecards. This field is initialized based on the Post To All flag in the PR Employees form, but can be changed at any time. If you change this field, then the Employee’s earnings need to be reprocessed.

##  Check Print Order

 Use this field to override the employee’s standard Check Print Order as assigned in PR Employees. Typically used to identify employee and pay sequence combinations that require immediate check processing (e.g., lay-offs). Use the Job and Crew fields in the grid to assist in sorting for employees to override.

## Number of Payments Covered

This field displays for Australian companies only.
This field defaults the value from the
 Number of
 Payments Covered field in PR Pay Period Control. You can accept the default
 or override it here for this specific employee. This value represent the number of payments
 to be made during a pay period. You would enter a numbers greater than 1 if you are
 paying the employee more than once due to time off that crosses pay periods. When you
 specify more than one payment, the system withholds the correct amount and prevents
 unwanted overstatement of PAYG withholding due to a higher payment for the pay period.

## Deductions: Dedn Code

Enter the deduction code that you want to override. This override applies only to the current Employee and Payment Sequence.
Note: You cannot add pre-tax deductions to this field. If you attempt to add a pre-tax deduction, the system displays a warning and you must select another deduction code.

##  Deductions: Override

 Check this box to override the calculated deduction amount.
 Do not check this box if the calculated deduction amount cannot be overridden.

##  Deductions: Override Amount

 Enter the amount that you want deducted.

## Deductions: PB Override

Check this box to override the calculated
 payback amount for this employee. Once you check this box, the system enables the
 Payback Over
 Amt field.
This box is enabled only for deductions that
 have been set as subject to arrears (you checked the Subject to Arrears box in PR
 Deductions/Liabilities, Arrears/Payback tab).

## Deductions: Payback Over Amt

Enter the override payback amount for this employee.

##  Liabilities: Liab Code

 Enter the liability code that you want to override. This override applies only to the current Employee and Payment Sequence.

##  Liabilities: Override

 Check this box to override the calculated deduction amount.
 Do not check this box if the calculated deduction amount cannot be overridden.

##  Liabilities: Override Amount

 Enter the amount that you want deducted.

##  Seq#

 Enter a Sequence Number to identify a specific direct deposit distribution for an Employee and Payment Sequence. This must be an integer between 1 and 255; integer is entered with new records, but not changeable on existing records.

##  Routing Transit #

 Enter a routing transit number to direct this deposit to the proper financial institution. This number is supplied by the bank and is not validated.

##  Bank Account #

 Enter the bank account number to direct this deposit to the proper account. This number is supplied by the bank and is not validated.

##  Type

 Enter “C” for checking or “S” for savings.

##  Amount

 Enter the dollar amount of net pay to deposit with this entry. New entries default to the Remaining amount. If the total of all sequences does not equal the Net Pay (i.e. the Remaining amount is not equal to 0.00), a message displays upon closing the form indicating that the net pay has not been properly distributed and that an EFT will not be produced.
