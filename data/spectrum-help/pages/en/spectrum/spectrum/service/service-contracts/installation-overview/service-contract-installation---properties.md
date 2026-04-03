---
title: "Service Contract Installation - Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-contracts/installation-overview/service-contract-installation---properties"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/service-contracts/installation-overview/service-contract-installation---properties"
---

# Service Contract Installation - Properties

Use this screen to specify what information will be recorded in the new work order. These settings can be changed as needed at any time.
Fields/Buttons
Descriptions

Printing options

Use auto-sequenced service contract numbers?
Select this checkbox to to
 auto-sequence the contract code. Like when adding customer codes, when a new
 contract is added to Spectrum, the next unused number will be assigned to the
 contract, if an alternate code has not been specified by the operator.
Next contract number

Sort by labor category on work order?
This is used in the Contract Work Order Process
 update. If you select Equipment
 parts, the parts from Site File Maintenance >  Equipment will update to work order. If you select Task parts, the tasks parts
 from the New/Edit Schedule
 Visit window will update to work order.On
 the [Service Contract Visits Report](/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/maintenance-overview/service-contracts/service-contract-visits-report), the option to include equipment part or task
 part notes will default based on which option is selected in this
 field.

Suppress subtasks in work ordered for repeated tasks on a work order?
Select this checkbox to suppress
 repeated subtasks and related notes when work orders are created using Service
 Contract.
Default 'as billed' invoice G/L invoice code
Enter the G/L account code you plan to
 title "service contract revenue" (or similar name) in your Spectrum chart of
 accounts. Be sure to include this G/L account number when you enter your chart
 of accounts. Enter a G/L account code in this field even if you do not have
 general ledger module installed on your computer.The
 system will default the G/L account number entered in this field during
 Contract Type File Maintenance. There is a field in the contract type file
 for the sales G/L account code. The code designated in this field will
 default there, but may be over-written if desired, if multiple service
 contract sales G/L account codes are desired. For example, some operations
 may designate different G/L account codes for residential and commercial
 service contract revenue. If the G/L account code field in the Contract Type
 File Maintenance screen is blank, the software will use the G/L code
 specified here as a last resort.

Default Work Order dispatch status
Enter a default dispatch status for new
 work orders, or press F4 or double-click on this field to select from a list of
 applicable dispatch codes. If a dispatch code is specified in this field, all
 new work orders created from the Service Contract module will be assigned this
 status by default. When the dispatch status includes a specified work order
 status, this will also be set when the work order is created.
Default Work Order priority
Enter a default priority for new work
 orders, or press F4
 or double-click on this field to select from a list of applicable priorities.
 If a priority code is specified in this field, all new work orders created from
 the Service Contract module will be assigned this priority by default.
Work order parts list
This is used in the Contract Work Order
 Processing update. If you select Equipment parts, the parts from Service Contracts will update
 to work order. If you select Task
 parts, the task parts from the Schedule Contract Visits screen
 will update to work order.On the Service Contract Visits
 Report, the Task parts
  or Equipment
 parts option will default based on which option is selected
 in this field.
