---
title: "Delete Work Order Labor Cost | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/delete-work-order-labor-cost"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/delete-work-order-labor-cost"
---

# Delete Work Order Labor Cost

Use this service to delete labor costs on work orders.
WSDL: DeleteWOLaborCost.jws
Method: DeleteWOLaborCost
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
Valid for the defined Work Order and Employee Code

WO_Number
Work Order
YES
Text
10
Must be created within the Work Order module
Valid Work Order

Employee_Code
Employee code
YES
Text
11
Valid Employee code
