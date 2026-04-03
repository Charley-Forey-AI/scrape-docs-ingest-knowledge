---
title: "Work Order Task Maintenance - Update Material | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/work-order-task-maintenance---update-material"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/work-order-task-maintenance---update-material"
---

# Work Order Task Maintenance - Update Material

Use this service to add or update the material on the Task Maintenance in the Work Order module.
WSDL: TaskWOMaterial.jws
Method: TaskWOMaterial
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Task Work Order Maintenance-Material information, the following file maintenance areas must be completed:

- System Administration > Installation > Work Order

- System Administration > Installation > Work Order > Labor Category

- System Administration > Installation > Inventory Control

- System Administration > Installation > Inventory Control > Inventory Items Maintenance

## Assumptions and Dependencies

- The Task Work Order Maintenance-Material Web service will add or update the Material on the Task Maintenance in the Work Order module.

- The Work_Task and Item_Code must exist.

- If the Item_Quantity and Item_Cost fields are defined then the Budget_Cost value must match the calculated value if defined.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

## Field Descriptions

Use the table below for reference when using this service.
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
Work Order Task

D
Item_Code
Item code
YES
Text
15
Inventory Item Master

E
Item_Description
Description
Text
35
Used to define non-stock item's description

F
Item_Quantity
Quantity
Numeric
8
Format=5.2 and no negatives.

G
Unit_of_Measure
Unit of Measure
Text
2

H
Item_Cost
Unit Cost
Numeric
9
Format=6.2 and no negatives.

I
Budget_Cost
Budget
Numeric
9
Format=6.2 and no negatives.
If Item_Quantity and Item_Cost is defined then Budget_Cost must match calculated value if defined.
