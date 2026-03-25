---
title: "Job Cost Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/costs-and-contracts/job-cost-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/costs-and-contracts/job-cost-features"
---

# Job Cost Features

Vista 2021 R2 delivers on user-requested Job Cost enhancements, fixes, and other improvements.

## Support Field Ticket Approval in Field Management

You can now approve field tickets in the Field Management web application (using the Field Ticket Dashboard) and have the approval information updated to the JC Field Tickets form.
Changes made for this update are as follows:

- Added Ticket Approved By and Ticket Date Approved fields to the Info tab. These fields are display only and are only populated when a field ticket is approved in the Field Management web application.

-  The Approved By and Date Approved fields were renamed to Billing Approved By and Billing Date Approved. These display only fields are only populated when a field ticket is approved for billing in the JC Field Ticket form.

## Associate Progress Entry with Job Cost Field Tickets

You can now assign field tickets to progress entry sequences, enabling you to link related costs to specific work activity on a job, and facilitate owner billing.
 To enable this functionality, a new Field Ticket field was added to the JC Progress Entry form. When you enter a progress entry sequence, you can associate it to a field ticket for the specified job/contract; however, the field ticket must be Open. You cannot post to field tickets with a Closed, Approved, Rejected, or Billed status.
Once you post the progress entry batch, the system automatically creates an entry on the Cost Detail tab of JC Field Ticket for each material use transaction, with a Source of JC Progres.
Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to progress entry sequences for a job is only useful if the job's contract/contract item has a bill type of T&M or Both.

For more information about associating field tickets with progress entry, see [JC Progress Entry](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-progress-entry-form#ID-00019a61--en__JCProgEntry_FieldTickets). For more information about the Field Tickets feature, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## Allow Syncing Jobs to ProjectSight

If you are using the ProjectSight web application, you can now sync jobs to ProjectSight.
To enable this functionality, the JC Jobs form now includes a new Sync to ProjectSight checkbox (on the Addl Info) tab. When you select this checkbox, the system sends the selected job to the ProjectSight web application, setting it up as a Project.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
