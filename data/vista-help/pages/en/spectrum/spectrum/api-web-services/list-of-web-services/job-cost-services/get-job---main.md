---
title: "Get Job - Main | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/get-job---main"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/get-job---main"
---

# Get Job - Main

Use this service to import Job Main Properties information.
WSDL: GetJobMain.jws
Method: GetJobMain
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

Phone
Telephone
Text
14

Fax_Phone
Fax
Text
14

Job_Site_Phone
Site phone
Text
14

Customer_Code
Customer Code
Text
10

Customer_Name
Customer Name
Text
30

Original_Contract
Original Contract
Numeric
14

Contract_Number
Contract Number
Text
30

Owner_Name
Owner name
Text
50

WO_Site
Site
Text
10

Comment
Comment
Text
250

Price_Method_Code
Price Type Code
Text
1
(F)ixed Price; (T)ime & Material; (C)ost Plus or (U)nit Price

Total_Units
Job units
Numeric
9

Unit_of_Measure
Unit of Measure
Text
5

Status_Code
Status
Text
1
(A)ctive, (I)nactive or (C )omplete

Latitude
Latitude
Numeric
11

Longitude
Longitude
Numeric
11

Legal_Desc
Legal Description
Text
350

Cost_Center
Job Cost Center
Text
10

Field_1
Field 1
Text
30
Placeholder for future fields

Field_2
Field 2
Text
30
Placeholder for future fields

Field_3
Field 3
Text
30
Placeholder for future fields

Field_4
Field 4
Text
30
Placeholder for future fields

Field_5
Field 5
Text
30
Placeholder for future fields

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
