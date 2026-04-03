---
title: "Equipment (Get) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/equipment-get"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/equipment-get"
---

# Equipment (Get)

Use this service to import Equipment
 information.
 WSDL: GetEquipment.jws Method: GetEquipment
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Authorization ID controls the security and defaults the pCompany_Code field if left blank in the parameter fields.

- Equipment Status is based on the status type defined for each status code.

- All parameter fields have SuperSelect logic except the following-

- pStatus_Code

- pCost_Center

- pSort_By

## Parameter Fields

Use the table below for reference when using this service.Element NameDescriptionReqTypeMaxField Information
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen.
GUIDUnique reference number created by programmingText36** See GUID definition
pCompany_CodeCompany CodeYESText3Valid Company in Spectrum. Defaults from the Authorization ID if not populated.
pEquipment_TypeEquipment TypeText4Equipment Type File Maintenance
pEquipment_MakeMakeText20Equipment Make Maintenance based on Install option
pEquipment_ModelModelText20Equipment Model Maintenance based on Install option
pYearYearNumeric2
pStatus_CodeEquipment StatusText4Define one specific Status type or leave blank to see Active and Inactive status types only
pCost_CenterEquipment Cost CenterText10Define one specific Cost Center or leave blank to see all based on Authorization ID
pSort_BySort By OptionsText1Blank = Equipment Code or T= Equipment Type

## Return Fields

Use the table below for reference when using this service.Element NameDescriptionTypeMaxField Information
Company_CodeCompany CodeText3Valid Spectrum Company
Equipment_CodeEquipment CodeText10Equipment File Maintenance
Equipment_TypeEquipment TypeText4
DescriptionEquipment DescriptionText30
Equipment_StatusStatusText4Displays data based on the Equipment Status type
YearYearNumeric2
Equipment_MakeMakeText20
Equipment_ModelModelText20
Owned_FlagAcquisition TypeText1O(wned), R(ent) or L(ease)
License_NumberLicense #Text15
Serial_NumberSerial # / VINText50
Division_CodeDivisionText5
Cost_CenterEquipment Cost CenterText10
Error_CodeError CodeText1Used for Error information if needed
Error_DescriptionError DescriptionText250Used for Error information if needed
Error_ColumnError ColumnText100Used for Error information if needed
