---
title: "About Clearing the Batch | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-clearing-the-batch"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-clearing-the-batch"
---

# About Clearing the Batch

When you create a batch, the system adds the data to a batch
 table and stores it until you are ready to post the batch.
Data is not updated online; therefore, you
 can delete it completely without affecting any modules, including the module in which
 you created the batch. To clear a batch table of stored data, select ‘Clear Batch’ from
 the File menu. The system will clear/delete all data from the batch.

-  Previously posted transactions
 added to the batch are only cleared from the batch—they are not deleted.

- The system creates an audit record
 each time you clear a batch. For information about cleared batches (i.e. user
 who cleared batch, as well as the date and time the batch was cleared), use the
 VA 'Other Events' Statistics report.

- The Clear Batch option is disabled
 if the batch’s status is 4 (Posting in Progress). This is to prevent partially
 updated batches from being deleted should the update process be interrupted
 (i.e. power outage, system failure, etc.). When a batch update is interrupted,
 only a portion of the intended updates may occur. If a user later clears the
 batch, there is no way to determine the updated data.
