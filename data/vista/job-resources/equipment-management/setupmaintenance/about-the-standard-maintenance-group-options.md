---
title: "About the Standard Maintenance Group Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-standard-maintenance-group-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-standard-maintenance-group-options"
---

# About the Standard Maintenance Group Options

The Standard Maintenance Group Options section in EM Company Parameters is comprised of two checkboxes.

- Initialize all Standard Maintenance Group Items

- Always Initialize Linked Standard Maintenance Groups

These checkboxes allow you to specify how you want the system to handle standard maintenance groups when selecting equipment for initialization in [EM Work Order Initialize ](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-initialize-form).
When selecting equipment for initialization, the
 system uses the search criteria you specify, along with the Days in
 Advance, Variances in Advance, Last Done Date,
 and maintenance scheduling interval to determine whether a piece of equipment is
 eligible for initialization. However, the maintenance items and linked maintenance
 groups included in the initialization process will depend on how you set the Standard
 Maintenance Group Options.
 The following describes how the system uses these checkboxes when selecting equipment for initialization.

1. If you select both the Initialize all
 Standard Maintenance Group Items and the Always Initialize
 Linked Standard Maintenance Groups checkboxes, the system will
 initialize all standard maintenance groups that are due for maintenance, along
 with all of associated maintenance items (even if the items are not due). In
 addition, it will initialize all linked maintenance groups, regardless of whether
 they due for maintenance.

1. If you select only the Initialize all
 Standard Maintenance Group Items checkbox, the system will
 initialize all standard maintenance groups that are due for maintenance, along
 with all of associated maintenance items (even if the items are not due); however,
 it will only include linked maintenance groups if they are due for maintenance.

1. If you select only the Always Initialize
 Linked Standard Maintenance Groups checkbox, the system will
 initialize all standard maintenance groups that are due for maintenance, along
 with all of associated maintenance items that are due for maintenance (items that
 are not due will be excluded). In addition, it will initialize all linked
 maintenance groups, regardless of whether they are due for maintenance.

1. If you do not select either checkbox, the system will initialize only those maintenance groups, items, and linked maintenance groups that are due for maintenance.
Note: Regardless of how these checkboxes are set, the system will initialize maintenance groups, items, and linked maintenance groups if they are not already on an open work order.

Related information

- [About the EM Standard Maintenance Groups Form](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-standard-maintenance-groups-form)
