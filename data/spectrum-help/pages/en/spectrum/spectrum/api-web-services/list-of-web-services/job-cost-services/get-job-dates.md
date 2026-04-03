---
title: "Get Job Dates | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/get-job-dates"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/get-job-dates"
---

# Get Job Dates

Use this service to import Job Dates information.
WSDL: GetJobDates.jws
Method: GetJobDates
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Authorization ID controls the security and defaults the pCompany_Code field if left blank.

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

pDivision
Division
Text
5

pStatus_Code
Status
Text
1
Define one specific Status or leave blank to see Active and Inactive only

pProject_Manager
Project Manager
Text
15

pSuperintendent
Superintendent
Text
15

pEstimator
Estimator
Text
15

pCustomer_Code
Customer Code
Text
10
Customer File Maintenance

pCost_Center
Job Cost Center
Text
10
Define one specific Cost Center or leave blank to see all based on Authorization ID

pSort_By
Sort By Options
Text
1
Blank = Job number, D=Division, P=Project Manager, S=Superintendent, E=Estimator, or C=Customer Code

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
Job File Maintenance

Job_Description
Job Description
Text
25

Est_Start_Date
Estimated Start Date
Date
10

Est_Complete_Date
Estimated Complete Date
Date
10

Projected_Complete_Date
Projected Complete Date
Date
10

Create_Date
Job Created Date
Date
10

Start_Date
Actual Start Date
Date
10

Complete_Date
Actual Complete Date
Date
10

Field_1
Field 1
Text
10
Place holder for other dates in future release

Field_2
Field 2
Text
10
Place holder for other dates in future release

Field_3
Field 3
Text
10
Place holder for other dates in future release

Field_4
Field 4
Text
10
Place holder for other dates in future release

Field_5
Field 5
Text
10
Place holder for other dates in future release

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
