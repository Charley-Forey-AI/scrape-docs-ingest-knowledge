---
title: "About Defining Allocation Amounts/Rates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-defining-allocation-amountsrates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-defining-allocation-amountsrates"
---

# About Defining Allocation
 Amounts/Rates

You can designate allocations as either a flat amount or
 calculated based on a specified rate.
If you elect to assign a flat amount, you'll enter the desired
 amount in the Amount To Allocate field. If you wish to have them
 calculated based on a rate, you'll enter the rate in the Allocation
 Rate field. If the basis for calculations is revenue or costs, the rate
 will be a percent of the amount. If the basis is hours, the rate will be a dollar amount
 per hour.
Another option that may be used is indicate the datatype from
 the Job file that will be used for the allocation amount or rate. With this method, you
 use the Job Amount Column or the Job Rate Column fields to designate the field in JC Jobs from which to pull the amount or rate. Then, when the allocation is performed,
 the system uses the amount or rate indicated by that field.
In order to use this feature, you must create a custom
 (user-defined) field in which to designate the amount and/or rate you wish to use. If
 you will be using both flat-amount allocations and rate-based allocations, you will need
 to create a field for each of these methods. To create these allocation amount/rate
 fields, use the VA Custom Fields Wizard form, which steps you through the process of
 creating a custom field.
Assuming that you have set up an allocation for Small Tool
 Expenses, the following is an example of the options you would select when creating the
 fields to use for cost allocation amounts and/or rates:

If Allocation is to be an amount:
If Allocation is to be a rate:

Steps in Wizard
Select/Enter
Select/Enter

Maintenance Form:
JC Jobs
JC Jobs

User Type:
User Numeric
User Numeric

Datatype:
bDollar
bPctor bRate

Column Name:
udSmTool
udSmTool

Field Label:
Small Tool Expense:
Small Tool Expense:

[](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)VA Custom Fields Wizard
