---
title: "Get Employee - UDF | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/get-employee---udf"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/get-employee---udf"
---

# Get Employee - UDF

Use this service to set up a GET service for Employee User-Defined fields.
WSDL: GetEmployeeUDF.jws
Method: GetEmployeeUDF
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Authorization ID controls the security and defaults the pCompany_Code field if left blank.

- All parameter fields have SuperSelect logic except the following-

- pStatus_Type

- pCost_Center

- pSort_By

## Parameter Fields

Use the table below for reference when setting up parameter fields for this service.
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
Text
3
Valid Spectrum Company

pWage_Class
Wage Code
Text
10

pUnion_Code
Union Code
Text
10

pOccupation
Occupation
Text
50

pTrade
Trade
Text
50

pStatus_Type
Status
Text
1
Define one specific Status or leave blank to see Active and Inactive only

pCost_Center
Employee Cost Center
Text
10
Define one specific Cost Center or leave blank to see all based on Authorization ID

pSort_By
Sort By Options
Text
1
Blank = Employee Code, A= Alphabetical by Employee_Name, F= First Name, L= Last name or D= Department code

## Return Fields

Use the table below for reference when setting up return fields for this service.
Return Field Name
Description
Type
Max
Field Information

Company_Code
Company Code
Text
3
Valid Spectrum Company

Employee_Code
Employee Code
Text
11
Employee File Maintenance

Employee_Name
Employee Name
Text
30

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
