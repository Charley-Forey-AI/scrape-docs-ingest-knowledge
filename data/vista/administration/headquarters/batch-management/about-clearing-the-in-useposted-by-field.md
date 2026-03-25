---
title: "About Clearing the In Use/Posted By Field | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/batch-management/about-clearing-the-in-useposted-by-field"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/batch-management/about-clearing-the-in-useposted-by-field"
---

# About Clearing the In Use/Posted By
 Field

All batches throughout the system are tracked in HQ Batch Control.
The information on this form is set up when you create a batch in any
 of the posting programs (e.g. AP Transaction Entry, GL Journal Transaction Entry, PR
 Timecards, etc.). However, you can edit the In Use/Posted By field.
The In Use/Posted By field on the HQ Batch
 Control form identifies which user is currently working with the batch. As long as there
 is an entry in this field, the batch cannot be accessed by another user. However, if
 necessary, you can clear this field to open up access to a batch, as long as the batch
 has not been processed (Status 5) or cancelled (Status 6). The most common reason for
 clearing this field is when a batch’s update procedure is interrupted (indicated by a
 Status of 4) and you need access to the batch to complete the update.
Note: If your security setup does not allow you access to HW Batch
 Control form, you can still clear the value in the In Use/Posted By field for batches you
 have locked via the Batch Selection form. Right-click in the In Use/Posted
 By column (of the desired Batch Selection form) and select the Unlock Batch
 option. This will clear the In Use/Posted By value and allow you
 to get back into your batch.

Related information

- [About the HQ Batch Control Form](/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form)
