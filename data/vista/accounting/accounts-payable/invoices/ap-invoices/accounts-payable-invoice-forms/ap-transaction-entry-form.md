---
title: "AP Transaction Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form"
---

# AP Transaction Entry Form

Use the AP Transaction Entry form to enter payable invoices or edit existing invoices, regardless of the form that was used to create the invoice.
In addition to entering invoices directly in this form, you can also edit AP invoices that may have come from any of these forms: AP Recurring Invoices, AP Unapproved Invoices, SL Worksheets, or MS Intercompany Invoices.
Note: The term "transaction" can be used in place of "invoice" because AP processing sometimes requires that an invoice be posted as more than one transaction to be processed appropriately.

Each invoice consists of a header and invoice lines. The header contains the vendor, invoice number, invoice dates, and the invoice total. Additionally, you can set payment and 1099 information, override the vendor's address, and specify an [addenda type](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form/field-definitions-ap-transaction-entry-form#ID-00006e4a--en). Invoice lines represent the detail for the invoice and each invoice must have at least one line.
For each invoice line, you must choose the line type: Job, Inventory, Expense, Equipment, EM Work Order, Purchase Order, Subcontract, or SM Work Order.
 The line type determines what information must be entered to appropriately expense that type of invoice and post it to the related module.

## Trimble Pay (US only)

If you have Trimble Pay, you can access it from this form using the Trimble Pay button (). When selected, you are taken to the Trimble Pay login screen. For more
 information about Trimble Pay, see
 [Trimble Pay](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId::trimble-pay:trimble-pay).

## Attachments

You can use the Attachments feature to add relevant documents to an invoice header or individual invoice lines (such as including a copy of the vendor's invoice). Attachments remain with the invoice/invoice lines through posting and can be viewed on certain reports (such as the AP Vendor Drilldown or GL Trial Balance reports). For information about attaching documents to a record, see [About Attaching Documents to Data Records](/en/vista/vista/system-tools/document-management/dm-workflow/manage-documents/about-adding-documents/about-attaching-documents-to-data-records).
If you are using ePayments to submit vendor payments, you must be set up for uploading invoice attachments to ePayments in order to include them with their associated invoices. You can do this via AP Company Parameters (on the Payment Services tab) by specifying a Client ID and Client Secret (provided by Corpay) and selecting the Upload Invoice Attachments to ePayments? checkbox.
Once you have set up the AP Company options, each time you process a batch, if attachments exist for an invoice, the system adds those attachments to a "queue" and then uploads them to Corpay after the batch processing step completes successfully. Then, when you export and upload invoices in AP ePayments Export, the attachments are linked to the payments on Corpay's website.

## PO/SL Invoice Lines

If you are entering PO or SL detail lines, the system enables the Other Info tab which displays additional information about the purchase order/item or subcontract/item that you referenced.
For purchase orders, the additional information includes the current, received, backordered, invoiced, and remaining units and costs. Additionally, when you enter a PO line, notes associated with the purchase order will display on the PO Notes tab. PO line item notes display in the Item Notes field and PO header notes display in the PO Notes field. Double-click either field to open the Grid Notes window; however, you cannot edit either field here. The PO Notes tab only displays if you have installed the PO module.
 For subcontracts, additional information includes the original, current, invoiced, and remaining units and costs. Additionally, if the invoice was generated from a subcontract claim, many of the fields are disabled. If you need to change the generated invoice, you must first delete the invoice using this form, change the claim using the SL Subcontract Claims form, and re-generate the invoice from the subcontract claim. For more information on subcontract claims, see [About Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims).

## SM Work Order Lines

When entering invoices lines with a line type of 8-SM Work Order, the work order scope specified for the line must be assigned a call type, rate template, and if a job-work order, a phase. If the scope is missing any of this information, the system displays an error and you will be unable to save the record until the specified information is entered for the work order scope in the SM Work Orders form.
If you specify a work order scope that is closed, you will receive a warning and you must either reopen the scope or enter a scope that is open.
For job work orders, if the job associated with the work order has been soft or hard-closed, you can save the record if you allow posting to closed jobs (checkboxes in JC Company Parameters). If you do not allow posting to closed jobs, you will be unable to save the record.
Once you process the invoice batch (via AP Batch Process), the system auto-generates work completed Misc lines (in SM Work Orders) for each invoice line assigned a type of 8-SM Work Order. The units, unit cost, gross, and tax values for the invoice line will become the cost values (Cost Qty, Cost Rate, Cost Subtotal, Cost Tax Type, Cost Tax Code, Cost Tax Basis, Cost Tax Amt, and Total Actual Cost) for the work completed line.

## Field Tickets

Field tickets enable you to link labor, material, and equipment costs related to specific work activity on a job, and facilitate owner billing. When you add job-related lines to an invoice, you can assign each line to a field ticket associated with the contract for the specified job. You can assign multiple invoice lines to a single field ticket, as long as the ticket is open (that is, it has a status of Open). Once the status for a field ticket is set to Closed, Approved, Rejected, or Billed, you can no longer post costs to that ticket.
For PO lines (initialized or manually added), this field is display only and only populates if you assigned a field ticket to the PO item (in PO Purchase Order Entry).
Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to invoice lines for a job is only useful if the job's contract/contract item has a bill type of T&M or Both.

 For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

Related information

- [Enter Accounts Payable Invoices](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/enter-accounts-payable-invoices)

- [Enter AP Invoice Lines: U.S.](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/enter-accounts-payable-invoices/enter-ap-invoice-lines-u.s.)

- [About Vendor Address Overrides for AP Invoices](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-vendor-address-overrides-for-ap-invoices)

- [Process Prepaid Invoices](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/process-ap-invoices/process-prepaid-invoices)

- [Add Posted Transactions Back into a Batch](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/add-posted-transactions-back-into-a-batch)

- [Copy Posted Transactions to an Open-Month Batch](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/copy-posted-transactions-to-an-open-month-batch)

- [Move Unposted Transactions to an Open-Month Batch](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/move-unposted-transactions-to-an-open-month-batch)

- [About Changing Posted AP Invoices](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-changing-posted-ap-invoices)

- [AP Hold and Release Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-hold-and-release-form)

- [AP Prepaid Process Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-prepaid-process-form)

- [AP Unapproved Invoice Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form)

- [AP Recurring Invoices Form](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form)

- [About Discounts](/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/about-discounts)

- [AP Purchase Order Initialize Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-purchase-order-initialize-form)

- [Processing VAT Invoices](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/process-ap-invoices/processing-vat-invoices)

- [On-Cost Invoices](/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices)

- [Process Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)
