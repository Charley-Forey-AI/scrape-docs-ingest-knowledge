---
title: "Project Management Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r1/project-management/project-management-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r1/project-management/project-management-features"
---

# Project Management Features

Vista 2022 R1 delivers on user-requested Project Management enhancements, fixes, and other improvements.

## Associate Purchase Orders with Job Cost Field Tickets

You can now assign Job Cost field tickets to purchase order items entered in the Project Management module, enabling you to link related costs to specific work activity on a job, and facilitate owner billing.
To enable this functionality, a Ticket field was added to the Non-Interfaced Items tab on the PM Purchase Orders form. When you enter a PO item, you can assign the item to a field ticket associated with the project's contract; however, the field ticket must have a status of Open. You cannot post to field tickets with a Closed, Approved, Rejected, or Billed status.A Ticket field was also added to the Interfaced Items tab; however, the field is display only and cannot be changed.
For more information about the Field Tickets feature, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## Updated Error Message for Cost Projections

When you open cost projections for a project that is currently in use by another user, the "Projection month and job in use by another user" error message now includes the user's login name. This error occurs as follows:

- If you selected the Load last opened Projection checkbox in PM Cost Project Options, and another user is currently using the project you last worked on, the error occurs when you open the PM Cost Projections form.

- If you are in the PM Cost Projections form and you manually enter a projection date and project being used by another user, the error occurs once you enter the project.

## Trimble Estimating Products Integration

You can now import Autobid, WinEst, and Quest export files into Vista using the new standard templates in PM Import Estimates template.
You can import and upload export files from your Trimble product using the PM VFE Auto Import form, which you can access from PM Projects or by clicking the Estimating icon  in PM Import Estimates.
For more information on auto importing estimates, see [Auto Importing Estimates from Third-Party Applications](/en/vista/vista/project-management/import-project-estimates/auto-importing-estimates-from-third-party-applications).

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
