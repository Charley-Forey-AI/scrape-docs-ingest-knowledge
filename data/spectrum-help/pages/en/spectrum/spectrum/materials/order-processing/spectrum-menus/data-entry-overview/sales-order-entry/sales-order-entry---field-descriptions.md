---
title: "Sales Order Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/sales-order-entry/sales-order-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/sales-order-entry/sales-order-entry---field-descriptions"
---

# Sales Order Entry - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/ButtonsDescriptions
 Buttons
Save, Cancel, DeleteClick Save to save all entries made in this screen; click Cancel to exit the screen without saving any entries, and click Delete to remove the record in context (the Delete option does not display when adding new records or if you don't have security to remove orders).
Pick ListClick this button to go to the [Print Pick List Form](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/reports-overview/print-pick-list-form) starting screen in context to the current order.
FormClick this button to go to the [Print Sales Order Form](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/reports-overview/print-sales-order-form) starting screen in context to the current order.
ConfirmClick this button to save the current record and display the [Order Confirmation](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/sales-order-entry/sales-order-entry---field-descriptions/order-confirmation) window. This option will not display if the Status = Quote.
The [More Order Information](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/sales-order-entry/sales-order-entry---field-descriptions/more-order-information) window displays based on your setting in the Operator Sales Order Entry Preferences window (accessed from the Command Bar at the top of the screen).
Payment EntryClick this button to open the [Payment Entry or Refund Entry](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/sales-order-entry/sales-order-entry---field-descriptions/payment-entry-or-refund-entry) window when adding or editing orders.
 Customer
Order #If an order is being created, press Enter to accept Spectrum assigned order number. The next number will default from the Next order number field , unless that number is already used. Spectrum will also verify that an invoice with the same number does not already exist when the Order Processing Installation  >  Properties tab option for Use same order/invoice number is selected. If the number is already used, Spectrum increments the next order number until the next order number defaults.
SeqThe sequence number displays. The sequence number indicates the number of back orders that have been created from the original order. New orders are automatically set to "00", and each subsequent back order is incremented by one ("01", "02", etc.). Spectrum now allows you to arrow back to the sequence number. The sequence number can be set to "01" instead of "00", which has the effect of backordering all items on the order. Items on this order will then appear on certain Order Processing reports when printed for backordered items only.
Customer codeEnter the code of the customer placing the order. Double-click to select from a list of available customer codes. Once an order has been created, the customer may not be changed. If the order contains an incorrect customer code, the order must be deleted and re-entered. Note: Since Order Processing does not support multi-currency functionality, entry of a new work order with a customer code that uses multi-currency is disallowed.

Cost centerSpectrum verifies that the cost center is authorized for the specified customer.
Customer P.OEnter the customer's purchase order number.
Customer's jobEnter the customer's job number, if applicable, or press F4 to select from a list of available customer jobs.Within the search window, there is a Maintenance button. Click this button to display the Customer Contract Maintenance window. Use this window (if the Materials Management module is present) to adjust maintenance settings for a selected customer's contract in the Materials Management module.

 Financials
Sales amountSpectrum computes the tax rate based on the current Accounts Receivable processing date.
Sales taxEnter the applicable sales tax code (up to 15 characters are allowed) for this item or press Enter for the customer's default tax code. You must enter a tax code in this field; each item has a taxable flag assigned to as assigned in Scale Interface. Double-click to select from a list of available sales tax codes.
VAT taxThis field only displays when the Utilize value added tax (VAT) tracking? checkbox in Company Installation is selected. Select the Value Added Tax Code you want to use (for example, GST). When selected, the VAT amount will automatically be calculated.
Order totalThe total dollar amount of the order (taxable plus non-taxable plus taxes) displays. No entry is allowed.
Order statusThe order status will default based on your setting in the Operator Sales Order Entry Preferences window (accessed from the Command Bar at the top of the screen). You can designate the order Active quote, Inactive quote, or Sales order. When making changes, you cannot change the order status from Sales order to Active quote or Inactive quote.
Order dateEnter the order date, or press Enter to accept the current processing date for the Order Processing module.
Requested dateEnter the default requested shipping date.
