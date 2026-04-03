---
title: "Add Vendor | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/add-vendor"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/add-vendor"
---

# Add Vendor

Use this service to import Vendor information.
WSDL: AddVendor.jws
Method: AddVendor
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Vendor information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Payable

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Accounts Payable > Use Tax Code Maintenance

- System Administration > Installation > Accounts Payable > Invoice Approval Routing Maintenance

- System Administration > Installation > Accounts Payable > Vendor User-Defined Fields Maintenance

## Assumptions and Dependencies

- The Vendor Master cost center flag is shared. The Vendor import will validate that the company has the cost center option set to Pending or Yes and will set the default for the new Vendor to Shared.

- The Vendor status will default to (A)ctive.

- The defined Contact_Name will be the primary contact.

- The Vendor-Add Web service supports the USA Year End Reporting information. The Vendor-Update Web service supports the Canadian Year End Reporting information.

- The Fed_1099_Indicator will defaults to 7 if the field is blank and the Send_1099_Flag is set to Y.

- If the Send_1099_Flag is blank or N and the Fed_1099_Indicator, Social_Sec_Number and/or the Fed_Id_Number are defined they will be added to the Vendor.

- The Social_Sec_Number and Fed_Id_Number cannot be populated at the same time. Each Vendor can only contain one of those two fields.

- If the Send_1099_Flag is set to Y, it is highly recommended that you include either the social security number or the Federal Tax ID number, along with the 1099 indicator (7 is non-employee compensation).

- The combined value of the Distribution % fields must equal 100%. For each G/L Account defined, a corresponding Distribution % must exist.

- This Web Service works with the defined Workflow process in Spectrum.

- The Authorized ID must have the user-defined fields defined, or mapped for this Web Service.

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
YES
Text
3
Valid Company in Spectrum

C
Vendor_Code
Vendor Code
YES
Text
10
Unique identifier / No commas
UPPERCASE FORMAT-NO SYMBOLS

D
Vendor_Name
Vendor Name
YES
Text
30
No commas

E
Alpha_Sort
Vendor Alpha Ref
YES
Text
6
No commas

F
Type
Vendor Type
Text
6

G
Address_1
Address 1
Text
30

H
Address_2
Address 2
Text
30

I
Address_3
City
Text
25

J
State
State/province
Text
2
2 character postal abbreviation

K
Zip_Code
Postal code
Text
10
ZIP or ZIP + 4 (for example, 98012-1234)

L
Phone
Phone Number
Text
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.
Remove the dashes from format when sending to Spectrum.

M
Fax_Phone
Fax #
Text
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.
Remove the dashes from format when sending to Spectrum.

N
Contact_Name
Contact Name
Text
20

O
Our_Account_Number
Account reference
Text
25

P
Terms_Code
Payment due terms (A or B only)
YES
Text
1
Enter 'A' if based on invoice date. Enter 'B' if based on 1st of next month.

Q
Terms_Days
Days Payment Due
YES
Numeric
3
Positive numbers only.

R
Terms_Disc_Code
Discount Due (A or B only)
YES
Text
1
Enter 'A' if based on invoice date. Enter 'B' if based on 1st of next month.

S
Terms_Disc_Days
Days Discount Due
Numeric
3
Positive numbers only.

T
Terms_Disc_Percent
Discount %
Numeric
6
Enter 10.25% as 10.25. Positive numbers only.

U
Insurance_Cert_Flag
Ins Cert
Text
1
(Y)es or(N)o only

V
Insurance_Exp_Date
Ins Expiration Date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010)

W
Hold_Flag
On Hold?
Text
1
(Y)es or(N)o only

X
Default_GL_Account
Default G/L Code
Numeric
12
Code must have an Active status.
G/L Master File Maintenance

Y
GL_Distribution_Acct_List1
Multiple G/L Code (1)
Numeric
12
Must be a Non-Direct G/L code with an Active status.
G/L Master File Maintenance

Z
GL_Distribution_Acct_List2
Multiple G/L Code (2)
Numeric
12
Must be a Non-Direct G/L code with an Active status.
G/L Master File Maintenance

AA
GL_Distribution_Acct_List3
Multiple G/L Code (3)
Numeric
12
Must be a Non-Direct G/L code with an Active status.
G/L Master File Maintenance

AB
GL_Distribution_Acct_List4
Multiple G/L Code (4)
Numeric
12
Must be a Non-Direct G/L code with an Active status.
G/L Master File Maintenance

AC
GL_Distribution_Acct_List5
Multiple G/L Code (5)
Numeric
12
Must be a Non-Direct G/L code with an Active status.
G/L Master File Maintenance

AD
GL_Distribution_Acct_List6
Multiple G/L Code (6)
Numeric
12
Must be a Non-Direct G/L code with an Active status.
G/L Master File Maintenance

AE
GL_Distribution_Acct_List7
Multiple G/L Code (7)
Numeric
12
Must be a Non-Direct G/L code with an Active status.
G/L Master File Maintenance

AF
GL_Distribution_Acct_List8
Multiple G/L Code (8)
Numeric
12
Must be a Non-Direct G/L code with an Active status.
G/L Master File Maintenance

AG
GL_Distribution_Acct_List9
Multiple G/L Code (9)
Numeric
12
Must be a Non-Direct G/L code with an Active status.
G/L Master File Maintenance

AH
GL_Distribution_Acct_List10
Multiple G/L Codes (10)
Numeric
12
Must be a Non-Direct G/L code with an Active status.
G/L Master File Maintenance

AI
GL_Distrib_Percent_List1
Distribution % (1)
Numeric
5
Enter 10.25% as 10.25. Positive numbers only.
The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.

