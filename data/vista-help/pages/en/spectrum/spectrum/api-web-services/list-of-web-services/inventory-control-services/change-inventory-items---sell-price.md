---
title: "Change Inventory Items - Sell Price | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/inventory-control-services/change-inventory-items---sell-price"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/inventory-control-services/change-inventory-items---sell-price"
---

# Change Inventory Items - Sell Price

Use this service to update existing inventory item's information for the defined fields only.
WSDL: UpdateInv_SellPrice.jws
Method: UpdateInv_SellPrice
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Inventory module must be set up.

- The Inventory Item code must exist in the defined Company code.

- The Inventory Items-Sell Price Web Service updates existing inventory item's information for the defined fields only.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the
 Spectrum Excel Office Add-in templates for data entry points.
Excel
Element Name
Description
Req
Type
Max
Format
Validation

Authorization_ID
Authorization ID to access the server
YES
Text
20
Data Exchange Installation Screen

GUID
Unique reference number created by programming
Text
36
** See GUID definition

B
Company_Code
Company Code
YES
Text
3
Valid Company in Spectrum.

C
Item_Code
Item Code
YES
Text
15
Valid Inventory Item Code must exist for the defined Company Code.

D
Standard_Cost
Standard Cost
Numeric
12
Format = 6.4. Enter decimals but no $ or commas. Positive numbers only.

E
Price_List1
Sell Price 1
Numeric
10
Format = 7.2. Enter decimals but no $ or commas. Positive only.

F
Price_List2
Sell Price 2
Numeric
10
Format = 7.2. Enter decimals but no $ or commas. Positive only.

G
Price_List3
Sell Price 3
Numeric
10
Format = 7.2. Enter decimals but no $ or commas. Positive only.

H
Price_List4
Sell Price 4
Numeric
10
Format = 7.2. Enter decimals but no $ or commas. Positive only.

I
Price_List5
Sell Price 5
Numeric
10
Format = 7.2. Enter decimals but no $ or commas. Positive only.

J
Price_Per_Factor
Price Per Factor
Numeric
8
Format = 4.4-

K
Sell_Unit_Of_Measure2
Sell Unit of Measure
Text
2

L
Markup_Price
Markup %
Numeric
7
Example: Enter 10.55% as 10.55. Format = 3.2-
