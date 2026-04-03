---
title: "Cash Receipts Journal | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal"
---

# Cash Receipts Journal

Use the Cash Receipts Journal screen to print the journal
 and cash receipts edit list. If the cash receipts edit list shows an out of balance error,
 correct this before proceeding. Once the journal is printed correctly, continue with the
 update to post transactions to the appropriate Accounts Receivable, Equipment Control, Job
 Cost and General Ledger accounts.
If the G/L account is set to 'Direct equipment cost', the Equipment code and Cost category code will be updated from the invoice distribution line.
Important: This report should be retained as a permanent
 audit record of the company.
Balanced entry protection is incorporated into this function to ensure the General Ledger will stay in balance. If debits do not equal credits (such as due to a power failure or data error), the software will provide a special screen message and disallow update until the problem is corrected. Consult the support desk at Viewpoint for instructions to correct an out-of-balance error.

## If Pay-When-Paid Worksheets are being used:

This screen offers a Fixed Subcontract Payment Worksheet and a Unit Subcontract Payment Worksheet based on the "pay-when-paid" selections made in the [Accounts Receivable Installation - Properties](/en/spectrum/spectrum/accounting/accounts-receivable/installation-overview/accounts-receivable-installation---properties) tab. Spectrum will determine whether any of the cash receipts were paying a draw request invoice with applicable subcontracts. The Accounts Receivable contract setup, not the subcontract setup, is used when determining whether a subcontract appears on the fixed price or unit price worksheet. Each of these optional reports includes a My Reports button to allow you to specify a custom report, if desired. The key to making this process work is to create a one to one relationship between revenue and cost. This relationship is accomplished by using the AR billing items. When the contract is created in Contract Maintenance and the schedule of values is broken down using billing items, the billing items are then attached to the individual phases in Job Cost Phase Maintenance. This creates the one-to-one relationship. If the operator recording and updating receipts is not the same staff person who evaluates the release of funds to subcontractors, these payment worksheets can be emailed to the subcontract administrators as part of the update process.
Note: If Pay-When-Paid processing terms (below) are being used, these worksheets should be disabled in the Installation screen because the processing terms replace the worksheet process.

## If Pay-When-Paid Terms are being used:

During the Cash Receipts Update, the system will look to see whether or not pay-when-paid processing is applicable on each 'Payment' transaction. By rule, only the primary customer is reviewed and transaction codes set as an 'Adjustment' are not included.
When pay-when-paid is applicable, the system then determines if the vendor invoices shall be 'auto-released' or set to 'Review' based on the job's pay-when-paid policy. Here the percentage paid is compared to the policy and vendor invoices are flagged accordingly. The percentage paid is calculated as the amount of the 'current portion' paid divided by the total amount of the 'current portion.' Said another way, the percentage is based on non-retention values of the customer invoice.

Related information

- [Cash Receipts Journal Report](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal/cash-receipts-journal-report)

- [Fixed Price Subcontract Payment Worksheet](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal/fixed-price-subcontract-payment-worksheet)

- [Unit Price Subcontract Payment Worksheet](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal/unit-price-subcontract-payment-worksheet)

- [Pay When Paid](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal/pay-when-paid)

- [Cash Receipts Edit List](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receiptsadjustment-entry/cash-receipts-edit-list)
