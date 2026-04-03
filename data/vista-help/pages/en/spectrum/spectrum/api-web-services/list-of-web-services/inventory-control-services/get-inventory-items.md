---
title: "Get Inventory Items | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/inventory-control-services/get-inventory-items"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/inventory-control-services/get-inventory-items"
---

# Get Inventory Items

Use this service to import inventory items.
WSDL: GetInventoryItems.jws
Method: GetInventoryItems
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Authorization ID controls the security and defaults the pCompany_Code field if left blank in the parameter fields.

- Inventory Status is based on the status type defined for each status code.

- All parameter fields have SuperSelect logic except the following-

- pStatus_Type

- pCost_Center

- pSort_By

## Parameter Fields

Element Name
Description
Req
Type
Max
Field Information

Authorization_ID
Authorization ID to access the server
YES
Text
20
Data Exchange Installation Screen.

GUID
Unique reference number created by programming
Text
36
** See GUID definition

pCompany_Code
Company Code
YES
Text
3
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

pItem_Category
Item Category
Text
4
Item Category File Maintenance

pItem_Description
Item Description
Text
35

pEDP_Part_Number
EDP Part #
Text
15

pVendor_Part_Number
Vendor Part #
Text
15

pPrimary_Vendor
Primary Vendor
Text
10
Vendor Maintenance

pStatus_Discontinue_Flag
Status
Text
1
Define one specific Status type of (A)ctive, (D)iscontinued, (N)ot used, or leave blank to see Active and Discontinued status types only.

pCost_Center
Item Cost Center
Text
10
Define one specific Cost Center or leave blank to see all based on Authorization ID

pSort_By
Sort By Options
Text
1
Blank = Item Code, C= Category, E= EDP part #, P= Vendor part #, or V= Primary Vendor

## Return Fields

Element Name
Description
Type
Max
Field Information

Company_Code
Company Code
Text
3
Valid Spectrum Company

Item_Code
Item Code
Text
15
Item Maintenance

Item_Description
Item Description
Text
35

Standard_Cost
Standard Cost
Numeric
11

Purchase_Unit_Of_Measure
Purchase Unit of Measure
Text
2
Displays data based on the Equipment Status type

Unit_Of_Measure_Conversion
Purchase Conversion Factor
Numeric
9

Price_List1
Sell Price 1
Numeric
11

Price_List2
Sell Price 2
Numeric
11

Price_List3
Sell Price 3
Numeric
11

Price_List4
Sell Price 4
Numeric
11

Price_List5
Sell Price 5
Numeric
11

Sell_Unit_Of_Measure
Sell Unit of Measure
Text
2

Price_Per_Factor
Price Per Factor
Numeric
10

Phase_Code
Default Item Phase
Text
20

Cost_Type
Default Cost Type
Text
3

Default_Cost_Category
Default Equip Cost Category
Text
4

Markup_Price
Markup %
Numeric
7

Item_Category
Category
Text
4

ABC_Class
ABC Class
Text
3

EDP_Part_Number
EDP Part #
Text
15

Vendor_Part_Number
Vendor Part #
Text
15

Primary_Vendor
Primary Vendor
Text
10

Alternate_Vendor
Alternate Vendor
Text
10

Unit_Weight
Weight
Numeric
9

Status_Discontinue_Flag
Status
Text
1
Displays data based on the Item Status

Date_Discontinued
Discontinued Date
Date
10

Error_Code
Error Code
Text
1
Used for Error information if needed

Error_Description
Error Description
Text
250
Used for Error information if needed

Error_Column
Error Column
Text
100
Used for Error information if needed
