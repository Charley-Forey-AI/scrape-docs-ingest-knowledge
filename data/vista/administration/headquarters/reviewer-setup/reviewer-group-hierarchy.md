---
title: "Reviewer Group Hierarchy | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/reviewer-setup/reviewer-group-hierarchy"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/reviewer-setup/reviewer-group-hierarchy"
---

# Reviewer Group Hierarchy

When creating a reviewer group for unapproved invoices in HQ Reviewer Groups, you can establish a hierarchy for the review process.
Setting a hierarchy involves assigning a sequence number to each reviewer, as well as determining the review process rules when a reviewer changes data for an invoice with prior approvals.
Sequences allow you to set up a hierarchical structure where reviewers from each sequence must review and approve lines in a specific order. You can establish how the sequence operates with the Allow Up Level Approvaldrop-down field:

- When you select the View and approve self only option, only one sequence of reviewers can view an invoice at a time. Once all the reviewers of the approval sequence approve the invoice, the next sequence of reviewers can then view the invoice. For example, if one or more reviewers are assigned as approval sequence 1 to an invoice, they can all view it at the same time and must approve it before any reviewer(s) assigned in sequence 2 may view and approve or reject.

- If you select the View and approve self and lower levels option, reviewers of all sequence levels can view the invoice, and reviewers are able to view and take action on invoices/lines that lower-sequence reviewers have not yet taken action on. In doing so, reviewers with a higher sequence can approve the invoice in lieu of all lower sequences. For example, if the reviewer associated with approval sequence 3 views the invoice first, and approves it, the system bypasses (removes the approval requirement of) reviewers in approval sequences 1 and 2. The same applies if that reviewer rejects the invoice.

Once you establish the sequence structure, you can define the review process rules. These rules determine the actions that the system takes when a user changes data on an invoice with prior approvals. Use the Action on changed data and Allow up level approval fields to determine the process rules. The following table displays the action that the system will take depending on the settings of both fields.
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

Related information

- [About the HQ Reviewer Group Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form)
