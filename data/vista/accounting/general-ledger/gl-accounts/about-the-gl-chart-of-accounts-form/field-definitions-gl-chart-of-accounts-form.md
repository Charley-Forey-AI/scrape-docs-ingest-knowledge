---
title: "Field Definitions: GL Chart of Accounts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-accounts/about-the-gl-chart-of-accounts-form/field-definitions-gl-chart-of-accounts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-accounts/about-the-gl-chart-of-accounts-form/field-definitions-gl-chart-of-accounts-form"
---

# Field Definitions: GL Chart of Accounts Form

The following is a list of field descriptions for the GL
 Chart of Accounts form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## GL Account

Enter a unique number, up to 20 characters (as defined by Viewpoint during installation), that identifies this account code.
Important:Vista will allow you to enter alpha characters in your account number and is case-sensitive. For example, the system considers the account numbers 2125-000-HI and 2125-000-hi as different.

##  Description

 Enter a description of this account code (up to 30 characters) as it should appear on reports and financial statements.

##  Account Type

An account type provides a way to define the purpose of an account code.
The type codes are as follows.

- A-Asset

- C-Capital

- E-Expense

- H-Heading

- I-Income

- L-Liability

- M-Memo

- P-Profit/Loss

Heading accounts, type H, may be used to identify a group of following accounts on lists and reports. Heading accounts may not be used for posting.
Memo accounts, type M, are used to record amounts in a manner different from other account types; for example, a memo account may be used to record numbers, such as hours or tons, to use on a financial statement. These amounts are not included in any standard report totals.
Account type P is used to store retained earnings from the previous year. The profit/loss amount for the year is automatically calculated by the system using expense and income accounts (types E and I) when running the GL Beginning Balance Update and the difference is added to this account for the next years beginning balance. This account balance is calculated by the system and, typically, you will never post anything to it.
The monthly profit/loss amount will be calculated on your financial statement by adding the income and expense amounts.

##  Normal Balance

 Select either debit or credit. Used as a default when maintaining balances and budgets.
Note: This field is not available for GL accounts with an Account Type of H (Heading).

## Sub Ledger Code

If this account should only be used when posting to certain types of entries, specify the entry type. Otherwise, leave blank.

- J-Job

- E-Equipment

- I-Inventory

- C-Cash

- P-Payables

- R-Receivables

- S-Service

Note: The S-Service sub ledger code only applies to accounts
 used for work completed labor, miscellaneous, and purchase lines on an SM work order.
 Accounts used for work completed equipment lines must have a subledger code of null or
 E-Equipment, and accounts used for work completed inventory lines must have a subledger
 code of null or I-Inventory.

## Cross Reference Memo Account

 This field allows you the
 option to interface payroll hours to General Ledger.
If you elect to update GL with payroll hours, you must specify an account (memo type) here for every account to which earnings will be posted. When payroll data is interfaced to GL (in PR Ledger Update), the system checks to see if a cross-reference account exists for the earnings account, and if so, will update the labor hours to that account.
If you do not want payroll hours updated to General Ledger, leave this field blank.

##  Summary Account

 Specify the summary account for this GL account. All account detail and balance totals are stored with the accounts used when the entry was posted.
 Summary accounts allow you to report at a more summarized level; however, this field is not used on any standard Viewpoint reports. Therefore, if you wish to see the detail summarized to this account, you will need to create a custom report.

## Reviewer Group

Optional field.
Enter the reviewer group that defaults for each line referencing this expense in AP Unapproved Invoice Entry.
Press F4 for a list of active reviewer
 groups.
Press F5 to access HQ Reviewer Group to manage
 reviewer groups.
For more information on reviewer groups, see
 [About the HQ Reviewer Group Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form#ID-0000f57a--en__ID-0000f57a).

##  Active

 Check this box if this is an active GL account.
 Leave this box unchecked if this GL account is inactive. (Note: You cannot post new entries to inactive accounts.)

##  Interface Detail

 Y = Select this option to interface transactions posted to this account from any of the sub ledgers with as much detail as possible.  N = Select this option to summarize detail for transactions posted to this account as indicated within the subsidiary ledger.
