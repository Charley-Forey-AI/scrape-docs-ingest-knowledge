---
title: "Add Job Phase | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/add-job-phase"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/add-job-phase"
---

# Add Job Phase

Use this service to create a new Phase or update an existing Phase.
WSDL: AddPhase.jws
Method: AddPhase
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Phase information, the following file maintenance areas must be completed:

- System Administration > Installation > Job Cost

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phases

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation > Payroll > Worker's Compensation Code Maintenance

- System Administration > Installation > Accounts Receivable > Unit of Measure File Maintenance

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The Phase web service will either create a new Phase or update an existing Phase.

- If creating a new Phase then the Description and Price_Method_Code fields are required.

- The Phase will default with a status of (A)ctive.

- The Job Cost Installation defines the phase mask and fill option which are used to create the phases.

- The Phase will not be added to a Job with a Complete status.

- The values defined for field names Original_Est_Quantity, Original_Est_Cost and Original_Est_Hours will default the same values into the Current quantity, costs, and hours in the Phase automatically based on the Job Installation settings if the Current values are left blank.

- The Job Cost Installation, 'Current Estimate display only?' cleared allows the Current_Est_Hours, Current_Est_Quantity, and Current_Est_Cost fields to be updated. If it is selected then it will not be updated.

- The Phase description is shared between all Phase/Cost Type combinations therefore the following logic will be applied when adding a new phase or changing the data.

- If adding a new phase/cost type combination then the first record created will be maintained in Spectrum and will ignore the remaining defined description(s) as additional combinations are added.

- If the phase/cost type combination exists within Spectrum and the record contains a different description then ALL phase/cost type combinations will be updated with the defined description.

- The Bid_Item_Number field will use the first two characters as the Billing Group if the Job is a unit price Job.

- Cost centers will validate against the Cost Center Maintenance table.

- Cost center information will only be allowed in if the Company is set to a Pending or Yes status.

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
Valid Company in Spectrum

C
Job_Number
Job Number
YES
Text
10
Must be an Active or Inactive Job.
Job File Maintenance

D
Phase_Code
Phase number
YES
Text
20
No dashes
Validates to the Phase mask on the installation screen.

E
Description
Description
Text
25
Required if adding a new phase. *See Assumptions and Dependencies for impact of updating the Phase Description.

F
Cost_Type
Cost type
YES
Text
3
Cost Type Maintenance

G
Original_Est_Quantity
Quantity Estimate
Numeric
11

H
Unit_of_Measure
Unit of measure
Text
3
Unit of Measure File Maintenance

I
Original_Est_Cost
Estimate Amount
Numeric
12

J
Original_Est_Hours
Hours Estimate
Numeric
10

K
Bid_Item_Number
Billing item
Text
10
 The billing item is broken into Group and Item for Unit Price jobs. The first 2 characters will be defined as the Group when the Job is Unit Price. *See Assumptions and Dependencies.

L
Alt_Phase_Code
Alternate phase
Text
20
No dashes

M
Work_Comp_Code
Worker's compensation
Text
6
Worker's Comp Code Maintenance

N
Price_Method_Code
Price type
YES
Text
1
(F)ixed Price; (T)ime & Material; (C)ost Plus; (U)nit Price or (J)ob default

O
Phase_Cost_Center
Phase Code Cost Center
Text
10
Cost Center Maintenance

P
Current_Est_Hours
Current Estimate Hours
Numeric
10
*See Assumptions and Dependencies

Q
Current_Est_Quantity
Current Estimate Quantity
Numeric
11
*See Assumptions and Dependencies

R
Current_Est_Cost
Current Estimate Amount
Numeric
12
*See Assumptions and Dependencies

S
Status_Code
Status Code
Text
1
(A)ctive; (I)nactive or (C)omplete. If blank then defaults to (A)ctive.
