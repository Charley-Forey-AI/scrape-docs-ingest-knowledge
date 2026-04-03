---
title: "Work Order Header | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/work-order-header"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/work-order-header"
---

# Work Order Header

Use this service to create new Work Orders within Spectrum or update an existing Work Order.
WSDL: WorkOrderHeader.jws
Method: WorkOrderHeader
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Work Orders information, the following file maintenance areas must be completed:

- System Administration > Installation > Work Order

- System Administration > Installation > Accounts Receivable

- System Administration > Installation > Service Contract

- System Administration > Installation > Job Cost

- System Administration > Installation > Work Order > Lead Source Maintenance

- System Administration > Installation > Work Order > Technician Maintenance

- System Administration > Installation > Work Order > Work Order Type Maintenance

- System Administration > Installation > Work Order > Case Type Maintenance

- System Administration > Installation > Work Order > Dispatch Status Maintenance

- System Administration > Installation > Work Order > Non-stock Markup File Maintenance

- System Administration > Installation > Work Order > Zone Maintenance

- System Administration > Installation > Work Order > Priority Maintenance

- System Administration > Installation > Work Order > G/L Department

- System Administration > Installation > Work Order > Site Maintenance

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Accounts Receivable > Customer Maintenance

- System Administration > Installation > Accounts Receivable > Sales Tax Code Maintenance

- System Administration > Installation > Accounts Receivable > Salesperson Code Maintenance

- System Administration > Installation > Accounts Receivable > Terms Code Maintenance

- System Administration > Installation > Accounts Receivable > Bill-to Code Maintenance

- System Administration > Installation > Service Contract > Service Contract Maintenance

- System Administration > Installation > Work Order > Work Order User-Defined Fields

- System Administration > Installation > Work Order > Work Order Note Topics Maintenance

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The Work Order Web Service will create new Work Orders within Spectrum or update an existing Work Order. Any Field that is left blank for an existing Work Order will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes the data with the defined data in the field name.

- The defined WO_Reference_Code defines the hierarchy used for the defaults for the following fields. The WO_Reference_Code is either for a Job or a Site within Spectrum.

- AR_Terms_Code

- Sales_Tax_Code

- Taxable_Flag

- GL_Department – site specific only. See help files for logic.

- Cost_Center

- Material_Price_Level

- Price_Level

- Markup_Code – site specific only. See help files for logic.

- Sales_Person – see help files for logic.

- The Dispatch_Status_Code status type controls the multiple dates that can be defined.

- Cost centers will validate against the Cost Center Maintenance Table and follow the standard WO_Reference_Code hierarchy (that is, Job vs. Site work order).

- Cost Center information will only be allowed in if Company is set to Pending or Yes status.

- If the Work Order Type is entered and has a cost center assigned to it, this cost center will default for a new work order. If the Work Order Type does not have a cost center assigned to it, the site's cost center will default instead.

- If the WO_Job division field is changed on an existing work order, the Work Order Type cost center will change as it does when importing a New Work Order header record.

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
Field Information
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
If blank defaults from Authorization ID.
Valid Company in Spectrum

C
WO_Number
Work Order number
Text
10
If left blank then uses next number on Work Order Installation. If defined and exists change data.

D
WO_Reference_Code
For Site or Job?
YES
Text
1
S(ite) or J(ob)

E
WO_Job_Number
Site code / Job number
YES
Text
10
Validates based on WO_Reference_Code
Work Order Site File Maintenance or Job File Maintenance

F
WO_Job_Division
Work Order Type
Text
5
Required if creating new Work Order Header unless default exists for Site specific work orders. Type must contain a non-direct cost flag for Site specific and a direct cost flag for Job specific Work Orders. Field will update if WO_Number exists.
Work Order Type Maintenance

G
Bill_Customer_Code
Customer
Text
10
Required if creating new Work Order Header. Field will update if WO_Number exists.
Customer Maintenance File

H
Contract_Number
Service contract
Text
10
For Site specific Work Orders
Service Contract Maintenance

I
Customer_PO_Number
Customer P.O.
Text
25

J
Customer_Job
Customer's job
Text
10
For Site specific Work Orders. Defaults from Site if defined.
No validation

K
WO_Phone1
Phone 1
Text
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225. Defaults from Site/Job or Customer if left blank.
Remove the dashes from format when sending to Spectrum.

L
WO_Phone2
Phone 2
Text
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225. Defaults from Site/Job or Customer if left blank.
Remove the dashes from format when sending to Spectrum.

