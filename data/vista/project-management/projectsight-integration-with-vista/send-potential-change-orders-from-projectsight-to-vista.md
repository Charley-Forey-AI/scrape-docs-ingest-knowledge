---
title: "Send Potential Change Orders from ProjectSight to Vista | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projectsight-integration-with-vista/send-potential-change-orders-from-projectsight-to-vista"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projectsight-integration-with-vista/send-potential-change-orders-from-projectsight-to-vista"
---

# Send Potential Change Orders from ProjectSight to Vista

Create and send potential change orders from ProjectSight to Vista PM Pending Change Orders and JC Change Orders.

1. Create a potential change order in ProjectSight. Potential change order
 items must have:

- Budget Applied Amount

- Budget Code

- Allocation

ProjectSight Help: For more information about creating new
 potential change orders in ProjectSight, see the ProjectSight Help: [Create Potential Change
 Orders](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/Online_Help/Records/BCM/Potential-Change-Orders.htm?#create-pco).

1. In
 ProjectSight, select Send to Vista to sync the data to Vista. Only authorized users can perform
 this function.A banner displays the
 syncing status as pending, successful, or failed.
ProjectSight Help: For more information about manually syncing records, see the ProjectSight Help on [Record Syncing](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/ERP/Web-ERP-Record-Syncing.htm).
Based on the allocation value you enter in ProjectSight, the following records
 are created in Vista:Allocation Value Entered in
 ProjectSightResulting Vista Record
 Created
Apprx RevPM Pending Change
 Orders
Pend RevPM Pending Change
 Orders
Appr RevJC Change Orders
 (Internal)
No AllocNo record created - ignored by
 integration
CancelledNo record created - ignored by
 integration

1. Make updates to the potential change order in
 ProjectSight. These changes
 will sync to the associated Vista
 records. Do not modify these records in Vista.

1. To view the records in Vista, go to either:

- Project
 Management > Programs > PM Pending Change
 Orders

- Job Cost > Programs > JC Change
 Orders
