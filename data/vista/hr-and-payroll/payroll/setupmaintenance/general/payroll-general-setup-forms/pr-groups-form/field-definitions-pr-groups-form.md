---
title: "Field Definitions: PR Groups Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-groups-form/field-definitions-pr-groups-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-groups-form/field-definitions-pr-groups-form"
---

# Field Definitions: PR Groups Form

The following is a list of field descriptions for the PR
 Groups form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Payroll Group

Enter a number (0-255) that identifies this
 payroll group.
Payroll groups are used to classify employees
 according to common pay periods and common bank accounts, as well as separate sensitive
 payroll data for security reasons.Using groups enables you to process several different
 types of payroll independently.

##  Description

Enter a description for this payroll group, up
 to 30 characters.

## Pay Period

Specify how often this PR Group is paid.

- W- Weekly

- B - Biweekly

- S - Semimonthly

- M- Monthly

## Pay Periods Per Year

This field displays for Canadian companies only.
This field automatically defaults based on the
 setting of the Pay
 Period field. If the Pay Period field is set to either
 W-Weekly or B-Biweekly, you can change the default to
 either 53 or 27, respectively. This enables proper calculation of payroll deduction and
 liability amounts in cases where an additional weekly or bi-weekly pay period occurs in the
 current year, based on pay period ending dates. For accurate calculations, you must update
 this field on an annual basis to match the actual number of pay periods.
The following table displays the defaults and additional allowed values for this field.
Pay Period field setting
Pay Periods Per Year default
Additional allowed values

W-Weekly
52
53

B-Biweekly
26
27

S-Semimonthly
24
N/A

M-Monthly
12
N/A

##  GL Accrual Account

Enter the account (i.e. Wages Payable) that
 will be credited for wages and burden to be accrued for one month when paid in a second
 month. Must be an account set up in GL Chart of Accounts with a blank subledger type.

##  CM Company

Specify the CM company to use when issuing
 checks or EFTs for this group. When first setting up a group, initially defaults the CM
 company assigned to the PR company in PR Company Parameters. If the default CM company is
 changed in PR Company Parameters, it does not update the CM company here. You will need to
 update this group's CM company manually.
This is the CM company used to determine the
 GL Account for Net Pay and is updated with CM Detail.

##  CM Account

Enter the bank account (from CM Accounts) to
 use when issuing checks or EFTs for this group. Must be a valid CM account for the
 specified CM company.

## Attach GL ledger update reports to pay period

Check this box to have the system attach GL ledger update reports to PR Pay Period control records for this group.
Note: To secure the attachments, you must enter an
 attachment type in the Attachment Type ID field. This will
 enable the attachments to be accessible only to users who have been granted permissions to
 the attachment type in VA Attachment Type Security.

## Attachment Type ID

Use this field to secure two batch report attachments:

- GL Ledger Update Report

- PR Timecard Entry Audit Report

Press
 F4
 to view and select from a list of attachment type ID codes. Users processing batches will
 only be able to access these two attachments if they have been granted permissions to the
 attachment type in VA Attachment Type Security.

##  Liability Code

Enter a liability code (from PR
 Deductions/Liabilities) that you want to print on the check stub. This is optional but may
 be used to show employer paid benefits on the check stub.

##  Leave Code

Enter a leave code (from PR Leave Codes) that
 you want to print on the check stub. This is optional but may be used to show vacation or
 other leave information on the check stub.

##  User

Specify the user you wish to include in the
 security group for this payroll group; press F4 for a list of valid users. Only users on
 this list will have access to information associated with this payroll group.
