---
title: "Field Definitions: AP Purchase Order Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-purchase-order-initialize-form/field-definitions-ap-purchase-order-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-purchase-order-initialize-form/field-definitions-ap-purchase-order-initialize-form"
---

# Field Definitions: AP Purchase Order Initialize Form

The following is a list of field descriptions for the AP Purchase Order Initialize form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## PO

The PO field on the AP Purchase Order Initialize form, Purchase Order tab and Receiver # tab.

Use this field to filter records for display in the grid.
Enter a PO number and select Apply Filter. The grid displays all purchase orders with the specified number and automatically highlights the PO that is an exact match.
If you do not know the entire number, or want to see PO numbers within a certain range, you can enter partial numbers to display records in the grid that contain the specified numbers. The more numbers you enter, the more restrictive the filter will be. For example, if you enter ‘100’, then all PO numbers that begin with ‘100’ will display. If you want to be more restrictive, you might enter ‘1001’. Then only PO numbers that begin with ‘1001’ would display.
Note: If you accessed this form from the AP Unapproved Invoice Entry header and you entered a purchase order in the header's PO field, this field automatically defaults the specified PO. You can override or clear the default if needed.

To remove the filter, clear this field and select Apply Filter.
You can manually select lines to initialize by highlighting each applicable row. When selecting multiple lines, use the Shift key for consecutive selection or the Ctrl
 key for random selection.
Once you have highlighted the lines to initialize, select the Initialize button. After the
 initialization process is complete, you are returned to the invoice entry screen (AP
 Transaction Entry or AP Unapproved Invoice Entry). If errors are found during
 initialization, a message displays indicating the problem, and focus remains in window.
Note: Any line in the grid that is shaded in Red indicates that the purchase order is in an
 open batch. If initializing via AP Transaction Entry, these purchase orders cannot be
 initialized. However, if you are initializing via AP Unapproved Invoice Entry, you can
 initialize these purchase orders, as long as there are units left to invoice (determined
 by invoiced amounts, plus all amounts for the PO in open AP batches and unapproved
 invoice sequences). If there are no units left to be invoiced, no initialization will
 occur.

## Receiver #

The Receiver # field on the AP Purchase Order Initialize form, Receiver # tab.

Use this field to filter the records displayed in the grid.
Enter the receiver number (assigned in PO
 Receipts Entry or PO Initialize Receipts) and select Apply Filter. The grid displays all purchase orders with the specified receiver number.
If you do not know the entire number, or want
 to see receiver numbers within a certain range, you can enter partial numbers to display
 and highlight records in the grid that contain the specified numbers. The more numbers you
 enter, the more restrictive the filter will be. For example, if you enter ‘100’, then all
 receiver numbers that begin with ‘100’ will be displayed; all other POs are excluded. If
 you want to be more restrictive, you might enter ‘1001’. Then only receiver #s that begin
 with ‘1001’ would display.
To remove the filter, delete all numbers and
 select Apply Filter.
You can manually select lines to initialize by highlighting each applicable row. When selecting multiple lines, use the Shift key for consecutive selection or the Ctrl
 key for random selection.
Once you have highlighted the lines to initialize, select Initialize. After the
 initialization process is complete, you are returned to the invoice entry screen (AP
 Transaction Entry or AP Unapproved Invoice Entry). The Items section includes all PO lines you selected to initialize. Additionally each item displays the specified receiver number in the Rec # field. The Rec # field is display only and therefore, cannot be edited.
 If errors are found during
 initialization, a message displays indicating the problem, and focus remains in window.
Note: Any line in the grid that is shaded in Red indicates that the purchase order is in an
 open batch. This will only occur if the purchase order was added manually or initialized
 using PO# rather than Receiver #. If initializing via AP Transaction Entry, these
 purchase orders cannot be initialized. However, if you are initializing via AP
 Unapproved Invoice Entry, you can initialize these purchase orders, as long as there are
 units left to invoice (determined by invoiced amounts, plus all amounts for the PO in
 open AP batches and unapproved invoice sequences). If there are no units left to be
 invoiced, no initialization will occur.
