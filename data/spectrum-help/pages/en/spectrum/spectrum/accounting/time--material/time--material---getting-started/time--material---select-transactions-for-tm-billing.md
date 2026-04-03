---
title: "Time + Material - Select Transactions for T+M Billing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/time--material---getting-started/time--material---select-transactions-for-tm-billing"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/time--material---getting-started/time--material---select-transactions-for-tm-billing"
---

# Time + Material - Select Transactions for T+M Billing

You can add or remove billing transactions as long as you
 have not yet transferred billing data to Accounts Receivable (using Update T+M
 Billings).
Select or deselect items for billing using Summary Billing
 Selection and Detail Billing Selection:

- Summary Billing Selection: Allows you to select or deselect
 billing transactions by job. You can select transactions for all jobs or specific
 jobs.

- Detail Billing Selection: Allows you to select or deselect
 specific line items on a job for billing.

1.  Select Time + Material > Data Entry > Summary Billing Selection.For field descriptions and a sample report, see [Summary Billing Selection](/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/summary-billing-selection). Totals shown in the Processing
 status area of this screen update as you make selections.

1. For Activity type, choose
 Select.

1. Enter a Job number.

1. Enter a Division,
 Phase, and Cost type.

1. Select the date range from which to select transactions:

- Use From transaction date and Through
 transaction date fields to select the first and last transaction
 dates. If you leave From transaction date blank, the
 system uses the earliest available Time + Material processing date.

- Use From PR work date and To PR work
 date if you want to include payroll transactions only.

1. If you have jobs with no billings but want the system
 to generate a billing record, select Create billing for jobs with no
 activity?. This option may be used to notify customers about ongoing
 projects that had no activity for the billing period.

1. Enter the Invoice date and
 G/L date for the invoice, or press
 Enter to accept the current Time + Material processing
 dates.

1. Select the types of transactions to include in the report. Options include:

- Accounts Payable

- Equipment

- General Ledger

- Inventory

- Job Cost

- Payroll

1.  Optionally, click the down arrow in the
 Processing status area to open the Detail
 Billing Selection screen.For field descriptions and a sample report, see [Detail Billing Selection](/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/detail-billing-selection). Totals shown in the Selected for billing area
 of this screen update as you make selections. You can also access Detail Billing
 Selection at any time from the Site Map (Time + Material > Data Entry > Detail Billing Selection).

1. In the Billings-in-Progress
 Summary window, select a job from the list, and click
 Detail Billing.

1. The Job number,
 Customer, and Billing #
 prefill based on the selected job. If applicable, select a different
 Billing #, or leave this field blank to view only
 those transactions not yet selected for billing.

1. Select transactions for billing:

- To include specific transactions, click a
 transaction in the grid. Then click Select.

- To include all transactions with a
 Status of Unselected,
 click Select All.

- Use Deselect and
 Deselect All as needed to remove
 transactions from the current billing. Deselected transactions may be
 selected for billing at a later time. If you delete a transaction, it
 is no longer eligible for billing. Only users with the applicable
 security access can delete transactions.

1. Click the check mark in the upper right of the
 Detail Billing Selection screen to save your
 selections.

1. Click OK in the
 Billings-in-Progress Summary screen.

1. In the Summary Billing
 Selection screen, click Continue to add
 selected transactions to billing.Important: If billings go over the Not
 to exceed amount established in [Time + Material - Customize Billing Setup, Labor Rates, and
 Equipment Rates for a Job](/en/spectrum/spectrum/accounting/time--material/time--material---getting-started/time--material---customize-billing-setup-labor-rates-and-equipment-rates-for-a-job), the system provides a warning and automatically
 generates the Not to Exceed Billing Exceptions Report. You can use the [Time + Material - Modify Billing](/en/spectrum/spectrum/accounting/time--material/time--material---getting-started/time--material---modify-billing) screen to
 identify specific items, such as add-ons or fees, that may have caused the bill to
 exceed the set amount.
