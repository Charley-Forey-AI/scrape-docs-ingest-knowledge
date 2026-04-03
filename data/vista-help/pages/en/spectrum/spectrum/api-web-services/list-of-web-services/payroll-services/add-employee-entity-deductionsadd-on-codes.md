---
title: "Add Employee Entity Deductions/Add-on Codes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/add-employee-entity-deductionsadd-on-codes"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/add-employee-entity-deductionsadd-on-codes"
---

# Add Employee Entity Deductions/Add-on Codes

Use this service to import Employee Entity Deduction/Add-on codes.
WSDL: UpdateEmpEntityDedAddon.jws
Method: UpdateEmpEntityDedAddon
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Employee Entity Ded/Add-on information, the following file maintenance areas must be completed:

- System Administration > Installation > Payroll

- System Administration > Installation > Enterprise Management > Entities

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

- System Administration > Installation > Payroll > Employee Maintenance

- System Administration > Installation > Payroll > Deduction/Add-on Code Maintenance

- System Administration > Installation > Payroll > Formula File Maintenance

- System Administration > Installation > Accounts Payable > Vendors

- System Administration > Installation > Human Resource > Recurring Benefits Code Maintenance

## Assumptions and Dependencies

- The Payroll Module must be set up.

- The Employee code must exist in the defined Company code.

- The Employee-Entities Web service adds or updates an existing employee's entity information for the defined fields only.

- The Vol_Deduct_Code fields require that the Entity_Code field be populated.

- If the Vol_Deduct_Code does not exist on the Employee's Entity then it will be added. If it does exist on the Employee's Entity then the details of the code will be updated.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- If Human Resources module is active then it will update the Employee's Entity Benefits Master.

- Deduction/Add-on codes have specific rules regarding the status code option allowed and will follow the standard Spectrum rules.

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
Entity

E
Override_CC
Entity Specific Deductions/Add-ons Override Cost
 Center
Text
10
Must have a defined Entity_Code.
Cost Center Maintenance

F
Vol_Deduct_Code
Code
Text
10
Must have a defined Entity_Code if defined. If code is
 blank and detail lines are populated they will be ignored.
Deduction/Add- on Maintenace Table

G
Vol_Deduct_Status
Status
Text
1
(R)ecurring, (O)ne Time, (I)nactive or (S)kip one
Required if Vol_Deduct_Code is being added to the
 defined Employee_Code

H
Formula_Code
Formula
Text
5
Dependent on Status & Code defined. If blank
 defaults from defined code.
Formula code

I
Vol_Deduct_Amount
Amount
Numeric
9
Dependent on Status & Code defined. Format =
 -5.2

J
Vol_Deduct_Percent
Percent
Numeric
7
Dependent on Status & Code defined. Positive
 numbers only. Format = 2.3

K
Vol_Deduct_Limit
Annual Limit
Numeric
8
Dependent on Status & Code defined. Positive
 numbers only. Format = 5.2

L
Monthly_Limit
Monthly Limit
Numeric
8
Dependent on Status & Code defined. Positive
 numbers only. Format = 5.2

M
Cycle_Amount_Limit
Cycle Limit
Numeric
8
Positive numbers only. Format = 5.2

N
Cycle_Percent_Limit
Cycle Limit %
Numeric
6
Positive numbers only. Format = 2.3

O
Formula_Value_1
Variable 1
Numeric
9
Format = -4.3
Defaults to zero- Tied to Formula_Code field.

P
Formula_Value_2
Variable 2
Numeric
9
Format = -4.3
Defaults to zero- Tied to Formula_Code field.

Q
Formula_Value_3
Variable 3
Numeric
9
Format = -4.3
Defaults to zero- Tied to Formula_Code field.

R
Vendor_Code
Vendor
Text
10
Required if Vol_Deduct_Code requires it
Vendor Code

S
AP_Remark
AP Invoice Remarks
Text
30
