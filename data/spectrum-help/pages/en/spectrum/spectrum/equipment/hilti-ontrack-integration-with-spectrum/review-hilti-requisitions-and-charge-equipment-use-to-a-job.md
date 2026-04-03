---
title: "Review Hilti Requisitions and Charge Equipment Use to a Job | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/hilti-ontrack-integration-with-spectrum/review-hilti-requisitions-and-charge-equipment-use-to-a-job"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/equipment/hilti-ontrack-integration-with-spectrum/review-hilti-requisitions-and-charge-equipment-use-to-a-job"
---

# Review Hilti Requisitions and Charge Equipment Use to a Job

In Spectrum, view
 Hilti equipment tracking requisitions, edit entries as needed, and create transactions to
 charge equipment usage to jobs.

1. In Spectrum, go to
 Equipment Tracking > Data Entry > Approve Hilti
 Requisitions.The equipment tracking data from Hilti ON!Track flows into the Approve Hilti Requisitions
 screen. When you open this screen, Spectrum validates all of the entries and marks each with a
 validation status of either Valid or Error.
For more details about this screen and fields, see [Approve Hilti Requisitions](/en/spectrum/spectrum/equipment/equipment-tracking/spectrum-menus/data-entry-overview/approve-hilti-requisitions).

1. Review the records. You must correct all entries
 with an Error status.

1. To correct or update records, select Edit. This opens the Edit Hilti Transaction window,
 where you can update equipment data.
For more details, see [Edit Hilti Transaction](/en/spectrum/spectrum/equipment/equipment-tracking/spectrum-menus/data-entry-overview/approve-hilti-requisitions/edit-hilti-transaction).

1. Select OK to
 save changes.

1. To delete an entry, select Delete.

1. To refresh the screen and reflect any changes to
 the entries, select Refresh.

1. When you have finished reviewing the Hilti
 requisitions and resolving all errors, select Create Transactions.This processes and updates all valid Hilti records in
 chronological order and, if there are no errors in any of the records for a
 given piece of equipment, creates a new Equipment Revenue Transaction entry.
Important: You must
 resolve all errors on the Hilti equipment entries in order to
 successfully generate new Equipment Revenue Transaction entries. If
 Spectrum encounters *any* Hilti entries with errors, it
 will not update in order to keep all equipment tracking records in the
 correct sequential order.

Hilti transactions update independently of the standard
 Spectrum equipment
 transactions update process. Requisition numbers are assigned when the
 transaction is created.
The equipment usage on this Equipment Revenue Transaction
 entries will then be charged to the job using the charge rates set up
 previously. Equipment usage is charged in two types of transactions:
Job TransactionsThis involves equipment initially requisitioned to a job, as well as
 equipment moved from one job and sent to another.Spectrum will start billing the new job for
 the piece of equipment and stop billing the previous job, if
 there was one.
Yard TransactionsThis involves equipment returned to the yard.Spectrum will stop
 billing the previous job.

For each piece of equipment, you can view the time in
 use, charge rates, and costs on the Equipment Financial Summary screen.See the
 following video for information about reviewing Hilti requisitions and approving
 transactions in Spectrum.
