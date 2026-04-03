---
title: "Add G/L Journal Entries | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/general-ledger-services/add-gl-journal-entries"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/general-ledger-services/add-gl-journal-entries"
---

# Add G/L Journal Entries

Use this service to import G/L Journal Entries
 information.
 WSDL: AddGLTrans.jws Method: AddGLTrans
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing G/L Journal Entries information, the following file maintenance areas must be completed:

- System Administration > Installation > General Ledger

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phases

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation > Equipment Control > Equipment

- System Administration > Installation > Equipment Control > Cost Category File Maintenance

- System Administration > Installation > Work Order > Site File Maintenance

- System Administration > Installation > Work Order > Work Order Entry

- System Administration > Installation > Service Contracts > Service Contract File Maintenance

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The GL JE transactions sent will be grouped as a batch, create one journal entry, and must be in balance.

- The GL Journal Web service is company-specific, therefore each group (or batch) sent must be for the same company code.

- The import file has a record limitation of 900 records per batch. If the journal entry contains a significant amount of inter-company cost center transactions, then you should create manageable journal entries so that the General Ledger Journal Entry Update can process them correctly.

- The first record of the import will define the following fields for the Journal Entry header information:

- Journal Entry Transaction date

- Journal Entry Description

- Journal Entry Remark

- If the General Ledger Code is set to Direct Cost = N (Non-direct):

- Any data defined in the Job Cost,
 Equipment, or Work Order fields will
 be ignored and not populated.

- If the General Ledger Code is set to Direct Cost = Y (Job Cost):

- The Job_number, Phase_code, and Cost_type are mandatory and validated.

- In Spectrum Companies not using Cost Centers, when the Job Cost Installation's "Validate job division with G/L department?' is:

- cleared then the G/L code must be a direct cost code and valid for the cost type.

- Checked but the 'Auto default G/L department?' is not checked then the G/L code is validated to the Job's Division code and an error is received: "The Job Division does not match the G/L department' when they do not match.

- Checked AND the 'Auto default G/L department?' is checked then the G/L code will be auto-switched to match the Job's Division and G/L Department codes.

- If the General Ledger Code is set to Direct Cost = E (Equipment):

- The Equipment_Code and Equipment_Cost_Category are both mandatory and validated.

- The Equipment_Work_Order is required optional or not allowed (none) based on the defined Equipment Cost Category data entry rule.

- The Equipment Cost Category Code contains General Ledger Overrides.

- If field is blank then will default from the Cost Category Code.

- If defined it will validate to the GL Overrides and the Cost Category Code.

- If the General Ledger Code is set to Direct Cost = W (Work Order):

- The WO_Number is required.

- The WO_Equipment is required and validated when the Work Order
 InstallationRequire equipment code for work order transactions? checkbox
 is selected.

- The WO_Component is required and validated when the Work Order
 InstallationRequire component code for work order transactions? checkbox
 is selected AND the WO Equipment assigned has Components.

- The WO_Contract is not required, but if it is populated it will be validated.

- The WO_Sellprice is not required, but defaults the GL debit or credit amount.

- This Web Service will work the defined Workflow process in Spectrum.

- Cost center information will only be allowed in if the Company is set to a Yes status.

- The first record must contain the Cost Center for the Header.

- The detail lines will follow standard Cost Center logic.

- For a Cost Center company, the following logic is used:

- The Cost_Center field name is mandatory and validated for a non-direct GL_Account field name.

- The Cost_Center field name is not required for a direct cost GL_Account because it will use standard Spectrum logic based on the direct cost type defined below:

- For direct Job cost GL_Account fields it will attempt to use the Phase cost center; if it is blank then it will use the Job cost center.

- For a direct Equipment cost GL_Account it will attempt to use the Equipment cost category's cost center; if it is blank then it will use the Equipment cost center.

- For a direct Work Order cost GL_Account it will attempt to use the Work Order's cost center.

- Once the Expense_Cost_Center is determined for direct cost records, it is then validated against the Distribution G/L code's cost centers.

- This Web Service will work with the defined Workflow process in Spectrum.

- The transaction data being submitted using this web service are stored within the General Ledger Journal Entry screen; the data must manually be updated within Spectrum.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
B
Company_CodeCompany CodeYESText3Valid Company in Spectrum
C
Transaction_DateTransaction DateYESDate10Enter as: MM/DD/CCYY (for example, 01/05/2010). First record is used for the header and all records will match.Must be within current G/L Processing Date.
D
Journal_DescJournal Entry DescriptionYESText30First record is used for the header and all records will match.
E
Journal_RemarksJournal remarksYESText100First record is used for the header and all records will match.
F
GL_AccountGeneral Ledger CodeText12** See Assumptions and Dependencies. No dashes.G/L Master File
G
Line_ReferenceLine Item ReferenceText15
H
Job_NumberJob NumberText10Job Master File
I
Phase_CodePhase CodeText20No dashes.Phase Master File
J
Cost_TypeCost TypeText3Phase Master File
K
Equipment_CodeEquipment CodeText10Equipment Master File
L
Equipment_Cost_CategoryEquipment Cost CategoryText4** See Assumptions and Dependencies.Equipment Cost Categories
M
Equipment_Work_OrderEquipment Work OrderText10Equipment Work Order is required, optional or none based on Equipment Cost Category data entry rule.Equipment Item must exist on the Equipment Work Order for required or optional settings.
N
GL_Debit_AmountDebit AmountNumeric14Positive values only.
O
GL_Credit_AmountCredit AmountNumeric14Positive values only.
P
WO_NumberWork Order #Text10Valid Work Order with a not complete status (for example, not a status of C)
Q
WO_EquipmentWO Site EquipmentText8Work Order Site Master File/Equipment Tab
R
WO_ComponentWO ComponentText2Work Order Site Master File/Equipment Tab /Component Tab (old systems)
S
WO_ContractWO Service ContractText10Work Order Site Master File/Service Contract Tab
T
WO_SellpriceWO Sell PriceNumeric14
U
Cost_CenterJournal Entry Cost CenterText10Required for First Record to define the Header Information.Cost Center Maintenance; G/L Account Cost Center; Job Cost Center; Phase Cost Center; Equipment Cost Center; Equipment Type Cost Center and Work Order Cost Center
