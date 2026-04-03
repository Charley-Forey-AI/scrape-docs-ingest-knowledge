---
title: "Purchase Order Installation - Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/installation-overview/purchase-order-installation---properties"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/installation-overview/purchase-order-installation---properties"
---

# Purchase Order Installation - Properties

Use this tab to select default properties settings for the Purchase Order module. These settings can be changed as needed at any time.
Field/ButtonDescription
Next purchase order numberThe system is prompting for the next P.O. number it should assign for new purchase orders. Enter the next number the software should use during Purchase Order Entry. Spectrum features auto-count P/O numbers, or the operator may specify the desired P/O number while adding purchase orders. It is recommended that this number be initialized at some point significantly higher or lower than purchase order numbers presently in use, so that auto-counted P.O. numbers will not interfere with purchase orders already issued to vendors. For example, if purchase orders are currently numbered 1500 to 1600, you may choose to set the next P.O. number to 5001. Alternatively, if purchase orders are presently numbered in the 80000 range, you may elect to commence the Spectrum purchase orders at 10001.

Max received quantity % over orderThe system is prompting for the allowable percentage of overrun when receiving quantities on purchase orders. If the shipment quantity received is greater than the quantity ordered, it may be received only if it does not exceed the designated overrun percentage. If zero is specified in this field, you cannot receive quantities in excess of the ordered amount. If 100% is entered in this field, you may receive up to twice as much as ordered before being stopped. This feature is also useful for companies with "unit price contracts." This type of company can set up purchase orders with each phase of the job listed as a line item with the planned quantities and budgeted unit prices. You can set the percentage to 999% (or other percentage of planned receipts). Unit price contracts allow payment based on quantity installed; therefore, this feature provides the ability to receive more quantity than ordered without having to alter the original (historical/planned) quantity.
Enter the allowable percentage of overrun on received quantities.

Warning for partial receipt in P.O. packing list entry?Select this checkbox to display a warning in the Packing List Quantity Entry page when a partial order has been received; otherwise, leave this checkbox clear. If this checkbox is not selected, the Back Order Alert / Print Options window will not display in the Packing List Quantity Entry page when partial orders are received. Likewise, if this checkbox is selected, the Back Order Alert / Print Options window will display in the Packing List Quantity Entry page when partial orders are received.

Update inventory?Note: Applicable only if the Inventory Control module is installed for this company.
If you select this checkbox, inventory items received into your warehouse during Purchase Order Receiving will be reflected as on-hand amounts in inventory, and will be available for on-page viewing and included on various inventory reports. If you do not select this checkbox, there will be no changes made to any figures in Inventory Control as a result of purchase order activity.

Update packing list to inventory before invoicing?Select this checkbox if this company will update quantities from the packing list whenever a purchase order is assigned the two-step method of receiving.
Update packing list to jobs before invoicing?If the Update packing list to inventory before invoicing option is selected, select this checkbox if this company will update quantities from the packing list to accrue costs to jobs. When this option is selected, the following fields are available for selection:

- Accrued purchase G/L account code. Enter a G/L liability account code that will be used for all direct accrued PO costs. When the accrual is made, Spectrum will debit the job and credit the accrual account. When the invoice arrives, the accrual amount will be credited.

- Default new job purchase orders to accrue costs? Select this option as a default setting in Purchase Order Entry when a new job PO is created. Important: Make sure to select the Post to G/L  >  Purchase Order packing lists option on the General Ledger Installation screen to post packing list transactions to G/L as part of the PO accrual process.

Allow user to override P.O. vendor code during invoicing?Select this checkbox to allow the Operator to record a different vendor code than was assigned to the original purchase order during invoicing.
Edit non-stock quantities in two-step receiving?Select this checkbox to allow quantity receiving of non-stock items in the Inventory Receiving page during the two-step receiving process.
Display received dollar amount in P.O. packing list entry?Select to have purchase order costing information appear on the Packing List Quantity Entry screen. The Unit cost and Extension columns showing amounts derived from costs given in the PO.
Default receiving methodThe system is prompting for you to choose from the following receiving options:

- One-step (invoice)

- Two-step (packing list + invoice)

The One-step process allows entry of quantity and invoice information in a single process.
The Two-step process involves first entering quantities received (often from a packing list), and then entering A/P invoice information when that document arrives from the vendor.
If any purchase orders exist without the receiving method set, the software will prompt to update them during installation.

Update non-job standard costNote: Applicable only if the Inventory Control module is installed for this company.
The system is prompting for to select from the following options:

- Yes

- No

- Update only if cost lower

If you select Yes, the unit cost of the item will be recorded as the new standard cost in the Inventory Item File Maintenance (when an inventory item is included on a purchase order).
If you select No, there will be no change made to the standard cost figure in Inventory Control as a result of purchase order activity.
If you select Update only if cost lower, the standard cost will only be updated from Purchase Order Receiving when the unit cost on the purchase order is lower than the current standard cost in inventory. The standard cost is set when the receiving is finalized in Purchase Order Receiving; this is the same time the A/P invoice is created.

Update standard cost for job detailNote: Applicable only if the Inventory Control module is installed for this company.
Decide whether to update the standard cost figure in the Inventory Item File Maintenance in Inventory Control based on entries during Purchase Order Receiving for job-related Purchase Order Detail; and, if so, under what circumstances. Yes - when an inventory item is included on a purchase order, the unit cost of the item will be recorded as the new standard cost in the Inventory Item File Maintenance.
No - there will be no change made to the standard cost figure in Inventory Control as a result of Purchase Order Receiving.
Update only if cost lower - the standard cost will only be updated from Purchase Order Receiving when the unit cost on the purchase order is lower than the current standard cost in inventory.
