---
title: "About Garnishment Allocations | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-garnishment-allocations"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-garnishment-allocations"
---

# About Garnishment Allocations

The Garnishment Allocations section in PR Employees (Add'l Info tab), allows you to properly distribute disposable income among garnishment deductions when the total amount of all deductions exceeds the available amount of disposable income.
Although this feature was designed primarily for child support allocations, it can be used for any other types of allocations that need to be prorated or divided equally.
If an employee has multiple child support orders and the total support exceeds the disposable income limit, the state in which the employee works determines how the available income is to be allocated amongst the various child support deductions. Most states rule that support amounts will be prorated, though a few prefer to divide the disposable income equally among the support orders. Many states also distinguish current support orders from arrears and require that the payment of any current support takes priority over arrears payments.

## Setting up Garnishment Allocations

First, you must specify the method to use for allocating garnishments. If you will be dividing allocations proportionally, select the Prorate option. If allocated amounts should be divided equally, select the Divide Equally option.
Next, specify the Withholding Limit Percentage, which indicates the maximum percentage of disposable earnings allowed for garnishment. For example, if you are setting up allocations for child support, this value typically represents the limit set by the federal government. However, many states have set their own limits, which is allowable as long as they do not exceed the federal limit.
Note: If you do not specify a value here, no allocations will occur.

Finally, you must specify the garnishment group (set up in PR Garnish Groups) that will be used to calculate the disposable income. Make sure the garnishment group is properly set up with all applicable deductions and liabilities.
Once you have set up Garnishment criteria, you must then select the Subject to Garnishment Allocations checkbox for each applicable deduction in PR Employee Dedns/Liabs. However, it is important to note that you can only use this feature with one type of allocation at a time. For example, if an employee has both child support allocations and another type of allocation (e.g. tax levies), you would typically set up the garnishment allocations for the child support here, then check the Subject to Garnishment Allocations option for each child support deduction code in PR Employee Dedns/Liabs.
You also need to make sure you have correctly assigned a processing sequence to the employee deductions to ensure proper priority when the deductions are processed.
For more information about the 'subject to garnishment allocations' and 'processing sequence' for employee deductions, see Dedns/Liabs in Related Topics below.

For examples of garnishment calculations, see .[Garnishment Calculations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-garnishment-allocations/garnishment-calculations).

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [Garnishment Calculations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-garnishment-allocations/garnishment-calculations)
