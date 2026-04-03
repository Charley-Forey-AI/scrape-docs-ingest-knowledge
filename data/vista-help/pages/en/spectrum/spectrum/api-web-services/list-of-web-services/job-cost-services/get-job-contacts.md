---
title: "Get Job Contacts | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/get-job-contacts"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/get-job-contacts"
---

# Get Job Contacts

Use this service to import Job contact information.
WSDL: GetJobContact.jws
Method: GetJobContact
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Authorization ID controls the security and defaults the pCompany_Code field if left blank.

- All parameter fields have SuperSelect logic except the following-

- pStatus_Code

- pCost_Center

- pSort_By

## Parameter Fields

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

pJob_Number
Job Number
Text
10
Defined on the Job Master

pStatus_Code
Status
Text
1
Define one specific Status or leave blank to see Active and Inactive only

pProject_Manager
Project Manager
Text
15
Defined on the Job Master

pSuperintendent
Superintendent
Text
15
Defined on the Job Master

pEstimator
Estimator
Text
15
Defined on the Job Master

pFirst_Name
Contact First Name
Contact Master

pLast_Name
Contact Last Name
Contact Master

pPhone_Number
Contact Primary Phone
Primary phone number defined on Contact Master

pTitle
Contact Title
Text
10
Contact Master

pCost_Center
Job Cost Center
Text
10
Define one specific Cost Center or leave blank to see all based on Authorization ID

pSort_By
Sort By Options
Text
1
Blank = Company code, C=Contact ID, P=Project Manager, S=Superintendent, E=Estimator, or L=Last name

## Return Fields

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

Status_Code
Job status
Text
1
Defined on the Job Master

Project_Manager
Project Manager
Text
15
Defined on the Job Master

Superintendent
Superintendent
Text
15
Defined on the Job Master

Estimator
Estimator
Text
15
Defined on the Job Master

Cost_Center
Job Cost Center
Text
10
Defined on the Job Master

Contact_ID
Contact Id
Number
10

First_Name
Contact First Name
Text
20

Last_Name
Contact Last Name
Text
30

Title
Contact Title
Text
50

Addr_1
Contact Primary Address 1
Text
30

Addr_2
Contact Primary Address 2
Text
30

Addr_City
Contact Primary Address City
Text
25

Addr_State
Contact Primary Address State
Text
2

Addr_Zip
Contact Primary Address Zip
Text
10

Addr_Country
Contact Primary Address Country
Text
25

Phone_Number
Contact Primary Phone
Text
14

Email1
Contact Email 1
Text
80

Email2
Contact Email 2
Text
80

Email3
Contact Email 3
Text
80

Remarks
Contact Remarks
Text
250

Status
Contact Status
Text
1

OType
Organization Type
Text
1
Contact Organization - V(endor), C(ustomer), E(mployee) or O(ther)

OName
Organization Name
Text
40

OCity
Organization City
Text
25

OState
Organization State
Text
2

OStatus
Organization Status
Text
1

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
