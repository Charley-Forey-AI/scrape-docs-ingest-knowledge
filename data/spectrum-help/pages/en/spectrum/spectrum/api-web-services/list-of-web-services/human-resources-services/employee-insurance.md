---
title: "Employee Insurance | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/human-resources-services/employee-insurance"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/human-resources-services/employee-insurance"
---

# Employee Insurance

Use this service to import Human Resources-Employee
 Insurance information.
 Web Service WSDL:
 HREmpInsurance.jws
Web Service Method name:
 HREmpInsurance[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Human Resources-Employee Insurance information, the following file maintenance areas must be completed:

- System Administration > Installation > Human Resources

- System
 AdministrationInstallationHuman
 ResourcesInsurance Codes

- System
 AdministrationInstallationHuman
 ResourcesInsurance Type

- System
 AdministrationInstallationPayrollEmployees

- System
 AdministrationInstallationEnterprise
 ManagementCost Center Maintenance

## Assumptions and Dependencies

- The Human Resources module must be setup.

- The Employees must exist in the defined Company code.

- The following field names must be defined to add or update an existing record-

- Employee_Code

- Employee_Dependent_Type

- Employee_Dependent_Name

- Employee_Dependent_Sex

- Insurance_Code

- Wipe_Expiration_Date field logic

- If adding a new record, then this field will be ignored if defined.

- If record exists and the Insurance_Expiration_Date is define along with this field it will cause an error for the user to change.

- If record exists and the Insurance_Expiration_Date is blank and this field is defined then it will remove the expiration date.

- The Notes will append to the existing notes.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

## Field Descriptions

Use the table below for reference when using this service.Excel
Element NameDescriptionReqTypeMaxFormatValidation
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
Define [SELF] (to match standard Spectrum) in field if
 information is for the Employee otherwise define a valid Employee
 Dependent name.
Valid HR Employee Depedent Name in Spectrum.

F
Employee_Dependent_Sex
Gender
Text
1
(M)ale or (F)emale

G
Insurance_Code
Insurance Code
Text
12
Valid Insurance Code in Spectrum.

H
Insurance_Status
Status Code
Text
1
(C)ancelled, (O)Cobra, (X)Cobra Expired, (D)eclined,
 (E)nrolled, (N)/A, (P)ending

I
Policy_Number
Policy number
Text
30
Only used for Insurance_Status of C, O, X, E, or N.
 Not required.

J
Insurance_Effective_Date
 Effective date of policy
Date
10
Enter as MM/DD/CCYY (for example, 01/05/1982)
 Only used for Insurance_Status of C, O, X, E, or N.
 Not required.

K
Insurance_Expiration_Date
Expiration date of policy
Date
10
Enter as MM/DD/CCYY (for example, 01/05/1982)
 Only used for Insurance_Status of C, O, X, E, or N.
 Not required. **See Assumptions and Dependencies.

L
Wipe_Expiration_Date
Clear the expiration date (changing record only?)
Text
 1
 (Y)es, Blank = No
If (Y)es, the Insurance_Expiration_Date field will be
 cleared. Ignored if Insurance_Expiration_Date is provided. **See
 Assumptions and Dependencies.

M
Insurance_Cobra_Amt
Cobra amount
Numeric
11
Format = --7.2
Only used for Insurance_Status of O or X. Not
 required.

N
Insurance_Memo
Notes
 Text
250
Notes will be appended to any existing notes.
