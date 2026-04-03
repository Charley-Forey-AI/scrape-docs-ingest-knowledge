---
title: "Add Inventory Items | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/inventory-control-services/add-inventory-items"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/inventory-control-services/add-inventory-items"
---

# Add Inventory Items

Use this service to import Inventory Items information.
WSDL: AddInv_Req.jws
Method: AddInv_Req
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Inventory Items information, the following file maintenance areas must be completed:

- System Administration > Installation > Inventory Control

- System Administration > Installation > Inventory Control > Category File Maintenance

- System Administration > Installation > Inventory Control > Warehouse File Maintenance

- System Administration > Installation > Inventory Control > Discount File Maintenance

- System Administration > Installation > Inventory Control > Item Location File Maintenance

- System Administration > Installation > Inventory Control > Item User-Defined Fields Maintenance

- System Administration > Installation > Accounts Payable > Vendors

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation > Equipment Control > Cost Category Maintenance

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The Inventory module must be set up.

- The Inventory Item Master cost center flag is shared. The Inventory Items import will validate that the company has the cost center option set to Pending or Yes and will set the default for the new Inventory Items to Shared.

- The Inventory Item status will default to (A)ctive if left blank.

- The Location field is required if the Inventory Control Installation screen is set to validate. Otherwise it is a data entry field.

- Warehouse_Code hierarchy

- If populated then validate and set up the warehouse.

- If the Inventory Control Installation screen option 'One Warehouse' is selected, the default warehouse is defined and the field is blank then the field is required. If the default warehouse is defined then set up the item for the defined warehouse code.

- If the Inventory Control Installation screen option 'One Warehouse' is NOT selected and the field is blank then set up the item for ALL warehouses.

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
Unique identifier
No dashes if using Traser.

D
Item_Description
Item Description
YES
Text
35

E
Item_Category
Category
YES
Text
4
Category File Maintenance

F
ABC_Class
ABC Class
Text
3

G
Alternate_Item_Code1
EDP Part #
Text
15

H
Standard_Cost
Standard Cost
Numeric
11
Format = 6.4. Enter decimals but no $ or commas. Positive numbers only.

I
Unit_Of_Measure_Conversion
Purchase Conversion Factor
YES
Numeric
9
Format = 4.4. Positive numbers only.

J
Purchase_Unit_Of_Measure1
Purchase Unit of Measure
YES
Text
2

K
Price_List1
Sell Price 1
Numeric
11
Enter decimals but no $ or commas. Positive only.

L
Price_List2
Sell Price 2
Numeric
11
Enter decimals but no $ or commas. Positive only.

M
Price_List3
Sell Price 3
Numeric
11
Enter decimals but no $ or commas. Positive only.

N
Price_List4
Sell Price 4
Numeric
11
Enter decimals but no $ or commas. Positive only.

O
Price_List5
Sell Price 5
Numeric
11
Enter decimals but no $ or commas. Positive only.

P
Price_Per_Factor
Price Per Factor
Numeric
10
Defaults to 1 if left blank. Format = 4.4-

Q
Sell_Unit_Of_Measure2
Sell Unit of Measure
YES
Text
2

R
Vendor_Part_Number
Vendor Part #
Text
15

S
Vendor_Code_List1
Primary Vendor
Text
10
Vendor Maintenance

T
Vendor_Code_List2
Alternate Vendor
Text
10
Vendor Maintenance

U
Markup_Price
Markup %
Numeric
7
Example: Enter 10.55% as 10.55. Defaults to 0.0% if left blank. Format = 3.2-

V
Phase_Code
Default Item Phase
Text
20
 No Dashes

W
Cost_Type
Default Cost Type
Text
3
Cost Type Maintenance

X
Default_Cost_Category
Default Equip Cost Category
Text
4
Equipment Cost Category Maintenance

Y
Discount_Code
Promotional Discount Code
Text
2
Discount File Maintenance

Z
Unit_Weight
Weight
Numeric
9
Format = 3.4-

AA
Taxable_Flag
Subject to Sales Tax?
Text
1
(Y)es or (N)o only.

AB
Use_Tax_Flag
Subject to Use Tax?
Text
1
(Y)es or (N)o only.

AC
Commission_Flag
Commissions?
Text
1
(Y)es or (N)o only.

AD
Mix_Flag
Auto-create Mix?
Text
1
(Y)es or (N)o only.

AE
Status_Discontinue_Flag
Status
Text
1
(A)ctive, (D)iscontinued or (N)ot used. Defaults to Active if blank.

AF
Date_Discontinued
Discontinued Date
Date
10
Enter as: MM/DD/CCYY (that is, 01/05/00)

AG
Warehouse_Code
Default Warehouse
Text
10
If Installation option 'One warehouse' is not selected and field is left blank then all warehouses will be setup. If 'One warehouse' selected and no default warehouse then field is required.
Warehouse File Maintenance

AH
Location
Item Location
Text
10
Required if I/C Installation screen is set to Y to Validate Item Location. Otherwise this is a user-defined field.

AI
Reorder_Point
Item Reorder Point
Numeric
7
No decimals. Whole numbers.

AJ
Reorder_Quantity
Item Suggested Quantity
Numeric
7
No decimals. Whole numbers.

AK
Exclude_SI_Ticket
Exclude from scale ticket quantity?
Text
1
(Y)es or (N)o only.

AL
Exclude_SI_Freight
Exclude from freight quantity?
Text
1
(Y)es or (N)o only.
