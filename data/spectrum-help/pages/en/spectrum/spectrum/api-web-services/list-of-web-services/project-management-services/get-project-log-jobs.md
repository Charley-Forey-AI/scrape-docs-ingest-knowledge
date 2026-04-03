---
title: "Get Project Log Jobs | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/project-management-services/get-project-log-jobs"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/project-management-services/get-project-log-jobs"
---

# Get Project Log Jobs

Use this service to import Project Log Jobs
 information.
 WSDL: GetPJJob.jws Method: GetPJJob
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Authorization ID controls the security and defaults the pCompany_Code field if left blank in the parameter fields.

- All parameter fields have SuperSelect logic except the pSort_By

## Parameter Fields

Use the table below for reference when using this service.Element NameDescriptionReqTypeMaxField Information
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen.
GUIDUnique reference number created by programmingText36** See GUID definition
pCompany_CodeCompany CodeYESText3Valid Company in Spectrum. Defaults from the Authorization ID if not populated.
pJob_Number Job NumberText10
pStatus_Codeif left blank then active and inactive onlyText1(A)ctive, (I)nactive or (C )omplete
pCost_Centerif blank then all for company and operator or enter one onlyText50Project Log Discipline
pSort_BySort By OptionsText1Blank = Company Code or D= Log Class

## Return Fields

Use the table below for reference when using this service.Element NameDescriptionTypeMaxField Information
Company_CodeCompany CodeText3Valid Spectrum Company
Job_NumberJob NumberText10
Job_DescriptionJob NameText25
Status_CodeStatusText1(A)ctive, (I)nactive or (C )omplete
CategoryProject Log CategoryText30
PJ_Reference_NumLast Project Log Reference Number per CategoryText10Display the Reference Number from the Project Log table per Category
Cost_CenterJob Cost CenterText10
Error_CodeError CodeText1Used for Error information if needed
Error_DescriptionError DescriptionText250Used for Error information if needed
Error_ColumnError ColumnText100Used for Error information if needed
