---
title: "Get Pay Types | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/get-pay-types"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/get-pay-types"
---

# Get Pay Types

Use this service to import Pay Types information.
WSDL: GetPayType.jws
Method: GetPayType
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Authorization ID controls the security and defaults the pCompany_Code field if left blank.

- Pay Types within Spectrum are hard coded within the software.

- The Incentive (*I) is not supported for this web service.

- All parameter fields have SuperSelect logic except the following-

- pPay_Type

- pSort_By

## Parameter Fields

Use the table below for reference when using this service.
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

pPay_Type
Pay Type
Text
2

pSort_By
Sort By Options
Text
1
Blank = Company Code and Pay Type or T= Pay Type

## Return Fields

Use the table below for reference when using this service.
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

Pay_Type
Pay Type
Text
4

Pay_Type_Desc
Pay Type Description
Text
30

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
