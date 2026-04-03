---
title: "Delete Work Order Other Charges | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/delete-work-order-other-charges"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/delete-work-order-other-charges"
---

# Delete Work Order Other Charges

Use this service to delete Work Order Other Charges Cost transactions.
WSDL: DeleteWOOtherCharges.jws
Method: DeleteWOOtherCharges
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

Other_Cost_Item
Item Code/Other Charge Code
YES
Text
15
