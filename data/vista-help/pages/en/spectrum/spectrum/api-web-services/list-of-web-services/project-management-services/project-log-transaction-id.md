---
title: "Project Log Transaction ID | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/project-management-services/project-log-transaction-id"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/project-management-services/project-log-transaction-id"
---

# Project Log Transaction ID

Use this web service to return the Project Log web service details including the Transaction ID for the use with the Project Log Image web service.

## Connection Information

URL = https://<SPECTRUM-SERVER>:/projectLog/{companyCode}/{jobNumber}?category={category}&referenceNumber={referenceNumber}
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: GET
Supported formats: JSON

## Sample JSON Body

```
`[
 {
 "Company_Code": "SP2",
 "Job_Number": " 450",
 "ProjectLogTran_Id": "71AFBD9D-454E-44A0-A254-3987815C39BB",
 "Category": "ISSUE ",
 "Reference_Num": " 2",
 "Topic": "99-I am writing this memo to ... ",
 "Issue_Date": "May 4, 2026",
 "Resp_Req_Date": "May 5, 2026",
 "Answered_Date": "May 20, 2026",
 "Cost_Impact": " ",
 "Schedule_Impact": " ",
 "Status": "O",
 "Activity": "A",
 "Priority": "M",
 "Classification": "Issue",
 "Spec_Section": "?",
 "Phase": "",
 "Building": " ",
 "Area": " ",
 "Responsibility": "2-I am writing this memo to ...",
 "Reference": "3-I am writing this memo to ...",
 "Sent_via": "? ",
 "Direction": " ",
 "Email_Date": "Jun 1, 2026",
 "Weather": "4-I am writing this memo to ...",
 "AM_Temperature": "? ",
 "PM_Temperature": "? ",
 "Precipitation_Amount": 0,
 "Wind": "? ",
 "External_Ref1": "?",
 "External_Ref2": "?",
 "External_Link": "Y",
 "External_Id": "5-I am writing this memo to ...",
 "Authored_By": "6-I am writing this memo to ...",
 "Cost_Impact_Amount": 1234567890.12,
 "Sent_To_Submitter": "Jan 2, 2026",
 "Required_From_Submitter": "Jan 3, 2026",
 "Received_From_Submitter": "Jan 4, 2026",
 "Sent_To_Approver": "Jan 5, 2026",
 "Required_From_Approver": "Jan 6, 2026",
 "Received_From_Approver": "Jan 7, 2026",
 "Return_To_Submitter": "Jan 8, 2026",
 "Scheduled_Delivery": "Jan 9, 2026",
 "Actual_Delivery": "Jan 10, 2026",
 "Inspection": "Jan 11, 2026",
 "Re_Inspection": "Jan 12, 2026",
 "Scheduled_Complete": "Jan 13, 2026",
 "Signed_Off": "Jan 14, 2026",
 "Scheduled_Impact_Days": 0,
 "Log_Status": " ",
 "Subsection": " "
 }
]`
```

## Underlying File Maintenance

Prior to using the GET-Project Log Transaction ID web service, the following file maintenance areas must be completed:

- System Administration > Installation > Job Cost

- System Administration > Installation > Project Management > Project Log

- System Administration > Installation > Project Management > Category Maintenance

## Assumptions and Dependencies

- The Web Service will return the Project Log web service details including the Transaction ID for the use with the PJ Project Log Image Web Service.

- Parameter for get services will be Company Code, Job number, Category and Reference Number.

- Any field with a NULL value in the table will not be returned in the web service.

