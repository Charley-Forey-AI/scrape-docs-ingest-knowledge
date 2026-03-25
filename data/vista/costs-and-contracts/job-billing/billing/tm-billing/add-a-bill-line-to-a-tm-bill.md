---
title: "Add a Bill Line to a T&M Bill | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/add-a-bill-line-to-a-tm-bill"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/add-a-bill-line-to-a-tm-bill"
---

# Add a Bill Line to a T&M Bill

You can manually add lines to a T&M billing.
The following steps detail how to add lines to a bill manually.

1. Start a new line record by entering “New”, “N”, or “+” in the Line field

1. Enter a valid sequence for the template (as defined in JB T&M Template Setup) in the Template Seq field.

1. Enter information in the Template Sort Order fields. The template’s sort order determines the order of entry. For example, if the sort order is Job/Phase, enter a value in the Job and Phase fields.

1. Override the Basis field, as necessary. Note: Detail sequences determine the basis for each line; typically, you do not need to enter an amount. The system allows overrides to this field, with the exception of sequences with “Source” types. To edit the basis amount for Source lines, use the Detail section of the form.

1. Edit the Markup Rate and Additional Markup fields, as necessary. Note: The Markup Rate and Additional Markup fields default the values specified for the template sequence in JB T&M Template Setup. Changes to these amounts affect the line’s total, but not the markup amounts for each detail sequence. Edit detail sequence markups manually.

1. Click the Reseq Lines button to re-sequence line numbers. Note: The system re-sequences line number in increments of ten without affecting the sort order. For example, current line numbers might be 10, 20, and 30. When you add two new lines to the billing, they are numbered 15 and 25 (based on the template sequence and the type of data). After you click the Reseq Lines button, the system reconfigures the numbers to be 10, 20, 30, 40, and 50.

1. Click the chevron button to save the line record. The detail section of the form is now active.

1. Enter sequence details. [Click here for more information about Detail Sequences.](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-line-sequences-form)
