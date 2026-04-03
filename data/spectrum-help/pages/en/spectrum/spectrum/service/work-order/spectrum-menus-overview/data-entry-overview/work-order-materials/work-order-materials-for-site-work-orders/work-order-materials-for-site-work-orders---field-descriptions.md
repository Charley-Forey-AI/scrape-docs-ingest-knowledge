---
title: "Work Order Materials for Site work orders - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-materials/work-order-materials-for-site-work-orders/work-order-materials-for-site-work-orders---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-materials/work-order-materials-for-site-work-orders/work-order-materials-for-site-work-orders---field-descriptions"
---

# Work Order Materials for Site work orders - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field
Description

Item code
Enter an Inventory item code here. This
 field will be view-only when editing a material item. If
 a non-stock item code is entered here, the operator will be prompted for an
 item description. Click the Proceed as Non-Stock button to proceed with the invalid
 entry.

Warehouse
Enter a warehouse code. For Purchase
 Order or A/P Invoice source transactions, the Vendor code will display in this
 field, and the Invoice # will display in the field beneath it.
Quantity
Enter a quantity for the selected
 inventory item. The quantity can be left blank and the material will not be
 billed, even if an invoice extension is entered. When the
 Inventory Control module is present, the software will check the quantity
 entered against available items in this warehouse. If the software
 determines that the available quantity for this item is less than the
 quantity entered, a warning message will appear. This message will not
 appear in the Edit or View
 windows.

Unit of measure
For stock items this field will be
 display-only. For non-stock items the operator will need to enter a unit of
 measure.
Source
The source of the material transaction
 (Entry, Purchase Order, A/P Invoice) displays in this view-only field.
Status
The status of the material transaction
 displays in this view-only field.
Details

G/L department
Enter a G/L Department for this
 transaction.
Task
Enter a work order task for this
 transaction.
Task completed?
If a task was entered above, this check
 box will be available to select if the task was completed.
Equipment
This field will default from the task
 setup in the work order header, when a task code has been entered for the
 transaction. Entry of a valid equipment code will be
 required if the Work Order installation option Require equipment
 code for work order transactions is selected. A warning will
 display if the operator enters an inactive equipment code, but entry will
 still be permitted.
Note: This field
 will be view-only for Purchase Order and A/P Invoice
 transactions.

Component
Enter a component code. The component
 will default from the previous line if the operator remains in Add mode to
 enter multiple detail lines. This field will only be
 enabled if components are set up for the previously selected piece of
 equipment, or the Work Order installation option Require
 component code for work order transactions is
 selected.
Note: This field will be
 display-only for Purchase Order and A/P Invoice transactions.

Contract
Enter a service contract number. If a
 service contract is specified in the work order header, the contract number
 will default if valid for the previously selected equipment and component, or
 the Contract field can be left blank. If the next
 Equipment code selection disables the contract, this field will be disabled. Entry of a proposed service contract will be
 disallowed.
A contract specified in the Flat Rate
 Task Table will default when a particular task code has been specified if
 (a) there is a valid contract code assigned to the task, and (b) the
 equipment code for the task is the same as the one specified in the
 Labor Hours transaction entry window.
Note: This field will be display-only for
 Purchase Order and A/P Invoice transactions.

Accrue use tax
Select this checkbox if the material
 item will accrue use tax instead of sales tax. When selected, this amount will
 be included in the Standard Cost calculation.
Customer billing

Bill customer for this material?
Select this checkbox to bill the
 customer for the material transaction. For flat-rate work orders the default is
 cleared.
Taxable on customer invoice?
Select this checkbox if you wish to
 make the material transaction taxable to the customer. This checkbox will be
 unavailable if Bill customer for this material is
 cleared.
Show this item on A/R invoice in detail?
Select this checkbox if you wish to
 show this material transaction on the A/R invoice. This checkbox will be
 unavailable if Bill customer for this material is
 cleared.
Standard cost
This field will be labeled according to
 the type of entry and item code entered.

- If a stock item is entered, this field will be
 labeled Standard
 cost and will be display-only.

- For non-stock items, this field will be labeled
 Unit cost
 and the operator will be permitted to enter a unit cost for the item.

- For Purchase Order source transactions, this field
 will be labeled P.O. unit
 cost. This display-only field will show the extension from
 the corresponding P.O. detail line, plus any sales or use tax. This total
 will be the original P.O. unit cost, determined at the time the billing
 entry was created. To view the actual cost for P.O. source transactions,
 refer to the Work Order Cost History Inquiry.Note: If this information is incorrect, the operator will need to make
 corrections to the P.O. itself in Purchase Order Entry.

- For A/P Invoice source transactions, this field will
 be labeled Actual unit
 cost. This total will be computed by dividing the total
 cost by the work order quantity in the header, and multiplying by 100 if
 the unit of measure is "C", or multiplying by 1000 if the unit of measure
 is "M". Unit cost will be equal to total cost when the quantity is 1 or
 0.

Unit price
When a direct work order cost entry is
 added, the software automatically calculates the Unit price, including material
 markup rates. If the Unit cost or Quantity is changed, the software will
 automatically recalculate and default a new Unit price value.If the operator clicks OK, the
 software will default the new lowest price in this field and update the
 Invoice Extension total. The work ordered (entered) date is used by default
 to calculate the best price. If the operator wants to calculate based on a
 different date, click the lookup icon to open the [Item Price Inquiry](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-recurring-invoice-entry/item-price-inquiry) window and select a different date.

Invoice extension
This field computes the invoice amount
 when the Bill customer for this material checkbox is
 selected.

- For stock items, the invoice extension is computed
 by multiplying Quantity x Unit Price / Price-per-factor.

- For non-stock items, the invoice extension is
 computed by multiplying Quantity x Unit Price. If the Unit of measure is
 "C" the extension is divided by 100, and if the Unit of measure is "M"
 the extension is divided by 1000.

Example:
Qty = 23
 Unit cost = $5.00
Cost basis
 (Extension) = $115.00 (Say Cost basis 100.01 through 200.00 = 25% in the
 Non-stock Markup table)
 $115.00 x 1.25 = $143.75

This amount backs into the Unit price ($6.25)
 using the markup associated with the cost basis.

Warranty

Expiration date
This view-only field will display the
 warranty expiration date if warranty information is stored in the site table
 for the previously selected component. If multiple warranties are specified in
 Site File Maintenance, the latest date will be shown
 here.
Bill manufacturer for this material?
Select this checkbox to bill the
 manufacturer for the material transaction. The default is cleared, unless the
 previously selected equipment component has an active warranty.
Taxable on manufacturer invoice?
Select this checkbox if you wish to
 make the material transaction taxable to the manufacturer. This checkbox will
 be unavailable if Bill customer for this material is
 cleared.
Manufacturer
The Manufacturer code will default from
 warranty setup if a warranty exists for the previously selected equipment
 component. If Bill manufacturer for this material is
 checked, a valid manufacturer code must be specified.
Billing rate
This field will default from the
 material price of the item based on the warranty setup. If the operator changes
 the manufacturer code setting, the billing rate will be reset to 0.00. Billing rates for non-stock warranty items will need to
 be entered manually.

Warranty extension
This field computes the warranty
 invoice amount when "Bill manufacturer for this material" is selected.

- For stock inventory items, the warranty extension is
 computed by multiplying Quantity x Billing rate / Price-per-factor.

- For non-stock materials, the warranty extension is
 computed by multiplying Quantity x Billing rate. If the unit of measure
 is "C" the extension is divided by 100, and if the unit of measure is "M"
 the extension is divided by 1000.
