---
title: "AP Unapproved Invoice Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form"
---

# AP Unapproved Invoice Entry Form

Use the AP Unapproved Invoice Entry form to enter invoices that you want to pass through the review and approval workflow before posting and payment.
Until invoices are posted, they do not update any subledger or GL, are not eligible for payment, and are not reported as Open Payables (though they are included in Committed Costs). Invoices entered using this form are stored and tracked in a separate set of files until the review and approval process is complete.
Similar to invoices entered directly in the AP Transaction Entry from, you can set payment and 1099 information, override the vendor's address, and set information at the header level. Unlike invoices entered in AP Transaction Entry, however, much of the information in this form is not required in order to save the entry.
Invoice lines represent the detail for the invoice. You can have multiple lines on an invoice, each of the same or differing line types (Job, Inventory, Expense, Equipment, EM Work Order, Purchase Order, Subcontract, and SM Work Order). The line types determine what information must be entered to appropriately expense that type of invoice and post it to the related module.

## Trimble Pay (US only)

If you have Trimble Pay, you can access it from this form using the Trimble Pay button (). When selected, you are taken to the Trimble Pay login screen. For more
 information about Trimble Pay, see
 [Trimble Pay](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId::trimble-pay:trimble-pay).

## Automatic Invoicing with Trimble Construction One

For validated unapproved invoices, you can use Automatic Invoicing in Trimble Construction One to automatically enter invoice headers into Vista without performing manual data entry.
Note: You can only take advantage of Automatic Invoicing if you have Trimble Construction One
 with SSO enabled.

If you are already logged into Trimble Construction One (with your Trimble ID login/password), you can access Automatic Invoicing from this form by selecting the Automatic Invoice Entry button below the toolbar. You can also access Automatic Invoicing as follows:

- From the Vista main menu, by selecting Accounts Payable > Programs > AP Automatic Invoice Entry.

- From the Trimble Construction One workcenter, by logging into [team.viewpoint.com](http://team.viewpoint.com/) and then selecting Accounts Payable from the main menu.

Note: If you do not have Trimble Construction One
 with SSO enabled, selecting the Automatic Invoice Entry button in AP Unapproved Invoice Entry or the AP Automatic Invoice Entry link in the Accounts Payable Programs menu accesses a Trimble Viewpoint Automatic Invoicing product page.

For instructions on how to enable and use Automatic Invoicing, see [Automatic Invoicing (for Trimble Construction One Users)](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/automatic-invoicing-for-trimble-construction-one-users).

## Attachments

You can use the Attachments feature to add relevant documents to an unapproved invoice header or individual invoice lines. For example, you may want to include a copy of the vendor's invoice at the line level so that reviewers can access it during their review. The attachments added to an invoice header or invoice line will remain with the invoice through the review and posting process, and can be viewed on certain reports (such as the AP Unapproved Invoice Drilldown report).
 For information about attaching documents to a record, see [About Attaching Documents to Data Records](/en/vista/vista/system-tools/document-management/dm-workflow/manage-documents/about-adding-documents/about-attaching-documents-to-data-records).

## Field Tickets

Field tickets enable you to link labor, material, and equipment costs related to specific work activity on a job, and facilitate owner billing. When you add job-related lines to an unapproved invoice, you can assign each line to a field ticket associated with the contract for the specified job. You can assign multiple invoice lines to a single field ticket, as long as the ticket is open (that is, it has a status of Open). Once the status for a field ticket is set to Closed, Approved, Rejected, or Billed, you can no longer post costs to that ticket.
For PO lines (initialized or manually added), this field is display only and only populates if you assigned a field ticket to the PO item (in PO Purchase Order Entry).
Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to invoice lines for a job is only useful if the job's contract/contract item has a bill type of T&M or Both.

 For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

Related information

- [About the HQ Reviewers Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewers-form)

- [About the HQ Reviewer Group Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form)

- [Process Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)

- [About Setting Up Default Reviewers for Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-setting-up-default-reviewers-for-unapproved-invoices)

- [About Reviewer Groups' Interaction with Individual Reviewers](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-reviewer-groups-interaction-with-individual-reviewers)

- [Optional Reviewer](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form/field-definitions-hq-reviewer-groups-form#ID-0000f72b--en)
