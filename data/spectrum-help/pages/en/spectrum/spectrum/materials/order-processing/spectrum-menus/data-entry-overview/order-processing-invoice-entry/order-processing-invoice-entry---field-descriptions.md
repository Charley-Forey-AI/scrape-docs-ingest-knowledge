---
title: "Order Processing Invoice Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/order-processing-invoice-entry/order-processing-invoice-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/order-processing-invoice-entry/order-processing-invoice-entry---field-descriptions"
---

# Order Processing Invoice Entry - Field Descriptions

Use the table below for reference when completing the
 header fields. You may navigate between the header and grid portion of the screen during
 entry.
Fields/Buttons
Descriptions

Buttons

Listing
Click this button to go to the [Invoice Edit List](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/order-processing-invoice-entry/invoice-edit-list) screen.

Form
Click this button to go to the [Print Order Processing Invoice Form](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/order-processing-invoice-entry/print-order-processing-invoice-form)
 starting screen.

Update Sale
Click this button to go to the [Invoice Register Report](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/order-processing-invoice-entry/invoice-register-report) screen.

Update G/L
Click this button to go to the [Invoice G/L Detail Report](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/order-processing-invoice-entry/invoice-gl-detail-report)
 screen.

Reverse
Click this button to go to the [Reverse Order Processing Invoice](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/order-processing-invoice-entry/reverse-order-processing-invoice)
 window.

Fields

Invoice number
If you are adding an invoice and the Use same order/invoice
 number checkbox is selected on the Order Processing
 Installation - Properties screen, the invoice number will default to the
 next available order number that is specified in the Next order number field
 (also located on the Properties screen). Press Enter to accept this
 default or select a different invoice.

Type
Select the entry type from the drop-down list: Invoice or
 Credit memo.

Customer code
Enter the code of the customer being invoiced. Once an
 invoice has been created, the customer may not be changed. If the invoice
 contains an incorrect customer code, the invoice must be deleted and
 re-entered. Double-click to select from a list of available customer codes.
Note:
 Since Order Processing does not support multi-currency
 functionality, entry of a new work order with a customer code that uses
 multi-currency is disallowed.


Cost center
Spectrum verifies that the cost center is authorized for the specified customer.
 Spectrum compares the
 Invoice Entry cost center with the list of cost centers for the customer; if
 the cost center is not listed, then the entry is not allowed.

Customer P.O.
Enter the customer's purchase order number.

Customer's job
Enter the customer's job number, or select from a list of
 available customers using the available Search Material Contracts for
 Customer window.

Financials

Sales amount
This is the total of the amounts displays in the
 Extension column of the grid.

Sales tax
The total sales tax for the current invoice displays.


VAT tax
 This field only displays when the Utilize value added tax (VAT)
 tracking? checkbox in Company Installation is selected.
 Select the Value Added Tax Code you want to use (for example, GST). When
 selected, the VAT amount will automatically be calculated.

Invoice total
This is the sum of the sales amount, sales tax, and any
 VAT tax amounts.

Status
The invoice status displays.

Invoice G/L date
This date is validated against the minimum/maximum date
 setup in [Processing Date Change](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/processing-date-change).

Requested date
This date is validated against the minimum/maximum date
 setup in [Processing Date Change](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/processing-date-change).

From order
This order number field only displays if the invoice
 originated from Order Confirmation.
