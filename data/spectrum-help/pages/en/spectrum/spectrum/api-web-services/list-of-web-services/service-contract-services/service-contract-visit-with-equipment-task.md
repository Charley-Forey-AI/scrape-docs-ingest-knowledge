---
title: "Service Contract Visit with Equipment Task | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/service-contract-services/service-contract-visit-with-equipment-task"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/service-contract-services/service-contract-visit-with-equipment-task"
---

# Service Contract Visit with Equipment Task

Use this service to add new Visits with equipment tasks if needed to the Service Contract.

## Connection information for POST

URL = https://<SPECTRUM-SERVER>:8482/serviceContract/Visit
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "serviceContractVisits": [
 {
 "Company_Code": "md2",
 "Site_ID": "mld",
 "Contract_Number": "woequip",
 "Visit_Date": "12/17/2025",
 "Work_Summary": "Testing insert 2",
 "Budget_Hours": "2",
 "Budget_Cost": "100.00",
 "Preupdate_Alert": "This is my alert test 12/18",
 "SC_Visit_Notes": "Here are my visit notes",
 "Visit_Tasks": [
 {
 "Equipment": "stuff",
 "Task": "lll1",
 "Task_Unit_Price": "25",
 "Quantity": "1",
 "SC_Equip_Task_Notes": "Here are some task notes"
 },
 {
 "Equipment": "",
 "Task": "",
 "Task_Unit_Price": "",
 "Quantity": "",
 "SC_Equip_Task_Notes": ""
 }
 ]
 }
 ]
}`
```

## Underlying File Maintenance

Prior to importing Service Contract Visits information, the following file maintenance areas must be completed:

- System Administration > Installation > Service Contract

- System Administration > Installation > Service Contract > Service Contract

- System Administration > Installation > Work Order > Site ID

## Assumptions and Dependencies

- The web service will add new Visits with equipment tasks if needed to the Service Contract.

- A Valid combination of Site_ID and Contract_Number must exist to add the data.

- To add multiple pieces of Equipment to the Visit then the following fields must match:

- Company_Code

- Site_ID

- Contract_Number

- Visit_Date

- Work_Summary

- Budget_Hours

- Budget_Cost

- The number of scheduled visits shown on the header record will be managed within the Web service logic so that is is correct with existing dates and newly added.

- The Equipment must be valid as a covered equipment for the service contract and exist on the work order site.

- If multiple visits on the same date exist, then the Equipment will be applied to the first available date.

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.
Excel
Element Name
Description
Req?
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
YES
 Text
3
 Valid Company in Spectrum

C
Site_ID
Site
YES
Text
10
Valid combination of Site_ID and Contract_Number.
Work Order Site

D
Contract_Number
Contract
YES
 Text
10
Valid combination of Site_ID and Contract_Number if changing information
Service Contract

E
Visit_Date
Scheduled Date
 Date
8
 Format: MMDDYYYY. Must be within the min/max processing dates.

F
Work_Summary
Work Summary
Text
 250

G
Budget_Hours
Budget Hours
Numeric
12
Format: 9.2 positive numbers only

H
Budget_Cost
Budget Cost
Numeric
12
Format: 9.2 positive numbers only

I
Preupdate_Alert
Pre-update alert
Text
250

J
SC_Visit_Notes
Visit Notes
Text
1000

K
Equipment
Equipment Code
Text
 8
Valid Covered Equipment on Service Contract and Site.

L
Task
Task
Text
15
Valid Work Order Task

M
Task_Unit_Price
Price per unit
 Numeric
12
Format: 9.2 positive numbers only

N
Quantity
Quantity
Numeric
12
Format: 9.2 positive numbers only
Defaults to 1 if blank.

O
SC_Equip_Task_Notes
Equipment Task Visit Notes
Text
1000
