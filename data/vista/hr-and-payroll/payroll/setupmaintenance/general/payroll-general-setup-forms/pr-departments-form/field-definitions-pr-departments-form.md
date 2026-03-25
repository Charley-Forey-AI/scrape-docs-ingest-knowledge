---
title: "Field Definitions: PR Departments Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-departments-form/field-definitions-pr-departments-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-departments-form/field-definitions-pr-departments-form"
---

# Field Definitions: PR Departments Form

The following is a list of field descriptions for the PR
 Departments form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Department

Enter a code, up to 10 characters, that uniquely identifies this department. Departmental classification directs entries to the General Ledger.
If using Job Cost or Equipment departments for Payroll, the General Ledger entries are based on those departments. However, you still need to set up a department for each employee.

##  Description

 Enter a description for this department, up to 30 characters.

##  JC Fixed Rate GL Account

 Enter the GL account to credit when a fixed
 rate is used to calculate an employee’s labor and burden for JC. Offsets expenses debited
 to the JC Department’s Open/Closed Labor accounts by earnings type.
If you leave this field blank, job timecard lines will result in an error when you do the
 Ledger Update.

##  EM Fixed Rate GL Account

 Enter the GL account to credit when a fixed rate is used to calculate an employee’s labor and burden for EM. Offsets expenses debited to the EM Department’s cost type or cost code account.
If you leave this field blank, mechanic timecard lines will result in an error when you do
 the Ledger Update.

## SM Fixed Rate GL Account

 Enter the GL account to credit when a fixed
 rate is used to calculate an employee’s labor and burden for an SM work order (customer
 work orders only). Offsets expenses debited to the SM Department's standard labor account
 or override labor account (if overrides are defined by call type and/or cost type).
If you leave this field blank, SM Work Order timecard lines will result in an error when
 you do the Ledger Update.

##  Earnings Types: Earn Type

Enter an earnings type (from HQ Earn Types).
 The description automatically displays to the right.

##  Earnings Types: Earnings Expense

Enter the GL expense account that will be
 debited when earnings are posted to this department. Account must be set up in GL Chart of
 Accounts with a blank subledger type. The description automatically displays to the right.

##  Earnings Types: JC Applied Earnings

Enter the GL account to credit when posting
 earnings to jobs. Offsets earnings expensed to JC by earnings type.

##  Earnings Types: EM Applied Earnings

Enter the GL account to credit when posting
 earnings to equipment. Offsets earnings expensed to EM by earnings type.

## Earnings Types: SM Applied
 Earnings

nter the GL account to credit when posting
 labor hours to SM work orders. Offsets the labor hours expensed to SM by earnings type.

##  Earnings Types: Interco Applied Earnings

 Enter the GL account to credit when posting intercompany earnings. Offsets earnings expensed to Intercompany Payroll by earnings type.

##  Liability Types: Liab Type

Enter a liability type (from HQ Liability
 Types). The description automatically displays to the right.

##  Liability Types: Burden Expense

Enter the GL expense account that will be
 debited when burden is posted to this department. Account must be set up in GL Chart of
 Accounts with a blank subledger type. The description automatically displays to the right.

##  Liability Types: JC Applied Burden

Enter the GL account to credit when burden is
 charged to Job Cost. This offsets the accounts debited to the JC department’s Open/Closed
 Burden account by liability type. If charging Job Cost with an amount other than Exact,
 this is typically a contra account to the accounts set up by Liability Type below. The form
 credits this account with the burden charged to Job Cost. If using the exact method for all
 liabilities, you may want to use the same account here as you set up by Liability Type
 below. Since the debits and credits will be equal, no actual entry is made.

##  Liability Types: EM Applied Burden

Enter the GL account to credit when burden is
 charged to equipment for mechanics. This offsets the account debited to the EM department’s
 cost type or cost code account. If charging equipment with an amount other than Exact, this
 will typically be a contra account to the accounts set up by Liability Type below. The
 program will credit this account with the burden charged to equipment. If using the exact
 method, you may want to use the same account here as you set up by Liability Type below.
 Since the debits and credits will be equal, no actual entry will be made.
An account must be set up here if using EM
 Departments for PR (option set up in EM Company parameters) even if using the exact method.

## Liability Types: SM Applied Burden

Enter the GL account to credit when burden is
 charged to Service Management for work performed on work orders. Credits to this account
 offset the debits for labor burden expense made to the GL account defined for the work
 completed labor line in SM Work Orders (the Cost Account or Cost WIP Account, depending on
 whether you are tracking WIP for the work order scope).

##  Liability Types: Interco Applied Burden

Enter the GL account to credit when posting
 intercompany burden. Offsets burden expensed to Intercompany Payroll by liability type.
