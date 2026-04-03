---
title: "Delete Work Order Task | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/delete-work-order-task"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/delete-work-order-task"
---

# Delete Work Order Task

Use this service to delete work tasks from work orders.
WSDL: DeleteWOTask.jws
Method: DeleteWOTask
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
Unique reference # created by programming
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
Valid WO# must exist in defined company

System_Key
Unique System Key
YES
Text
24
Must be valid Key for Work Order

Work_Task
Task Code
YES
Text
15
