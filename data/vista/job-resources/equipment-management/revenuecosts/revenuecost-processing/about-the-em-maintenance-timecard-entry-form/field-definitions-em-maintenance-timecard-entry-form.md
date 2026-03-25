---
title: "Field Definitions: EM Maintenance Timecard Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-maintenance-timecard-entry-form/field-definitions-em-maintenance-timecard-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-maintenance-timecard-entry-form/field-definitions-em-maintenance-timecard-entry-form"
---

# Field Definitions: EM Maintenance Timecard Entry Form

The following is a list of field descriptions for the EM
 Maintenance Timecard Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq #

 Enter the sequence number of an existing entry or enter N, New, or + to add a new sequence. The system will automatically assign the next available sequential number.

## Action

The Action drop-down on multiple forms throughout Vista.
When entering new records, this field defaults to A (Add) and cannot be accessed.
For existing records, select the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all related module files. (The delete functions in the toolbar and Records menu only delete the entry from the batch.

##  PR Co

 Specify the PR company (from PR Company Parameters) of the employee to which this time card entry applies.

##  Employee

 Specify the employee (from PR Employees) who performed maintenance work on the equipment.

##  Date

 Specify the posting date for this transaction.

## EM Type

Specify the transaction type. EM type determines what fields are displayed for input.

- Equip-Equipment. Select this option for work performed on equipment that is not on a work order.

- ·WO-Work Order. Select this option for work performed on equipment that is on a specific work order.

##  Equipment

 This field is only accessible if EM Type is ‘Equip-Equipment’.
 Specify the piece of equipment (from EM Equipment) on which the maintenance work was performed.

## Component Type

This field is only accessible if EM Type is ‘Equip-Equipment’ and you have checked the Post Costs to Components flag for the equipment (in EM Equipment).
If this timecard is for maintenance performed on a component of the equipment, specify the component’s type here.

##  Component

 This field is only accessible if EM Type is ‘Equip-Equipment’ and you have checked the Post Costs to Components flag for the equipment (in EM Equipment).
 If this timecard is for maintenance performed on a component of the equipment, specify the component here. Component must be valid for the specified component type and be set up for the equipment (in EM Equipment). Initially defaults the component first component of the specified component type.

##  Work Order

 This field is only accessible if EM Type is ‘Equip-Equipment’.
 Specify the work order (EM Work Orders) to which this timecard entry applies.

##  WO Item

 This field is only accessible if EM Type is ‘Equip-Equipment’.
 Specify the work order item to which the timecard entry applies.

##  Cost Code

 This field is only accessible if you have specified to allow changes to cost codes when posting labor costs (flag in EM Company Parameters (Info tab).
 Specify the cost code to which you are posting labor costs. If an ‘Equipment’ transaction and you specified a component type/component, defaults the cost code designated for the component type (in EM Component Types). If a ‘Work Order’ transaction, defaults the cost code specified on the work order.

##  Hours

 Specify the number of hours it took to complete the maintenance work on the piece of equipment.
