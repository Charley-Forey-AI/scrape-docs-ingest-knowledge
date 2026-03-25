---
title: "About Linked Groups | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-linked-groups"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-linked-groups"
---

# About Linked Groups

This tab allows you to link maintenance groups together.
You will typically use this feature when one
 maintenance group should always include additional maintenance groups. For example, you
 have a piece of equipment that you service at 250, 500, and 1,000 hours. At 500 hours,
 the service includes the items performed at the 250-hour service plus some additional
 items, and the 1,000-hour service includes the items performed at the 250- and 500-hour
 services, plus some additional items. You will set up the items for the 250- and
 500-hour service once and link them to the other service levels.
EquipmentStd Maint GroupLinked Maint
 Group
101011 (250-hour
 service)—
101012 (500-hour
 service)1 (250-hour
 service)
10101  3 (1,000-hour
 service)  2 (250-hour service) 1
 (500-hour service)

When selecting equipment for work order generation
 in EM Work Order Initialize, the system initializes maintenance groups based on the
 selection criteria, and the specified days and variances in advance. In addition, how
 you set the Always Initialize Linked Standard Maintenance Groups checkbox in EM
 Company Parameters determines whether the system will include / exclude linked
 maintenance groups during initialization if they are not due. For more information, see
 [About the Standard Maintenance Group Options](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-standard-maintenance-group-options).
