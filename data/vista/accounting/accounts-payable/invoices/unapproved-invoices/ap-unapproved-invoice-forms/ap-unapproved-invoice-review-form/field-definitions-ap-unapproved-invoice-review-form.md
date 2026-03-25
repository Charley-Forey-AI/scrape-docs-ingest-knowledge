---
title: "Field Definitions: AP Unapproved Invoice Review Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-review-form/field-definitions-ap-unapproved-invoice-review-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-review-form/field-definitions-ap-unapproved-invoice-review-form"
---

# Field Definitions: AP Unapproved Invoice Review Form

The following is a list of field descriptions for the AP Unapproved Invoice Review form.

## Reviewer

Enter the initials of the Reviewer whose assigned invoices you want to view.
Press F4 for a list of active Reviewers from
 which to choose.
In order for you to approve the invoices as a
 particular reviewer, your log-in must be included in the User Name
 column on the User Names tab of HQ Reviewers (press F5 in the Reviewer field
 to access HQ Reviewers).

## Line Types

Use this box to select the line types you want to review. Line types available for selection are:

- Job

- Inventory

- Expense

- Equipment

- EM Work Order

- Purchase Order

- Subcontract

- SM Work Order

 If an invoice has at least one of the selected line types, it will be included in the invoice selection. If a line type is not selected, all line types display.
Note: If you select Job, PO, or Subcontract line types, you
 also have the option to select invoices for review by job.

## Display All Reviewer Invoices

Display All Reviewer Invoices checkbox in the AP Unapproved Invoice Review form
 Select this checkbox if you want to include
 all invoices that are assigned to this reviewer, even those flagged as 'approved' or
 'rejected' as well as those that have been approved by any higher-level, non-optional
 reviewer (for lines assigned to a Reviewer Group with the Allow up level
 approval option set to View and approve self and lower levels in the [HQ Reviewer Groups](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form) form).
Even if you select this checkbox, the grid does not display:

- invoices not yet marked as 1 -
 Ready

- invoices with approval sequences lower than that
 assigned to this reviewer (unless the View and approve self and lower levels option
 is selected in the [HQ Reviewer Groups](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form) form)

- approved invoices that have been updated to an AP transaction batch

Related information

