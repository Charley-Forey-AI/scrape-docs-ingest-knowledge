---
title: "Set up Override Offset Accounts by Cost Type | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/set-up-override-offset-accounts-by-cost-type"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/set-up-override-offset-accounts-by-cost-type"
---

# Set up Override Offset Accounts by Cost Type

If you require separate offset cost accounts based on SM cost type, you can set up override offset accounts by cost type for each department in SM Departments.
When you post miscellaneous work completed lines or work completed inventory lines for non-stocked materials that reference an SM cost type, the system adds an offsetting cost entry to GL using the override account defined for the specified cost type. If no override offset is found for the cost type, the system uses the standard offset account defined for the department.
Note: For work completed miscellaneous lines that reference both a standard item and an SM cost type, the standard item override account is used instead of the cost type override account. The system will only use the cost type override account if the standard item does not have an override account defined.Service Management > Programs > SM Departments > Standard Items

1. From the main menu,
 select Service Management > Programs > SM
 Departments.

1. In the Department field, enter the department to work with.

1. Click on the Cost Types tab.

1. In the Seq
 field, enter + to add
 a new record.

1. In the Cost
 Type field, enter the SM cost type or press F4
 to select from a list of valid SM cost types.

1. In the Misc Offset GL
 Acct field, enter the GL account to use for offsetting GL
 entries. Press F4 to select from a list of
 valid GL accounts.

Related information

- [SM Departments Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-departments-form)
