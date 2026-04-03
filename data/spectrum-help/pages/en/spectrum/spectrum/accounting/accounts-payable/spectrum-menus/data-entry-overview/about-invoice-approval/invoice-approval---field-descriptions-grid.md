---
title: "Invoice Approval - Field Descriptions: Grid | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/invoice-approval---field-descriptions-grid"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/invoice-approval---field-descriptions-grid"
---

# Invoice Approval - Field Descriptions: Grid

Use this table for reference when completing the grid
 portion of the Invoice Approval screen.
Only the Approve/Confirm and Reject checkboxes allow entry. All other fields are display-only.
FieldsDescriptions
Group byIf you select one of the 'Group by' options, rows display their shared
 values/entries. Exceptions include: for dates, the earliest date
 displays; for dollar amounts, the sum displays; for the Hold column, all items
 are checked if any were checked.
Selection checkboxesUse these checkboxes to identify the invoices you want to approve, reject, or clear, and then select the corresponding action button.The invoice status will change to Confirmed on those invoices where the operator is the Confirmer, and to Approved on all others.

Vendor
Name
The vendor code and name.
Invoice #The invoice number.
TypeThe invoice type (Invoice or Credit Memo).
StatusStatus types include Unapproved, Approved, and Rejected. If a transaction is approved for confirmation, the status will be Ready to confirm, and Confirmed after being selected for approval.
Status imageDisplays a green check if the status is Approved, or a red 'x' if the status is Rejected.
NotesA blue icon displays if there is at least one routing note record present for the selected invoice. Select the line item and them select the Routing / Notes button to open the [Invoice Approval Routing History Inquiry](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/invoice-approval-routing-history-inquiry) window where you can view existing notes or add a new note. Once a note is added, it cannot be deleted or edited.
Unassigned phasesIf there are any unassigned phases on this invoice, a red exclamation mark appears.
Total AmountThis is the same amount that displays in the heading section of Vendor Invoice Entry. Credit memos display as negative numbers. If using [Approval Limits](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/approval-limits), this amount is what is considered for each reviewer's limit.

PO #When the cursor is on a row with a valid purchase order number, data populates the Purchase Order Info Bar.
Accrued POThis column displays 'YES' if Purchase Order costs were previously accrued for the invoice, and the adjustment amount appears in the invoice distribution section of this window.
SubcontractWhen the cursor is on a row with a valid subcontract number, data populates the Subcontract Info Bar.Note: If a rejected invoice originated from Subcontract Kiosk,
 that billing will be returned to the My Subcontract Billing Entry screen in
 Subcontract Kiosk.

JobThe job code for the invoice displays in this field.
Invoice remarksIf present, invoice remarks display from the invoice header.
Hold?Indicates if the invoice is currently on hold.
Rejected byIf the invoice has been rejected, the reviewer's ID displays.
Invoice dateThe invoice date.
$ before taxThe same amount that displays in the heading section of Vendor Invoice Entry as 'Total before tax'.
TaxThe same amount that displays in the heading section of Vendor Invoice
 Entry. Note: If VAT processing is being used,
 this number includes the 'Total VAT' amount.

Pre-paid?This checkbox is selected if the Instant manual check option is selected in the Payment Details window of Vendor Invoice Entry.
Discount dateThe discount date, if a discount was applied.
Discount $The discount amount defaults from the invoice header.
Last reviewerThe Operator who entered the invoice or last approved it. This field is helpful as a grouping option when reviewing invoices.
Cost centerIf the cost center feature is enabled in the Enterprise Installation screen, the cost center assigned to the invoice header displays.
