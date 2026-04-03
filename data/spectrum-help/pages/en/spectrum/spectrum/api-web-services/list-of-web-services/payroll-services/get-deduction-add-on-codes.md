---
title: "Get Deduction Add-on Codes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/get-deduction-add-on-codes"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/get-deduction-add-on-codes"
---

# Get Deduction Add-on Codes

Use this service to import deduction and add-on codes into the Payroll module.

## Connection Information

WSDL: GetDedAddon.jws
Method: GetDedAddon
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Authorization ID controls the security and defaults the pCompany_Code field if left blank.

- All parameter fields have SuperSelect logic except the following-

- pDeduct_Type

- pCost_Center

- pSort_By

## Parameter Fields

Element NameDescriptionReqTypeMaxField Information
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation
 Screen.
GUID
Unique reference number created by programming
Text36** See GUID definition
pCompany_Code
Company CodeText3Valid Company in Spectrum. Defaults from the
 Authorization ID if not populated.

pVol_Deduct_CodeDeduction/Add-on CodeText10Deduction/Add-on Code
 Maintenance
pDeduct_Type
TypeText1Define one specific type or leave blank to see all.

pCost_Center
Cost CenterText10Define one specific Cost Center, or leave blank to see all
 based on Authorization ID.

pSort_By
Sort By OptionsText1Blank = Deduction/Add-on Code or T= Deduction Type then
 Deduction/Add-on Code

## Return Fields

Element NameDescriptionTypeMaxField Information
Company_CodeCompany CodeText3Valid Spectrum Company
Vol_Deduct_CodeDeduction/Add-on CodeText10Deduction/Add-on Code Maintenance
Vol_Deduct_DescriptionDescriptionText15
Deduct_TypeTypeText1(A)dd-on or (D)eduction
Calc_Method
Calculation MethodText1(F)ixed Amount; (G) Percent of Gross
 Amount; (N) Percent of Net Amount; (S) Percent of Straight
 Time Equivalent; (R ) Regular Equivalent Hours; (O)vertime
 Equivalent Hours; (A)ll Hours; (U)ser Defined Formula;
 (P)ercent of Related Code; (C ) Prevailing Wage Adjustment
 or (H) Employer Health & Welfare Benefits only.

Error_CodeError CodeText1Used for Error information if needed
Error_Description Error DescriptionText250Used for Error information if needed
Error_Column Error ColumnText100Used for Error information if needed
