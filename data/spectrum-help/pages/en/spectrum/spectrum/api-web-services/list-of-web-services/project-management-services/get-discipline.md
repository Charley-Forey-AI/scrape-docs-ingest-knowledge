---
title: "Get Discipline | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/project-management-services/get-discipline"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/project-management-services/get-discipline"
---

# Get Discipline

Use this service to import Project Log Discipline information.

## Connection Information

WSDL: GetDiscipline.jws
Method: GetDiscipline
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Authorization ID controls the security and defaults the pCompany_Code field if left blank in the parameter fields.

- All parameter fields have SuperSelect logic except the pSort_By

## Parameter Fields

Element NameDescriptionReqTypeMaxField Information
 Authorization_ID Authorization ID to access the server YES Text20Data Exchange Installation Screen
GUID
Unique reference number created by
 programming
Text36** See GUID definition
pCompany_Code
Company CodeYESText3Valid Company in Spectrum. Defaults from
 the Authorization ID if not populated.

pLog_ClassDisciplineText50Project Log Discipline
pSort_BySort By OptionsText1Blank = Company Code or D= Log Class

## Return Fields

Element NameDescriptionTypeMaxField Information
Company_CodeCompany CodeText3Valid Spectrum Company
Log_ClassDisciplineText50Project Log Discipline
Error_CodeError CodeText1Used for Error information if needed
Error_Description Error DescriptionText250Used for Error information if needed
Error_ColumnError ColumnText100Used for Error information if needed
