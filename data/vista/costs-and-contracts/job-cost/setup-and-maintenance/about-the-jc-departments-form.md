---
title: "About the JC Departments Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-departments-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-departments-form"
---

# About the JC Departments Form

Use this form to create and maintain
 departments.
Departments are assigned to contract items
 using the [JC Contracts ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form) form and they define which General Ledger
 accounts will be used when posting contract revenue and job costs. If your general
 ledger contains more than one set of Job Cost and Revenue accounts (to further breakdown
 job costs), then create separate departments for each set of accounts.
Note: All general ledger account codes specified here must
 first be set up in using the [GL Chart of Accounts ](/en/vista/vista/accounting/general-ledger/gl-accounts/about-the-gl-chart-of-accounts-form) form, and must have either
 J-Job or nothing selected in the Sub Ledger Code field on the Info tab
 of that form.
There are five tabs for defining GL account
 assignments:

- Info – Used to define the revenue
 accounts for open contracts/jobs and closed contracts/jobs.

- Cost Types – Used to set up the open
 and closed WIP (work in progress) accounts for each cost type you specify.

- Phase Overrides – Used to define
 override open/closed GL accounts by phase. An “Exclude PR” option allows you to
 specify that the phase override will not be used if the transaction’s source is
 Payroll.

- Liability Types—Used to set up the
 open/closed burden accounts for each of the liability types you specify. You
 need only set up overrides here if you want that portion of burden expense to go
 to an account other than the one assigned to the corresponding cost type.

- Earnings Types—Used to set up the
 open/closed labor accounts for certain types of earnings that you need to break
 out to separate GL accounts, rather than following the cost type of the earnings
 code. In Payroll, you can assign an earnings code to a special earnings type. If
 you do, the PR Ledger Update program will look here for the GL accounts, then
 use the standard account for the related cost type if an account is not set up
 here. An example might be if you wanted Subsistence to be directed to a separate
 GL Account, but to the Labor cost type.

Note: The 'closed' GL accounts will only be used if you
 allow posting to closed jobs (the 'Allow Posting to Closed Jobs' flag is checked in JC
 Company Parameters).

## Leaving Accounts Blank

When setting up departments, you do have
 the option to leave a department’s cost account blank so there will be no default
 account in posting programs. This might be useful if a department has more accounts
 to which costs are posted than you want to have separate cost types.
Note: If you elect to leave the cost accounts blank,
 you cannot use the automatic GL posting feature in the contract close
 process.

[Job Cost and General Ledger](/en/vista/vista/costs-and-contracts/job-cost/job-cost-and-general-ledger)
