---
title: "Update Equipment UDF | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/update-equipment-udf"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/update-equipment-udf"
---

# Update Equipment UDF

Use this service to update Equipment User-Defined Field
 information.
 WSDL: UpdateEquip_UDF.jws Method:
 UpdateEquip_UDF
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Equipment module must be set up.

- The Equipment code must exist in the defined Company code.

- The Equipment Items user-defined field Information Web Service updates existing equipment's information for the defined fields only.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- The Equipment user-defined fields need to be defined in Spectrum.

- The Authorized ID must have the user-defined fields defined or mapped for this Web Service.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
B
Company_CodeCompany CodeYESText3Valid Company in Spectrum
C
Equipment_CodeEquipment CodeYESText10Equipment Code must exist for the defined Company Code.
D
UDF1User Defined Alpha/Numeric/Date 1+20Web Service Authorization ID Service UDF defined.
E
UDF2User Defined Alpha/Numeric/Date 2+20Web Service Authorization ID Service UDF defined.
F
UDF3User Defined Alpha/Numeric/Date 3+20Web Service Authorization ID Service UDF defined.
G
UDF4User Defined Alpha/Numeric/Date 4+20Web Service Authorization ID Service UDF defined.
H
UDF5User Defined Alpha/Numeric/Date 5+20Web Service Authorization ID Service UDF defined.
I
UDF6User Defined Alpha/Numeric/Date 6+20Web Service Authorization ID Service UDF defined.
J
UDF7User Defined Alpha/Numeric/Date 7+20Web Service Authorization ID Service UDF defined.
K
UDF8User Defined Alpha/Numeric/Date 8+20Web Service Authorization ID Service UDF defined.
L
UDF9User Defined Alpha/Numeric/Date 9+20Web Service Authorization ID Service UDF defined.
M
UDF10User Defined Alpha/Numeric/Date 10+20Web Service Authorization ID Service UDF defined.
N
UDF11User Defined Alpha/Numeric/Date 11+20Web Service Authorization ID Service UDF defined.
O
UDF12User Defined Alpha/Numeric/Date 12+20Web Service Authorization ID Service UDF defined.
P
UDF13User Defined Alpha/Numeric/Date 13+20Web Service Authorization ID Service UDF defined.
Q
UDF14User Defined Alpha/Numeric/Date 14+20Web Service Authorization ID Service UDF defined.
R
UDF15User Defined Alpha/Numeric/Date 15+20Web Service Authorization ID Service UDF defined.
S
UDF16User Defined Alpha/Numeric/Date 16+20Web Service Authorization ID Service UDF defined.
T
UDF17User Defined Alpha/Numeric/Date 17+20Web Service Authorization ID Service UDF defined.
U
UDF18User Defined Alpha/Numeric/Date 18+20Web Service Authorization ID Service UDF defined.
V
UDF19User Defined Alpha/Numeric/Date 19+20Web Service Authorization ID Service UDF defined.
W
UDF20User Defined Alpha/Numeric/Date 20+20Web Service Authorization ID Service UDF defined.
