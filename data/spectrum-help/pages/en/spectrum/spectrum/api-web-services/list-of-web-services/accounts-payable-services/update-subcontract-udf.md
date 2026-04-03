---
title: "Update Subcontract UDF | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/update-subcontract-udf"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/update-subcontract-udf"
---

# Update Subcontract UDF

Use this service to add or update an existing Subcontract's User Defined Field information for the defined fields only.
WSDL: UpdateSubcon_UDF.jws
Method: UpdateSubcon_UDF
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Subcontract User-Defined Field information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Payable

- System Administration > Installation > Accounts Payable > Subcontract Maintenance

- System Administration > Installation > Accounts Payable > Subcontract User_Defined Fields Maintenance

## Assumptions and Dependencies

- The unique combination of the Vendor code and Subcontract number must exist in the defined Company code.

- The Subcontract-UDF Web Service adds or updates an existing Subcontract's User Defined Field information for the defined fields only.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- The Subcontract user-defined fields need to be defined in Spectrum.

- The Authorized ID must have the user-defined fields defined, or mapped for this Web Service.

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
Text
3
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Vendor_Code
Vendor Code
YES
Text
10
Valid combination of Vendor_Code and Subcontract_Number
Vendor

D
Subcontract_Number
Subcontract Number
YES
Text
10
Valid combination of Vendor_Code and Subcontract_Number
Subcontract

E
UDF1
User Defined Alpha/Numeric/Date 1
+
20
Web Service Authorization ID Service UDF defined.

F
UDF2
User Defined Alpha/Numeric/Date 2
+
20
Web Service Authorization ID Service UDF defined.

G
UDF3
User Defined Alpha/Numeric/Date 3
+
20
Web Service Authorization ID Service UDF defined.

H
UDF4
User Defined Alpha/Numeric/Date 4
+
20
Web Service Authorization ID Service UDF defined.

I
UDF5
User Defined Alpha/Numeric/Date 5
+
20
Web Service Authorization ID Service UDF defined.

J
UDF6
User Defined Alpha/Numeric/Date 6
+
20
Web Service Authorization ID Service UDF defined.

K
UDF7
User Defined Alpha/Numeric/Date 7
+
20
Web Service Authorization ID Service UDF defined.

L
UDF8
User Defined Alpha/Numeric/Date 8
+
20
Web Service Authorization ID Service UDF defined.

M
UDF9
User Defined Alpha/Numeric/Date 9
+
20
Web Service Authorization ID Service UDF defined.

N
UDF10
User Defined Alpha/Numeric/Date 10
+
20
Web Service Authorization ID Service UDF defined.

O
UDF11
User Defined Alpha/Numeric/Date 11
+
20
Web Service Authorization ID Service UDF defined.

P
UDF12
User Defined Alpha/Numeric/Date 12
+
20
Web Service Authorization ID Service UDF defined.

Q
UDF13
User Defined Alpha/Numeric/Date 13
+
20
Web Service Authorization ID Service UDF defined.

R
UDF14
User Defined Alpha/Numeric/Date 14
+
20
Web Service Authorization ID Service UDF defined.

S
UDF15
User Defined Alpha/Numeric/Date 15
+
20
Web Service Authorization ID Service UDF defined.

T
UDF16
User Defined Alpha/Numeric/Date 16
+
20
Web Service Authorization ID Service UDF defined.

U
UDF17
User Defined Alpha/Numeric/Date 17
+
20
Web Service Authorization ID Service UDF defined.

V
UDF18
User Defined Alpha/Numeric/Date 18
+
20
Web Service Authorization ID Service UDF defined.

W
UDF19
User Defined Alpha/Numeric/Date 19
+
20
Web Service Authorization ID Service UDF defined.

X
UDF20
User Defined Alpha/Numeric/Date 20
+
20
Web Service Authorization ID Service UDF defined.

+ NOTE = the UDF (1-20) elements can be Numeric, Date or Text depending on how they are created within Spectrum.
