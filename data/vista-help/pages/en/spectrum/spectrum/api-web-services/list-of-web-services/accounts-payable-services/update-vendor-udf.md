---
title: "Update Vendor UDF | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/update-vendor-udf"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/update-vendor-udf"
---

# Update Vendor UDF

Use this service to add or update an existing Vendor's User Defined Field information for the defined fields only.
WSDL: UpdateVendor_UDF.jws
Method: UpdateVendor_UDF
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Vendor-UDF information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Payable

- System Administration > Installation > Accounts Payable > Vendor

- System Administration > Installation > Accounts Payable > Vendor User-Defined Fields Maintenance

## Assumptions and Dependencies

- The Vendor code must exist in the defined Company code.

- The Vendor-UDF Web Service adds or updates an existing Vendor's User Defined Field information for the defined fields only.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- The Vendor user-defined fields need to be defined in Spectrum.

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
Vendor Code must exist for the defined Company Code.

D
UDF1
User Defined Alpha/Numeric/Date 1
+
20
Web Service Authorization ID Service UDF defined.

E
UDF2
User Defined Alpha/Numeric/Date 2
+
20
Web Service Authorization ID Service UDF defined.

F
UDF3
User Defined Alpha/Numeric/Date 3
+
20
Web Service Authorization ID Service UDF defined.

G
UDF4
User Defined Alpha/Numeric/Date 4
+
20
Web Service Authorization ID Service UDF defined.

H
UDF5
User Defined Alpha/Numeric/Date 5
+
20
Web Service Authorization ID Service UDF defined.

I
UDF6
User Defined Alpha/Numeric/Date 6
+
20
Web Service Authorization ID Service UDF defined.

J
UDF7
User Defined Alpha/Numeric/Date 7
+
20
Web Service Authorization ID Service UDF defined.

K
UDF8
User Defined Alpha/Numeric/Date 8
+
20
Web Service Authorization ID Service UDF defined.

L
UDF9
User Defined Alpha/Numeric/Date 9
+
20
Web Service Authorization ID Service UDF defined.

M
UDF10
User Defined Alpha/Numeric/Date 10
+
20
Web Service Authorization ID Service UDF defined.

N
UDF11
User Defined Alpha/Numeric/Date 11
+
20
Web Service Authorization ID Service UDF defined.

O
UDF12
User Defined Alpha/Numeric/Date 12
+
20
Web Service Authorization ID Service UDF defined.

P
UDF13
User Defined Alpha/Numeric/Date 13
+
20
Web Service Authorization ID Service UDF defined.

Q
UDF14
User Defined Alpha/Numeric/Date 14
+
20
Web Service Authorization ID Service UDF defined.

R
UDF15
User Defined Alpha/Numeric/Date 15
+
20
Web Service Authorization ID Service UDF defined.

S
UDF16
User Defined Alpha/Numeric/Date 16
+
20
Web Service Authorization ID Service UDF defined.

T
UDF17
User Defined Alpha/Numeric/Date 17
+
20
Web Service Authorization ID Service UDF defined.

U
UDF18
User Defined Alpha/Numeric/Date 18
+
20
Web Service Authorization ID Service UDF defined.

V
UDF19
User Defined Alpha/Numeric/Date 19
+
20
Web Service Authorization ID Service UDF defined.

W
UDF20
User Defined Alpha/Numeric/Date 20
+
20
Web Service Authorization ID Service UDF defined.
