---
title: "Get Job UDF | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/get-job-udf"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/get-job-udf"
---

# Get Job UDF

Use this service to import Job User-Defined Fields information.
WSDL: GetJobUDF.jws
Method: GetJobUDF
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Authorization ID controls the security and defaults the pCompany_Code field if left blank.

- All parameter fields have SuperSelect logic except the following-

- pStatus_Code

- pCost_Center

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

UDF1
User Defined Alpha/Numeric/Date 1
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF2
User Defined Alpha/Numeric/Date 2
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF3
User Defined Alpha/Numeric/Date 3
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF4
User Defined Alpha/Numeric/Date 4
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF5
User Defined Alpha/Numeric/Date 5
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF6
User Defined Alpha/Numeric/Date 6
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF7
User Defined Alpha/Numeric/Date 7
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF8
User Defined Alpha/Numeric/Date 8
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF9
User Defined Alpha/Numeric/Date 9
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF10
User Defined Alpha/Numeric/Date 10
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF11
User Defined Alpha/Numeric/Date 11
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF12
User Defined Alpha/Numeric/Date 12
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF13
User Defined Alpha/Numeric/Date 13
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF14
User Defined Alpha/Numeric/Date 14
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF15
User Defined Alpha/Numeric/Date 15
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF16
User Defined Alpha/Numeric/Date 16
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF17
User Defined Alpha/Numeric/Date 17
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF18
User Defined Alpha/Numeric/Date 18
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF19
User Defined Alpha/Numeric/Date 19
+
20
UDF's must be defined on Web Service for Authorization ID.

UDF20
User Defined Alpha/Numeric/Date 20
+
20
UDF's must be defined on Web Service for Authorization ID.

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

NOTES:
• + = the UDF (1-20) elements can be Numeric, Date or Text depending on how they are created within Spectrum.
• The UDF's need to be mapped based on the Authorization ID being used.
