---
title: "Get Wage Code | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/get-wage-code"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/get-wage-code"
---

# Get Wage Code

Use this service to import Wage Code
 information.
 WSDL: GetWageCode.jws Method:
 GetWageCode
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Authorization ID controls the security and defaults the pCompany_Code field if left blank.

- All parameter fields have SuperSelect logic except the following-

- pSort_By

- Wage Codes can be defined globally for Unions, be Job specific or be Phase/Cost type specific within Spectrum.

- To see global Wage Codes leave the pJob_Number parameter blank.

- To see Job specific Wage Codes define pJob_Number parameter with ALL.

- To see Phase/Cost type specific Wage Codes leave the pJob_Number parameter blank and define the specific pPhase_Code and/or pCost_Type parameters.

## Parameter Fields

Use the table below for reference when using this service.Element NameDescriptionReqTypeMaxField Information
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen.
GUIDUnique reference number created by programmingText36** See GUID definition
pCompany_CodeCompany CodeYESText3Valid Company in Spectrum. Defaults from the Authorization ID if not populated.
pWage_CodeWage CodeText10Wage Code File Maintenance
pUnion_CodeUnion CodeText10Union Code File Maintenance
pJob_NumberJob NumberText10Job File Maintenance
pPhase_CodePhase CodeText20Phase File Maintenance
pCost_TypeCost TypeText3Cost Type File Maintenance
pSort_BySort By OptionsText1Blank = Wage Code, J= Job number or U= Union Code

## Return Fields

Use the table below for reference when using this service.Element NameDescriptionTypeMaxField Information
Company_CodeCompany CodeText3Valid Spectrum Company
Job_NumberJob NumberText10Job File Maintenance
Wage_CodeWage CodeText10
Union_CodeUnion CodeText10
Short_DescriptionShort DescriptionText10
Full_DescriptionFull Wage DescriptionText30
Worker_Comp_CodeWorker's Compensation CodeText6
Effective_DateEffective DateDate8
Error_CodeError CodeText1Used for Error information if needed
Error_DescriptionError DescriptionText250Used for Error information if needed
Error_ColumnError ColumnText100Used for Error information if needed