AJ
GL_Distrib_Percent_List2
Distribution % (2)
Numeric
5
Enter 10.25% as 10.25. Positive numbers only.
The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.

AK
GL_Distrib_Percent_List3
Distribution % (3)
Numeric
5
Enter 10.25% as 10.25. Positive numbers only.
The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.

AL
GL_Distrib_Percent_List4
Distribution % (4)
Numeric
5
Enter 10.25% as 10.25. Positive numbers only.
The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.

AM
GL_Distrib_Percent_List5
Distribution % (5)
Numeric
5
Enter 10.25% as 10.25. Positive numbers only.
The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.

AN
GL_Distrib_Percent_List6
Distribution % (6)
Numeric
5
Enter 10.25% as 10.25. Positive numbers only.
The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.

AO
GL_Distrib_Percent_List7
Distribution % (7)
Numeric
5
Enter 10.25% as 10.25. Positive numbers only.
The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.

AP
GL_Distrib_Percent_List8
Distribution % (8)
Numeric
5
Enter 10.25% as 10.25. Positive numbers only.
The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.

AQ
GL_Distrib_Percent_List9
Distribution % (9)
Numeric
5
Enter 10.25% as 10.25. Positive numbers only.
The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.

AR
GL_Distrib_Percent_List10
Distribution % (10)
Numeric
5
Enter 10.25% as 10.25. Positive numbers only.
The combined value of the 'Distribution %' fields must = 100%. For each GL Account defined a corresponding Distribution % must exist.

AS
Use_Tax_Code
Sales/Use Tax Code
Text
15
Use Tax Code Maintenance

AT
Send_1099_Flag
1099
Text
1
(Y)es or(N)o only
*See Assumptions and Dependencies.

AU
Alt_1099_Name
Alternate Name
Text
30
No commas

AV
Fed_1099_Indicator
1099 Pmt Indicator
Text
1
1; 2; 3; 4; 5; 6; 7; 8; 9 or A only (7 for non-employee compensation box)
* See Assumptions and Dependencies. Defaults to 7 if blank and the Send_1099_Flag = Y.

AW
Social_Sec_Number
Social Security #
Text
9
Format = 123-45-6789 or 123456789. If defined then Fed_Id_Number must be blank.
Remove the dashes from format.

AX
Fed_Id_Number
Federal ID #
Text
12
If defined then Social_Sec_Number must be blank.

AY
Disadv_Business_Flag
DBE
Text
1
(Y)es or(N)o only

AZ
Disadv_Business_Type
DBE Type
Text
10

BA
Routing_Code1
Routing Code for Invoice Approval
Text
10
Routing Code Maintenance

BB
Routing_Code2
Routing Code for Over Limit Invoice Approval
Text
10
Routing Code Maintenance

BC
Routing_Limit
Routing Limit Invoice Approval
Numeric
13
Positive numbers only.

BD
Vendor_Email
Vendor Email
Text
80
Example: Jon@xxx.com
Must be the basic layout for an email address.

BE
Contact_Phone
Contact Phone
Text
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.
Remove the dashes from format when sending to Spectrum.

BF
UDF1
User Defined Alpha/ Numeric/Date 1
+
20
Web Service Authorization ID Service UDF defined.

BG
UDF2
User Defined Alpha/ Numeric/Date 2
+
20
Web Service Authorization ID Service UDF defined.

BH
UDF3
User Defined Alpha/ Numeric/Date 3
+
20
Web Service Authorization ID Service UDF defined.

BI
UDF4
User Defined Alpha/ Numeric/Date 4
+
20
Web Service Authorization ID Service UDF defined.

BJ
UDF5
User Defined Alpha/ Numeric/Date 5
+
20
Web Service Authorization ID Service UDF defined.

BK
UDF6
User Defined Alpha/Numeric/Date 6
+
20
Web Service Authorization ID Service UDF defined.

BL
UDF7
User Defined Alpha/ Numeric/Date 7
+
20
Web Service Authorization ID Service UDF defined.

BM
UDF8
User Defined Alpha/ Numeric/Date 8
+
20
Web Service Authorization ID Service UDF defined.

BN
UDF9
User Defined Alpha/ Numeric/Date 9
+
20
Web Service Authorization ID Service UDF defined.

BO
UDF10
User Defined Alpha/ Numeric/Date 10
+
20
Web Service Authorization ID Service UDF defined.

BP
UDF11
User Defined Alpha/ Numeric/Date 11
+
20
Web Service Authorization ID Service UDF defined.

BQ
UDF12
User Defined Alpha/ Numeric/Date 12
+
20
Web Service Authorization ID Service UDF defined.

BR
UDF13
User Defined Alpha/ Numeric/Date 13
+
20
Web Service Authorization ID Service UDF defined.

BS
UDF14
User Defined Alpha/ Numeric/Date 14
+
20
Web Service Authorization ID Service UDF defined.

BT
UDF15
User Defined Alpha/ Numeric/Date 15
+
20
Web Service Authorization ID Service UDF defined.

BU
UDF16
User Defined Alpha/ Numeric/Date 16
+
20
Web Service Authorization ID Service UDF defined.

BV
UDF17
User Defined Alpha/ Numeric/Date 17
+
20
Web Service Authorization ID Service UDF defined.

BW
UDF18
User Defined Alpha/ Numeric/Date 18
+
20
Web Service Authorization ID Service UDF defined.

BX
UDF19
User Defined Alpha/ Numeric/Date 19
+
20
Web Service Authorization ID Service UDF defined.

BY
UDF20
User Defined Alpha/ Numeric/Date 20
+
20
Web Service Authorization ID Service UDF defined.

+ NOTE = the UDF (1-20) elements can be Numeric, Date or Text depending on how they are created within Spectrum.
