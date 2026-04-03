---
title: "Other Purchase Order Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/other-purchase-order-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/other-purchase-order-information"
---

# Other Purchase Order Information

Use this window to enter sales tax and routing information
 for the purchase order, as well as credit card payment information (if applicable).
When entering a new purchase order, this window will automatically open after the purchase
 order status is selected.
Note: When adding a new purchase order, all sales tax,
 routing codes, and credit card codes entered in this window must be valid in order to exit
 the window and save. If editing an existing purchase order, existing invalid data does not
 need to be corrected in order to exit the window and save.
Field/Button
Description

Properties

Sales/use tax
Enter the default sales or use tax code
 for this purchase order, if any, or press Enter to accept the default.
 The tax code entered here will default when new rows are added in the Purchase
 Order Entry grid.The tax code will default from Vendor
 Defaults when adding a new P.O. If there is no tax code specified on this
 screen, the tax code will default from the Purchase Order
 Installation screen. If there is no tax code specified on
 either screen, this field will remain blank.
Spectrum computes the sales/use tax rate based on the current Accounts
 Payable processing date and current tax rate.

Routing code
Enter the applicable routing code if
 you are using invoice approval routing for this purchase order.If a routing code is specified, then the code will
 default in One-Step Purchase Order Receiving and Two-Step Invoice Receiving
 Entry. Otherwise, if this field is left blank, then the code derived from
 the routing code hierarchy will automatically default into the receiving
 screen.

Delivery date
Enter the anticipated date of delivery,
 or press Enter to
 leave the date blank. The date entered here will then default onto each detail
 line added in the Purchase Order Detail screen.
Last received
The last date items were received on
 this Purchase Order displays.
Receiving method

Receiving method
Select a receiving method for the
 purchase order:

- One-step (invoice)

- Two-step (packing list + invoice)

This field can be changed at any time until packing
 list entry has been added for this purchase order, invoice receiving has
 been performed for this purchase order, or a revision has been
 created.

Accrue purchase orders costs
If the 'Default new job purchase orders
 to accrue costs' option is selected in the PO
 Installation screen, the purchase order header is set to 'Job',
 and the two-step receiving method is selected above, select this checkbox to
 accrue job purchase orders. If you do not have field-level security access to
 this field, you cannot change the default setting.
Pricing type

Pricing type
Select a pricing type for the purchase
 order:

- Unit price

- Lump sum

This field can be changed at any time until there
 are details present in the grid, or a revision has been created.

Credit card transaction

Purchased with credit card?
Select this checkbox if the purchase
 order items are expected to be purchased using a company credit card. Note: The credit card fields will be unavailable
 if the Cash Management module is not installed.

Credit card account
If the Purchased with credit card
 checkbox is selected, enter the applicable credit card account. The credit card account entered in this field will
 default during Invoice Receiving Entry. During receiving, the software will
 verify that the credit card account is compatible with the cost center
 assigned to this invoice.
Note: This field
 displays only if the credit card account in the Credit card
 account field has multiple credit cards associated with it;
 credit card accounts are set up and maintained in Cash Management > Account File
 Maintenance.

Card #
If the Purchased with credit card
 checkbox is selected, enter the applicable credit card number. This field only
 displays if the credit card account in the Credit card account field has
 multiple credit cards associated with it. Credit card accounts are set up and
 maintained in Cash Management > Account File Maintenance. Note: Credit card information entered in
 this field is simply a default for when the P.O. is received. Spectrum will
 verify that the Operator has security authorization to enter a credt card #,
 but will not validate that the credit card is approved for the cost center.


Other information

Comment
Enter any comments related to the
 purchase order transaction.
