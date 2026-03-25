---
title: "About Attaching SM Batch Reports to HQ Batch Control | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company/about-attaching-sm-batch-reports-to-hq-batch-control"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company/about-attaching-sm-batch-reports-to-hq-batch-control"
---

# About Attaching SM Batch Reports to HQ Batch Control

 You can have Service Management batch reports attached to HQ
 Batch control records so that you can access them for review after a batch is
 posted.
Service Management handles batch processing
 a little differently than other modules in that they are processed "behind the scenes".
 This means that the system automatically creates, validates, and posts a batch without
 ever exposing the batch processing form.
For purchase orders, this happens as soon as
 you save a purchase order (in SM Purchase Order Entry) and close the form. For work
 completed inventory, miscellaneous, and equipment lines, the Auto Post New Work
 Completed checkbox in SM Company determines whether batch processing
 occurs when saving a work completed line or when selecting to process them via the SM
 Work Order Cost Posting form.
Work completed labor lines and work
 completed purchase lines are handled as follows:

- When you save a work completed labor
 line, the system auto-generates a timesheet record (in PR Timesheets). Once you
 approve the timesheet and send it to PR Timecard Entry, it will go through the
 standard timecard batch process.

- Work completed purchase lines are
 created automatically when you post an SM-related PO batch; no further batch
 processing occurs at the work completed line level.

Because batches are processed behind the
 scenes, you do not have access to the audit reports generated during batch validation.
 However, you do have the ability to access the reports after batch processing has
 occurred by attaching the batch reports to the related batch records in HQ Batch
 Control. You can do this by selecting the Attach Batch Reports to HQ Batch
 Control checkbox in SM Company Parameters (highly recommended). Once a
 batch is posted, you can retrieve the related batch reports in HQ Batch Control. For
 information about how to retrieve SM batch reports, see [Retrieving SM Batch
 Reports](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company/about-attaching-sm-batch-reports-to-hq-batch-control/retrieve-sm-batch-reports).

## Security

If you elect to use the Attach Batch Reports option, make sure
 that users who will be entering work completed or posting cost batches (via SM Work
 Order Cost Posting) have access to the related batch reports. The system checks
 security for the related batch reports during the batch process. If a user does not
 have access to the appropriate batch reports, they will be unable to save work
 completed lines (if auto-posting batches) or process a work completed batch (if not
 auto-posting batches). For more information about auto-posting batches, see [Auto Post New Work Completed](https://cdnedge.viewpointcs.com/help/Production/Vista/6190/Content/Viewpoint/SM/Programs/SM_Company_Parameters/Field%20Defs/smcoparams_autopostnewworkcompleted.htm).
Additionally, access to attachments generated through this process is restricted to
 HQ Batch Control. If you have secured the HQ Batch Control form, users will only be
 able to access the batch reports if they have access to HQ Batch Control. Unlike
 regular attachments, indexes are not created for batch report attachments and you
 cannot access them using DM Attachment Search.

Related information

- [SM Company Parameters Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form)

- [About the HQ Batch Control Form](/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form)
