---
title: "About GL Account Overrides | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/about-gl-account-overrides"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/about-gl-account-overrides"
---

# About GL Account Overrides

If you require a more detailed level of cost and revenue
 breakdown for GL accounting when posting work completed for a work order, you can set up
 override accounts at multiple levels in SM Departments.

## Cost & Revenue Account Overrides

Use the Overrides tab in SM Departments to define overrides for your Cost, Revenue,
 Cost WIP, and Revenue WIP accounts by call type and/or cost type. When you post work
 completed in SM Work Orders, the system updates these accounts for all work
 completed lines matching the specified call type/cost type combination using the
 following hierarchy:

1. Call Type / Cost Type

1. Cost Type

1. Call Type

If no match is found at the overrides
 level, the system uses the standard accounts defined on the Info tab (in SM
 Departments).
You can also set up Cost and Cost WIP
 overrides for Labor Burden. Selecting the Labor cost type category enables the
 Burden checkbox, allowing you to specify whether the override is
 for labor burden (selected) or labor only (not selected). If the override is for
 labor burden, the Liability field is also enabled,
 allowing you to define cost account overrides by liability type and, if applicable,
 call type and/or cost type. The system update these accounts for work completed
 lines matching the specified liability type/call type/cost type combination using
 the following hierarchy:

1. Call Type / Cost Type / Liability Type

1. Cost Type / Liability Type

1. Call Type / Liability Type

1. Liability Type

1. Call Type / Cost Type

1. Cost Type

1. Call Type

If no match is found at the overrides
 level, the system uses the standard burden Cost or WIP accounts defined on the Info
 tab (in SM Departments).

## Standard Item Offset Account Overrides

Use the Standard Items tab to define override offset GL accounts by standard item.
 These accounts override the standard miscellaneous cost offset account defined for
 the department (on the Info tab), and are used when the miscellaneous work completed
 line references a standard item. When the work completed line is posted, the system
 checks to see if an override account exists for the standard item, and if so,
 creates one offsetting cost entry to GL using that account. If an override account
 is not found, the system uses the offset account defined for the department.

## Cost Type Offset Account Overrides

Use the Cost Types tab to define override offset GL accounts by SM cost type. These
 accounts override the standard miscellaneous cost offset account defined for the
 department (on the Info tab), and are used when a work completed miscellaneous line
 or an inventory line for a non-stocked material references an SM cost type. When the
 work completed miscellaneous or inventory line is posted, the system checks to see
 if an override account exists for the SM cost type. If one exists, the system
 creates one offsetting cost entry to GL using that account. If no override account
 is found, the system uses the offset account defined for the department.

Related concepts

- [About GL Update Hierarchy](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/about-gl-account-overrides/about-gl-update-hierarchy)

Related tasks

- [Set up Override Cost & Revenue GL Accounts](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/set-up-override-cost--revenue-gl-accounts)

- [Set up Override Offset Accounts for Standard Items](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/set-up-override-offset-accounts-for-standard-items)

- [Set up Override Offset Accounts by Cost Type](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/set-up-override-offset-accounts-by-cost-type)

Related information

- [Set up Override Cost & Revenue GL Accounts](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/set-up-override-cost--revenue-gl-accounts)

- [SM Departments Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-departments-form)
