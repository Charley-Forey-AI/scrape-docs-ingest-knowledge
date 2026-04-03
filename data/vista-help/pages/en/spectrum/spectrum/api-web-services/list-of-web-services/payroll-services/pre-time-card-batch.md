---
title: "Pre-Time Card Batch | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/pre-time-card-batch"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/pre-time-card-batch"
---

# Pre-Time Card Batch

Use this service to import Pre-Time Card Batch information.
Connection Information
URL: https://<SPECTRUM-SERVER>:8482/timecard/timecards
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`[
 {
 "companyCode": "MD2",
 "serviceUniqueID": "7385673F-5CEE-40E5-9447-7A0AA61A64A3",
 "systemKey": "20170407KSM000000d009964",
 "employeeCode": "",
 "checkSequenceNumber": "",
 "checkType": "",
 "checkNumber": "",
 "payType": "Q",
 "dayOfWeek": "",
 "unionCode": "",
 "certifiedFlag": "",
 "hours": 0,
 "payRateCode": 0,
 "payRate": 0,
 "payExtension": 0,
 "departmentCode": "",
 "jobNumber": " AR0448U",
 "phaseCode": "000001",
 "costType": "L",
 "burdenAmount": 0,
 "workerCompCode": "",
 "updateFlag": "",
 "equipmentCode": "",
 "costCategoryCode": "",
 "equipmentHours": 0,
 "equipmentRate": 0,
 "wageCode": "",
 "batchCode": "MLD0421Q",
 "billRate": 0,
 "equipmentBillRate": 0,
 "laborBillCode": "",
 "equipmentBillCode": "",
 "interCompanyCode": "",
 "dayOfMonth": "04/21/2026",
 "tmUpdateFlag": "",
 "state": "",
 "workCounty": "",
 "workLocality": "",
 "message": "",
 "unionFringe": 0,
 "workerCompBurden": 0,
 "workerCompDeduct": 0,
 "pmWorkOrder": "",
 "equipmentRateType": "",
 "certifiedJobNumber": "",
 "statusFlag": "",
 "quantityFlag": "",
 "compRate": 0,
 "companyCode3": "",
 "prevailingWageRate": 0,
 "crewNumber": "",
 "costCenter": "102",
 "additionalJTDQuantity": 4.00,
 "userID": "",
 "woNumber": "",
 "woEquipment": "",
 "woComponent": "",
 "scContract": "",
 "incentivePayFlag": ""
 }
]`
```

## Underlying File Maintenance

Prior to importing Pre-Time Card Transaction information, the following file maintenance screens must be completed. To access any one of these, begin with System Administration > Installation:
Payroll

- Tax Table Maintenance

- Deduction/Add-on Code Maintenance

- Department Expense Maintenance

- Worker's Comp Base Code

- Worker's Compensation Code Maintenance

- Non-Union Pay Group Maintenance

- Union File Maintenance

- Wage Code File Maintenance

- Crew Maintenance

- Employee Status Code Maintenance

- Employees Maintenance

General Ledger

- G/L Department File Maintenance

- G/L Master File Maintenance

Human Resources

- Triggers Maintenance

Job Cost

- Jobs Maintenance

- Cost Type Maintenance

- Phases Maintenance

Equipment Control

- Equipment Status File Maintenance

- Equipment Maintenance

- Equipment Components File Maintenance

- Cost Category Maintenance

- Job Specific Equipment Charge Rates

Preventive Maintenance

- Equipment Work Order Entry

Work Order

- Site File Maintenance

- G/L Department File Maintenance

- Work Order Type File Maintenance

- Labor Category File Maintenance

- Labor Billing Rates Maintenance

- Work Order Standard Phase

- Work Order Entry

Service Contract

- Contract Type File Maintenance

- Service Contract File Maintenance

Time & Material

- Job Billing Maintenance

- Labor Billing Rates

- Job Labor Billing Rates Maintenance

- Equipment Billing Rates

- Job Equipment Billing Rates Maintenance

Enterprise

- Cost Center Maintenance

## Assumptions & Dependencies

General Guidelines

- The transaction data being submitted using this web service are stored within the Payroll Pre-Time Card Import Errors screen by Employee or by Quantity and requires the data to be manually rechecked within Spectrum using the Recheck button on the screen.

- To maintain Spectrum's flexibility, the Data Exchange logic will validate the web service authorization, required fields, numeric, date, and generic validations only.

- The Payroll and General Ledger Modules must be setup.

- The flexibility within the Pre-Time Card web service creates new employee and quantity records. The SDX manual defines the specific guidelines for each type of record.

- Validation will be performed on the CompanyCode, WorkDate, and PayType.

- Cost center information will only be allowed if the Company is set to a Yes status.

Employee Record Guidelines

- Any PayType other than Q(uantity) will be sent to the Pre-Time Card Import Errors screen located within the Pre-Time Card Import logic.

- Non-direct departments should not have any Job, Equipment, or Work Order details defined.

- All standard Spectrum Pay Types and Add-on / Deduction codes are supported and validated to the CompanyCode. See the Pay Types options defined in layout.

Quantity Record Guidelines

- The Quantity pay type 'Q' is used to designate that a quantity record is to be created and submitted to the Pre-time Card Quantity Import Errors screen within the Pre-Time Card Import logic.

## Field Descriptions

Use the table below for reference when using this service.
Field NameDescriptionREQ?TypeMaxField InformationValidation
companyCodeCompany CodeText3Company where the records will be created.Valid Company in Spectrum. Defaults from the Authorization ID if not populated.
batchCodeBatch CodeYESText8New or existing batch code
employeeCodeEmployeeText11Must exist in company per the CompanyCode entry. Not required for quantity records.
checkSequenceNumberCheck Sequence NumberNumeric1Not required; must be an integer from 1 to 9
departmentCodeDepartmentText6Not required for quantity records.
payTypePay TypeYESText10(R)egular; (O)vertime; (D)ouble time; (H)oliday; (V)acation; (S)ick; (M)iscellaneous; (SA)-Special amount; (ER)- Equipment- Regular; (EO)- Equipment- Overtime; (ED)- Equipment-Double time; (EU)- Equipment usage; (RP)-Retro-pay; (JX)-Job only adjustment hours; (1,2 or 3)- Description set in Payroll Installation screen; (Q)uantity entries only; (I)ncentive pay or (U)npaid time and Add-on or Deduction codes.Validates to the defined CompanyCode field name. All pay types supported including Incentive pay types when specified on the Payroll Installation screen (for example, IR, IO, ID when "I" is specified), Add-on and Deduction codes.
hoursEmployee HoursNumeric8Enter decimals but no $ signs or commas. Can be positive or negative; Not required for quantity records.
jobNumberJobText10Required for Quantity records.
phaseCodePhaseText20No dashes. Required for Quantity records.
costTypeCost typeText1Required for Quantity records.
dayOfMonthDateYESText10Enter as: MM/DD/CCYY (such as 01/05/2010).Within P/R processing date range
messageMessageText30
payRateCodeRate levelText11 thru 9 only
wageCodeWage codeText10
unionCodeUnion code OR Pay groupText10
workerCompCodeWork CompText6
stateWork stateText10
workCountyWork countyText10
workLocalityWork localText10
equipmentCodeEquipmentText10
equipmentHoursEquipment HoursNumeric8Enter decimals but no $ signs or commas. Can be positive or negative
additionalJTDQuantityAdd'l JTD QtyNumeric14Enter decimals but no $ signs or commas. Can be positive or negative
interCompanyCodeCompany Code 2Text3For use with inter-company payroll.
companyCode3Company Code 3Text3For use with inter-company payroll.
payRatePay RateNumeric12Enter decimals but no $ signs or commas. Can be positive or negative
costCategoryCodeCost CategoryText4
crewNumberCrewText10
woNumberWork OrderText10
woEquipmentWO Site EquipmentText8
woComponentWO ComponentText2
scContractWO ContractText10
pmWorkOrderEquipment Work OrderText10
costCenterCost CenterText10Cost Center Maintenance; G/L Account Cost Center; Job Cost Center; Phase Cost Center; Equipment Cost Center; Equipment Type Cost Center and Work Order Cost Center
