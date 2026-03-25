---
title: "Field Definitions: HQ Reviewer Groups Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form/field-definitions-hq-reviewer-groups-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form/field-definitions-hq-reviewer-groups-form"
---

# Field Definitions: HQ Reviewer Groups Form

The following is a list of field descriptions for the HQ
 Reviewer Groups form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Reviewer Group

 Enter an ID for the reviewer group, up to 10
 alphanumeric characters. Press F4 to view a list of previously
 established groups.

##  Description

 Enter a description for the group, up to 30 characters.

## Active

Check to indicate the Reviewer Group is active.
If you deactivate a reviewer group, you may receive a message that the reviewer group is currently assigned in the system, and asks you to manually replace the group with another "active" group in any listed locations.

## Responsible Person

The Responsible Person field in the HQ Reviewer Group form.
Enter the ID for the reviewer who is
 responsible for this group. Press F4 for a list of valid reviewers.
When used with AP Unapproved Invoices, the Responsible Person oversees a reviewer group by reviewing the status of each invoice assigned to the group using the AP Unapproved Invoice Status form and taking action if desired. This person can also receive emailed status updates according the settings for the group in the HQ Reviewer Group form. For more information, see [About Responsible Persons for Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-responsible-persons-for-ap-unapproved-invoices).

## Reviewer Group Type

Select the reviewer group type. This field designates the type of transactions that this group reviews. The following options are available:

- 1-Invoice - Select this type when setting up reviewer groups for unapproved invoices.

- 2-Timesheet - Select this type when setting up reviewer groups for timesheets. When you select this option the system disables the rest of the fields on the Info tab.

- 3-Job Billing - Select this type when setting up reviewer groups for JB progress and T&M billings. When you select this option the system disables the rest of the fields on the Info tab.

## Action on Changed Data

Action on Changed Data
The system enables this field when you select
 1-Invoice from the Reviewer Group Type field.
This field sets the action that the system takes when a reviewer makes changes (to any data or the amount only) for an unapproved invoice.
Shown below are examples of this setting in
 combination with the Allow up level approval setting.

Action on Changed Data

Allow Up Level Approval
Clear Prior Approval on Data Change
Clear Prior Approval on Amount Change
Nothing

View and Approve Self Only
Reviewer changes any data and the system clears the approval or rejection for all previous reviewers/sequences. If the current reviewer approves the invoice/line, lower-sequence reviewers are still required to review again.
Reviewer changes amount only and the system clears the approval or rejection for all previous reviewers/sequences. If the current reviewer approves the invoice/line with the new amount, lower-sequence reviewers are still required to review again.
Reviewer changes either data or amount, but the system maintains all prior approvals or rejections.

View and Approve Self and Lower Levels
Reviewer changes any data and the system clears the approval or rejection for all previous reviewers/sequences. If the current reviewer approves the invoice/line, the system approves all previous reviewer sequences.
Reviewer changes amount only and the system clears the approval or rejection for all previous reviewers/sequences. If the current reviewer approves the invoice/line with the new amount, the system approves all previous reviewer sequences.
Reviewer changes either data or amount and the system maintains all prior approvals or rejections.

A change to the any of the following fields is considered an amount-only change.
Gross
Misc Amt

Ret %
Ret Amt

Disc%
Disc Amt

A change to the any of the following fields is considered a data change.
Type
GL Co
GL Acct
UM
Units

UC
ECM
Gross
Misc Amt
Ret %

Ret Amt
Disc%
Disc Amt
Tax Type
Code

Basis
Amt
Pay Category
Pay Type
Supplier

JC Co
Job
Phase
CT
Material

IN Co
Loc
EMCo
Equipment
Comp Type

Component
Cost Code
Cost Type
WO
WO Item#

PO
PO Item#
PO Item Line
SL
SL Item

SMCo
SM Work Order
Scope Seq
SM Cost Type
JC Cost Type

## Allow Up Level Approval

The system enables this field when you select
 1-Invoice
 from the
 Reviewer Group Type
 field.
Approval sequences allow you to set up a hierarchical structure where reviewers must review and approve lines in a specific reviewer order. You can assign multiple reviewers to the same approval sequence to enable reviews to happen simultaneously. You can establish how the sequence operates with this drop-down field:

- When you select the
 View and approve self only
 option, only one sequence of reviewers can view an invoice at a time. Once all the reviewers of the approval sequence approve the invoice, the next sequence of reviewers can then view the invoice. For example, if one or more reviewers are assigned as approval sequence 1 to an invoice, they can all view it at the same time and must approve it before any reviewer(s) assigned in sequence 2 may view and approve or reject.

