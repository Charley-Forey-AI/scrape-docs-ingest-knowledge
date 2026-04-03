---
title: "Get Employee | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/get-employee"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/get-employee"
---

# Get Employee

Use this service to create a GET service for Employee fields.
WSDL: GetEmployee.jws
Method: GetEmployee
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Authorization ID controls the security and defaults the pCompany_Code field if left blank.

- All parameter fields have SuperSelect logic except the following-

- pStatus_Type

- pCost_Center

- pSort_By

## Parameter Fields

Use the table below for reference when setting up parameter fields for this service.
Element Name
Description
Req
Type
Max
Field Information

Authorization_ID
Authorization ID to access the server
YES
Text
20
Data Exchange Installation Screen.

GUID
Unique reference number created by programming
Text
36
** See GUID definition

pCompany_Code
Company Code
YES
Text
3
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

pWage_Class
Wage Code
Text
10

pUnion_Code
Union Code
Text
10

pOccupation
Occupation
Text
50

pTrade
Trade
Text
50

pStatus_Type
Status
Text
1
Define one specific Status or leave blank to see Active and Inactive only

pCost_Center
Employee Cost Center
Text
10
Define one specific Cost Center or leave blank to see all based on Authorization ID

pSort_By
Sort By Options
Text
1
Blank = Employee Code, A= Alphabetical by Employee_Name, F= First Name, L= Last name or D= Department code

## Return Fields

Use the table below for reference when setting up return fields for this service.
Element Name
Description
Type
Max
Field Information

Company_Code
Company Code
Text
3
Valid Spectrum Company

Employee_Code
Employee Code
Text
11
Employee File Maintenance

Employee_Name
Employee Name
Text
30

Supervisor_Code
Supervisor Code
Text
2

Employment_Status
Employee Status
Text
1

Department_Code
Department Code
Text
6

Union_Code
Union Code
Text
10

Wage_Class
Wage Code
Text
10

Worker_Comp_Code
Worker's Comp Code
Text
6

First_Name
Employee First Name
Text
20

Middle_Name
Employee Middle Name
Text
20

Last_Name
Employee Last Name
Text
20

Occupation
Occupation
Text
50

Trade
Trade
Text
50

Title
Employee Title
Text
50

Employee_Mobile_Phone
Work Mobile Phone
Text
14

Employee_Extension
Work Extension
Text
15

Cost_Center
Employee Cost Center
Text
10

Error_Code
Error Code
Text
1
Used for Error information if needed

Error_Description
Error Description
Text
250
Used for Error information if needed

Error_Column
Error Column
Text
100
Used for Error information if needed
