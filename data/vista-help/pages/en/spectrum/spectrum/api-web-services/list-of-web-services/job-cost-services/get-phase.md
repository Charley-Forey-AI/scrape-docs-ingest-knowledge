---
title: "Get Phase | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/get-phase"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/get-phase"
---

# Get Phase

Use this service to import Phase information.
WSDL: GetPhase.jws
Method: GetPhase
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Authorization ID controls the security and defaults the pCompany_Code field if left blank.

- The JTD, Projected and Estimated return fields do not include contract labor hours, Pre-time card information, committed costs or unapproved invoices.

- All parameter fields have SuperSelect logic except the following-

- pStatus_Code

- pCost_Center

- pSort_By

## Parameter Fields

Use the table below for reference when using this service.
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

pCost_Type
Cost Type
Text
3
Cost Type File Maintenance

pJob_Number
Job Number
Text
10
Job File Maintenance

pStatus_Code
Status
Text
1
Define one specific Status or leave blank to see Active and Inactive only

pCost_Center
Phase Cost Center
Text
10
Define one specific Cost Center or leave blank to see all based on Authorization ID

pSort_By
Sort By Options
Text
1
Blank = Job number, Phase and Cost type or C= Cost Type, Job number and Phase

## Return Fields

Use the table below for reference when using this service.
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

Job_Number
Job Number
Text
10

Phase_Code
Phase Number
Text
20

Cost_Type
Cost Type
Text
3

Description
Description
Text
25

Status_Code
Status Code
Text
1
(A)ctive, (I)nactive or (C )omplete

Unit_of_Measure
Unit of Measure
Text
3

JTD_Quantity
JTD Quantity
Numeric
11
See Assumptions and Dependencies

JTD_Hours
JTD Hours
Numeric
10
See Assumptions and Dependencies

JTD_Actual_Dollars
JTD Cost
Numeric
12
See Assumptions and Dependencies

Projected_Quantity
Projected Quantity
Numeric
11
See Assumptions and Dependencies

Projected_Hours
Projected Hours
Numeric
10
See Assumptions and Dependencies

Projected_Dollars
Projected Cost
Numeric
12
See Assumptions and Dependencies

Estimated_Quantity
Estimated Quantity
Numeric
11
See Assumptions and Dependencies

Estimated_Hours
Estimated Hours
Numeric
10
See Assumptions and Dependencies

Current_Estimated_Dollars
Estimated Cost
Numeric
12
See Assumptions and Dependencies

Cost_Center
Phase Cost Center
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
