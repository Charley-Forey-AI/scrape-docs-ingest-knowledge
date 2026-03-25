---
title: "Review Unapproved Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/review-unapproved-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/review-unapproved-invoices"
---

# Review Unapproved Invoices

Use the AP Unapproved Invoice
 Review form to view invoices assigned to you. Approving and rejecting are the most common tasks when reviewing unapproved invoices and invoice lines.
 You can apply a variety of filtering options to locate specific invoices. Once you
 find the appropriate invoice, you can then set an approval status to the invoice/lines.Tip: To review all
 unapproved invoices within a specified month range, regardless of status, use the AP Unapproved Invoices report. You can also run
 this report to show rejected invoices by selecting the “Print Rejected Only?” report
 parameter and leaving the Beginning and Ending Month parameters blank. Access this report
 from the AP Reports folder or by selecting Options > Reports from this form.
To review unapproved invoices:

1. In the AP Unapproved Invoice
 Review form, enter the reviewer ID in the Reviewer field. Press F4 for a list
 of available reviewers. Your current login must be associated with the reviewer for the
 system to allow access to the invoices assigned to a reviewer ID. Login access is defined
 in [HQ Reviewers](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewers-form).

1. Select the line types for
 filtering from the Line Types field. This field defaults to all line types selected. To filter
 by one line type, click the line type. Shift-click to select multiple, consecutive line
 types. Control-click to select multiple line types that are not consecutive.

1. Select the Display All Reviewer
 Invoices checkbox to filter for all invoices that are assigned to this
 reviewer, even those that are approved or rejected. If you do not select this checkbox, only
 invoices that are not either approved or rejected will display.Note: Even if this checkbox is selected, the following do not display in the grid:

- Approved invoices that are in a posting batch or that have
 already been posted. See [AP Unapproved Invoice Posting](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-posting-form).

- Invoices with readiness status of 0 - Not Ready.

1. To search for invoices related to a specific job, select the
 Display Invoices posted to a selected job
 checkbox. The system enables the
 JC Co #
 and
 Job
 fields. Enter the company and job in the
 JC Co #
 and
 Job
 fields.

1. To display all invoices meeting the criteria you've entered, click
 Refresh. Tip: The filtering section of the form collapses when records
 display in the header grid. Click the
 button to reopen the filtering section.
Note: If you are using a hierarchical method of approval, the
 system only displays to you the invoices/lines whose lower approval sequences have already
 been sufficiently approved by reviewers assigned to those sequences. For more
 information, see [Setting Hierarchy to Reviewers in Groups](/en/vista/vista/administration/headquarters/reviewer-setup/reviewer-group-hierarchy).

1. To assign the same status to all invoice lines currently displayed in the line detail level of the form, set the status at the header by selecting either the
 Approved
 or
 Rejected
 checkbox. If you choose to reject the invoice, the system enables the
 Reject Reason
 field; use this field to enter the reason for rejection or press
 F4
 for a list of [available reasons](/en/vista/vista/administration/headquarters/company-setup/hq-reason-codes-form).Note: If the selected invoice is missing data, the system
 displays “Missing Information” in red in the header area of the form. If you have
 security access to the AP Unapproved Invoice Entry form, you can click
 Invoice
 Setup
 to add additional data. When you access the AP Unapproved Invoice Entry
form in this way, you can view and edit only the currently selected invoice.If you are reviewing
 invoices as a member of a reviewer group, and can approve any lower-level
 sequences assigned to other reviewers, the system displays “Up Level Approver”
 in blue in the header section of the form. For more information see [Setting Hierarchy to Reviewers in
 Groups](/en/vista/vista/administration/headquarters/reviewer-setup/reviewer-group-hierarchy).

1. To assign approval status to an
 invoice line, highlight the invoice in the header level. The system displays all lines for
 the invoice in the detail section of the form.

1. To set the approval status for each line individually, select the line and then select either the
 Approved
 or
 Rejected
 checkbox. If you choose to reject the line, the system enables the
 Reject Reason
 field; use this field to enter the reason for rejection or press
 F4
 for a list of [available reasons](/en/vista/vista/administration/headquarters/company-setup/hq-reason-codes-form). Note: Additional fields allow you to make changes to specific
 line information. These fields display based on line type, but are limited to:

- Job: JC Co, Job,
 Phase, and Cost Type

- Inventory: IN Co and Location

- Expense: GL Co and GL
 Acct

- Equipment: EM Co, Equipment, Cost Code, and Cost
 Type

- SM Work Order: SM Co, SM Work
 Order, Scope, SM Cost
 Type, and JC Cost Type (job-related work
 orders only).

When you review lines whose type is PO or SL, the system displays additional information. See [About Reviewing PO and SL Lines](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-reviewing-po-and-sl-lines).
 If you need to make additional changes, click
 Invoice Setup
 to access the AP Unapproved Invoice Entry form.

Certain members of reviewer groups can receive email notifications when
 any reviewer of that group rejects an invoice or line of an invoice. Set these options in
 the HQ Reviewer Group form. Additionally, if you're using WF Notifier functionality and if the reviewers are
[set up in VA User Profile for email notifications](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/set-user-notification-preferences), the system can send out emails to the relevant reviewers based on other events.

1. You can enter notes about
 the invoice using the Invoice Notes header tab or the Line Notes tab or the Reviewer
 Notes tab by first double-clicking in the field. Lines notes are posted with a time
 stamp and cannot be deleted. Tip: Additionally, you can assign standard notes
 to either the Invoice Notes or Line Notes tabs. Select a tab and then select
 Edit  >  Insert
 Standard Note. The Std Note Copy form displays. Use this form to enter a standard note.
 For more information, see [Standard Note Copy ](/en/vista/vista/system-tools/user-interface-guide/system-forms/add-a-standard-note-to-a-field).

1. Save the record as normal.

 If you did not select
 the Display All
 Reviewer Invoices checkbox in step 3, the system removes each line that you
 approve or reject from view. To view already-approved or rejected invoices, click the  button and select
 the box, then click Refresh.
