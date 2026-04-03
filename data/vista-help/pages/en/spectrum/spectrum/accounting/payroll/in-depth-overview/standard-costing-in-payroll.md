---
title: "Standard Costing in Payroll | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/standard-costing-in-payroll"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/standard-costing-in-payroll"
---

# Standard Costing in Payroll

Contractors who self‐perform work as well as those who
 engage in substantiated / cost plus projects may use the concept of 'standard labor costs'
 when managing their jobs. Instead of charging the employee's actual costs and burdens to the
 job, a fully burdened labor rate is used.
While this rate charged out will be different based on different types of activities, the
 employee is still paid their "normal" actual rate.
As with contractors that use standard cost for inventory items, use of standard labor rates is a company philosophy on how to run their business. Contractors use standard cost payroll because it allows the PM to manage labor based on hours used without worrying about the price of that labor. As the standard labor costs are the same used to develop the estimate, there are no costing variances to worry about. When the PM does not have the ability to control the mix of laborers working on his project, standard labor rates removes having to worry about the "more expensive" employees.
Standard costing can also be used to obscure the employee's true pay rate in Job Cost.

## Key Terms

- Actual
 Costs – These are the true costs of the employee including actual
 labor costs and all burdens.

- Standard
 Costs – These are the costs of the employee valued using the Standard
 Labor Rate.

- Standard Labor
 Rate – Also known as the Fully Burdened Rate. Typically, this is the
 rate that was used to estimate the labor portion of the project.

## Setup and Configuration

## Payroll Installation

Navigate to the [Payroll Installation - Defaults](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults) screen. Select the checkbox titled Post to Job Cost using standard labor rates? to enable the standard labor cost functionality.

## Payroll Department File Maintenance

As an implementation strategy, use only non‐direct G/L codes on the [New/Edit Department - Employer Expense](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/department-expense-maintenance/newedit-department---employer-expense) tab to charge tax and burden expenses. These amounts are already part of the standard labor rate so including would only overcharge the job.
Once Payroll has been configured to use standard costing, select the Post with standard rates? checkbox on the [New/Edit Department - Direct Cost](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/department-expense-maintenance/newedit-department---direct-cost) tab on and two additional fields will appear:

- Standard cost
 variance (Non‐direct) This code is used record the offset to the
 direct cost adjustment. It must be a non‐direct G/L code. This is a required field
 when available.

- Direct cost
 adjustment (Direct Job Cost) This code is used to adjust direct labor
 to standard. It must be a direct job cost G/L code. This is a required field when
 available.

##  Power User Tips

- The Payroll Department controls whether labor posted to Job Cost
 uses standard labor rates. This means that two Payroll Departments will be used when
 there is a mix of employees who charge to the job using actual costs and standard
 costs.

- While the Direct cost adjustment code can be the same as the
 Salary and Wages G/L code, it can also be a different account. The rationale for
 doing this is that it offers a way to see "actual" payroll costs within the G/L.

- The system calculates the standard cost for all pay types except
 Retro Pay (RP) and Equipment Usage (EU). With Retro Pay, the job has already been
 charged the standard rate, so no additional charges are needed.

## Wage Code Maintenance

The standard labor rate is stored by wage code in the 'Standard job rates' fields. These rates are only used when the Payroll Department is set to charge the job using standard rates.
Important: Standard job rates are not date sensitive.
 While wage code rates paid to the employee are date sensitive, standard labor rates
 are not. Standard job rates of zero are allowed. For maximum flexibility, the
 standard rate of zero can be used. In the event that the user forgot to enter a
 standard rate, the rate of zero will be charged to Job Cost.

## Job Payroll Setup

## Payroll Burden

By rule, no burden will be charged to the job when standard costs are used. The job's burden rules will continue to apply for employees charged with actual costs however.

## Payroll Overhead

The treatment of payroll overhead is different. The system will apply payroll overhead when defined on the job.
Important: The percentage method is based on the actual cost of
 labor plus all burdens. Regardless of whether the job uses actual or standard costs, the
 fully burdened actual cost is used as the basis of the calculation.
