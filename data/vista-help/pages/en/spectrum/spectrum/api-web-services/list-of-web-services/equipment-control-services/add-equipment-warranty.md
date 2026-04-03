---
title: "Add Equipment Warranty | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/add-equipment-warranty"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/add-equipment-warranty"
---

# Add Equipment Warranty

Use this service to add warranty information to existing
 equipment items.
 WSDL: AddEquip_Warranty.jws Method:
 AddEquip_Warranty
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Equipment module must be set up.

- The Equipment code must exist in the defined Company code.

- The Equipment Warranty type and Warrantor code must exist in the defined Company code.

- The Equipment Items - Warranty Information Web Service adds Warranty information to existing Equipment's Item.

- The Warranty information will be for the Equipment level only.

- The Warranty_Meter must exist on the Equipment and have a defined start and expired meter readings to be added.

- The Warranty can be added to the Equipment repeatedly if desired based on the Spectrum Database.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
B
Company_CodeCompany CodeYESText3Valid Company in Spectrum
C
Equipment_CodeEquipment CodeYESText10Valid Equipment Code in Spectrum
D
Warranty_TypeWarranty TypeYESText10Equipment Warranty File
E
Warrantor_CodeWarrantorYESText10Equipment Warrantor File
F
Warranty_StartWarranty Start DateDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)Valid date corresponding to expiration date if entered
G
Warranty_ExpirationWarranty Expiration DateDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)Valid date corresponding to start date if entered
H
Warranty_Strt_MeterWarranty Start Meter ReadingNumeric9Positive numbers onlyValid number corresponding to expiration meter reading if entered
I
Warranty_Expire_MeterWarranty Expiration Meter ReadingNumeric9Positive numbers onlyValid number corresponding to start meter reading if entered
J
Warranty_MeterWarranty Meter NumberText1Enter Meter number (1, 2, 3 or 4). Warranty_Strt_Meter and Warranty_Expire_Meter must be populated if defined.Meter must be defined on the Equipment.
K
Warranty_CommentsWarranty CommentsText100
