---
title: "Add Work Order Task Maintenance | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/add-work-order-task-maintenance"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/add-work-order-task-maintenance"
---

# Add Work Order Task Maintenance

Use this service to create work tasks in the Work Order module.
WSDL: TaskWO.jws
Method: TaskWOAdd
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Task Work Order Maintenance information, the following file maintenance areas must be completed:

- System Administration > Installation > Work Order

- System Administration > Installation > Work Order > Labor Category

## Assumptions and Dependencies

- The Task Work Order Maintenance Web service will create the Task Maintenance in the Work Order module. This is an add only Web Service.

- The Work Task cannot already exist.

- The Price_Method is required if the Flat_Rate is marked as Y(es).

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the
 Spectrum Excel Office Add-in templates for data entry points.
Excel
Field Name
Description
Req
Type
Max
Format
Validation

B
Company_Code
Company Code
YES
Text
3
Valid company in Spectrum

C
Work_Task
Work Task
YES
Text
15
no duplicates
Work Order Task

D
Task_Description
Description
YES
Text
40

E
Flat_Rate
Flat Rate?
Text
1
Y=checked or N=cleared/blank

F
Recalculate_Task
Recalculate components?
Text
1
Y=checked or N=cleared/blank

G
Price_Method
Price Method
Text
1
C=use flat subtask cost P=use flat subtask price
Required if Flat Rate? is Yes.

H
Labor_Category
Labor Category
Text
10
Work Order Labor Category

I
Task_Notes
Notes
Text
100
