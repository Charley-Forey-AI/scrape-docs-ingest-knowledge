---
title: "Equipment Tracking Requisition | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-tracking-services/equipment-tracking-requisition"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-tracking-services/equipment-tracking-requisition"
---

# Equipment Tracking Requisition

Use this service to import Equipment Tracking Requisitions
 information.
 WSDL: AddET_Requisition.jws Method:
 AddET_Requisition
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Equipment Tracking Requisitions information, the following file maintenance areas must be completed:

- System Administration > Installation > Equipment Tracking

- System Administration > Installation > Inventory Control

- System Administration > Installation > Equipment Tracking > Transaction Code Maintenance

- System Administration > Installation > Equipment Control > Equipment Code Maintenance

- System Administration > Installation > Inventory Control > Inventory Item File Maintenance

- System Administration > Installation > Inventory Control > Warehouse File Maintenance

- System Administration > Installation > Inventory Control > G/L Department File Maintenance

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phases

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Security > Operator Maintenance

## Assumptions and Dependencies

- The Equipment Tracking Requisition web service updates the History tables automatically due to how they are created in Spectrum using the 'Continue' logic and bypasses the Data Entry tables. **WARNING**

- The Equipment Tracking Requisition web service checks the Historical SQL tables to define whether or not to create a new Requisition or to add detail lines to an existing Requisition based on the required fields matching. The data is appended to an existing Requisition only.

- The Equipment Tracking Requisition header contains the following fields which must match in order to add detail lines to the History table. **WARNING** If all fields match in History they will be added as detail lines.

- Company_Code

- Tool_Requisition_Number

- Transaction_Code

- Job_Company_Code

- Job_Number

- Site_ID

- Requistition_Date

- Expected_Billing_Period

- If the Tool_Requisition_Number exists in the standard Data Entry table then it will not be created.

- If the Tool_Requisition_Number exists in History but none of the other required fields needed for the Requisition header match, then the service will prevent the information from being added.

- The import has a record limit of 990 records per Equipment Requisition and the service will prevent any additional detail lines to be added.

- If the Company_Code is blank then use the Authorization ID default value.

- The Tool_Requisition_Number and Transaction_Code are required fields.

- The Transaction_Code defines whether or not the requisition will be for a Job or Site.

- The Expected_Billing_Period field defaults from the Installation option if defined and not supplied in the record.

- The Inventory Item must exist for the defined warehouse.

- Inventory Non-stock items cannot be created.

- When an Equipment item exists on a current Equipment Tracking Requisition the system automatically creates the 'Return' within Spectrum using the next available Requisition number based on the Installation setting. Therefore if you have defined that number to be used within the web service an error will be returned because that number has already been used.

- Equipment Tracking Requisitions are not created when Physical Inventory is in progress.

- For Intercompany Equipment Tracking Requisitions

- The options and setup must be completed on the company Inventory and/or Equipment Control Installation screens.

- Available for requisitions with direct cost transaction codes (that is, Job deployment type for Transaction Code) and defined in the Equipment's primary company.

- The Quantity field logic

- Required for a requisition that has a defined Item_Code.

- Some requisitions that have a define Equipment_Code require the Quantity to be populated.

- The Expected_Billing_Period field logic

- This is not a required field.

- If field is blank then it will defaults from the Equipment Tracking Installation unless NONE is selected then it will be blank.

- The Notes and Message fields will be truncated if they exceed the Max character length.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
B
Company_CodeCompany CodeText3Valid Company in Spectrum. Defaults from the Authorization ID if not populated.
C
Tool_Requisition_NumberRequisitionYESText7** See Assumptions and Dependencies for multiple detail line logic.Requisition History Table ( defines whether or not to add as a detail line or create new)
D
Transaction_CodeTransaction CodeYESText5Code defines whether it's a job or site requisition. ** See Assumptions and Dependencies for multiple detail line logic.Equipment Tracking Transaction Code
E
Job_Company_CodeIssue to Job Company CodeText3Used for Multi-company requisition feature for Job type Transaction Codes. If blank or option not selected use the Company_Code field for Job Transaction codes. ** See Assumptions and Dependencies for multiple detail line logic.Inventory Control or Equipment Control installation option for Multi-company requisition is defined. Valid Company in Spectrum.
F
Job_NumberJobText10If defined then Site_ID must be blank and Transaction_Code is for Job type. ** See Assumptions and Dependencies for multiple detail line logic.Valid Job in defined Job_Company_Code otherwise valid for defined Company_Code
G
Site_IDSiteText10If defined then Job_Number must be blank and Transaction_Code is for Non-job type. Must have an active status. ** See Assumptions and Dependencies for multiple detail line logic.Work Order Site File Maintenance
H
Requisition_DateRequisition dateDate10Enter as: MM/DD/CCYY (for example, 01/05/2010). Use Current Date for Equipment Tracking module if blank. ** See Assumptions and Dependencies for multiple detail line logic.Must be within the Equipment Tracking min/max dates.
I
Expected_Billing_PeriodMinimum billing periodText1D(aily), W(eekly), M(onthly) or blank only. If blank then use the selected default installation setting. ** See Assumptions and Dependencies for multiple detail line logic.** See Assumptions and Dependencies
J
NotesNotesText1000
K
Item_CodeItemText15If defined then Equipment_Code must be blank.Inventory Item Maintenance
L
Equipment_CodeEquipmentText10If defined then Item_Code must be blank.Equipment Code Maintenance
M
Phase_CodePhaseText20Defaults from Item_Code if left blank.Phase File Maintenance
N
Cost_TypeCost typeText3Defaults from Item_code if left blank. Validates to the defined GL_Debit_Account for direct job cost.Cost Type Maintenance
O
Yard_Or_WarehouseText10Used for Inventory Type only. Warehouse must be defined for Item_Code field. If blank defaults from Inventory Control Installation screen.Warehouse File Maintenance
P
QuantityQuantityNumeric9Allows negative. Whole numbers only.**See Assumptions and Dependencies
Q
MessageMessageText30Detail line message
