---
title: "Edit Job Compliance Log Entry | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/job-compliance-tracking/edit-job-compliance-log-entry"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/job-compliance-tracking/edit-job-compliance-log-entry"
---

# Edit Job Compliance Log Entry

Use this window to edit job compliance tracking items. The fields on this window will vary depending on whether this is a log entry for Job Cost tracking items, Accounts Payable document tracking items, or Customer Lien Release Entries.
Click the E-Mail button to send this entry in an email to the selected vendor, subcontract, or customer.
Field
Description

Job
The job code and description displays in this field. If a subcontract is present in the log record, the subcontract # and description will display to the right of this field.

Vendor / Customer / Sub-tier vendor

- The vendor code and name displays for A/P document tracking items.

- The customer code and name displays for customer lien release entries.

- If the selected log record is for a sub-tier vendor, the sub-tier vendor code displays in this field.

AP tracking item
The tracking item code and description displays in this field. For recurring entries, click the Edit Date Range button to adjust the recurring date range.

Lien release type AR invoice / AP check

- For customer lien release entries, enter the lien release type and A/R invoice # in these fields.

- For A/P lien releases, enter the lien release type and A/P check # in these fields.

Trigger basis
The trigger basis option for this log entry displays in this field:

- Date of expiration

- Yes/No completion

If this is a Job Cost tracking item, there will also be a trigger basis option for recurring items.

- Yes/No recurring every <interval>

When editing a recurring item, the Edit Date Range button will appear to the right of this field allowing you to modify the start and end date as desired.
If this is a customer lien release entry, this field will be hidden.

Log entry date
The log entry date appears in this field.

Status
Select a status for the tracking item:

- Open

- In Review

- Completed

For 'Date of Expiration' entries, when switching to a 'Completed' status you must enter an Expiration date. When switching from a 'Completed' status, the Expiration date will be cleared.

Details

Expiration date
If the Trigger basis is 'Date of expiration', enter an expiration date for the log entry in this field. This log entry closes when an expiration date is entered.

Completed?
Select whether the log entry is completed. This field will be hidden if the trigger basis is 'Date of expiration'.

Due by
Enter a due date for the log entry.There is no minimum/maximum date protection for this field.

Comment
Enter any comments related to this log entry. Entry in this field is allowed at any time, even when the record is closed.

Final renewal?
If this is a subcontract 'Date of expiration' tracking item, select this checkbox if there is no later iteration of this same tracking item code on the job with a 'Closed' status.
