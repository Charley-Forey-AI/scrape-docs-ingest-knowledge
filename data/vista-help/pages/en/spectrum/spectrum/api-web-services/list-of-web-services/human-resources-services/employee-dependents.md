---
title: "Employee Dependents | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/human-resources-services/employee-dependents"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/human-resources-services/employee-dependents"
---

# Employee Dependents

Use this service to import Human Resources-Employee
 Dependents information.
Web Service WSDL: HREmployeeDependents.jws
Web Service Method name: HREmployeeDependents
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File
 Maintenance

Prior to importing Human Resources-Employee Dependents information,
 the following file maintenance areas must be completed:

- System Administration > Installation > Human Resources

- System Administration > Installation > Payroll > Employees

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The Human Resources module must be setup.

- The Employees must exist in the defined Company code.

- The following field names must be defined to add or update an existing record-

- Employee_Code

- Employee_Dependent_Type

- Employee_Dependent_Name

- Employee_Dependent_Sex

- The Notes will append to the existing notes.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

## Field Descriptions

Use
 the table below for reference when using this service.Excel
Element Name DescriptionReq TypeMax Format Validation
Authorization_ID
Authorization ID to access the server
YES
Text
20
Data Exchange Installation Screen

GUID
Unique reference number created by programming
 Text
36
 ** See GUID definition

B
Company_Code
Company Code
 Text
 3
Valid Company in Spectrum. Defaults from the
 Authorization ID if not populated.

C
Employee_Code
Employee
Text
 11
Valid Employee Code in Spectrum

D
Employee_Dependent_Type
Type of dependent
Text
1
(S)pouse(C)hild or (O)ther
Only one dependent with type (S)pouse is allowed per
 employee.

E
Employee_Dependent_Name
Name of dependent
Text
 20

F
Employee_Dependent_Sex
Gender
Text
1
(M)ale or (F)emale

G
Employee_Dependent_Birth
Date of Birth
Date
10
 Enter as MM/DD/CCYY (for example, 01/05/1982)

H
Employee_Dependent_SSN
Social Security #
Numeric
9
Do not include dashes
Duplicates allowed.

I
Employee_Dependent_Notes
Notes
Text
 250
Notes will be appended to any existing notes.
