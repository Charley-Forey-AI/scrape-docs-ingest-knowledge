---
title: "Get Job | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/get-job"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/get-job"
---

# Get Job

Use this service to import Job information.
WSDL: GetJob.jws
Method: GetJob
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

Division
Division
Text
5

Address_1
Address Line 1
Text
30

Address_2
Address Line 2
Text
30

City
City
Text
25

State
State
Text
2

Zip_Code
Zip Code
Text
10

Project_Manager
Project Manager
Text
15

Superintendent
Superintendent
Text
15

Estimator
Estimator
Text
15

Certified_Flag
Certified Flag
Text
1

Customer_Code
Customer Code
Text
10

Status_Code
Status
Text
1
(A)ctive, (I)nactive or (C )omplete

Work_State_Tax_Code
Work State Tax Code
Text
10

Contract_Number
Contract Number
Text
15

Cost_Center
Job Cost Center
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
