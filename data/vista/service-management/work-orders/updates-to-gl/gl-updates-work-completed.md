---
title: "GL Updates: Work Completed | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed"
---

# GL Updates: Work Completed

The system creates entries in General Ledger each time you
 post and invoice work completed lines. The following discusses how the system determines the
 GL accounts to update and when they are updated.
When you post a work completed line, the system determines the transaction GL account to update based on the line type, the cost type category associated with the work completed line, and the cost accounts defined for cost type categories in SM Departments.
 If you selected the Track WIP checkbox for a call type (in SM Call Types), the system uses the Cost WIP account. If you are not tracking WIP, the Cost accounts are used instead. Overrides defined by call type and/or cost type (Overrides tab in SM Departments) are used whenever the work completed line references that call type and/or cost type. Overrides defined by liability type (Overrides tab) will be used whenever a work completed labor line is associated with the specified liability type.
In addition to the transaction GL account, the system also updates an offset account for each work completed line. These offset accounts are determined as follows:

- Equipment- Uses revenue code GL account from EM Departments.

- Labor - Uses SM Applied Earnings/SM
 Applied Burden GL accounts from PR Departments.

- Miscellaneous - Uses the offset GL account defined for the standard item in SM Departments (Standard Items tab), the offset GL account specified for the cost type (in SM Departments, Cost Type tab) if no override account is found for the standard item or no standard item is specified, or the miscellaneous offset account defined for the department (in SM Departments, Info tab) if no override account is found for the standard item or cost type, or the work completed line does not reference a standard item or a cost type.

- Inventory (Stocked Materials only) - Uses Inventory GL account
 from IN Location Category Override or IN Locations.

- Inventory (non-stocked and non-standard materials) - Uses the offset GL account defined for the cost type in SM Departments (Cost Types tab) or the miscellaneous offset account defined for the department (in SM Departments, Info tab) if no override account is defined for the cost type or no cost type is specified for work completed line.

- Purchase - Uses Accrual GL account from PO Company Parameters.

Note: If the work complete line (of any type) is on a job work
 order, the system will also create additional entries to the GL account defined for the
 phase or cost type in JC Departments for the job's department, as well as the Revenue or
 Revenue WIP account (if tracking WIP) specified for the work completed line.
Once you invoice a work completed line, the system updates the revenue amount to GL using the Revenue or Revenue WIP account for the line's cost type category. The offset account is determined by the receivable type specified on the invoice.
Job-related work orders are not invoiced using SM Invoice Review, rather, they are invoiced via Job Billing or Accounts Receivable. GL updates are handled using the accounts specified in those modules.

## Changes to Posted Work Completed Lines

If you make changes to a posted work completed line that affect the cost or the GL accounts, the system will create and post a batch, updating the related module and GL accounts accordingly. However, this will only occur if you change any of the following information:

- Post Month

- GL Co

- Cost or Cost WIP Accounts

- Cost Total

- Inventory Location, Material, or Qty (Inventory lines for stocked materials only)

- EM Co, Equipment, Revenue Code, Hours (Equipment lines)

- Billable Total (Job Work Orders only)

Any other changes made to a work completed line will be saved, but no batch will be created.

Related concepts

- [GL Updates: Work Completed Equipment](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-equipment)

- [GL Updates: Work Completed Labor](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-labor)

- [GL Updates: Work Completed Miscellaneous](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-miscellaneous)

- [GL Updates: Work Completed Inventory for Stocked Materials](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-inventory-for-stocked-materials)

- [GL Updates: Work Completed Inventory for Non-Stocked Materials](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-inventory-for-non-stocked-materials)

- [GL Updates: Work Completed Purchase](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-purchase)
