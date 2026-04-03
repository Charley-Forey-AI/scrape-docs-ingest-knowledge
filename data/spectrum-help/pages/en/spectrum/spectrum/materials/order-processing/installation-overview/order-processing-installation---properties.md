---
title: "Order Processing Installation - Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/order-processing/installation-overview/order-processing-installation---properties"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/order-processing/installation-overview/order-processing-installation---properties"
---

# Order Processing Installation - Properties

Use this screen to define the default properties settings for the Order Processing module. Usually you will only be using the installation screens when you are originally setting up a module, but these settings can be changed at any time.
Fields
Descriptions

Always link to payment entry?
The system allows you to either manually or automatically open the window in which to record point of sales receipts. If this checkbox is selected, the window will open automatically. If this checkbox is left clear, the window will not open automatically, but may still be opened by the user when needed.

Use same order/invoice number?
If this checkbox is selected, then invoices created via order confirmation will be assigned the number from that order, and invoices created in invoice entry will be assigned the next order number. If the two numbers should be different, leave this checkbox clear. One advantage to using different numbering sequences is that it will be easy to distinguish orders and invoices simply by looking at the number.
If this checkbox is selected, then when adding an order in Order Entry, adding an invoice in Invoice Entry, or confirming a quote, Spectrum will default the next available order number that is specified in the Next order number field at the bottom of this tab.

Maintain order log?
The system is prompting you to decide whether to maintain a log of your sales order activity. The log stores useful information about order number assignments, status, and deletions. If this checkbox is left clear, the order log file will not be updated during order and invoice processing. If this checkbox is selected, this information will be stored in the system.

Maintain invoice log?
The system is prompting you to decide whether to maintain a log of your invoicing activity. The log stores useful information about invoice number assignments, status, and deletions. If this checkbox is left clear, then the invoice log file will not be updated during order and invoice processing. If this checkbox is selected, then this information will be stored in the system.

Retain fully shipped items on orders?
The system is prompting you to decide whether to retain fully shipped line items on subsequent backorders created during the order confirmation processing. If you want your backorders to include only items yet to be shipped, then leave this checkbox blank. Otherwise, if all items ordered (including those already shipped in full) should remain listed on backorders, select this checkbox. Most users only wish to show unshipped items on backorder invoices; in this case, leave this checkbox blank. Entry in this field affects how backorders will appear.

List all ordered items on invoices?
The system is prompting you to decide whether to include all line items from the sales order on invoices created during the Order Confirmation process. If all items listed on the sales order (including those not currently being shipped) should be contained on invoices, select this checkbox.

Print negative inventory report with invoice register?
If you select this checkbox, an exceptions report will be included when the Invoice Register Report prints. The exceptions reports can be used to alert you that there is not enough stock to cover orders. Negative inventory might indicate that a receipt hasn't been processed, or that a wrong item code was entered.
If you leave this checkbox blank, you will not be notified when inventory does not cover orders.

Print negative inventory report with invoice detail register?
If you select this checkbox, an exceptions report will be included when the Invoice Detail Register prints. The exceptions reports can be used to alert you that there is not enough stock to cover orders. Negative inventory might indicate that a receipt hasn't been processed, or that a wrong item code was entered.
If you leave this checkbox blank, you will not be notified when inventory does not cover orders.

Next order number
The system is prompting for the next order number the system should assign for sales orders. Enter the next number the system should use during Order Entry. Spectrum features auto-count order numbers, or the operator may specify the desired order number while adding orders. Order numbers are not to be confused with invoice numbers: a sales order is created when a customer places an order; this order may result in one or more invoices depending upon whether some portions require a backorder; likewise, an order may occasionally result in no invoice at all if, for example, the customer soon cancels the order completely. It is recommended that the order number be initialized at some point significantly higher or lower than invoices issued to customers. For example, if invoices are to be numbered 5000, you may choose to set the next order number to 20001 or 101. Alternatively, if invoices are presently numbered in the 50000 range, you may elect to commence the Spectrum orders at 1001.
The number assigned in this field will applied to new invoices created in Invoice Entry if the User same order/invoice number checkbox is selected on this tab.

Next invoice number
The system is prompting for the next invoice number the system should assign for invoices. Enter the next number the system should use during Order Confirmation and Invoice Entry. Spectrum features auto-count invoice numbers, or the operator may specify the desired invoice number while adding invoices. It is recommended that this number be initialized at some point significantly higher or lower than invoice numbers presently in use so that auto-counted invoice numbers will not interfere with invoices already issued to customers. For example, if invoices are currently numbered 1500 to 1600, you may choose to set the next invoice number to 5001. Alternatively, if invoices are presently numbered in the 80000 range, you may elect to commence the Spectrum invoices at 10001.
If the User same order/invoice number checkbox is selected on this tab, the number assigned in this field will not be applied to new invoices created in Invoice Entry; in this situation, the next invoice number that defaults in Invoice Entry will be assigned according to the number in the Next order number field.

Use header cost center for invoices?
Select this checkbox to change the Order Processing G/L update to use the header cost center for Sales, Accounts Receivables and Cost of Goods Sold entries. Inventory entries will always use the cost center assigned to the warehouse.
Note: This field will only appear if cost centers are enabled for the selected Spectrum company.
