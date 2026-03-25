---
title: "Field Definitions: JB T M Bill JCDetail by Seq Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-jcdetail-by-seq-form/field-definitions-jb-t-m-bill-jcdetail-by-seq-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-jcdetail-by-seq-form/field-definitions-jb-t-m-bill-jcdetail-by-seq-form"
---

# Field Definitions: JB T M Bill JCDetail by Seq Form

The following is a list of field descriptions for the JB T M
 Bill JCDetail by Seq form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  JC Month

 Specify the JC transaction month to add to this detail sequence.

##  JC Trans

 Specify the JC transaction to add to this detail sequence. If the transaction’s detail matches the detail requirements defined for the template sequence (e.g.,. source, summary and sort opts, cost type, etc.), the transaction’s amounts (Units, Amount) are added to the totals of the detail sequence.
Note: The transaction’s Unit Price will not update the sequence’s Unit Price. In addition, the transaction’s units only update the sequence’s units if the unit of measure is the same.

## Billable

The system automatically checks this box for each transaction initialized to the detail sequence. The system allows overrides to this field.
When this box is checked, the system adds the transaction amount to the detail sequence’s total amount.
When this box is unchecked, the system does not add the transaction’s amount to the total amount. The transaction remains flagged as non-billable and will not show up on subsequent billings. However, if you delete the entire billing, then re-initialize the billing, this transaction will default as billable.
