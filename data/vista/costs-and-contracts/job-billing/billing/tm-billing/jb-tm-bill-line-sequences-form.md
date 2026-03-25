---
title: "JB T&M Bill Line Sequences Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-line-sequences-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-line-sequences-form"
---

# JB T&M Bill Line Sequences Form

Use this form (accessed by clicking the Bill Lines button in JB T&M Bill Edit) to edit/add bill lines to a billing.
You can add lines to a bill through initialization (in JB Time & Material Bill Init) or by manual entry. When adding a line manually, you must first select a valid sequence for the template (as defined in JB T & M Template Setup). Once you enter the template sequence, the template’s sort order determines what you enter next. For example, if the sort order is Job/Phase, you must enter a Job and Phase. If the sort order is Date, you must enter a date.
The system determines the Basis for each line based on the detail sequences added for the line. Therefore, you will typically not need to enter an amount. You can override amounts if necessary, with the exception of sequences with a type of 'Source'. For ‘source’ sequences, you will need to edit basis amounts via the detail sequences.
The Markup and Additional Markup fields will default the values specified for the template sequence in JB T&M Template Setup. You may also edit these if necessary. Be aware that changes to these amounts will affect the line’s total, but not the markup amounts for each detail sequence. You must edit markups for detail sequences manually.

## Detail Sequences

Use the lower portion of this form to enter detail for each line on the bill.
 Multiple sequences can exist for each bill line. The detail entered for each sequence depends on the source specified for the sequence, as well as the summary option, sort option, and cost types specified for the template sequence. For example, sequence types with a PR source will only allow entry of cost types defined for the PR source (Cost Types tab in JB T & M Template Setup), and may require input of Employee, Craft, Class, Shift, Earn Type, and/or Factor, depending on the sort/summary options.
Note: If a billing's contract is closed (indicated by the warning in red), you can only add lines and line sequences if you have checked one or both of the ‘allow posting to closed jobs’ flags in JC Company Parameters.

## Re-sequencing Lines/Details

Once you have added lines and/or detail to a billing, you can use the Reseq Lines or Reseq Detail buttons to have the system re-sequence the lines/detail for you.
The system re-sequences lines/detail in increments of ten without affecting the sort order. For example, if current line numbers (or detail sequences) are 10, 11, 12, 13, 14, and 15, re-sequencing will set them to 10, 20, 30, 40, 50, and 60. This allows you to insert additional lines/detail where needed without affecting the current order of lines or detail.
Click the JCDetail button to review the JC transaction detail for a particular bill line and detail sequence. For more information, refer to JB T&M Bill JCDetail By Seq in Related Topics below.

The following are related topics:

- [JB Bill Initialization Form](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-bill-initialization-form)

- [JB T&M Template Setup Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)

- [JB T&M Bill JCDetail By Seq Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-jcdetail-by-seq-form)
