---
title: "Send Purchase Orders from ProjectSight Into Spectrum | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/projectsight-integration-with-spectrum/send-purchase-orders-from-projectsight-into-spectrum"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/project-management/projectsight-integration-with-spectrum/send-purchase-orders-from-projectsight-into-spectrum"
---

# Send Purchase Orders from ProjectSight Into Spectrum

Create purchase orders in ProjectSight and sync the data into Spectrum Purchase Order Entry.
Before you
 can send data from ProjectSight to
 Spectrum, make sure that
 you or your administrator have identified a default G/L Account in Spectrum. ProjectSight records will be posted to
 this account. This setup is completed during the configuration of your
 integration.

1. Create a purchase order in ProjectSight.

1. Fill out the following fields, which are
 required for the integration:

- Quantity

- UOM

- Unit
 Price

- Budget
 Code

1. Mark as Approved for
 Budget.

Note: You cannot update or edit
 POs once you have sent them into Spectrum.

ProjectSight Help: For more information about setting up POs, see the ProjectSight Help on [Creating Purchase
 Orders](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/Online_Help/Records/BCM/Purchase-Orders.htm#create-po).

1. On the navigation toolbar in ProjectSight, select Send to Spectrum to sync the data to Spectrum. Only authorized users
 will be able to perform this function.A banner displays the
 syncing status as pending, successful, or failed.

1. View the associated record created in Spectrum. Go to Purchase Order > Data Entry > Purchase Orders.

Field mapping between ProjectSight and Spectrum:ProjectSight Purchase Order Field NameSpectrum Purchase Order Entry Field
 Name
Number (for Create Purchase Order)
Purchase Order number

To Company
Vendor

Item No.
Line Number

Quantity
Quantity

UOM
Um

Item
Item Code

Unit Price
Unit Price

Budget Code
Phase
Cost Type