- If you select the
 View and approve self and lower levels
 option, reviewers of all sequence levels can view the invoice, and reviewers are able to view and take action on invoices/lines that lower-sequence reviewers have not yet taken action on. In doing so, reviewers with a higher sequence can approve the invoice in lieu of all lower sequences. For example, if the reviewer associated with approval sequence 3 views the invoice first, and approves it, the system bypasses (removes the approval requirement of) reviewers in approval sequences 1 and 2. The same applies if that reviewer rejects the invoice.

For more information on reviewer sequences, see [About Assigning Approval Sequences for
 Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-assigning-approval-sequences-for-unapproved-invoices).
Shown below are examples of this setting in combination with the
 Action On Changed Data
 setting.
Action on Changed Data

Allow Up Level Approval
Clear Prior Approval on Data Change
Clear Prior Approval on Amount Change
Nothing

View and Approve Self Only
Reviewer changes any data and the system clears the approval for all previous reviewers/sequences. Even if the current reviewer approves the invoice/line, lower-sequence reviewers are still required to review again.
Reviewer changes amount only and the system clears the approval for all previous reviewers/sequences. Even if the current reviewer approves the invoice/line with the new amount, lower-sequence reviewers are still required to review again.
Reviewer changes either data or amount, but the system maintains all prior approvals.

View and Approve Self and Lower Levels
Reviewer changes any data and the system clears the approval for all previous reviewers/sequences. If the current reviewer approves the invoice/line, the system approves all previous reviewer sequences.
Reviewer changes amount only and the system clears the approval for all previous reviewers/sequences. If the current reviewer approves the invoice/line with the new amount, the system approves all previous reviewer sequences.
Reviewer changes either data or amount and the system maintains all prior approvals.

## Apply Reviewer Threshold Amount at Line Level

The system enables this field when you select
 1-Invoice from the Reviewer Group Type field.
Select this checkbox to add reviewers to each individual line based on the line’s gross amount (Gross field). If the invoice line’s gross is equal to or greater than the threshold amount, the system adds the reviewer to the line. If the invoice line’s gross amount is less than the threshold, the system does not add the reviewer. The system only adds reviewers to the line Reviewer tab on AP Unapproved Invoice Entry, and not to the header Reviewer tab.

## Email Invoice Originator

The Email Invoice Originator checkbox on the HR Reviewer Groups form, Info tab.
The system enables this field when you select
 1-Invoice from the Reviewer Group Type field.
Select this checkbox to have the system send a rejection notification to the user who created this invoice whenever a reviewer in this group rejects an invoice with this reviewer group.
When reviewing invoices in AP Unapproved Invoice Review, the system sends notifications based on the following:

- If an invoice is rejected at the header level, a rejection notice is sent for the header reviewer group only. If no header reviewer group exists, then no notification is sent.

- If an invoice is rejected at the line level, the following applies:

-  If the line reviewer group differs from the header reviewer group, one rejection notice is sent for the line reviewer group and one rejection notice is sent for the header reviewer group; however, this only occurs if both the line reviewer group and the header reviewer group have the Email Invoice Originator checkbox selected. If only one of the reviewer groups has this checkbox selected, notification is only be sent to that reviewer group.
If both the reviewer groups are the same, only one notification is sent.

- If there is no reviewer group at the line level, but there is at the header level, the system will send a notification for the header group, as long as the header reviewer group has the Email Invoice Originator checkbox selected. Otherwise, no notification is sent.

- If there is a reviewer group at the line level, but none at the header level, a rejection notification is sent for the line reviewer group, as long as the line reviewer group has the Email Invoice Originator checkbox selected. Otherwise, no notification is sent.

## Email Responsible Person

The Email Responsible Person checkbox on the HQ Reviewer Group form, Info tab.
The system enables this field when you select
 1-Invoice from the Reviewer Group Type field.
Select this checkbox to have the system send a notification to the responsible person every time a reviewer associated with the group rejects an invoice.
 When reviewing invoices in AP Unapproved Invoice Review, the system sends
 notifications based on the following:

- If an invoice is rejected at the header level, a rejection
 notice is sent for the header reviewer group only. If no header reviewer group
 exists, then no notification is sent.

- If an invoice is rejected at the line level:

- and the line reviewer group differs from the header
 reviewer group, one rejection notice is sent for line reviewer group and
 one notice is sent for the header reviewer group.
Note: If the responsible person is the same for
 both the header and line reviewer groups, they will receive two
 notifications.

