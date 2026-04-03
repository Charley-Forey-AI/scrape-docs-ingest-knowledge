---
title: "Send Subcontracts from ProjectSight Into Spectrum | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/projectsight-integration-with-spectrum/send-subcontracts-from-projectsight-into-spectrum"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/project-management/projectsight-integration-with-spectrum/send-subcontracts-from-projectsight-into-spectrum"
---

# Send Subcontracts from ProjectSight Into Spectrum

Create subcontracts in ProjectSight and send the data to Spectrum.
Before you
 can send data from ProjectSight to
 Spectrum, make sure that
 you or your administrator have identified a default G/L Account in Spectrum. ProjectSight records will be posted to
 this account. This setup is completed during the configuration of your
 integration.
Data synced from ProjectSight to Spectrum includes phase details and dollar
 amounts.

1. Create a contract in ProjectSight.

1. Fill out the
 required fields. For Type of Contract, choose
 Subcontract.

1. Make sure the Approved for
 Budget option is toggled on.

Note: Updates or edits to subcontracts will not sync
 once you have sent the record to Spectrum.

ProjectSight Help: For more information
 about setting up subcontracts, see the ProjectSight
 Help on [Creating
 Contracts](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/Online_Help/Records/BCM/Contracts.htm).

1. On the navigation toolbar in ProjectSight, select Send to Spectrum to sync the data to Spectrum. Only authorized users
 will be able to perform this function.A banner displays the
 syncing status as pending, successful, or failed.

1. View the associated record created
 in Spectrum. Go to Accounts Payable >
 Maintenance > Subcontracts.

Field mapping between ProjectSight and Spectrum:
ProjectSight Contract
 Field NameSpectrum
 Subcontract Phase Details Field Name
Number (for Create
 Contract)
Purchase Order number

To Company
Vendor

Item No.
Line Number

Description
Description

Sched Value
Orig Amount

Budget Code
Phase
Cost Type