- The unique combination of the Company Code, Job number, and Category will be validated.

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.ExcelElement NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
BCompany_CodeCompany CodeText3Can default from Authorization IdValid Company in Spectrum; defaults from the Authorization ID if not populated.
CJob_NumberJob codeYESText10Valid Job in Spectrum
DTransactionIdProject Log IDText36TransactionId is created within Spectrum when the project log is added. If defined, the record will be updated.Validates to the Project Log entry.
ECategoryCategoryText30Validates to the Project Management Category Maintenance
FReference_NumNumberText10Reference_Num is created within Spectrum when the project log is added. ** If defined and the Company_Code, Job_Number and Category is unique the record will be updated otherwise creates a new entry.Validates to the Project Log entry.
GTopicTopicText250
HIssued_DateIssued dateDate10Enter as: MM/DD/CCYY (01/15/2026) If left blank it will use the current date.
IResp_Req_DateRespond byDate10Enter as: MM/DD/CCYY (01/15/2026)
JAnswered_DateAnsweredDate10Enter as: MM/DD/CCYY (01/15/2026)
KCost_ImpactCost impact?Text1(Y)es or (N)o or blank field
LSchedule_ImpactSchedule impact?Text1(Y)es or (N)o or blank field
MStatusClosed?Text1(O)pen or (C)losed
NActivityActivity flag?Text1(A)cton needed, (I)nformation or (T)racking
OPriorityPriority flag?Text1(H)igh, (M)edium or (L)ow
PClassificationDisciplineText50Validates to the Project Management Classification Maintenance
QSpec_SectionSpec SectionText30
RPhasePhaseText20No dashesValidates to the Job Phase
SBuildingBuildingText10Validates to the Project Management Building / Area Maintenance
TAreaAreaText10Validates to the Project Management Building / Area Maintenance
UResponsibilityResponsibilityText250
VReferenceReferenceText250
WSent_viaSent viaText50
XDirectionDirectionText1(I)nbound or (O)utbound or blank
YEmail_DateE-mail dateDate10Enter as: MM/DD/CCYY (01/15/2026)
ZWeatherWeatherText250
AAAM_TemperatureAM TemperatureText6
ABPM_TemperaturePM TemperatureText6
ACPrecipitation_AmountPrecipitation AmountNumeric6Positive number only. Enter as : xx.xxx
ADWindWindText15
AEExternal_Ref1External IDText30
AFExternal_Ref2Owner numberText30
AGExternal_LinkAccess to External Program?Text1(Y)es or (N)o or blank field**See Assumptions and Dependencies.
AHExternal_IdExternal Program's Web URLText250Used to open details using the web link logic in Spectrum.**See Assumptions and Dependencies. If defined, then the External_Link = Y
AIAuthored_ByAuthored byText250
AJCost_Impact_AmountCost impact amountNumeric14Allows negatives; decimals OK
AKSent_To_SubmitterSent to submitterDate10Enter as: MM/DD/CCYY (01/15/2026)
ALRequired_From_SubmitterRequired from submitterDate10Enter as: MM/DD/CCYY (01/15/2026)
AMReceived_From_SubmitterReceived from submitterDate10Enter as: MM/DD/CCYY (01/15/2026)
ANSent_To_ApproverSent to approverDate10Enter as: MM/DD/CCYY (01/15/2026)
AORequired_From_ApproverRequired from approverDate10Enter as: MM/DD/CCYY (01/15/2026)
APReceived_From_ApproverReceived from approverDate10Enter as: MM/DD/CCYY (01/15/2026)
AQReturned_To_SubmitterReturned to submitterDate10Enter as: MM/DD/CCYY (01/15/2026)
ARScheduled_DeliveryScheduled deliveryDate10Enter as: MM/DD/CCYY (01/15/2026)
ASActual_DeliveryActual deliveryDate10Enter as: MM/DD/CCYY (01/15/2026)
ATInspectionInspectionDate10Enter as: MM/DD/CCYY (01/15/2026)
AURe_InspectionReinspectionDate10Enter as: MM/DD/CCYY (01/15/2026)
AVScheduled_CompleteScheduled completeDate10Enter as: MM/DD/CCYY (01/15/2026)
AWSigned_OffSigned offDate10Enter as: MM/DD/CCYY (01/15/2026)
AXSchedule_Impact_DaysSchedule Impact daysNumeric4Allows negatives; decimals OK
AYLog_StatusLog StatusText30
AZSubsectionSubsectionText10
