---
title: "PR Groups Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-groups-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-groups-form"
---

# PR Groups Form

Payroll groups are used to classify employees according to common pay periods and common bank accounts, as well as separate sensitive payroll data for security reasons.
Using groups enables you to process several different types of payroll independently. Setting up different groups allows you to process them at the same time, yet keep their information separate.
Separate groups must be used if they have different pay periods or are paid out of different bank accounts. There may be other operational reasons for using separate groups as well.
 An employee is typically associated with only one group at a time, since it requires changing the group number in PR Employees for the system to allow posting.
The concept of payroll groups is fundamental in the Payroll module. Most PR forms work on the payroll group concept. Most reports are run by group number, detail files are stored by group, and the system interfaces to Job Cost, General Ledger, and Equipment Management by group.

## GL and CM Accounts

The PR Groups form holds the GL accrual account code that may be used in the interface to General Ledger. When interfacing to GL, the accrual account is used if the month to which the timecards are posted and the month in which the employee is paid are different. This account is reversed in the month paid.
 The CM Account number must be specified for each group in order for checks to be printed. The information for direct deposits is also pulled from the associated CM account. The bank account may be overridden in the PR Employee Pay Sequence Control form for a manual check.

## Liabilities and Leave Codes

The Liabilities and Leave Codes tabs allow you to select liability codes and leave codes to be printed on the payroll checks for the group.

- Liability codes print the amount for the pay period and year-to-date; pension or employer-paid 401ks are examples of liability codes.

- Leave codes, such as vacation or personal time, show usage for the period and year-to-date, plus the available balance.

Select the following links for more information about using this form.
[Set Payroll Group Security](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-payroll-group-security)
[About Defining Payroll Groups](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-defining-payroll-groups)

Related information

- [Set up Oregon Transit Tax](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-oregon-transit-tax)
