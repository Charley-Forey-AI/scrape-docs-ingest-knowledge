---
title: "About Reviewer Groups' Interaction with Individual Reviewers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-reviewer-groups-interaction-with-individual-reviewers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-reviewer-groups-interaction-with-individual-reviewers"
---

# About Reviewer Groups' Interaction with Individual Reviewers

AP unapproved invoice reviewers from groups act in tandem with reviewers assigned to the same invoice/line that are not part of the group.
Here's what you should be aware of:

- The settings on the group only apply to the reviewers in the group, not to any individual reviewers assigned to the line who are not members of the line or header group(s).

- Individual reviewers that you add manually to the line will initially have a default approval sequence number of 1. The Optional Reviewer and Approve w/ Missing values will default from the HQ Reviewers form. You may alter these values.

- When individual reviewers are assigned by default onto invoice lines for more than one reason, preference for the approval sequence, Optional Reviewer, and Approve with missing data fields are given in a specific order.

- Reviewers defaulting onto the header from the

- header reviewer group retain the approval sequence, optional reviewer, and Approve with missing data values pre-assigned in that group.

- vendor (AP Vendors) are assigned approval sequence 1 while the optional reviewer and Approve with missing data values come from the HQ Reviewer form.

- Reviewers that default onto the line from the

- header retain the approval sequence, optional reviewer, and Approve with missing data values assigned in the header.

- line-type defaults from JC and PM retain the approval sequence pre-assigned in the respective form unless the reviewer is assigned to the header or is a member of the line's reviewer group.

- line-type defaults from EM, IN, GL,and SM receive an approval sequence of 1.

- line reviewer group retain the approval sequence pre-assigned in the reviewer group unless they are assigned to the header.

The following examples use the approval sequence settings to illustrate. Though not specified in these examples, the optional reviewer and Approve with missing data settings receive the same treatment, that is, the preferences described above create the same outcomes for those settings.

- Reviewer "ABC" is assigned to the vendor and is also a member of header reviewer group "123" where her pre-assigned approval sequence is 3. Her approval sequence on the line(s) will be 3 because the system gives preference to the header reviewer group approval sequence over the vendor approval sequence assignment.

- Reviewer "XYZ" is a member of header reviewer group "123" where his pre-assigned approval sequence is 2. He is also a reviewer on the job with pre-assigned approval sequence of 1. His approval sequence on the line will be 2 because the header reviewer group's approval sequence is preferred over the line-type reviewer's approval sequence assignment.

- Reviewer "ABC" is a reviewer on the job with pre-assigned approval sequence of 1. She is also a member of line reviewer group "456" where her pre-assigned approval sequence is 2. Her approval sequence on the line will be 2 because the system gives preference to the line reviewer group's approval sequence assignment over the line-type reviewer's approval sequence assignment.

Related information

- [About Setting Up Default Reviewers for Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-setting-up-default-reviewers-for-unapproved-invoices)

- [Create Reviewer Groups for AP Unapproved Invoices](/en/vista/vista/administration/headquarters/reviewer-setup/create-reviewer-groups-for-ap-unapproved-invoices)

- [About Thresholds for Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-thresholds-for-unapproved-invoices)

- [About Reviewer Groups for Unapproved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-reviewer-groups-for-unapproved-invoices)

- [About the HQ Reviewer Group Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form)
