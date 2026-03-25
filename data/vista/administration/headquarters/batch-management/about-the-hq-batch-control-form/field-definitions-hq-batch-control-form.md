---
title: "Field Definitions: HQ Batch Control Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form/field-definitions-hq-batch-control-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form/field-definitions-hq-batch-control-form"
---

# Field Definitions: HQ Batch Control Form

The following is a list of field descriptions for the HQ
 Batch Control form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Company

 Specify the company in which the batch was created.

##  Month

 Enter the month in which the batch you want to review was created.

##  Batch ID

 Specify the batch number. Use F4 to see a list of all batches created in the specified batch month.

##  Source

 Display only, the form in which the batch was originated.

##  Batch Table

 Display only, the 4-character name of the primary batch table.

##  Created By

 Display only, the name of the user who created the batch.

## Date & Time Created

Display only, the date and time the batch was initially created.

## Restricted Access

Enabled only if the current login is the login that created the batch status is not 5-Posted Successfully or 6-Cancelled.
Check this box if you want to restrict this batch so that only you (the login that created the batch) will have access to the batch.
Leave this box unchecked to make this an unrestricted batch (i.e., all users with like security settings will have access to the batch and will be able to add/edit/delete information in the batch).
Note: This setting overrides this batch's normal restricted
 or unrestricted batch status defined when the batch was opened using the Batch Selection
 window.

##  Posted to Adjustment Period

 For GL Entry batches only.
 Display only, indicating whether this is an Adjustment period batch.

##  PR Group

 For PR timecard batches only.
 Display only, the PR group to which the batch applies.

##  PR Ending Date

 For PR timecard batches only.
 Display only, the ending date for the specified payroll period.

## Status

Indicates the current status of the selected batch. Disabled if batch’s status is any of 4-Posting in Progress, 5-Posted Successfully, or 6-Cancelled.
0-Open
 — This status is assigned when a batch is first created, and will remain assigned to the batch as long as there is detail in the batch and the posting process has not yet been started.
1-Validation in Progress
 — This status is set by the validation procedure.
2-Validation Errors
 — This status is set by the validation procedure when errors exist in the batch file. You can print the audit and error list, but cannot post the batch.
25-Validation Warnings
 — This status is set by the validation procedure when warnings exist in the batch file. You can print the audit and error list and then you can post the batch.
3-Validation OK
 — This status is set by the validation procedure. You can print the audit and distribution lists, and proceed with posting and purging the batch.
4-Posting in Progress
 — This is set by the update (posting) procedure. If the update is interrupted, the batch will remain in this status, and will not be revalidated. If the interruption is caused by power failure, you can complete the update by clearing the
 In Use/Posted By
 field, and then proceeding with the update. If the update procedure is interrupted due to software error, call Software Support for assistance.
5-Posted Successfully
 — This is set by the update procedure once the batch has been successful updated.
6-Cancelled
 — This status is set by the posting program if the batch is empty when closing the posting form. The batch can be reopened.

##  In Use/Posted By

 Disabled when batch status is ‘5’ (Posted Successfully) or ‘6’ (Cancelled).
 Indicates who the batch is currently in use by or who posted the batch. You may clear this field, if necessary, to allow access to the batch. A common reason for this is when a batch’s update procedure has been interrupted (indicated by a status of 4) due to a power outage or system failure, and you need to access the batch to complete the update.
 If the update procedure is interrupted due to software error, in addition to clearing this field, you will also need to call Software Support for assistance.
Note: If your security setup does not allow you access to
 this form, you can still clear the ‘In Use/Posted By’ value for your own batches via the
 Batch Selection form. Just right-click your mouse in the In Use By column (of the desired
 Batch Selection form) and click on the Unlock Batch option. This will clear the ‘in use by’
 value and allow you to get into your batch.

##  Posting Date

 Display only, the posting date assigned to this batch prior to processing (posting) the batch.

## Date & Time Closed

Display only, the actual date and time the batch was posted.