- [Change Status](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form/field-definitions-ap-unapproved-invoice-entry-form#ID-00007205--en)

- [Invoice Status](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form/field-definitions-ap-unapproved-invoice-entry-form#ID-0000723b--en)

- [Automatically mark unapproved invoices Ready](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form/field-definitions-ap-company-parameters#ID-00005a89--en)

## Display Invoices Posted to a Selected Job

 Check this box to display invoices that are posted to a selected job (field below).
 Uncheck this box to include all invoices for all jobs.

## JC Co#

This field is only enabled when the Display Invoices Posted to
 a Selected Job box is checked.
Specify the JC company of the job whose invoices you want to display for review/approval.

## Job

 Specify the job for which to review/approve invoices.
 This field is only available if Display Invoices Posted to a Selected Job is checked.

## Month

 This field displays the month associated with the selected invoice.

## Seq #

 This field displays the sequence number associated with the selected invoice.

## Hold Code

The Hold Code field in the AP Unapproved Invoice Review form, header Info/Grid tabs.
Entry in this field is not required.
If applicable, enter the hold code for this unapproved invoice or press F4 to select from a list of valid hold codes. Hold codes prevent the invoice from being paid until the hold code is released. The hold code entered here is in addition to any hold code automatically placed on the transaction (or any portion of the transaction) because of retainage or a vendor hold.
Note: You cannot use this field to enter the hold code designated for retainage in AP Company Parameters. If you want to place a retainage hold, you must do so by invoice line in AP Unapproved Invoice Entry.

## Optional

 Optional column in the AP Unapproved Invoice Review form.
Select this checkbox to designate this reviewer as optional for this invoice line. This
 allows for one of several reviewers to approve at a given approval sequence. You can change
 this setting using AP Unapproved Invoice Entry.
As long as more than one optional reviewer is assigned to each invoice line’s approval sequence, only one reviewer must review and approve in order for the approval process to advance. However, if the only reviewer on an invoice line’s approval sequence is an Optional Reviewer, their approval becomes required in order for the approval process to advance.
Setting ALL reviewers on a sequence as optional does not eliminate the approval requirement for that sequence. If an invoice line’s approval sequence contains multiple reviewers, the following rules apply to allow the approval process to advance.

- if ALL reviewers on a sequence are set
 as optional, at least one must approve

- if ALL reviewers on a sequence are set
 as non-optional (Optional Reviewer checkbox is not selected), all must approve

- if some reviewers on a sequence are set
 as non-optional and some as optional, all non-optional must approve

## Approved

 Check this box to indicate this invoice is complete and approved. If approving invoices at this level, all lines for the invoice are automatically approved. Once approved, this invoice can be processed and added to an AP batch in AP Unapproved Invoice Posting.
 Do not check this box if this invoice is not ready to be approved.

## Rejected

Rejected checkbox on the AP Unapproved Invoice Review form, Invoice Header
 grid.
Select this checkbox to reject this invoice. Use the Rejection
 Reason column (right) to indicate why the invoice is being rejected. You can
 also use the Invoice Notes column to enter more detailed information
 about the rejection.
Note: Rejecting invoices at this level causes all lines for
 the invoice to be automatically rejected. However, removing the checkmark from this box
 does not automatically uncheck the invoice lines; they must be done manually.
Do not select this checkbox if you are not
 rejecting this invoice.
When you reject an invoice, if you have selected rejection notification recipients in HQ
 Reviewer Groups (Email Options on Rejection section), the system sends rejection
 notifications to the selected recipients as follows:

- If an invoice is rejected at the header level, a rejection notice is sent for the
 header reviewer group only. If no header reviewer group exists, then no notification
 is sent.

- If an invoice is rejected at the line level:

- and the line reviewer group differs from the header reviewer group, one
 rejection notice is sent for line reviewer group and one notice is sent for the
 header reviewer group.Note: For emails sent to responsible persons and reviewers, if the header
 reviewer group and line reviewer groups differ, but the responsible
 person or reviewer exists in both groups, that responsible person or
 reviewer will recieve two email notifications.

If both the reviewer groups are the same, only one notification is
 sent.

- If there is no reviewer group at the line level, but there is at the header
 level, the system will send a notification for the header group.

- If there is a reviewer group at the line level, but none at the header level,
 a rejection notification is sent for the line reviewer group.

## Rejection Reason

 Specify the reason for rejecting this invoice. Use F4 to see a list of valid reasons.

## Invoice Notes

Use this field to enter miscellaneous notes
 and information about this invoice. Notes cannot be entered directly in the grid; they must
 be entered via the Add Notes window, which is accessed by double-clicking in this
 field.
The Add Notes window is divided into two
 sections. The upper section is display only and shows all notes entered for the invoice.
 Each note is date-stamped and includes the reviewer’s initials. Because these notes track
 the approval process, they cannot be edited or deleted. The lower section is used to add
 new notes. Once you have entered your note text, click the Add button. This will add the
 note, along with the date and reviewers initials, to the upper section of screen.

### Add Standard Notes

To add standard notes (set up in HQ Standard Note), make sure focus is in the Notes box
 and click the right mouse button. From the shortcut menu, select the Standard Notes
 option, which brings up the Std Note Copy window. Enter the standard note to copy and
 click OK to add the note. Note will be appended to the end of existing note text (if
 applicable).

### Spelling Check

A spell check can be run for any notes entered in this window. Click
 the Spelling button in the toolbar () or select
 the Spelling option from the Tools or shortcut menu.Tip: To use the Tab feature (such as to indent the first line of a
 paragraph or create columns), you will need to press Ctrl + Tab for each tab
 increment.
Note: Invoice notes do not display in the
 Invoice Notes column. Instead, the date and reviewer of the first note written
 displays to indicate that notes exist (e.g. 11/22/2007 By MDM).

## Entered By

The Entered By field on the AP Unapproved Invoice Review form, invoice header Grid tab.
Display only, the user name of the person who entered the selected unapproved invoice.

## Approve

Check this box to indicate this invoice line is complete and approved. If you approved the invoice at the header level, all invoice lines are automatically marked as approved.
Note:All lines on the invoice must be approved before the invoice can be processed and added to an AP batch in AP Unapproved Invoice Posting.

Do not check this box if this invoice line is not ready to be approved.

## Reject

Select this checkbox to reject this invoice line. If you rejected the invoice at the
 header level, all lines on the invoice are automatically marked as rejected. Use the
 "Rejection Reason" column (right) to indicate why the invoice line is being rejected. You
 can also use the Line Notes column to enter more detailed information about the rejection.
Note: Once a line is rejected, corrections can be made in
 AP Unapproved Invoice Entry. Use the Reviewer tab to remove the checkmark from the
 Reject checkbox. Once the Reject box is
 unchecked, the invoice line will be available for review again.
Do not select this checkbox if you are not
 rejecting this invoice line.
When you reject an invoice, if you have selected rejection notification
 recipients in HQ Reviewer Groups (Email Options on Rejection section), the system sends
 rejection notifications to the selected recipients as follows:

- If an invoice is rejected at the header level, a rejection
 notice is sent for the header reviewer group only. If no header reviewer group
 exists, then no notification is sent.

- If an invoice is rejected at the line level:

- and the line reviewer group differs from the header
 reviewer group, one rejection notice is sent for line reviewer group and one
 notice is sent for the header reviewer group.Note: For emails sent to responsible persons and
 reviewers, if the header reviewer group and line reviewer groups differ,
 but the responsible person or reviewer exists in both groups, that
 responsible person or reviewer will recieve two email
 notifications.

If both the reviewer groups are the same, only one
 notification is sent.

- If there is no reviewer group at the line level, but there
 is at the header level, the system will send a notification for the header
 group.

- If there is a reviewer group at the line level, but none
 at the header level, a rejection notification is sent for the line reviewer
 group.

## Rejection Reason

 Specify the reason for rejecting this invoice line. Use F4 to view a list of valid reasons.

## JC Co

This field displays for job-related lines only.
Defaults the JC Co to which this invoice line was posted; may be overridden and the change will be updated to the invoice line in AP Unapproved Invoice Entry.

## JC Job

 This field displays for Job-related lines only.
 Defaults the job to which this invoice line was posted. If this is a ‘Job’ line, job may be overridden and the change will be updated to the invoice line in AP Unapproved Invoice Entry. If this is a 'PO' or 'SL' line, job cannot be overridden.

## JC Phase

 This field displays for Job-related lines only.
 Defaults the phase to which this invoice line was posted. If this is a ‘Job’ line, phase may be overridden and the change will be updated to the invoice line in AP Unapproved Invoice Entry. If this is a 'PO' or 'SL' line, phase cannot be overridden.

## JC Cost Type

 This field displays for Job-related lines only.
 Defaults the JC cost type to which this invoice line was posted. If this is a 'Job' line, cost type may be overridden and the change will be updated to the invoice line in AP Unapproved Invoice Entry. If this is a 'PO' or 'SL' line, cost type cannot be overridden.

## EM Co

This field displays for Equipment lines only.
Defaults the EM Co to which this invoice line was posted; may be overridden and the change will be updated to the invoice line in AP Unapproved Invoice Entry.

## EM Equipment

 This field displays for Equipment-related lines only.
 Defaults the equipment to which this invoice line was posted; may be overridden and the change will be updated to the invoice line in AP Unapproved Invoice Entry.

## EM Cost Code

 This field displays for Equipment-related lines only.
 Defaults the cost code to which this invoice line was posted; may be overridden and the change will be updated to the invoice line in AP Unapproved Invoice Entry.

## EM Cost Type

 This field displays for Equipment-related lines only.
 Defaults the EM cost type to which this invoice line was posted; may be overridden and the change will be updated to the invoice line in AP Unapproved Invoice Entry.

## IN Co

 This field displays for Inventory-related lines only.
 Defaults the IN Co to which this invoice line was posted; may be overridden and the change will be updated to the invoice line in AP Unapproved Invoice Entry.

## IN Location

 This field displays for Inventory-related lines only.
 Defaults the IN location to which this invoice line was posted; may be overridden and the change will be updated to the invoice line in AP Unapproved Invoice Entry.

## SMCo

This field only displays for invoice lines associated with an SM Work Order; that is, lines with a type of 8-SM Work Order or PO lines (type 6-PO) that reference an SM work order.
Defaults the SM Co to which this invoice line was posted; may be overridden.
Note:You may override the default for SM work order lines only (type of 8-SM Work Order); the system will update the information to the invoice line in AP Unapproved Invoice Entry.

## SM Work Order

This field only displays for invoice lines associated with an SM Work Order; that is, lines with a type of 8-SM Work Order or PO lines (type 6-PO) that reference an SM work order.
Defaults the SM work order to which this invoice line was posted.
Note: You may override the default for SM work order lines
 only (type of 8-SM Work Order); the system will update the information to the invoice line
 in AP Unapproved Invoice Entry.

## Scope

This field only displays for invoice lines associated with an SM Work Order; that is, lines with a type of 8-SM Work Order or PO lines (type 6-PO) that reference an SM work order.
Defaults the work order scope to which this invoice line was posted; may be overridden.
Note:You may override the default for SM work order lines only (type of 8-SM Work Order); the system will update the information to the invoice line in AP Unapproved Invoice Entry.

## SM Cost Type

This field only displays for invoice lines associated with an SM Work Order; that is, lines with a type of 8-SM Work Order or PO lines (type 6-PO) that reference an SM work order.
Defaults the SM cost type to which this invoice line was posted; may be overridden.
Note:You may override the default for SM work order lines only (type of 8-SM Work Order); the system will update the information to the invoice line in AP Unapproved Invoice Entry.

## JC Cost Type

This field only displays for job-related SM
 work order lines (i.e. lines with a Type of 6-PO or 8-SM Work Order that
 associated with a job-related SM work order).
Defaults the JC cost type to which this
 invoice line was posted.

-  You may override the default for SM work order
 lines only (type or 8-SM Work Order); the system will update the information to the
 invoice line in AP Unapproved Invoice Entry.

- The system shows related job information (SM JCCo,
 SM Job, and SM Phase) for each applicable line; however, this information is display
 only and cannot be edited.

## GL Co

This field is enabled for Expense lines only.
Defaults the GL Co to which this invoice line was posted; may be overridden and the change will be updated to the invoice line in AP Unapproved Invoice Entry.

## GL Account

 Defaults the GL account to which this invoice line was posted; may only be overridden for 'Expense' lines. Change will be updated to the invoice line in AP Unapproved Invoice Entry.

## Reviewer Notes

Use this field to enter miscellaneous notes and information about this invoice line. Notes cannot be entered directly in the grid; they must be entered via the Add Notes window, which is accessed by double-clicking in this field.
The Add Notes window is divided into two sections. The upper section is display only and shows all notes entered for the invoice line. Each note is date-stamped and includes the reviewer’s initials. Because these notes track the approval process, they cannot be edited or deleted. The lower section is used to add new notes. Once you have entered your note text, click the Add button. This adds the note, along with the date and reviewers initials, to the upper section of screen.
Add Standard Notes
To add standard notes (set up in HQ Standard Note), make sure focus is in the Notes box and click the right mouse button. From the shortcut menu, select the Standard Notes option, which brings up the Std Note Copy window. Enter the standard note to copy and click OK to add the note. Note will be appended to the end of existing note text (if applicable).
Spelling Check
A spell check can be run for any notes entered in this window. Click the Spelling button in the toolbar (

 ) or select the Spelling option from the Tools or shortcut menu.
Tip:To use the Tab feature (such as to indent
 the first line of a paragraph or create columns), you will need to press  Ctrl + Tab  for each tab
 increment.

Note: Line notes will not display in the Line Notes column.
 Instead, the date and reviewer of the first note written will display to indicate that
 notes exist (e.g. 11/22/2007 By MDM).

## Line Notes

Use this field to enter miscellaneous notes
 and information about this invoice line. Notes cannot be entered directly in the grid; they
 must be entered via the Add Notes window, which is accessed by double-clicking in this
 field.
The Add Notes window is divided into two
 sections. The upper section is display only and shows all notes entered for the invoice
 line. Each note is date-stamped and includes the reviewer’s initials. Because these notes
 track the approval process, they cannot be edited or deleted. The lower section is used to
 add new notes. Once you have entered your note text, click the Add button. This adds the
 note, along with the date and reviewers initials, to the upper section of screen.

### Add Standard Notes

To add standard notes (set up in HQ Standard Note), make sure focus is in the Notes box
 and click the right mouse button. From the shortcut menu, select the Standard Notes
 option, which brings up the Std Note Copy window. Enter the standard note to copy and
 click OK to add the note. Note will be appended to the end of existing note text (if
 applicable).

### Spelling Check

A spell check can be run for any notes entered in this window. Click
 the Spelling button in the toolbar () or select
 the Spelling option from the Tools or shortcut menu.Tip: To use the Tab feature (such as to indent the first line of a
 paragraph or create columns), you will need to press Ctrl + Tab for each tab
 increment.
Note: Invoice notes do not display in the
 Invoice Notes column. Instead, the date and reviewer of the first note written
 displays to indicate that notes exist (e.g. 11/22/2007 By MDM).
