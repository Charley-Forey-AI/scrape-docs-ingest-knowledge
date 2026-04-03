---
title: "Inventory Item Code Field Definitions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/procedures-overview/in-depth-overview/inventory-item-code-field-definitions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/procedures-overview/in-depth-overview/inventory-item-code-field-definitions"
---

# Inventory Item Code Field Definitions

Learn about the Inventory Item Code Field
 Definitions.
This field displays the purchase unit of measure. For example, if a purchase price is per case, "CS" displays.
Sell Um
This field displays the sell unit of measure. For example, if an item's sell price is per box, "BX" displays.
Um Conversion
This field displays the conversion factor that relates to the Purchase Um and Sell Um fields. Divide the purchase Um by the sell Um to determine the Um conversion.
Price per factor
This field displays the number of goods contained in each unit of measure sold (Sell Um). For example, nails are purchased by the case and each case contains 10 boxes of 500 nails. The nails are sold per box. But when the price is quoted to customers, the quote is per 500 nails. Therefore, the entries in the related item fields will be as follows:
Purchase Um
=
CS

Sell Um
=
BX

Um Conversion
=
10

Price per factor
=
500

If the conversion and price per factor are equal, entry in the Price per Factor field is not required.
Standard Cost
This field displays the cost of purchasing the item from the vendor. When the conversion factor and/or price per factor is used, the standard cost needs to be the price in the Purchase Um field. Spectrum will calculate the unit cost based on the entries in the other fields.
List price
This field displays the selling price or prices, depending upon if you have different price levels for your customers. There are up to five price levels. Given no amount is entered in the PriceperFactor field, then the list price needs to correlate with the Sell Um field. If an amount is entered in the Price per Factor field, the list price needs to correlate with the Purchase Um field.
For example, if nails were purchased for $50.00 per case, the standard cost will be $50.00 and the list price per box will be $5.00. This is calculated as follows:
$50.00 case / 10 boxes
=
$5.00 per box

$5.00 box / 500 nails
=
$0.01 per nail
