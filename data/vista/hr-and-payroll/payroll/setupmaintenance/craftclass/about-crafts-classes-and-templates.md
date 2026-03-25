---
title: "About Crafts, Classes, and Templates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-crafts-classes-and-templates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-crafts-classes-and-templates"
---

# About Crafts, Classes, and Templates

You can use crafts and classes to establish pay rates, deductions, and liabilities that can cover many employees.
For union contractors, a craft is the equivalent to a union. There should be one craft set up in the system for each union that requires separate reporting. A class is equivalent to the classification of employees within a union (for example, Journeyman, Foreman, Apprentice level 1, etc.). The pay rates for craft employees are determined by the settings for the class.
Note: For non-union contractors, crafts and classes may still be used to establish standard pay rates, deductions, and liabilities, although they will not be required.
While crafts and classes apply to many employees, you may find that you need to tailor craft/class information for a specific job. In this case, you can create a template for the craft or class and use that template to override the standard pay rates, deductions, and/or liabilities. There are two types of templates, craft templates and craft class templates.
The system uses a hierarchy to determine which rates to use for a specific employee. The following details that hierarchy:

- Crafts - This is the lowest level of the hierarchy
 and the most generic. You can assign specific deductions/liabilities to the
 craft, if necessary. You can also specify additional earnings (add-on earnings)
 that employees receive when working for this craft. The system will apply these
 add on earnings and deduction/liabilities (to an employee with subject
 earnings), in addition to any other deduction/liabilities that the employee is
 subject to. To associate employees with a craft, you must specify the craft
 number in PR Employees (Craft field). For more
 information, see [Setting Up Crafts](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-crafts).

- Craft Classes - This is the next level of the
 hierarchy and allows you to specify a specific pay rate for a class, as well as
 any add-on earnings or deduction/liability overrides to the craft level. If you
 do not specify a pay rate for the class, the system uses the standard pay rate
 for the employee in PR Employees (Standard Pay section, Add'l Info tab). If you
 do not specify any add-on earnings or deduction/liability overrides here, the
 system uses the settings at the craft level. To associate employees with a
 class, you must specify the class in PR Employees (Class field). For more information, see [Setting Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes).

- Craft Templates - You can use craft templates to override selected craft information for specific jobs. The system will apply any add-on earnings or deductions/liabilities to an employee with subject earnings when the timecard references the job associated with the template. If you do not specify any add-on earnings or deduction/liability overrides here, the system uses the settings at the craft class level. For more information, see [Setting Up Craft Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-templates).

- Craft Class Templates - This is the highest level of the hierarchy. You can use craft class templates to override pay rates, add-on earnings, and deductions/liabilities for a craft class associated with a specific job. The system will apply any add-on earnings or deductions/liabilities to an employee with subject earnings when the timecard references the job associated with the craft template. For more information, see [Setting Up Craft Class Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-class-templates).

You can also use crafts and classes to determine rates for prevailing wage jobs. For more information, see [Setting Capped Codes and Limits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-capped-codes-and-limits).
