---
title: "Add Work Order Task | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/add-work-order-task"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/add-work-order-task"
---

# Add Work Order Task

Use this service to add work tasks to existing work orders.
WSDL: AddWOTask.jws
Method: AddWOTask
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Field Descriptions

Use the table below for reference when using this service.
Element Name
Description
Req?
Type
Max
Format
Validation

Authorization_ID
Authorization ID to access the server
YES
Text
20
Data Exchange Installation screen

GUID
Unique reference number created by programming
Text
36
** See GUID definition

Company_Code
Company Code
YES
Text
3
Valid company in Spectrum

WO_Number
Work Order Number
YES
Text
10
Valid WO# must exist in the defined company

Work_Task
Task Code
YES
Text
15
Valid task code must exist in the defined company

System_ID
Site Equipment Code
Text
8
Valid equipment code for site must exist in the defined company

Task_Price
Sell Price
Num
13
Negative number allowed: Format = -10.2
If Price Type of Task is T+M, then do not import Task_Price

Quantity
Quantity
YES
Num
3
Format = 3
Must be positive number (non-zero)
