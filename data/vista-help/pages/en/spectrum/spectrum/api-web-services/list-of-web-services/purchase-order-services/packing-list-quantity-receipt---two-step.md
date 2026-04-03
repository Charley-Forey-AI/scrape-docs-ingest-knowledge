---
title: "Packing List Quantity Receipt - Two-Step | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/purchase-order-services/packing-list-quantity-receipt---two-step"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/purchase-order-services/packing-list-quantity-receipt---two-step"
---

# Packing List Quantity Receipt - Two-Step

Use this service to import Purchase Order Packing List Quantity Receipt-two step information.

## Connection Information for POST

URL = https://<SPECTRUM-SERVER>:8482/purchaseOrder/PackingList
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Example JSON package

```
`{
 "purchaseOrdersPackingLists": [
 {
 "Company_Code": "em1",
 "PO_Number": "15096",
 "Receipt_Number": "011",
 "Pack_List_Number": "new",
 "Receipt_Date": "01/01/2026",
 "Remarks": "This project will be done on a Time and Material Basis.This proje",
 "PO_Line_Number": "002",
 "Item_Code": "!cups",
 "Quantity_Received": 8
 }
 ]
}`
```

## Underlying File Maintenance

Prior to importing Purchase Order Packing List Quantity Receipt-two step information, the following file maintenance areas must be completed:

- System Administration > Installation > Purchase Order

- System Administration > Installation > Purchase Order > Purchase Order

- System Administration > Installation > Inventory > Inventory Items

## Assumptions and Dependencies

- The Purchase Order Pack List Quantity Receipt web service works for two-step receiving only.

- The web service does not have a 'receive in full?' option. The user must define the quantities per line.

- The web service does not update Sequence Number that have been invoiced.

- The Purchase Order Installation has a setting that allow the user to receive a certain percentage over the quantity. The web service will check this setting.

- If Company_Code is blank then use the Authorization ID default value.

- The PO_Number must exist and have an 'Open' status in order to receive a quantity.

- The PO Line # and Item Code must exist on the Purchase Order.

- The web service will confirm that the Total pack list receipt quantity cannot be greater than the quantity due.

- If the Receipt number is blank it will use the next available numeric value.

- If duplicate records exist to be updated, then they will all be updated as they are processed.

## Field Descriptions

Use the table below for reference when using this service.
Element Name
Description
Req?
Type
Max
Field Information
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

Company_Code
Company code
Text
3
Valid company in Spectrum. Defaults from the Authorization ID if not populated.

PO_Number
PO Number
Text
10
Must exist and be set for 2-step receiving
Purchase Order

Receipt_Number
Sequence #
Numeric
3
Defaults to next available number if blank.

Receipt_Date
Receipt Date
Date
1
If blank, then default to system date. Format: MM/DD/YYYY

 Pack_List_Number
Pack List #
Text
15
Optional

Remarks
Reamrks
Text
65
If the data exceeds the Max characters, it will ignore the remaining characters.

 PO_Line_Line_Number
Purchase Order Line #
Text
3
Combination of PO Line # and Item Code must be valid on the PO

 Item_Code
Item Code
Text
15
Combination of PO Line # and Item Code must be valid on the PO
Inventory Item Code

 Quantity_Received
Quantity Received
Text
12
Format: -7.2.
Total pack list receipt quantities cannot be greater than qty due. Check the PO's system administration settings to see if it allows a specific percentage to be received.
