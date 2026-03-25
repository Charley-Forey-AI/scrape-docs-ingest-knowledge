---
title: "Set Up Garnishments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-garnishments"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-garnishments"
---

# Set Up Garnishments

If you have an employee for whom you must set up a wage garnishment, you can use one of four different types of garnishments, depending on your needs.
The following is a list of four different types of garnishments that might be used, followed by instructions on how to set them up:

- Percent of Disposable Net Income

- Flat Amount

- Fixed Weekly Amount

- Percent of Gross Wages

1. Set up a Percent of Disposable Net Income garnishment. To set up a garnishment that is based on a percent of disposable net income, but is subject to the [Minimum Net Pay](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-minimum-net-pay) calculation, use a deduction that is a Rate of Net method

1. In PR Employee Dedns/Liabs, Calculations section, select the Override Standard Rate/Amount option.

1. In the Rate/Amount field, enter the percentage rate (as determined by the Garnish Group specified for the D/L code) to use in the garnishment's calculation.

1. Indicate whether the Minimum Net Pay is Based on Percent of Net Pay or Based on Amount of Net Pay and enter the appropriate value in the Percent/Amount field.The Minimum Net Pay comparison is made after the net disposable earnings times the rate has been calculated.

1. Set up a Flat Amount garnishment.To set up a garnishment that is a flat dollar amount (that is, the garnishment is a fixed amount every paycheck), but is subject to the [Minimum Net Pay](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-minimum-net-pay) calculation, use a deduction that is a Rate of Net method.

1. In PR Employee Dedns/Liabs, Calculations section, select the Override With a Fixed Amount option.

1. Indicate whether the Minimum Net Pay is Based on Percent of Net Pay or Based on Amount of Net Pay and enter the appropriate value in the Percent/Amount field.This option directs the system to use the amount entered without regard to limits; however, the Minimum Net Pay comparison is taken into account. Think of this option as a permanent calculation override

1. Set up a Fixed Weekly Amount garnishment.If you have a garnishment that is a fixed amount every week, but has an overall limit to the garnishment (e.g. a tax levy - $50/week up to $2,000), use a deduction that is an Amount method.

1. In PR Employee Dedns/Liabs, Calculations section, select the Override Standard Rate/Amount option.

1. Enter amount in the Rate/Amount field ($50)

1. Select the Override Standard Limit checkbox and enter the limit amount in the Limit field ($2,000).No Minimum Net Pay comparison is made with this option

1. Set up a Percent of Gross Wages garnishment. For garnishments that are a percent of the gross wages, but have an overall limit to the garnishment, use a deduction that is a Rate of Gross method; you will specify the earnings codes during the Deductions/Liabilities setup.

1.  In PR Employee Dedns/Liabs, Calculations section, select the Override Standard Rate/Amount option.

1. Enter an amount in the Rate/Amount field.

1.  Select the Override Standard Limit checkbox and enter the limit amount in the Limit field

1. If applicable, select the Subject to Garnishment Allocations checkbox.If you have set up Garnishment Allocations (in PR Employees, Add'l Info tab), this option identifies which employee-based deductions to include in the allocation. This feature is intended primarily for allocating child support orders. However, it can be used for other types of garnishments that need to be divided equally or proportionally. If an employee has both child support allocations and some other type of allocation, you can only set this up for one allocation type (typically child support).Note: Make sure to check this option for each child support deduction code. However, if this option is checked for a deduction, but no Withholding Limit Percentage has been specified (in PR Employees, Add'l Info), no allocations will occur.

1. If you selected the Subject to Garnishment Allocations checkbox, use the Garnishment Allocation Group field to enter the garnishment allocation group.The most typical use of this feature is to separate current child support order from arrears child support payments and to indicate the order in which to process the groups. For example, since most states require that current child support be paid before arrears payments, you might assign garnishment group #1 to each deduction code defined for current child support and garnishment group #2 to each deduction code defined for arrears child support. When the allocations are processed, all deductions in group #1 are processed first. If all allocations are satisfied and there are any remaining disposable earnings, they are distributed to the allocations in group #2.Note: The garnishment group only determines the order in which allocations flagged as 'Subject to Garnishment Allocations' are processed. It does not determine processing order in relation to all other employee-based deductions or garnishments for the employee. To ensure proper processing priority, specify a processing sequence value (see next step).

1.  To ensure proper processing priority of this garnishment, specify a value in the Processing Seq# field. The standard precedence for garnishments is as follows:

1. Tax levies (payment of federal and state back-taxes)

1. Child support orders

1. Other garnishments

1. Student loans and other federal garnishments

Note: The only time a tax levy can be processed after child support would be if the child support order was received by the employer prior to the tax levy

Related information

- [About Minimum Net Pay](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-minimum-net-pay)
