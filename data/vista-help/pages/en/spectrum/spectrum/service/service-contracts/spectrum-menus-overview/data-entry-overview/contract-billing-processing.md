---
title: "Contract Billing Processing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/data-entry-overview/contract-billing-processing"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/data-entry-overview/contract-billing-processing"
---

# Contract Billing Processing

Use Contract Billing Processing to create invoices in
 Accounts Receivable, and will only select scheduled contract billings that have not already
 been updated.
If an alternate bill-to address is specified for the selected contract, this address will
 be transferred to the invoice during the update.
Important: This report should be retained as a permanent
 audit record of the company.
The update screen displays after the Pre-Update Register prints, and will create A/R invoices for the Service Contracts based on the selections of date and customer. The Post-Update Register is based on the invoice date. The update will create one invoice for each scheduled billing in the selected date range. The Post-Update Register will only show billings that were actually updated. When the billing amount in the Contract Billing Table is a negative number, the update will create an A/R credit memo instead of an invoice.
In the event that you need to reverse contract billings updated from
 Contract Billing Processing, use the Accounts Receivable > Reverse Open Invoice Entry screen. When an A/R invoice originating from Contract Billing Processing is
 reversed, the billing records in Service Contract will be updated to reflect the reversal.
 Following the reversal, you can view any of the invoices or credit memos generated for this
 contract, including reversals.
If the invoice being updated references a service contract with an Earned revenue basis of 'As billed', the software will add a record to the Earned Revenue G/L Distribution History Table. The update will assign a different G/L account code to the A/R Invoice Distribution Table when the Earned revenue basis of the contract is not 'As billed'. In this case, the update will assign the 'Invoice deferred revenue G/L account' from the Contract Type Table.
If the billing source for the contract is from Service Contract, the contract will be included in the batch. If the billing source for the contract is from Work Order, then that contract will be skipped during the report compilation and update.
Note: To prevent inactive contracts from being updated to
 Accounts Receivable, remove the 'scheduled date' from the billing records.

Related information

- [Contract Billing Processing - Pre-Update Register](/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/data-entry-overview/contract-billing-processing/contract-billing-processing---pre-update-register)
