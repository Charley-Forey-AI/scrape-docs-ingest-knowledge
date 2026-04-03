---
title: "Change Employee - Personal Info | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/change-employee---personal-info"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/payroll-services/change-employee---personal-info"
---

# Change Employee - Personal Info

Use this service to import Employee Personal information.
WSDL: UpdateEmp_Personal.jws
Method: UpdateEmp_Personal
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- The Payroll module must be set up.

- The Employee code must exist in the defined Company code.

- The Employee-Personal Information Web Service updates an existing employee's information for the defined fields only.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- Any changes made to the Employee for the following fields will update the Employee Contact record.

- Title

- Email

- Mobile Phone

- Work Extension

- Status

- The Balance and YTD hours will be summed for the 'Bank balance' total in the Employee Time Off Bank screen.

- If you want to deduct Balance hours from YTD hours, enter a negative Balance hours amount (that is, -32 (Vacation_Hours_Balance) + 40 (Vacation_Hours_YTD) = 8 (Bank balance)).

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.
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
Employee_Code
Employee Code
YES
Text
11
Unique Identifier / No commas
Employee Code must exist in the defined Company Code

D
Employment_Status
Employee Status
Text
1
Employee Status Code Maintenance

E
Termination_Date_List3
Latest Termination Date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010)
Required if Employee Status = 'T' or 'D'

F
Street_Address
Mailing Address
Text
25

G
Street_Address2
Mailing Address Line 2
Text
25

H
City_Address
Mailing City
Text
25

I
State
Mailing State
Text
2
2 character postal abbreviation

J
Zip_Code
Mailing Zip Code
Text
10

K
Domicile_Address
Domicile Street Address
Text
25

L
Domicile_Address2
Domicile Street Address Line 2
Text
25

M
Domicile_City
Domicile City
Text
25

N
Domicile_State
Domicile State
Text
2
2 character postal abbreviation

O
Domicile_Zip_Code
Domicile Zip Code
Text
10

P
Phone
Personal telephone
Text
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.
Remove the dashes from format when sending to Spectrum.

Q
Employee_Fax
Employee Fax
Text
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.
Remove the dashes from format when sending to Spectrum.

R
Employee_Email
Work E-mail Address
Text
80
Structure = name@domain.com. Use a semi-colon between multiple addresses

S
Emergency_Contact
Emergency Contact
Text
25

T
Emergency_Phone
Emergency Phone
Text
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.
Remove the dashes from format when sending to Spectrum.

U
Emergency_Relationship
Relationship of Emergency Contact
Text
15

V
Supervisor_Code
Supervisor Code
Text
2
Supervisor Code Maintenance

W
Employee_Location
Employee Location Code
Text
10
Text field if HR module is not installed.
Human Resources Location Codes if installed

X
Union_Code
Union Code
Text
10
Union File Maintenance

Y
Wage_Class
Wage Code
Text
10
Validated in combination with union code
Union & Wage Code combination in Wage Code File Maintenance

ZEmployee_Work_ClassWork ClassText1(J)ourneyman, (A)pprentice, or (T)raineeCan be only one of J, A, or T
AA
Pay_Rate_Code
Pay Level
Text
1
1 - 9 only

AB
EEO_Class_Code
EEO Class Code
Text
3
EEO Classification Maintenance

AC
Social_Security
Social Security #
Text
9
Format = 123-45-6789 or 123456789
No duplicates allowed. Remove the dashes from format.

AD
Title
Employee Title
Text
50
Text field if HR module is not installed.
Human Resources Job Title. If installed and selected.

AE
Sex
Employee Sex
Text
1
(M)ale or (F)emale only

AF
Race
Employee Race
Text
1
(A)- Asian; (B) - Black; (C)- White; (H) -Hispanic; (N)- American Indian; (O) -Other only;(P)- Pacific Islander

AG
Number_Of_Dependents
Dependents
Numeric
3

AH
Certified_Flag
Certified Report
Text
1
(Y)es or (N)o only

AI
Marital_Status
Marital Status
Text
1
(D)ivorced; (M)arried; (S)ingle; (W)idowed or (U)nknown only

AJ
Delete_Flag
Purge at Year End?
Text
1
(Y)es or (N)o only
Only allowed with a status type of T(erminated) or D(ecreased)

AK
Months_To_Next_Review
Months To Next Review
Numeric
3

AL
Hire_Date_List1
Original Hire Date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/1982)

AM
Birth_Date_List4
Date of Birth
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/1982)

AN
Rehire_Date_List2
Latest Rehire Date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/1982)

AO
Last_Review_Date_List7
Date of Last Review
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/1982)

AP
Spouse_Birth_Date_List6
Spouse Birth Date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/1982)

AQ
Spouse_Name
Spouse Name
Text
15

AR
Driver_License
Driver's License #
Text
25

AS
Employee_Driver_License_Expire
Driver's License Expiration Date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/1938)

AT
Vacation_Hours_Balance
Vacation Hours Balance
Numeric
7
Format = -3.2. Allows negatives.

AU
Vacation_Hours_YTD
Vacation Hours YTD
Numeric
7
Format = -3.2. Allows negatives.

AV
Vacation_Control_Code
Vacation Control Code
Text
2
Hours Bank Code Maintenance with a Type of Vacation

AW
Holiday_Hours_Balance
Holiday Hours Balance
Numeric
7
Format = -3.2. Allows negatives.

AX
Holiday_Hours_YTD
Holiday Hours YTD
Numeric
7
Format = -3.2. Allows negatives.

AY
Holiday_Control_Code
Holiday Control Code
Text
2
Hours Bank Code Maintenance with a Type of Holiday

AZ
Sick_Hours_Balance
Sick Hours Balance
Numeric
7
Format = -3.2. Allows negatives.

BA
Sick_Hours_YTD
Sick Hours YTD
Numeric
7
Format = -3.2. Allows negatives.

BB
Sick_Control_Code
Sick Control Code
Text
2
Hours Bank Code Maintenance with a Type of Sick

BC
I9_Flag
I9 Status
Text
1
(A)lien or (P)ermanent only

BD
I9_Expire_Date
I9 Expiration Date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/1982)

BE
Employee_Mobile_Phone
Work mobile Phone
Text
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.
Remove the dashes from format when sending to Spectrum.

BF
Employee_Extension
Work extension
Text
15

BG
Employee_Termination_Reason
Termination Reason
Text
30

BH
Employee_Rehire_Rating
Rehire rating (0-10)
Numeric
2
0-10 only. Required if Employee has an Employment status of Terminated.
