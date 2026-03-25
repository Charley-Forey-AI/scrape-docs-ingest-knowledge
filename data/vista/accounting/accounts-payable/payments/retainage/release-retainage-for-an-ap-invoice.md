---
title: "Release Retainage for an AP Invoice | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice"
---

# Release Retainage for an AP Invoice

You can release the retainage for one or more AP invoices using the AP Release Retainage form.
 You must be set up to account for retainage on payable invoices and have already applied retainage to invoices via the AP Transaction Entry form. If this is not the case, see [Enable Retainage for Payable Invoices](/en/vista/vista/accounting/accounts-payable/payments/retainage/enable-retainage-for-payable-invoices) for more information.
Note: The title of the AP Release Retainage form is AP Release Retention for companies in Australia and AP Release Holdback for companies in Canada. References to retainage throughout this topic also mean retention or holdback.
 When you apply retainage to an invoice line (in the AP Transaction Entry form), the system automatically assigns a retainage hold code (defined in the AP Company Parameters form) to the retainage amount. When you create a release retainage batch, you can only add those transactions assigned the specified retainage hold code.
The following video demonstrates releasing retainage for AP invoices.
Note: You must use a browser on your local computer to view this video, and not a browser in the cloud. If you are currently using a cloud-based browser, copy this page's URL and paste it into a web browser on your local computer.

To release retainage on payable transactions:

1. From the main menu, select Accounts Payable > Programs > AP Release Retainage.The Batch Selection form displays.

1. Open a batch using one of the following methods:

- Select Create a new batch and enter the batch month in the Batch Month field.

- Select Use an existing batch and select the appropriate batch from the Unposted Batches grid.Note: If you select this option, you must use a batch that does not contain transactions for placing released retainage back on hold. The system does not allow mixing "release retainage" transactions with "place released retainage on hold" transactions in the same batch.

1. Select OK.The AP Release Retainage form displays.

1. To initialize transactions to the grid:

1. Select the arrow by the Selection Criteria for Release Hold heading to expand the section.

1. Use the selection criteria options to restrict by job, phase, vendor, AP reference number, subcontract number, payable type, and/or payment control code. See the F1 help on individual fields for more information.Note: If you want to release a specific amount, you must select the Restrict by Vendor checkbox, even if you select to use other restriction options.

1. In the Release Date field, enter the release date to apply to all transactions added to the batch.

1. In the Percent of Total drop-down, select how to release retainage. Choose from the following:

- Specific Amount

- Percent of Total

- Percent on Each Invoice

- Manual Entry by Invoice Line

For detailed information about each of the options and how the system uses them, see the F1 help.

1. Select Fill Grid.The populates the grid with all transactions meeting the selected criteria.Note: It is important to note that not all transactions meeting the selection criteria are populated to the grid. The system only includes those transactions where the system was able to fully or partially release held retainage based on the specified or calculated retainage amount.

1. If you wish to initialize additional entries using different filter criteria, repeat the process.Note: Initialization is an iterative process; therefore, regardless of how many times you initialize, the system only adds transactions that meet the criteria and that do not already appear in the grid.

1. Use the grid to update the Release Date and/or Amount for individual transactions as needed.

1. To manually add transactions to the grid:

1. In the Batch Seq field, enter +, N, or New to create a new record.The system assigns the next sequence number.

1. In the Type field, accept the default value (2-Release). This is the only option applicable when releasing retainage for a transaction.

1. In the Expense Month field, enter the expense month for the original AP transaction (the posted month of the original transaction for which retainage was withheld.)The month specified here determines the retainage transactions that are available for selection.

1. Use the Transaction and Line fields to specify the transaction / line for which to release retainage. Press F4 to select from a list of available transactions/lines for the specified expense month.

1. In the Release Date field, enter the release date or accept the default date (today's date).

1. In the Amount field, enter the amount of retainage to release or accept the default amount (original retainage amount less any previously released retainage).

1. [Process the batch](/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/batch-processing/process-a-batch#task-8952--en__task-8952).

The system releases the specified retainage amounts for the selected transactions. For companies that use VAT taxes (such as Australia and Canada), released retainage includes the GST portion of the VAT tax based on the current tax rate. In addition, the system also updates the appropriate GL accounts.For more information about how the system handles the GL updates, see [Updates to GL for Retainage](/en/vista/vista/accounting/accounts-payable/payments/retainage/about-updates-to-gl-for-retainage).

When you are ready, pay the open retainage. For more information, see [Create a Released Retainage Payment Workfile](/en/vista/vista/accounting/accounts-payable/payments/retainage/create-a-released-retainage-payment-workfile).

Related information

- [AP Release Retainage/Retention/Holdback Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-release-retainageretentionholdback-form)

- [AP Payment Posting Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-posting-form)
