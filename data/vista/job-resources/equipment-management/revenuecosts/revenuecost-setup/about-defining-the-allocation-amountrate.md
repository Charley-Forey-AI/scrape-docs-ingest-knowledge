---
title: "About Defining The Allocation Amount/Rate | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-defining-the-allocation-amountrate"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-defining-the-allocation-amountrate"
---

# About Defining The Allocation Amount/Rate

Cost allocations can be either designated as a flat amount or
 they can be calculated based on a specified rate.
If you elect to assign a flat amount, you
 enter the desired amount in the Allocation Amt field. If you wish
 to have them calculated based on a rate, enter the rate in the Allocation
 Rate field. If the basis for calculations is revenue or costs, the rate
 will be a percent of the amount. If the basis is hours, the rate will be a dollar amount
 per hour.
Another option that may be used is to
 indicate the datatype (variable) from the Equipment master file that will be used for
 the allocation amount or rate. With this method, you use the Equip Amt Column or the
 Equip Rate Column fields to designate a specific field from the EM Equipment form from
 which the amount or rate will be pulled. Then, when the allocation is performed, the
 system uses the amount or rate indicated by that field.
Note: In order to use this feature, you must create a
 custom field in which to designate the amount and/or rate you wish to use. If you will
 be using both flat-amount allocations and rate-based allocations, you will need to
 create a field for each of these methods. To create these allocation amount/rate fields,
 you must use the VA Custom Fields Wizard, which steps you through the process of
 creating a custom (user-defined) field.
Assuming that you have set up an allocation
 for Small Tool Expenses, the following is an example of the options you might select
 when creating the user-defined fields for cost allocation amounts and/or rates:

If Allocation is to be
 an amount:
If Allocation is to be a
 rate:

Steps in Wizard
Select/Enter
Select/Enter

Form:
EMEquipment
EMEquipment

Name of Custom Field:

udSmTool
udSmTool

Type of Input:
1-Numeric
1-Numeric

Use Datatype:
bDollar
bPct or bRate

Control to Use
2-Textbox
2-Textbox

Form Label:
Small Tool Expense
Small Tool Expense

Grid Column Heading: 
 (if including in Grid)
Small Tool Exp
Small Tool Exp

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)
