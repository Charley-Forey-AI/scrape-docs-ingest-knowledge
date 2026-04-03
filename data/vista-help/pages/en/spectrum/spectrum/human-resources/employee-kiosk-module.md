---
title: "Employee Kiosk Module | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/human-resources/employee-kiosk-module"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/human-resources/employee-kiosk-module"
---

# Employee Kiosk Module

The Employee Kiosk module offers remote employee time card entry via Dashboard Apps. No concurrent Spectrum license is used when you are working in these apps.

- The '[My Time Entry](/en/spectrum/spectrum/human-resources/employee-kiosk-module/my-time-entry)' app provides summary information about time card entries over the past week and facilitates access to enter (or edit) new time card records.

- The '[My Earnings Statement](/en/spectrum/spectrum/human-resources/employee-kiosk-module/my-earnings-statement)' app provides summary information about recent pay checks and allows the employee to print Earnings Statements.

Access to data through the Employee Kiosk is limited to the current user's payroll information (as defined using the 'contact' link between the employee code and operator code).

## Enable the EK Module

The Employee Kiosk (EK) module must be enabled on your Company Installation screen. Navigate to System Administration > Installation > Company Installation. On the Modules tab, select the Employee Kiosk checkbox.

## Establish a Server Connection

The user must be able to access the Spectrum server in order to use the Employee Kiosk. There are multiple ways to accomplish this; two options are creating a virtual private network (VPN) or hosting your Spectrum system on a public URL. Please consult your technical expert to determine the optimal connection method for your organization.

## Create an Employee Kiosk Template User

Every employee with access to the Employee Kiosk module requires a Spectrum Logon ID. This ID is then assigned to the appropriate Employee code and Contact within the system.
To get started, create a new Spectrum operator that has access to the Employee Kiosk (EK) module only. Be sure to enter EK as the 'Profile' and set them to an Inactive status.
Grant this operator security access of level 2 for the EK module. (This can also be done using a security scheme.)

## Create Employee Logons

Every employee who accesses the Employee Kiosk must have a Spectrum Logon.
Spectrum includes a Create Employee Logins screen (accessible from the System Administration > Security menu on the Site Map) to facilitate creating and managing employee logons for field personnel and other employees that do not presently have a Spectrum logon code. This utility also provides an optional email out.
This screen builds a list of active employees who do not have an assigned Spectrum Logon so it is also helpful to set up any new hires in the future. The Administrator can review and edit the information as desired and then perform the update to create the new Spectrum operators.
View a PDF of [Instructions for App Users](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/9aa1aee0-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiI5YWExYWVlMC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMjQ3NzgsImp0aSI6ImY3MzAyNDFmNWZjYTQ0ZmU4NWQwN2FmOWRhODYzY2ZlIiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.9ylhykjjd1kMpcbUAdn6KPLu3FzCVGXy9skTs1TWA04&response-content-disposition=filename%3D%22Employee_Kiosk_Instructions.pdf%22).
