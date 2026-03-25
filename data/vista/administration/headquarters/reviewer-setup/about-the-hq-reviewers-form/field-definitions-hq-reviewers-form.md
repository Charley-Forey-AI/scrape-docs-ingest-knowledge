---
title: "Field Definitions: HQ Reviewers Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewers-form/field-definitions-hq-reviewers-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewers-form/field-definitions-hq-reviewers-form"
---

# Field Definitions: HQ Reviewers Form

The following is a list of field descriptions for the HQ
 Reviewers form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Reviewer

Reviewer field in the HQ Reviewers form header
This is a unique code that identifies each reviewer. For example, you can use the initials of the reviewer or create a numeric code.
The reviewer code can be up to 3 characters long.

Related information

- [About the HQ Reviewers Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewers-form)

## Name

Name field in the HQ Reviewers form
Enter the reviewer’s name, up to 30 characters.

Related information

- [About the HQ Reviewers Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewers-form)

## Active

Active checkbox in the HQ Reviewers form
Check this box if this Reviewer can be assigned to perform reviews.
If you deactivate a reviewer, you may receive a message that the reviewer is currently assigned as a reviewer, and asks you to manually replace with another "active" reviewer in any listed locations.
The system may also notify you that the particular reviewer you are attempting to deactivate is the Responsible Person in at least one HQ Reviewer Group and therefore cannot be inactivated in HQ Reviewers. In such an instances, you must change the Responsible Person in that particular reviewer group in order to deactivate the selected reviewer.

## Approve with missing data

Approve with missing data checkbox in the HQ Reviewers form.
The setting on this checkbox provides the default value that is applied by the system when you add this reviewer to a reviewer group in the HQ Reviewer Group form and when the reviewer gets placed on an invoice line in the AP Unapproved Invoice Entry form. Other factors may override this default setting at the invoice line level. See [About Reviewer Groups' Interaction with Individual Reviewers](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-reviewer-groups-interaction-with-individual-reviewers) for more details.
When the checkbox is selected on the invoice line, the reviewer can approve it even if it lacks some portion of data. This allows the lines to progress in the review process. The missing data must still be entered before posting, but can be entered at some time after the reviewer's approval.

## Email

Email field in the HQ Reviewers form
Enter this reviewer’s email address. The unapproved invoice queries (e.g. APUnappNotify, APUnappNotifyRange,
 APUnappNotifyWaiting, and APUnappRejectNotify) send emails to this address to alert
 this reviewer when unapproved invoices need their review/approval or have been rejected by
 other reviewers.

Related information

- [About the HQ Reviewers Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewers-form)

## User Name

User Name field in the HQ Reviewers form, User Names tab
Enter the authorized user name for this reviewer as defined in VA User Profile.
 In most cases, the reviewer’s user name is the only one you should enter here.
The exception to this is if any other users are authorized to review unapproved invoices on behalf of this reviewer; if so, add their user name(s) here as well. In order to review in behalf of this reviewer, other users whose names you enter here must use the Reviewer code assigned to this reviewer (not their own Reviewer code).
If you find you are using this option extensively, consider using the Optional Reviewer functionality.

Related information

- [About the HQ Reviewers Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewers-form)

- [About Optional Reviewers for Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-optional-reviewers-for-unapproved-invoices)
