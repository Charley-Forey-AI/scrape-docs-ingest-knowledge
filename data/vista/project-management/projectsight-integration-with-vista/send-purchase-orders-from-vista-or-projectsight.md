---
title: "Send Purchase Orders from Vista or ProjectSight | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projectsight-integration-with-vista/send-purchase-orders-from-vista-or-projectsight"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projectsight-integration-with-vista/send-purchase-orders-from-vista-or-projectsight"
---

# Send Purchase Orders from Vista or ProjectSight

Create and send purchase orders in either Vista or ProjectSight to sync the data to the other system.
The direction of data flow between linked systems (either
 from Vista into ProjectSight, or from ProjectSight into Vista) is determined during your
 organization's initial integration setup. The direction of data flow can vary
 for different types of records. Check with your administrator to verify the
 direction of data flow for your organization for this record type.
Send Purchase Orders from ProjectSight to Vista
If your integration is set up to send data from ProjectSight to Vista, complete the following:

1. Create a purchase order in ProjectSight. The PO must have:

- At least one item

- UOM (unit of measure) that is valid in Vista

- Budget Code

Note: The integration uses the
 default tax from Vista.

1. Mark as Approved for
 Budget.ProjectSight Help: For more information about setting up POs,
 see the ProjectSight Help on
 [Creating Purchase Orders](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/Online_Help/Records/BCM/Purchase-Orders.htm#create-po).

1. In
 ProjectSight, select Send to Vista to sync the data to Vista. Only authorized users can perform
 this function.A banner displays the
 syncing status as pending, successful, or failed.
ProjectSight Help: For more information about manually syncing records, see the ProjectSight Help on [Record Syncing](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/ERP/Web-ERP-Record-Syncing.htm).

1. After the PO has successfully been sent to
 Vista, you must make any
 modifications manually in both systems.

1. To view the associated record in Vista, go to Purchase Orders > Programs > PO Purchase Orders.

Send Purchase Orders from Vista
 to ProjectSight
If your integration is set up to send data from Vista to ProjectSight, complete the following:

1. Create a purchase order in Vista. The PO must have:

- At least one item

- UM (Unit of Measure)

- Job Phase

- Cost Type

Note: Tax is calculated and
 added to the header in ProjectSight.

1. Post the purchase order.When you post a PO in Vista, the PO is created in ProjectSight.

1. After the PO has successfully been created in
 ProjectSight, you must make any
 modifications manually in both systems.

If an integrated PO is deleted, you must manually delete the
 associated PO in the other system.
Associated fields in
 Vista and ProjectSight:
Vista PO Purchase Orders Field
 NameProjectSight Purchase Orders Field
 Name
DescriptionDescription
PO #Number
VendorTo Company
Order DateDate

Vista PO Purchase Orders Field
 NameProjectSight Purchase Order Items Field
 Name
ItemItem No.
UMUOM
DescriptionDescription
Total CostUnit Price
Phase
Cost Type
Budget Code