M
Bill_Contract
Contact note
Text
20

N
Zone
Zone
Text
3
Defaults from Site if defined.
Work Order Zone Maintenance File

O
Priority_Code
Priority
Text
2
Work Order Priority Maintenance

P
WO_Case_Type
Case type
Text
10
Defaults from Site if defined.
Case Type Maintenance

Q
Price_Type
Price method
Text
1
F(lat Rate) or T(+M). If blank use Work Order Installation default.

R
Total_Quote_Amount
Quote
Numeric
10
Positive numbers only.

S
Projected_Hours
Quote Hours
Numeric
8
Positive numbers only.

T
Est_Arrival
Est. arrival
Text
15

U
Dispatch_Status_Code
Dispatch code status
Text
1
Dispatch Status Codes

V
Summary_Description
Work summary (customer request)
Text
250

W
Ordered_Date
Ordered date
Date
10
Text format for import MM/DD/CCYY.

X
Time_Entered
Ordered time
Numeric
6
Format HHMMSS. Hours cannot exceed 24, minutes and seconds cannot exceed 59.

Y
Requested_Date
Requested date
Date
10
Text format for import MM/DD/CCYY

Z
Estimated_Complete_Time
Requested time
Numeric
6
Format HHMMSS. Hours cannot exceed 24, minutes and seconds cannot exceed 59.

AA
Scheduled_Start_Date
Scheduled date
Date
10
Text format for import MM/DD/CCYY

AB
Scheduled_Start_Time
Scheduled time
Numeric
6
Format HHMMSS. Hours cannot exceed 24, minutes and seconds cannot exceed 59.

AC
Date_Assigned
Assigned date
Date
10
Text format for import MM/DD/CCYY

AD
Time_Assigned
Assigned time
Numeric
6
Format HHMMSS. Hours cannot exceed 24, minutes and seconds cannot exceed 59.

AE
Arrival_Date
Arrived date
Date
10
Text format for import MM/DD/CCYY

AF
Arrival_Time
Arrived time
Numeric
6
Format HHMMSS. Hours cannot exceed 24, minutes and seconds cannot exceed 59.

AG
Complete_Date
Finished date
Date
10
Text format for import MM/DD/CCYY
Must have a Dispatch code status type of Finished to be populated

AH
Complete_Time
Finished time
Numeric
8
Format HHMMSS. Hours cannot exceed 24, minutes and seconds cannot exceed 59.
Must have a Dispatch code status type of Finished to be populated

AI
Lead_Source
Lead source
Text
15
Required if the Work Order Installation option is selected. Defaults from Site if defined.
Lead Source Maintenance

AJ
Sales_Person
Salesperson
Text
3
Defaults from Service Contract then Customer if left blank based on the WO_Reference_Code defined.
Salesperson Code Maintenance

AK
Taken_By
Taken by
Text
3
If blank then default the services operator code.

AL
AR_Terms_Code
Terms code
Text
1
If blank then default from WO_Reference_Code defined hierarchy.
Customer Term Code Maintenance

AM
Sales_Tax_Code
Sales tax code
Text
15
If blank then default from WO_Reference_Code defined hierarchy.Â Defaults from Site if defined.
A/R Sales Tax Code Maintenance

AN
Taxable_Flag
Taxable?
Text
1
(Y)es or (N)o only. If blank then default from WO_Reference_Code defined hierarchy.

AO
GL_Department
G/L department
Text
5
Site work order specific field. Defaults from Work Order Type File Maintenance. Required if Work Order Type is not defined.
WO GL Department Maintenance and Work Order Type definitions.

AP
Cost_Center
Cost center
Text
10
Hierarchy defined based on the WO_Reference_Code field.
Cost Center Maintenance. Job and Customer Cost Center. Service Contract, WO Site and Customer Cost Center.

AQ
Billto_Code
Alternate Bill-to code
Text
4
Defaults from Site if blank. Must be valid for the defined Customer Code.
Customer Bill-to Address Maintenance

AR
Override_ERO_Markup
Override markup %
Numeric
6
Positive numbers only. Format XXX.XX%

AS
Material_Price_Level
Material level
Numeric
1
1 - 5 only. If blank then default from WO_Reference_Code defined hierarchy.

AT
Price_Level
Labor level
Numeric
1
1 - 5 only. If blank then default from WO_Reference_Code defined hierarchy.

AU
Markup_Code
Non-stock markup
Text
10
Site work order specific field. If blank then follows standard spectrum hierarchy.
Non-stock Markup File Maintenance
