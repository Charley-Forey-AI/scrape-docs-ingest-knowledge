---
title: "About Assigning Approval Sequences for Unapproved Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-assigning-approval-sequences-for-unapproved-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-assigning-approval-sequences-for-unapproved-invoices"
---

# About Assigning Approval Sequences for
 Unapproved Invoices

You can assign approval sequences to unapproved invoices to
 control the order in which the invoice lines are exposed to reviewers who are assigned to the
 same invoice line.
Sequences can be pre-assigned to reviewers in
 reviewer groups or you can set/adjust the sequence when adding reviewers individually to
 invoice lines using the AP Unapproved Invoice Entry form.
If you do not need a hierarchical structure, assigning a sequence
 number of "1" to all reviewers will allow all reviewers to access the invoice lines at the
 same time. The invoice can be posted once all non-optional reviewers have approved. If an optional reviewer is the only one assigned to a sequence, their approval is considered non-optional.
Note: When assigning a reviewer group to an invoice/line, the system applies the
 reviewer sequence numbers that were set up at the group level. For more information on
 reviewer groups, refer to [HQ
 Reviewer Group](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form).
You can pre-assign approval sequences to reviewers so that when
 the reviewer defaults or is manually assigned to the invoice/line, the approval sequence is
 already in place. Do this is the Reviewers tab in any of the following forms:

- HQ Reviewer Groups

- JC Jobs

- PM Projects

During invoice entry, you can assign multiple
 reviewers to a single approval sequence to enable reviews to happen simultaneously. For
 reviewers assigned to a group that is assigned to an invoice, you can establish how the
 approval sequence operates with the Allow Up Level Approval drop-down field
 in the HQ Reviewer Group form:

- When you select the View and approve self only option, only
 reviewers from any one approval sequence can view an invoice at a time. Once all
 reviewers from that approval sequence approve the invoice, the reviewers in the next
 approval sequence can view the invoice.

- If you select the View and approve self and lower levels
 option, reviewers with any approval sequence assignment can view the invoice, but
 reviewers with a higher approval sequence number can approve the invoice for all
 lower approval sequences. For example, if a reviewer associated with approval
 sequence 3 views and approves the invoice first, the system automatically approves
 sequences 1 and 2.

Note: You can add reviewers at the invoice header level after lines are created.
 The system automatically adds the reviewers to the line Reviewers tab, if the
 reviewer/sequence does not already exist.

Related information

- [Create Reviewer Groups for AP Unapproved Invoices](/en/vista/vista/administration/headquarters/reviewer-setup/create-reviewer-groups-for-ap-unapproved-invoices)
