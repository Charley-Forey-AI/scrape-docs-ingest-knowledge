---
title: "Employee Entity Time Bank | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/employee-entity-time-bank"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/employee-entity-time-bank"
---

# Employee Entity Time Bank

Use this service to import Employee Entity Time Bank information.
WSDL: UpdateEmpEntityTimeBank.jws
Method: UpdateEmpEntityTimeBank
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Employee Entity Time Bank information, the following file maintenance areas must be completed:

- System Administration > Installation > Payroll

- System Administration > Installation > Enterprise Management > Entities

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

- System Administration > Installation > Payroll > Employee Maintenance

- System Administration > Installation > Payroll > Hours Bank Code Maintenance

## Assumptions and Dependencies

- The Payroll Module must be set up.

- The Employee code must exist in the defined Company code.

- The Employee-Entity Time Off Bank Web service adds or updates an existing employee's entity time off bank information for the defined fields only.

- If the Time Off Bank codes do not exist then they will be added to the employee's entity.

- If the Time Off Bank codes do exist then the details for the code will be updated.

- The Time Off Bank codes are not required to populate the Year to Date or Balance fields. This is standard Spectrum entry logic. If a code is not defined then the default display on the main Entity screen will not be marked to indicate that data exists.

- The Balance and YTD hours will be summed for the 'Bank balance' total in the Employee Time Off Bank screen.

- If you want to deduct Balance hours from YTD hours, enter a negative Balance hours amount (that is, -32 (Vacation_Hours_Balance) + 40 (Vacation_Hours_YTD) = 8 (Bank balance)).

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the
 Spectrum Excel Office Add-in templates for data entry points.
Excel
Element Name
Description
Req
Type
Max
Format
Validation

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
Employee Code
YES
Text
11
Valid Employee and must exist for the defined Company
 Code.

D
Entity_Code
Entity
YES
Text
10
Define the specific Entity for the Employee.
Valid Entity

E
Vacation_Hours_Balance
Vacation Hours Balance
Numeric
7
Allows negative numbers. Format = -3.2

F
Vacation_Hours_YTD
Vacation Hours YTD
Numeric
7
Allows negative numbers. Format = -3.2

G
Vacation_Control_Code
Vacation Control Code
Text
2
Hours Bank Code Maintenance with a Type of
 Vacation

H
Holiday_Hours_Balance
Holiday Hours Balance
Numeric
7
Allows negative numbers. Format = -3.2

I
Holiday_Hours_YTD
Holiday Hours YTD
Numeric
7
Allows negative numbers. Format = -3.2

J
Holiday_Control_Code
Holiday Control Code
Text
2
Hours Bank Code Maintenance with a Type of Holiday

K
Sick_Hours_Balance
Sick Hours Balance
Numeric
7
Allows negative numbers. Format = -3.2

L
Sick_Hours_YTD
Sick Hours YTD
Numeric
7
Allows negative numbers. Format = -3.2

M
Sick_Control_Code
Sick Control Code
Text
2
Hours Bank Code Maintenance with a Type of Sick
