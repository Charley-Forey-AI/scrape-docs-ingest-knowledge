---
title: "About the GL Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-company-parameters-form"
---

# About the GL Company Parameters Form

Use the GL Company Parameters form to set up standards for each GL company on your system, including setting up account codes, balancing journal entries, and establishing the number of months available for posting.
It is recommended that you restrict this form so that only the System Administrator has access to it.
You must set up all companies in the HQ Company Setup form before you can access them in General Ledger. Entering a company number here designates it as being an active GL company.

## Last Month Closed

This section tracks the last month you closed the subsidiary ledgers for Accounts Payable, Accounts Receivable, and All Other Sub Ledgers, as well as the General Ledger.
These are automatically updated by the month-end close process (in GL Month End Close) and may not be changed in this program after transactions are posted.
During implementation, it is suggested that you set the last month closed in sub ledgers to two months before the month that you plan to go live on the system. This allows you to enter balances to the month before you will go live and then begin entering live data into the next month.
Example:
If you plan to go live in January of 2009, enter 11/08 (for November, 2008) as the last month closed in sub ledgers. This allows you to enter balances into December of 2008 and then go live in January.
The last month closed in general ledger should normally be set to the last month of your prior fiscal year. This allows you to enter beginning balances for the current year, and then enter net activity for each month prior to the month you plan to go live.

## Maximum Number of Open Months

The maximum number of open months specified in this file controls the number of months that may be open in the subledgers simultaneously.
You will need at least 2 months open at a time. It is recommended that you set this field to 2–4 months, change it only when necessary, and do not specify any more than 24 open months.

## Audit Options

The audit options determine when new entries are added to the HQ Master Audit (HQMA) table.
Click [here](/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-company-parameters-form/field-definitions-gl-company-parameters-form#ID-0000e15f--en) for more information.

## Unbalanced Journals

The Allow Unbalanced Journals flag allows the option for unbalanced entries to be made in GL Journal Transaction Entry.
This feature is normally only used in the rare circumstance of correcting a computer-generated error. It is suggested that this remain unchecked unless discussed with a Viewpoint Support Representative.

## Workflow Tab

If you have the Workflow module and are using the Process Workflow feature, you can use the Workflow tab to define which workflows apply to the entire company. The workflow processes set up here override the workflow processes set up using the Workflow tab on the HQ Company Setup form.
Note: You can also set up company-level workflow processes using the Assigned Companies tab on the WF Workflow Process form.

For more information about the workflow process and hierarchy, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

For more information about GL companies, see [Deciding and Defining When To Go Live](/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/deciding-and-defining-when-to-go-live).
