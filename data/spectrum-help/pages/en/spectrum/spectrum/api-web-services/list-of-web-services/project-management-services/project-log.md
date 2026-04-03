---
title: "Project Log | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/project-management-services/project-log"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/project-management-services/project-log"
---

# Project Log

Use this service to import Project Log
 information.
 WSDL: ProjectLog.jws Method: ProjectLog
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Project Log information, the following file maintenance screens must be completed:

- System Administration > Installation > Job Cost

- System Administration > Installation > Project Management > Building / Area Maintenance

- System Administration > Installation > Project Management > Category Maintenance

- System Administration > Installation > Project Management > Classification Maintenance

- System Administration > Installation > Project Management > Project Note Topics Maintenance

- System Administration > Installation > Job Cost > Job Phases

## Assumptions and Dependencies

- If Company_Code and Category field names are blank then use the Authorization ID default value. Both fields are required in order to process the web service.

- The TransactionId and Reference_Num field name can be defined or not.

- If they are both blank then a new entry is created using the auto sequencing logic.

- If the TransactionId is defined and valid then it will update the pre-existing record.

- Any field that are left blank they will not be updated in Spectrum.

- The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- If the Reference_Num is defined along with the Company_Code, Job_Number, and Category and the unique combination of those fields are valid then it will update the pre-existing record.

- Any field that are left blank they will not be updated in Spectrum.

- The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- If the Reference_Num is defined along with the Company_Code, Job_Number, and Category and the unique combination of those fields does not exist then a new entry is created using the defined Reference_Num.

- If the defined 'Category' in the record has a default value defined and the information is not valid then the default value will be used.

- If there is no default value defined then the field will be left blank.

- No error will be returned to the user.

- The following fields are validated against the defined Spectrum Project Management Tables.

- Classification

- Phase

- Building

- Area

- Once the Record is entered into Spectrum the user will receive a Response message defining the following:

- TransactionId for their records that is stored in their system and is used as a selection criteria if known.

- If duplicate records exist to be updated, then they will all be updated as they are processed.

- External_Link and External_Id field logic

- These fields are used to define if a third party web connection is being used.

- External_Link = states if a web address is defined in the field. This is a yes or no field.

- External_Id = stores the complete web address such as http://www.msn.com

- The defined Web URL (External_Id) controls how the information is opened in Spectrum. If it is defined then it uses the Spectrum Web link logic.

- If the External_Id is defined then External_Link will be Y(es).

- External_Id and External_Link fields DO NOT display on the Project Log detail tab screen.

- Project Logs tied to an External_Id URL will be opened using the defined URL and can't be viewed within Spectrum.

- Issued_Date and Resp_Req_Date field logic

- If the Job has a defined Default Project Log for the Days to Respond then this field will be calculated when the new entry is made.

- The Resp_Req_Date is only calculated if the default exists for the Job and Category.

- If the Issue_Date is blank, it uses the system date and will calculate the Resp_Req_Date as well if the Job has defaults defined.

- The Resp_Req_Date is not calculated if the Entry is being changed.

- This Web Service will work with the defined Workflow process in Spectrum.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
B
Company_CodeCompany CodeText3Can default from Authorization IdValid Company in Spectrum. Defaults from the Authorization ID if not populated.
C
Job_NumberJob codeYESText10Valid Job in Spectrum
D
TransactionIdProject Log IDText36TransactionId is created within Spectrum when the project log is added. If defined then the record will be updated.Validates to the Project Log entry.
E
CategoryCategoryText30Validates to the Project Management Category Maintenance
F
Reference_NumNumberText10Reference_Num is created within Spectrum when the project log is added. ** If defined and the Company_Code, Job_Number and Category is unique the record will be updated otherwise creates a new entry.Validates to the Project Log entry.
G
TopicTopicText250
H
Issued_DateIssued dateDate10Enter as: MM/DD/CCYY (for example, 01/05/2010) If left blank it will use the current date.
I
Resp_Req_DateRespond byDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
J
Answered_DateAnsweredDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
K
Cost_ImpactCost impact?Text1(Y)es or (N)o or blank field
L
Schedule_ImpactSchedule impact?Text1(Y)es or (N)o or blank field
M
StatusClosed?Text1(O)pen or (C )losed
N
ActivityActivity flag?Text1(A)cton needed, (I)nformation or (T)racking
O
PriorityPriority flag?Text1(H)igh, (M)edium or (L)ow
P
ClassificationDisciplineText50Validates to the Project Management Classification Maintenance
Q
Spec_SectionSpec SectionText30
R
PhasePhaseText20No dashesValidates to the Job Phase
S
BuildingBuildingText10Validates to the Project Management Building / Area Maintenance
T
AreaAreaText10Validates to the Project Management Building / Area Maintenance
U
ResponsibilityResponsibilityText250
V
ReferenceReferenceText250
W
Sent_viaSent viaText50
X
DirectionDirectionText1(I)nbound or (O)utbound or blank
Y
Email_DateE-mail dateDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
Z
WeatherWeatherText250
AA
AM_TemperatureAM TemperatureText6
AB
PM_TemperaturePM TemperatureText6
AC
Precipitation_AmountPrecipitation AmountNumeric6Positive number only. Enter as : xx.xxx
AD
WindWindText15
AE
External_Ref1External IDText30
AF
External_Ref2Owner numberText30
AG
External_LinkAccess to External Program?Text1(Y)es or (N)o or blank field **See Assumptions and Dependencies.
AH
External_IdExternal Program's Web URLText250Used to open details using the web link logic in Spectrum.**See Assumptions and Dependencies. If defined then the External_Link = Y
AI
Authored_ByAuthored byText250
AJ
Cost_Impact_AmountCost impact amountNumeric14Allows negatives. Decimals OK
AK
Sent_To_SubmitterSent to submitterDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
AL
Required_From_SubmitterRequired from submitterDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
AM
Received_From_SubmitterReceived from submitterDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
AN
Sent_To_ApproverSent to approverDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
AO
Required_From_ApproverRequired from approverDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
AP
Received_From_ApproverReceived from approverDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
AQ
Returned_To_SubmitterReturned to submitterDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
AR
Scheduled_DeliveryScheduled deliveryDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
AS
Actual_DeliveryActual deliveryDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
AT
InspectionInspectionDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
AU
Re_InspectionReinspectionDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
AV
Scheduled_CompleteScheduled completeDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
AW
Signed_OffSigned offDate10Enter as: MM/DD/CCYY (for example, 01/05/2010)
AX
Schedule_Impact_DaysSchedule Impact daysNumeric4Allows negatives. Decimals OK
AY
Log_StatusLog StatusText30
AZ
SubsectionSubsectionText10

NOTE = Invalid data will be ignored based on the layout requirements.
