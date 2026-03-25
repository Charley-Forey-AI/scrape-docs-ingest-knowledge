---
title: "Send Subcontracts from Vista or ProjectSight | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projectsight-integration-with-vista/send-subcontracts-from-vista-or-projectsight"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projectsight-integration-with-vista/send-subcontracts-from-vista-or-projectsight"
---

# Send Subcontracts from Vista or ProjectSight

Create and send subcontracts in either Vista or ProjectSight
 and sync the data to the other system.
The direction of data flow between linked systems (either
 from Vista into ProjectSight, or from ProjectSight into Vista) is determined during your
 organization's initial integration setup. The direction of data flow can vary
 for different types of records. Check with your administrator to verify the
 direction of data flow for your organization for this record type.
Send Subcontracts from ProjectSight to Vista
If your integration is set up to send data from ProjectSight to Vista, complete the following:

1. Create a subcontract in ProjectSight. The subcontract must
 have:

- At least one item

- UOM (unit of measure) that is valid in Vista

- Budget Code

- To
 Company that is a linked vendor from Vista

Note: Only committing contract
 types can be sent from ProjectSight to Vista.

1. Mark as Approved for
 Budget.ProjectSight Help: For more information about setting up
 subcontracts, see the ProjectSight Help on [Creating Contracts](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/Online_Help/Records/BCM/Contracts.htm).

1. In
 ProjectSight, select Send to Vista to sync the data to Vista. Only authorized users can perform
 this function.A banner displays the
 syncing status as pending, successful, or failed.
ProjectSight Help: For more information about manually syncing records, see the ProjectSight Help on [Record Syncing](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/ERP/Web-ERP-Record-Syncing.htm).

1. After the subcontract has successfully been sent
 to Vista, you must make any
 modifications manually in both systems.

1. To view the record in Vista, go to Subcontract Ledger > Programs > SL Subcontracts.

Send Subcontracts from Vista to
 ProjectSight
If your integration is set up to send data from Vista to ProjectSight, complete the following:

1. Create a subcontract in Vista. The subcontract must have:

- At least one item

- UM (Unit of Measure)

- Job Phase

- Cost Type

- Vendor that is linked to a ProjectSight company

1. Post the subcontract.When you post a subcontract in Vista, the subcontract is created in
 ProjectSight.

1. After the subcontract has successfully been
 created in ProjectSight, you must
 make any modifications manually in both systems.

If an integrated subcontract is deleted, you must manually delete
 the associated subcontract in the other system.
Associated fields in
 Vista and ProjectSight:
Vista SL Subcontracts Field
 NameProjectSight Contract Field Name
SubcontractNumber
DescriptionDescription
VendorTo Company

Vista SL Subcontracts Field
 NameProjectSight Schedule of Values Field
 Name
Item #Item No.
Phase
Cost Type
Budget Code
DescriptionDescription
UMUOM
Total CostScheduled Value
UnitsScheduled Quantity
Unit CostUnit Price
