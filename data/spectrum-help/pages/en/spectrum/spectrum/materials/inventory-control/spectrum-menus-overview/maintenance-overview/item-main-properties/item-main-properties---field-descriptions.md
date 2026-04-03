---
title: "Item Main Properties - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/maintenance-overview/item-main-properties/item-main-properties---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/maintenance-overview/item-main-properties/item-main-properties---field-descriptions"
---

# Item Main Properties - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field/Button Description
Item codeEnter the item code. The code may be any combination of letters and numbers.
DescriptionEnter a description of the item. This description will print on purchase orders, sales orders and invoices. It will also be displayed on the screen whenever the item code is referenced.
The current standard cost valuation of the mix item displays below this field.

Purchase
Standard costEnter the usual cost of this item from the vendor. This is the cost used throughout the software for default purposes and when the standard costing method is specified. The date this field was last changed is saved, but is updated with the current processing date any time the standard cost is amended using a related screen (such as Inventory Transaction Update, Purchase Order Receiving, and so forth). Entry of a negative number will be disallowed.
Unit of measureEnter an abbreviation for the unit of measure used when this item was purchased. For example, PR for pairs, DZ for dozen, SL for sling, or EA for each. Important: The unit of measure must be set up in Accounts Receivable.

Conversion factorThe conversion factor is used to convert the purchase unit of measure into the sell unit of measure: Purchase unit of measure ÷ sell unit of measure = conversion factor

Sell
Price 1 -5Price 1 (list):
You may assign up to five prices to each inventory item. Customers are assigned a price level (1-5) in the mat level field of the Customer File Maintenance screen for use with the Work Order, Order Processing Materials Management, or Time + Material modules; this amount defaults when the customer price level is 1 or is blank. The item discount in the discount code field is applied only to the first item price, which is considered the list price.
Enter the price which customers or Time + Material jobs with "mat level" equal to 2 will be charged for this inventory item. Entry in this field is not required. Repeat for fields price 3, price 4, and price 5. The date these fields were last changed is saved, but is updated with the current processing dateany time the price is amended using a related screen such as Inventory Transaction Update, Purchase Order Receiving, and so forth. In addition, if changes are made to the Price-per-factor field, these price fields are automatically reset to $0.00.

Unit of measureEnter an abbreviation for the unit of measure used when this item was sold. For example, PR for pairs, DZ for dozen, SL for sling, or EA for each.
Price per factorPrice per factor represents the total number of items being sold at price level 1-5. For example, for an item with a price per factor of 100 and a list price of $35, when 100 units are sold to a customer, the price will be $35. When entering the quantity sold, 100 units are recorded. The unit price is $35. The extension is $35 for the 100 units, and is determined by this formula:
units sold ÷ price per factor X unit price = extension

- Example #1: sell 100 units ÷ 100 X 35 = $35.00

- Example #2: sell 1 unit ÷ 100 X 35 = $0.35

- Example #3: sell 250 units ÷ 100 X 35 = $87.50

The price per factor also applies identically to standard cost, and computation of the actual costs during processing.
The default for this field is 1.0000. Other typical entries are 100.0000 and 1000.0000. You may enter another factor when appropriate, but whenever a change is made to this field, a warning message reminds you that any transactions currently recorded for this item in Purchase Order, Order Processing, Work Order or Inventory Control may be adversely affected by changing the price per factor.
If changes are made, the Standard cost field and Price fields will automatically be reset to $0.00 for this item.

Defaults
PhaseIf this item will only be used during one phase, that phase code may be entered in this field. This phase code will then default in Job Requisition Entry and Purchase Order Entry if the Inventory Control Module is installed. Entry in this field is not required.
Cost typeEnter the default cost type for this item.
Eq cost categoryIf this item will only be used for a specific cost type such as Materials, that cost type may be entered here, if applicable. This cost type will then default in Job Requisition Entry and Purchase Order Entry if the Inventory Control Module is installed.
Markup %Use this (optional) field to enter the markup percentage for items. This will then default in Job Requisition Entry. Note: If you provide materials for your customers at-cost, then mark up the entire job, leave this field blank.

