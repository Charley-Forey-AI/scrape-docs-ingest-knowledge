---
title: "Add Employee Entity | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/add-employee-entity"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/add-employee-entity"
---

# Add Employee Entity

Use the following service to import Employee Entity information.
WSDL: UpdateEmpEntity.jws
Method: UpdateEmpEntity
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Employee Entity information, the following file maintenance areas must be completed:

- System Administration > Installation > Payroll

- System Administration > Installation > Enterprise Management > Entities

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

- System Administration > Installation > Payroll > Employee Maintenance

## Assumptions and Dependencies

- The Payroll Module must be set up.

- The Employee code must exist in the defined Company code.

- The Employee-Entity Web service adds or updates an existing employee's entity information for the defined fields only.

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
Main_Comp_Status
Main Company: Authorized for payment from this
 entity?
Text
1
(A)uthorized or (I)nactive. Defaults to (A)uthorized
 if blank.

E
Main_Comp_OverrideCC
Main Company Override Cost Center
Text
10
Cost Center Maintenance

F
Entity_Code
Entity
Text
10
Define the specific Entity for the Employee.
Valid Entity in Spectrum

G
Status
Entity Specific: Authorized for payment from this
 entity?
Text
1
Must have a defined Entity_Code if defined.
 (A)uthorized or (I)nactive. Defaults to (A)uthorized if blank.

H
Override_CC
Entity Specific Deductions/Add-ons Override Cost
 Center
Text
10
Must have a defined Entity_Code.
Cost Center Maintenance
