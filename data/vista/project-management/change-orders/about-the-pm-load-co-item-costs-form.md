---
title: "About the PM Load CO Item Costs Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/about-the-pm-load-co-item-costs-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/about-the-pm-load-co-item-costs-form"
---

# About the PM Load CO Item Costs Form

Use this form to load actual units, hours, and costs from JCCD (Cost Detail) into your change order item phases/cost types.
You can open this form by:

- Selecting Load PCO Item Costs from the
 Task drop down on [PM Pending Change Orders](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)

- Selecting Load ACO Item Costs from the
 Tasks drop down on [PM Approved Change Orders](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)

In order to use this feature, phases and cost types
 must already be set up for the change order item
 into which costs will be loaded. Phases/cost types
 can be added manually or using the Generate Detail
 function, which will initialize phases/cost types
 with zero values.
You can specify a beginning/ending month range
 and/or actual date range by which to restrict the
 JC detail transactions that will be used when
 accumulating phase cost type totals. You can also
 leave criteria blank if you want to include all
 months and/or dates.
The Replace Existing Values option allows you to
 update units, hours, and costs already defined for
 phases/cost types with accumulated values from
 JCCD. If this option is left unchecked, only
 phases/cost types with zero amounts will be
 updated; phases/cost types with existing amounts
 will be left intact.
Once you have entered your criteria, click the
 Update button. The update process will cycle
 through each phase/cost type for the change order
 item and:

- sum the actual units, hours, and costs from JCCD for the phase/cost type
 using the month and date ranges. If the actual
 units, hours, and costs are zero, will skip to the
 next phase cost type;

- check for existing units, hours, or costs. If they exist and the 'Replace
 existing values' option is unchecked, the
 phase/cost type will be skipped;

- set units to zero for each phase/cost type with a LS unit of measure.

If an error occurs during the process for a
 phase/cost type, the update process will end;
 however, any actual values loaded for previous
 phases/cost types will be left intact.
If the item is a pending change order item, the
 pending amount will be calculated once the update
 process is complete.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change
 Orders
[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change
 Orders
