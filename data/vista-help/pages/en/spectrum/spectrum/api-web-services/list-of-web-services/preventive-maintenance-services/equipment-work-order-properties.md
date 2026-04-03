---
title: "Equipment Work Order Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/preventive-maintenance-services/equipment-work-order-properties"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/preventive-maintenance-services/equipment-work-order-properties"
---

# Equipment Work Order Properties

Use this service to add new Preventive Maintenance (PM)
 Equipment Work Orders or update existing Preventive Maintenance Equipment Work
 Orders.
 WSDL: EquipWOProperties.jws Method:
 EquipWOProperties
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Preventive Maintenance Equipment Work Order Properties information, the following file maintenance areas must be completed:

- System Administration > Installation > Preventive Maintenance

- System Administration > Installation > Equipment Control

- System Administration > Installation > Preventive Maintenance > Equipment Work Order Maintenance

- System Administration > Installation > Preventive Maintenance > Repair Status File Maintenance

- System Administration > Installation > Preventive Maintenance > Problem Type File Maintenance

- System Administration > Installation > Preventive Maintenance > Problem Cause File Maintenance

- System Administration > Installation > Preventive Maintenance > Priority File Maintenance

- System Administration > Installation > Equipment Control > Equipment File Maintenance

- System Administration > Installation > Accounts Payable > Invoice Routing Approval File Maintenance

## Assumptions and Dependencies

- If Company_Code is blank then use the Authorization ID default value.

- The web service will add new Preventive Maintenance (PM) Equipment Work Orders or update existing Preventive Maintenance Equipment Work Orders.

- The unique combination of the Maintenance_WO_Number and Equipment_Code must exist in order to update an existing record.

- The Equipment_Code is required if creating a new Equipment Work Order.

- The WO_Status is required when creating a new Preventive Maintenance Equipment Work Order. It will use the existing status for validation when updating the record unless otherwise defined.

- Based on the Preventive Maintenance Installation screen Problem_Type and Problem_Cause may be required in the Equipment Work Order.

- The Equipment Work Dates are dependent on the Work Order Status and will use the following logic.

- All dates except the 'Required_Date' must be within the defined modules Processing Dates.

- The status of 'O'pen cannot have the Work_Finished_Date, Work_Finished_Time and Closed_Date populated.

- The status of 'F'inished

- The Closed_Date cannot be populated.

- The Work_Finished_Date is required.

- The status of 'C'losed

- The Work_Finished_Date is required if it does not exist on the Work Order already.

- The Closed_Date must be defined.

- The status and Closed_Date will not update if there are outstanding Purchase Orders for the Equipment Work Order.

- If duplicate records exist to be updated, then they will all be updated as they are processed.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
B
Company_CodeCompany CodeText3Valid Company in Spectrum
C
Maintenance_WO_NumberEquipment Work OrderYESText10** See Assumption and Dependencies.Valid Equipment Work Order that exists.
D
Equipment_CodeEquipment CodeText10** See Assumption and Dependencies.Valid Equipment Code.
E
Create_NewCreate a New Work Order?Text1Must be Y for new. All others will update. ** See Assumption and Dependencies.
F
DescriptionDescriptionText50
G
Service_PersonMechanicText15
H
Meter_NumberMeter numberNumeric1Allows 1, 2, 3 or 4. If blank defaults to 1.
I
PriorityPriorityText10Valid Priority
J
Equipment_Repair_StatusEquipment repair statusText10Valid Equipment Repair Status
K
Routing_CodeRouting codeText10Valid Routing Code
L
WO_StatusWork order statusText1O=Open, F=Finished or C=Closed. Required if creating a new Work Order. ** See Assumption and Dependencies.
M
Problem_TypeProblem typeText10May be required based on the Preventive Maintenance Installation settings.Valid Problem Type
N
Problem_CauseProblem causeText10May be required based on the Preventive Maintenance Installation settings.Valid Problem Cause
O
Order_DateOrder dateDate10Enter as: MM/DD/CCYY (for example, 01/05/2010). If blank then defaults to system date. * See Assumptions and Dependencies
P
Required_DateRequired dateDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
Q
Work_Start_DateWork start dateDate10Enter as: MM/DD/CCYY (for example, 01/05/2010) * See Assumptions and Dependencies
R
Work_Start_TimeWork start date timeText5Military time. Format = HHMM or HH:MMÂ Example = 1602 or 16:02
S
Work_Finished_DateWork finish dateDate10Enter as: MM/DD/CCYY (for example, 01/05/2010).* See Assumptions and Dependencies
T
Work_Finished_TimeWork finish date timeText5Military time. Format = HHMM or HH:MMÂ Example = 1602 or 16:02
U
Return_To_Service_DateReturn to serviceDate10Enter as: MM/DD/CCYY (for example, 01/05/2010) * See Assumptions and Dependencies
V
Closed_DateClosed dateDate10Enter as: MM/DD/CCYY (for example, 01/05/2010). ** See Assumptions and Dependencies
W
Reported_ByReported byText30
X
Contact_NameContact nameText30
