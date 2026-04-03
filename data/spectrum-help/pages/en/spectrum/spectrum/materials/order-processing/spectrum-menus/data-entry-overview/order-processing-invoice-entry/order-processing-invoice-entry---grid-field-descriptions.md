---
title: "Order Processing Invoice Entry - Grid Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/order-processing-invoice-entry/order-processing-invoice-entry---grid-field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/order-processing-invoice-entry/order-processing-invoice-entry---grid-field-descriptions"
---

# Order Processing Invoice Entry - Grid Field Descriptions

Use the table below for reference when completing the grid fields. You may navigate between the header and grid portion of the screen during entry.
Fields/Buttons
Descriptions

Buttons

The [More Invoice Information](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/sales-order-entry/sales-order-entry---grid-field-descriptions/more-invoice-information) window displays automatically after completing the Requested date field.

Internal Notes
Use this window to enter any relevant invoice notes. The Internal Invoice Notes window displays date-stamped note entries for a specific customer invoice (or credit memo).

Payment Entry
The [Payment Entry or Refund Entry](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/sales-order-entry/sales-order-entry---field-descriptions/payment-entry-or-refund-entry) window is only available if the invoice has not been updated.

Grid Fields

Type
Select Detail or Message from the available drop-down list. Your selection here will determine which column your cursor moves to next.

Item code
 The item code is used for one of two purposes:

1.  It is used to enter a message that will appear on the printed sales order and the picking sheet.

1.  It is used to enter items to be purchased.
If entering a non-stock item, the software will insert the exclamation mark character if you indicate a non-stock item when entering a category code or invalid item code.
 If TRA-SER Pro is present on your system, to import items click the Quick Link button in the Search Inventory Items window. Once TRA-SER opens, highlight one or more items to initiate the inventory retrieval. When items are imported from TRA-SER into this screen, they can be brought in as either 'stock items' that are set up in the inventory file at that time automatically, or as 'non-stock items' for one-time use.

Description
This is a display-only field unless a non-stock item is being entered.

Drop ship?
Select this checkbox is this is a drop ship item. If the item is neither a drop shipment nor a non-stock item and Inventory Control is installed, the item must be stored in the warehouse entered in the first screen. If it is not, an error message displays and the cursor returns to the item code field.

Warehouse
The warehouse will default from the More Invoice Information window or the Inventory Control Installation screen. This field will be blank for non-stock items.
If the 'One warehouse?' checkbox is NOT selected in Inventory Control Installation, you may enter a different warehouse code here.

U/m
If a stock item is entered and the Inventory Control module is installed, the unit of measure in which this item is sold displays. No entry is allowed.
 If a non-stock item is entered or the Inventory Control module is not installed, enter the unit of measure in which this item is sold, for example, EA for each. Enter C to indicate a price per hundred or enter M to indicate a price per thousand. If C or M is used on a non-stock line, the extension will be per-hundred and per-thousand respectively.

Shipped quantity
The quantity of the item previously shipped from this order displays. No entry is allowed.
If Inventory Control is installed, Spectrum checks to see if the quantity ordered is currently available in the warehouse specified on the line item. If the quantity ordered exceeds the quantity available in the specified warehouse, the message QTY > AVAILABLE displays, along with the in-stock quantity available. This message is just a warning message. The quantity ordered can be greater than the quantity on hand. If, when the order is filled, the quantity ordered is still greater than the quantity on hand, a back order can be created. Back orders are created in Order Confirmation.
 More info There is also the option of specifying that an alternate item should be shipped instead, if Inventory Control is installed. If an alternate was specified when this item was entered in Spectrum through Inventory Control, alternate item information is presented. To order the alternate item in place of the original item, enter Y in the field. If the alternate is not acceptable, press Enter.

Back order qty
The number of this item that are on back order displays. If, when the order is filled, the quantity ordered is still greater than the quantity on hand, a back order can be created. Back orders are created in Order Confirmation.
 There is also the option of specifying that an alternate item should be shipped instead, if Inventory Control is installed. If an alternate was specified when this item was entered in Spectrum through Inventory Control alternate item information is presented.
 If this is a credit memo and all items are being credited as bad, enter 0 here so that they are not re-added to the inventory. If items are being credited because of a double billing mistake, enter the same quantity returned as entered in the quantity shipped. When creating a credit memo, enter the quantity to be returned to the inventory.

List price
If Inventory Control is installed, the item price displays. To accept the price, press Enter.
To change the price, type in the different price. If Inventory Control is not installed, enter the list price of one item.

Multiplier
This field is used to link the list price of the previous column with the sell price of the following column. Enter the number by which the list price should be multiplied to obtain the sell price.
After a number is entered, the sell price of the next column will be calculated. If desired, this field can be left blank and a sell price entered; in this case, the multiplier will be calculated automatically.
Note: Example: Enter .9 to provide a 10% discount. For an item with a $700 list price, the sell price is $630 ($700 X .9 = $630).

Sell price
Press Enter to accept the default sell price or enter a new sell price. The sell price is calculated as the product of the two previous columns; that is, list price times multiplier.
 If a number is typed into this field, the multiplier displayed in the previous column will be automatically calculated as the quotient of the list and sell prices.

Extension
The extension, calculated by multiplying the sell price times the quantity ordered, displays. If the customer's credit limit has been exceeded, "OVER CREDIT LIMIT" displays in the message field.

Tax code
Enter the applicable sales tax code for this item or press Enter for the customer's default sales tax code. You must enter a tax code in this field; each item has a taxable flag assigned to as assigned in Scale Interface. Double-click to select from a list of available sales tax codes.
 If you enter a customer sales tax code, that code must have been previously defined in the Accounts Receivable Sales Tax Code Maintenance screen. Spectrum uses the invoice date to compute the sales tax due based on the current tax rate specified in the Accounts Receivable Rate History window.

Tax rate
Spectrum computes the tax rate based on the invoice date.

Taxable?
Select this checkbox if this item is taxable; otherwise, leave this checkbox clear. Detail line items will default to taxable if the customer and item are taxable; otherwise, the line will be nontaxable. This checkbox is updated from the Scale Interface ticket when updated to Order Processing.

G/L department
Enter the G/L department code for this item. These codes are set up in Inventory G/L Department Code Maintenance. Double-click to select from a list of available G/L departments.

Req date
The requested shipment date that was entered in the first Order Entry or Invoice Entry screen displays. Press Enter to accept the default or enter a new requested shipment date for this line item

Commission
The commission modifier specifies the percentage of the sell price of the item that is subject to commission. The default commission modifier is 100%, meaning the salesperson would earn commissions on 100% of this item. If 50% were entered, for example, the salesperson would earn commissions on half the value of the item. The commission modifier can be any amount from 0 to 100%.

Vendor
The vendor code displayed in this field (as recorded in the Inventory Item File Maintenance screen) will only be used when a drop-shipment item is added. No entry name is required. If the item is a non-stock entry, this field is unavailable.

Unit cost
Enter the unit cost for a non-stock drop-ship item.
If an override exists at the warehouse level, default the standard cost from there. If the warehouse-specific standard cost is blank or zero, the standard cost from Item Main Properties will default instead.

Message
Enter any message associated with this item. Double-click to select from a list of available messages.
