---
title: "Add Equipment Cost | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/add-equipment-cost"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/add-equipment-cost"
---

# Add Equipment Cost

Use this service to import Equipment Cost Transaction
 information.
 WSDL: AddEquip_Cost.jws Method:
 AddEquip_Cost
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File
 Maintenance

Prior to importing Equipment Cost Transaction information, the
 following file maintenance screens must be completed:

- System Administration > Installation > Equipment Control

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Equipment Control > Equipment File Maintenance

- System Administration > Installation > Equipment Control > Cost Category File Maintenance

- System Administration > Installation > Equipment Control > Equipment Status File Maintenance

- System Administration > Installation > Equipment Control > Equipment Type File Maintenance

- System Administration > Installation > Equipment Control > Fuel / Oil File Maintenance

- System Administration > Installation > Equipment Control > Equipment Location File Maintenance

- System Administration > Installation > Equipment Control > Yard File Maintenance

- System Administration > Installation > Equipment Control > Job/Equipment Rates File Maintenance

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The import file has a recommended record limitation of 9000
 records per batch.

- All transactions will be assigned a source code of "EC".

- Transaction_Amount field hierarchy

- If the Fuel_Oil_Code is defined then the
 Transaction_Quantity will be required and the Transaction_Amount will be
 calculated.

- If the Fuel_Oil_Code is not defined then the
 Transaction_Amount field is required and the value defined will be used.

- If the Transaction_Quantity, Fuel_Oil_Code and
 Transaction_Amount are defined and valid then the Transaction_Amount will be
 used for the import and the calculation logic for the Fuel_Oil_Code logic
 will be ignored.

- The Fuel_Oil_Code is available based on the defined
 Cost_Category_Code. The standard Cost_Category_Code heirarchy applies and if a
 Fuel_Oil_Code is defined that does not tie to the Cost Category Code defined then
 it will be an error.

- The Debit G/L Code must use a Direct Cost Equipment Cost
 Account for these transactions.

- The GL Account must be a Direct Cost Equipment Cost
 Account for these transactions.

- The Equipment Cost Category Code contains General Ledger
 Overrides. If defined it will validate to the GL Overrides and the Cost
 Category Code.

- The Credit G/L Code must us a Non-direct Cost Account for these
 transactions.

- Cost center information will only be allowed in if the Company
 is set to a Yes status.

- The transaction data being submitted using this web service are
 stored within the Equipment Cost Transaction Entry screen; the data must manually
 be updated within Spectrum.

## Field Descriptions

Use
 the table below for reference when using this service. The Authorization_ID and GUID
 elements are not shown on the Spectrum Excel Office Add-in templates for data entry
 points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the
 serverYESText20Data Exchange Installation
 Screen
GUIDUnique reference number created by
 programmingText36** See GUID definition
B
Company_CodeCompany CodeYESText3Valid Company in Spectrum
C
Transaction_DateTransaction DateYESDate10Format MM/DD/CCYYWithin Fiscal Year Calendar and
 Equipment Cost Processing Date Range
D
Batch_IDBatchYESText10Recommend using a unique batch code
 to keep them separate while validating and updating Equipment Cost
 Transactions.Recommend limiting the 'Batch
 Code/Tran Date' quantity of Record to 9000.
E
Equipment_CodeEquipmentYESText10Equipment File Maintenance
F
Cost_Category_CodeCost CategoryYESText4** See Assumptions and
 DependenciesEquipment Cost Category File
G
Transaction_QuantityQuantityNumeric10Allows negative. Decimals ok.
 Required if Fuel_Oil_Code defined.
H
Fuel_Oil_CodeFuel/OilText2Cost_Category_Code controls the
 logic for this field. Codes tied to Fuel or Oil will use the associated rate
 for the Transaction amount calculation.Fuel/Oil File Maintenance
I
Transaction_AmountAmountNumeric11Allows negative. Zero value
 not allowed. Decimals OK.Defined amount overrides
 hierarchy. ** See Assumptions and Dependencies for field
 logic.
J
GL_Debit_AccountDebit G/L CodeYESText12No dashes. ** See Assumptions and
 DependenciesG/L Master File - use a Direct Cost
 = Equipment
K
GL_Credit_AccountCredit G/L CodeYESText12No dashes.G/L Master File - use a Non-direct
 Cost Account
L
Equipment_WO_NumberEquipment Work OrderText10Equipment Work Order is either
 required or optional based on Equipment Cost Category data entry
 rule.Equipment Item must exist on the
 Equipment Work Order and not have a closed status.
M
RemarksRemarksText30
N
Credit_Cost_CenterCredit Cost CenterText10Cost Center Maintenance; Equipment
 Cost Center; Cost Category Cost Center and G/L Account Cost Center
