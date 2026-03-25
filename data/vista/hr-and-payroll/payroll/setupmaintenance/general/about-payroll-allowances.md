---
title: "About Payroll Allowances | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances"
---

# About Payroll Allowances

Payroll allowances enable you to pay an employee additional earnings based on a set time period.
Allowances are different than add-on earnings in that they are rules-based, which enables you to create specific calculations to determine the amount that an employee is to receive for the time period. Similar to add-on earnings, allowances represent earnings that an employee can earn when working in a specific craft/class. This functionality was designed for Australian users, however United States and Canadian users may also find it useful.
Note: For United States users: For information on car/auto allowances, see [Setting Up Car/Auto Allowances](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/setting-up-carauto-allowances).
When creating an allowance, you will specify at what craft/class/template level the system will use to locate the processing rules. Once you have created the allowance, you will define the associated rules. Each allowance will be associated with a rule set, that contains the processing rules that determine the allowance amount for the employee. Rule sets can have a single rule or many rules associated with it. Once you have both the allowance and rule set created, you can then associate them with the specific craft/class/template that requires the allowance.
When processing allowances, the system does not pay attention to the craft/class template hierarchy. When processing add-on earnings, for example, the system will use the hierarchy to determine which level the rates are pulled from. With allowances, if the employee is eligible for an allowance amount at more than one level, the system will calculate an allowance amount for each applicable level they worked on for the allowance time period. For more information on the craft/class template hierarchy, see [About Crafts, Classes, and Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-crafts-classes-and-templates).
Note: Australian users can also calculate allowances using pre-defined routines. For more information, see [Earnings Based Routines: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/earnings-based-routines-australia). The preferred way to set up allowances is to create a rule set as described in this topic.
The following instructions provide an overview on how to set up payroll allowances. Click the associated links for more information on each step.

1. Create the allowance in PR Allowances. For more information, see [Create Allowances](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances/create-allowances).

1. Create the rule set and all applicable rules in PR Allowance Rule Sets. For more information, see [Create Allowance Rule Sets](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances/create-allowance-rule-sets).

1. Set up an earnings code for the allowance. For more information, see [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form).
Note: You do not have to set up a specific earnings code for the allowance, however, the system does not report based on allowance but on earnings. Therefore if you use a generic earnings code for each allowance, the system will only display a lump sum amount for earnings and you will be unable to tell which allowances contributed to the amount (PR Employee Pay Seq Control, Earnings Code tab, for example).

1. Assign the allowance, rule set, and earnings code to the appropriate craft, class, or template. For more information, click on the following links: [Assign Allowances to Crafts](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-allowances-to-crafts), [Assign Allowances to Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-allowances-to-craft-classes), [Assign Allowances to Craft Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-allowances-to-craft-templates), or [Assign Allowances to Craft Class Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-allowances-to-craft-class-templates).

1. When processing payroll, the system will determine any applicable amounts for employees. For more information, see [How the System Calculates Allowances](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances/how-the-system-calculates-allowances).
