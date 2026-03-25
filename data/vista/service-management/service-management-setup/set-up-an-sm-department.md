---
title: "Set Up an SM Department | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department"
---

# Set Up an SM Department

You must set up one or more departments that define the GL accounts for cost and revenue on a work order.
The cost accounts you define here are updated when posting work completed in SM Work Orders. The cost account updated depends on the line type and whether or not you are tracking WIP. When you bill work completed, the system then updates the appropriate revenue accounts.
Note: You must define GL accounts for all cost and revenue cost type categories, regardless of whether you will be using them or not.

1. From the main menu, select
 Service
 Management > Programs > SM
 Departments.

1. In the Department field, enter a code (numeric or alpha) to identify the department.

1. Enter a description of the department in the Description field.

1. In the Cost, Revenue, Cost WIP, and Revenue WIP sections, enter the appropriate GL accounts for each cost type category. Press F4 for a list of valid GL expense accounts.

1. In the Agreement: Revenue field, enter the GL account to use when processing periodic billings (invoices) for service agreements associated with this department. Press F4 for a list of valid GL accounts.

1. In the Agreement: Deferred Rev field, enter the GL account to use when recognizing revenue for service agreements associated with this department. Press F4 for a list of valid GL accounts.

1.  In the Misc Offset Account: Cost field, enter the GL account to use as the offset account when posting miscellaneous work completed lines associated with this department. Press F4 for a list of valid GL accounts.

1. In the
 Work Order: Deferred Rev
 field, enter a Work Order Revenue Deferral GL Account. Press F4
 for a list of valid GL accounts.

1. Save the record.

1. [Set up GL account overrides](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/set-up-override-cost--revenue-gl-accounts).

1. [Set up burden rates.](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/set-up-burden-rates)

1. [Set up override offset accounts for standard items](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/set-up-override-offset-accounts-for-standard-items).

1. [Set up override offset accounts by cost type](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/set-up-override-offset-accounts-by-cost-type).

Related information

- [SM Departments Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-departments-form)
