---
title: "Delete Work Order Material Cost | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/delete-work-order-material-cost"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/delete-work-order-material-cost"
---

# Delete Work Order Material Cost

Use this service to delete materials costs on work orders.
WSDL: DeleteWOMaterialCost.jws
Method: DeleteWOMaterialCost
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Field Descriptions

Use the table below for reference when using this service.
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

Company_Code
Company Code
YES
Text
3
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

System_Key
System Key
YES
Text
24
Valid Combination of Work Order and Item Code.

WO_Number
Work Order
YES
Text
10
Must be created within the Work Order module
Valid Work Order

Item_Code
Item Code
YES
Text
15