If both the reviewer groups are the same, only one
 notification is sent.

- If there is no reviewer group at the line level, but
 there is at the header level, the system will send a notification for the
 header group.

- If there is a reviewer group at the line level, but
 none at the header level, a rejection notification is sent for the line
 reviewer group.

## Email Reviewers Who Approved

The Email Reviewers Who Approved checkbox on the HQ Reviewer Group form, Info tab
The system enables this field when you select
 1-Invoice from the Reviewer Group Type field.
Select this checkbox to have the system send a rejection notification to all reviewers who previously approved the invoice, including options reviewers.
Alerts will only be sent to reviewers listed on the Reviewers tab for this group, not necessarily all reviewers assigned to the line/invoice.
When reviewing invoices in AP Unapproved Invoice Review, the system sends
 notifications based on the following:

- If an invoice is rejected at the header level, a rejection
 notice is sent to each reviewer in the header reviewer group only. If no header
 reviewer group exists, then no notification is sent.

- If an invoice is rejected at the line level:

- and the line reviewer group differs from the header
 reviewer group, one rejection notice is sent to each reviewer in the line
 reviewer group and each reviewer in the header reviewer group.
Note: If a reviewer exists in both groups, they
 will receive two notifications.

If both the reviewer groups are the same, notification
 is only sent for the line reviewer group.

- If there is no reviewer group at the line level, but
 there is at the header level, the system will send a notification to each
 reviewer in the header group.

- If there is a reviewer group at the line level, but
 none at the header level, a rejection notification is sent to each
 reviewer in the line reviewer group.

## Reviewer

Enter the reviewer’s ID or press F4 for a list
 of valid reviewers.

## Active

Check this box if this Reviewer can be assigned to perform reviews for this Reviewer Group.
If you activate a reviewer for a group, you may receive a message asking whether the activated reviewer should be added to all unposted invoices assigned to the reviewer group of which the reviewer is a member.

## Approval Sequence

The system enables this field when you select
 1-Invoice from the Reviewer Group Type field.
Enter the reviewer’s sequence number. Sequence numbers determine the order in which reviewers can approve invoices. For more information, see [About Assigning Approval Sequences for
 Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-assigning-approval-sequences-for-unapproved-invoices).

## Optional Reviewer

The Optional Reviewer checkbox on the HQ Reviewer Group form, Reviewers tab
The system enables this field when you select 1-Invoice from the Reviewer Group Type drop down on the Info tab.
Select this checkbox to designate this reviewer as optional for all accounts payable invoice lines to which this group is assigned. This allows for one of multiple reviewers to approve invoice lines with a given approval sequence.
As long as more than one optional reviewer is assigned to each invoice line’s approval sequence, only one reviewer must review and approve in order for the approval process to advance. However, if the only reviewer on an invoice line’s approval sequence is an Optional Reviewer, their approval becomes required in order for the approval process to advance.
Setting ALL reviewers on a sequence as optional does not eliminate the approval requirement for that sequence. If an invoice line’s approval sequence contains multiple reviewers, the following rules apply to allow the approval process to advance.

- if ALL reviewers on a sequence are set as optional, at least one must approve

- if ALL reviewers on a sequence are set as non-optional (Optional Reviewer checkbox is not selected), all must approve.

- if some reviewers on a sequence are set as non-optional and some as optional, all non-optional must approve

Related information

- [About the HQ Reviewer Group Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form)

## Approve with missing data

Approve with missing data checkbox in the HQ Reviewer Group form
The
 system enables this column when you select 1-Invoice from the Reviewer Group
 Type drop down. The default value for each reviewer comes from the
 same-named checkbox in the HQ Reviewers form. You can override an individual reviewer's
 permission for this group if you want, by clicking the box on that reviewer's record.
The setting on this checkbox provides the default value that is applied by the system when the reviewer gets placed on an invoice line in the AP Unapproved Invoice Entry form. Other factors may override this default setting at the invoice line level. See [About Reviewer Groups' Interaction with Individual Reviewers](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-reviewer-groups-interaction-with-individual-reviewers) for more details.
When the checkbox is selected on the invoice line, the reviewer can approve it even if it lacks some portion of data. This allows the lines to progress in the review process. The missing data must still be entered before posting, but can be entered at some time after the reviewer's approval.

## Threshold Amount

The Threshold Amount field on the Reviewer Group form, Reviewers tab.
The system enables this field when you select
 1-Invoice from the Reviewer Group Type field. Enter a
 threshold amount for this reviewer if desired. See [About Thresholds for Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-thresholds-for-unapproved-invoices) for more
 information.
