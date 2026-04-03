---
title: "Equipment Revenue Transactions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/equipment-revenue-transactions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/equipment-revenue-transactions"
---

# Equipment Revenue Transactions

Use this service to import Equipment Revenue Transaction
 information.
 WSDL: AddEquip_Revenue.jws Method:
 AddEquip_Revenue
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Equipment Revenue Transaction information, the following file maintenance screens must be completed:

- System Administration > Installation > Equipment Control

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > General Ledger > G/L Department File Maintenance

- System Administration > Installation > Equipment Control > Equipment File Maintenance

- System Administration > Installation > Equipment Control > Cost Category File Maintenance

- System Administration > Installation > Equipment Control > Equipment Status File Maintenance

- System Administration > Installation > Equipment Control > Equipment Type File Maintenance

- System Administration > Installation > Equipment Control > Fuel / Oil File Maintenance

- System Administration > Installation > Equipment Control > Equipment Location File Maintenance

- System Administration > Installation > Equipment Control > Yard File Maintenance

- System Administration > Installation > Equipment Control > Job/Equipment Rates File Maintenance

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phases

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation > Time + Material > Job Equipment Billing Rates

- System Administration > Installation > Time + Material > Equipment Billing Rates

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The import file has a recommended record limitation of 9000 records per batch.

- The Rate_Type_Code field

- If defined as Job then the Job information is required and the GL_Debit_Account will be a direct cost account.

- If defined as Rental then the Job information will be ignored if defined and the GL_Debit_Account will be a non-direct cost account.

- The Job_number field

- If defined then the Phase_Code and Cost_Type are both validated and mandatory.

- If not defined then the 'Rental Debit Cost Center' is both validated and mandatory.

- Two of the following fields must be defined in order to create a record:

- Transaction_Hours

- Transaction_Rate

- Can be blank as long as the Time+Material rate hierarchy logic exists for the Time+Material Job.

- Transaction_Amount

- If the Transaction_Amount is defined and the calculation of the Transaction_Hour and Transaction_Rate fields don't match, then the Transaction_Rate value will be recalculated.

- If no hours exist then the rate will store what is defined in the record.

- The amount defined for the Transaction_Amount field will overrule all other values.

- For rental-related transactions, neither of the GL_Debit_Account or GL_Credit_Account can be direct, equipment or a work order cost code.

- The GL_Debit_Account

- Subject to the Job Cost Installation flag to "validate job division with G/L department". If this is set to yes, then the G/L code must match the job division code.

- The Debit code must be a direct cost code for job-related transactions, and a non-direct cost account for rental transactions.

- The GL_Credit_Account

- Subject to the Equipment Control Installation flag to "validate equipment division with G/L department". If this is set to yes, then the G/L code must match the equipment division code.

- The Credit code must be a non-direct cost account for both job and rental type transactions.

- Defaults from the Equipment Control Installation GL Codes tabs if field is not populated.

- The Billing_Rate field

- Available if the Time + Material module is installed.

- Used on Job's with a price type of Cost Plus or Time + Material only.

- Hierarchy logic for the field (requires Time + Material module installed). Rates defined are based on the TM billing details defined.

- Use the defined value in the file.

- Use the default value from Time + Material Equipment Billing Rate by Job.

- Use the default value from Equipment Billing Rate in Time + Material module.

- Follows standard Master Job and Sub-Job hierarchy.

- Stand-by billing rates assigned to the equipment and any attachments will
 default from the stand-by rates defined on the Time + Material > Job Equipment Billing Rate Maintenance screen, based on Hourly, Daily, Weekly or Monthly rates. If there
 is no rate defined there, Spectrum will look to the Equipment Billing Rate
 Maintenance table for the stand-by billing rate. If no rate is defined there,
 the billing rate is zero.

- The Inter_Company_Code field is allowed if the Equipment Control Installation 'Multi Company?' is selected. If selected then the Job information must match this company code.

- Cost center information will only be allowed in if the Company is set to a Yes status.

- The transaction data being submitted using this web service are stored within the Equipment Revenue Transaction Entry screen; the data must manually be updated within Spectrum.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
B
Company_CodeCompany CodeText3Valid Company in Spectrum. Defaults from the Authorization ID if not populated.
C
Transaction_DateTransaction DateDate10Format MM/DD/CCYYWithin Fiscal Year Calendar and Equipment Cost Processing Date Range
D
Batch_IDBatchText10Recommend using a unique batch code to keep them separate while validating and updating Equipment Cost Transactions.Recommend limiting the 'Batch Code/Tran Date' quantity of Record to 9000. Defaults from the Authorization ID's defined Operator Code if not populated.
E
Equipment_CodeEquipmentYESText10Equipment file maintenance
F
Source_CodeSourceYESText2(EU) Equipment Usage or (ES) Equipment Standby only
G
Rate_Type_CodeActivityYESText1(J)ob or (R )ental onlyIf (J)ob defined then Job fields are required. If (R)ental then the Job fields are ignored if populated.
H
Rate_FlagRate TypeYESText1(H)ourly, (D)aily, (W)eekly, or (M)onthly only
I
Tran_TypeTransaction TypeText1(F)ull or (O)perating onlyUsed for EU-Equipment Usage Transactions only.
J
Transaction_HoursHoursNumeric10Format = -6.2 Allows negatives. **See Assumptions and Dependencies.
K
Transaction_RateRateÂNumeric6Format = -2.2 Allows negative. Default using standard Spectrum Hierarchy if blank. **See Assumptions and Dependencies.
L
Transaction_AmountExtensionNumeric11Format = -7.2 Required if Transaction_Hours and/or Transaction Rate are blank. Allows negative. If Extension is different from the calculated value for hours and rate then use Extension and calculate the rate. **See Assumptions and Dependencies.
M
GL_Debit_AccountDebit G/L CodeYESNumeric12No dashes.G/L Master File - Subject to the Job Cost Installation options defined. **See Assumptions and Dependencies.
N
GL_Credit_AccountCredit G/L CodeNumeric12No dashes. Defaults from Equipment Control Installation if not populated.G/L Master File - Subject to the Equipment Control Installation options defined. **See Assumptions and Dependencies.
O
Job_NumberJobText10Must be valid for the defined Alt_Company_Code.Job File Maintenance
P
Phase_CodePhaseText20No dashes.Job/Phase File Maintenance
Q
Cost_TypeCost TypeText3Cost Type Maintenance
R
RemarksRemarksText30
S
Billing_RateBilling RateNumeric11Allows negative. Format = -6.3*See Assumptions for hierarchy. Time & Material module and Job specific billing rates. Job Cost type specific.
T
Debit_Cost_CenterRental Debit Cost CenterText10Cost Center Maintenance; Equipment Cost Center; Job Cost Center; Phase Cost Center; G/L Account Cost Center
U
Inter_Company_CodeJob Company CodeText3Valid Company in Spectrum. **See Assumptions and Dependencies.