Classification
CategoryEnter the category code to which this item belongs. The product category must be previously defined in Category File Maintenance. The drop-down list displays all valid inventory categories.
ABC classThe ABC class field is used to sub-categorize inventory items within a category. For example, within the category LUMBER, ABC classes could be FORM, FRAMING, TRIM, TREATED, PLYWOOD, and so forth. Because only three characters are allowed, abbreviations are necessary.
Other possible uses for ABC class could be to track high volume to low volume items, high profit margin to low profit margin items, or to track items that require some special handling or review.

EDP part #This field is provided only for use in conjunction with Trade Services.
If a Trade Services disk or CD-ROM is loaded, the part number automatically writes to this field and to the "item code" field. Later the "item code" is changed if desired; when future trade services disks are loaded, this EDP part number is read, and prices modified accordingly.
The EDP part # can be changed in Edit windows if the operator has a security level of 8. Otherwise, the field is display-only.

Vendor part #Enter the part number for this item (up to 15 characters)
Primary vendorEnter the code of the primary vendor of this item. If either the Accounts Payable module or the Purchase Order module is installed, a search window is available for viewing valid vendor codes. Entry is prevented if the vendor status is Not used. A warning is provided when the status is 'Inactive'.
The Reorder Report is sorted by this vendor code to ease order preparation.

Alternate vendorEnter the code of an alternate vendor for this item. If either the Accounts payable module or the Purchase Order module is installed, a search window is available for viewing valid vendor codes. Entry is prevented if the vendor status is Not used. A warning is provided when the status is 'Inactive'.
Status
StatusDesignate the item as Active, Discontinued, or Not used.
If the item has been discontinued, enter the Discontinued date as well.

Options
 Subject to sales tax? Select this checkbox if this inventory item is taxable. If selected, the item will default as Taxable in the Work Order Material Entry screen and in the Order Processing module during Order Entry and Invoice Entry.
Subject to use tax?Select if this item is subject to use tax. Leave clear if the item is not subject to use tax. This field appears only if the Use tax classification checkbox in Job Cost Installation is selected.
Commissions?Select if the person who sells this item will receive a commission. Leave this checkbox clear if the person who sells this item will not receive a commission. Used for information purposes by companies that sell products and is not used by the Order Processing module during Order Entry and Invoice Entry.
Auto-create mix?Select if this is a mix parent code that will be auto-generated during the Materials Management Scale Ticket Update.
Exclude from scale ticket quantity?Select to override the system default of automatically summing all items on the same ticket (in the ticket header). You might select this checkbox to exclude an item with an unusual unit of measure, for example, a ticket which includes 12 tons sand, 12 tons rock, and 1 can of oil.
If you want this item included in the header's sum of quantities, do not select this checkbox.

Exclude from freight quantity?Select to exclude this inventory item from the scale interface freight quantity. This overrides the system default of automatically summing all items on the same freight quantity. You might select this checkbox to exclude an item with an unusual unit of measure, or for an item which has no charge.
If you want this item included on the Scale Interface freight quantity, do not select this checkbox.

Other information
WeightEnter the weight of one sell unit of this item. Total weight will show at the top of purchase orders and in Order Processing during Order Entry and Invoice Entry; the information may be useful for shipping purposes. Entry in this field is not required.
Promotional discountEnter the discount code for this item, if applicable. Discounts are for the companies that sell products through Order Processing during Order Entry and Invoice Entry. Any codes entered here must have been previously defined in Discounts File Maintenance.
Entry in this field is not required, and is irrelevant if the Order Processing module is not installed on the system. When determining the discount price for Work Order materials, the application determines the best material price based on the type of item (stock or non-stock), and whether the item is set up in Inventory Items.
