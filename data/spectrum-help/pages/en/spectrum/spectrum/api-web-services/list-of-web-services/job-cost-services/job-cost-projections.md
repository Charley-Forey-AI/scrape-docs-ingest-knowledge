---
title: "Job Cost Projections | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/job-cost-projections"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/job-cost-projections"
---

# Job Cost Projections

Use this service to import Job Cost Projections information.
WSDL: JobCostProjections.jws
Method: JobCostProjections
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Job Cost Projections information, the following file maintenance areas must be completed:

- System Administration > Installation > Job Cost

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phases

- System Administration > Installation > Job Cost > Cost Type File Maintenance

## Assumptions and Dependencies

- The Job Cost Projection Web Service will use the 'At Completion' logic. The standard projected cost entry screen logic will not be created and no reporting will be created.

- The 'At completion' logic will be used for the Web Service for Dollars, Hours and Quantity values therefore the final numbers will be defined in the service.

- The web service doesn't 'update' existing projection entries.

- One of the following fields is required in order to modify the projected values. The blank fields will not be updated and to clear a value a zero must be defined.

- Amount

- Projected_Hours

- Projected_Quantity

- The Job Cost Installation options for Projections will be used when posting the new projections.

- Projections that have already been posted for a subsequent date will be treated as a 'correction' to the previous projection but will not affect the current projections.

- If the Projection value already exists in the system for the given Job/Phase/Cost type then it will be ignored.

- Any active Projected Cost Transaction File (that is, Build) created will be ignored.

- The Phase in the record must match the current phase mask defined on the Job.

- The Operator code will be used to define who updated the Projections.

- The Web Service will ignore any projections that are in process (that is, are built in standard Spectrum).

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
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Job_Number
Job Number
YES
Text
10
*See Assumptions and Dependencies.
Job

D
Phase_Code
Phase number
YES
Text
20
No dashes. *See Assumptions and Dependencies.
Phase

E
Cost_Type
Cost type
YES
Text
3
*See Assumptions and Dependencies.
Cost Type

F
Transaction_Date
Transaction Date
YES
Date
10
Back dated projections will be made as corrections and won't change the current projections. Enter as: MM/DD/CCYY (for example, 01/05/2010).
*See Assumptions and Dependencies.

G
Amount
Projected Dollars At Completion
Numeric
14
Must be defined if Projected_Hours and Projected_Quantity are blank. Allows Negative number. Format = -10.2
*See Assumptions and Dependencies.

H
Projected_Hours
Projected Hours At Completion
Numeric
14
Must be defined if Amount and Projected_Quantity are blank. Allows Negative number. Format = -10.2
*See Assumptions and Dependencies.

I
Projected_Quantity
Projected Quantity At Completion
Numeric
14
Must be defined if Amount and Projected_Hours are blank. Allows Negative number. Format = -10.2
*See Assumptions and Dependencies.

J
Note
Memo
Text
80

K
Operator
Operator code
Text
3
Define the Spectrum Operator code. If blank default Web Service code.
Valid Operator Code
