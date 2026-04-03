---
title: "Equipment Work Order Component | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/preventive-maintenance-services/equipment-work-order-component"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/preventive-maintenance-services/equipment-work-order-component"
---

# Equipment Work Order Component

Use this service to import Preventive Maintenance Equipment
 Work Order Components information.
 WSDL: EquipWOComponent.jws Method:
 EquipWOComponent
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Preventive Maintenance Equipment Work Order Components information, the following file maintenance areas must be completed:

- System Administration > Installation > Preventive Maintenance

- System Administration > Installation > Equipment Control

- System Administration > Installation > Preventive Maintenance > Equipment Work Order Maintenance

- System Administration > Installation > Preventive Maintenance > Repair Status File Maintenance

- System Administration > Installation > Equipment Control > Equipment Components Maintenance

- System Administration > Installation > Equipment Control > Component File Maintenance

## Assumptions and Dependencies

- If Company_Code is blank then use the Authorization ID default value.

- The Maintenance_WO_Number must have a Work Order Status of Open or Finished to add Components. The Work Order Components will not be updated or a new one added if the status is Closed.

- The Component_Group, Component_Code and Component_Seq are related and all pieces must be tied to the Equipment code defined on the Equipment Work Order.

- To update an existing record the following logic will be applied once a valid Maintenance_WO_Number has been found-.

- Hierarchy Logic

- The unique combination of the Component_Group, Component_Code and Component_Seq.

- The unique combination of the Component_Group, and Component_Code.

- The unique combination of the Component_Group.

- If a unique combination is not found and a record exists it will be updated with the defined information.

- If multiple records exist for an Equipment Work Order for any of the above combinations then an error message will be provide for the user to correct. The web service cannot select which record to update.

- The Work_Ordered_Note is a data field within the screen and will not be appended. It will replace any existing information.

- If duplicate records exist to be updated, then they will all be updated as they are processed.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
B
Company_CodeCompany CodeText3Valid Company in Spectrum. Defaults from the Authorization ID if not populated.
C
Maintenance_WO_NumberEquipment Work OrderYESText10Vaid Equipment Work Order that exists.
D
Component_GroupComponent groupText10** See Assumptions and Dependencies.Valid Equipment Component Group
E
Create_NewCreate New ComponentText1Y=Yes If blank then defaults to N.Creates a new Equipment Component for the Work Order.
F
Warranty_Related_StatusWarranty-relatedText1Y=Yes, P=Possible, E= No, Expired, or N=No, not applicable. If blank then defaults to N.K
G
Repair_Status_CodeRepair StatusText10Valid Repair Status Code
H
Work_Ordered_NoteWork order noteText250Any data provided here will be updated on the screen. It will not append.
I
Component_CodeComponent referenceText10If defined then it must be valid for the defined Component_Group.Â ** See Assumptions and Dependencies.Valid Equipment Component
J
Component_SeqSequenceText5Format = all 5 characters. If defined then it must be valid for the defined Component_Code. ** See Assumptions and Dependencies.Valid for Sequence of the Equipment Component
K
Estimated_HoursEstimated hoursNumeric7Format = 4.2 Positive number only.
L
Actual_HoursActual hoursNumeric7Format = 4.2 Positive number only.
M
Detail_StatusStatusText1O=Open, P=Pending or C=Closed. If blank then defaults to Open.
