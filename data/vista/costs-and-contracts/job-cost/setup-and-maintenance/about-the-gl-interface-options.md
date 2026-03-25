---
title: "About the GL Interface Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-gl-interface-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-gl-interface-options"
---

# About the GL Interface Options

Use the GL Cost, GL Revenue, GL Close, and
 Materials interface options in JC Company Parameters to define if the GL will be updated, and what level of detail
 will be interfaced.
If you elect to update GL, you must indicate
 the update level for each type of detail. If you choose to update at the Summary level,
 entries are summarized by batch and account, and one entry per account posted to GL. So,
 for example, if you have 15 transactions posted to three separate accounts in the batch,
 the summarization will produce three entries in GL. Additionally, you have the option to
 enter a summary transaction description, which identifies each of the entries in GL.
Important: If you are using the Summary level for updates
 to GL and the Interface Detail option in the GL Accounts program is selected for any
 account referenced in a transaction, it will override the Summary level option in this
 program, and transaction detail will interface at the Detail level. In addition, it is
 suggested that you enter both a Summary and a Detail Transaction Description, so that if
 the Summary option is overridden, the GL entries are not without a description.
If you elect to update GL at the Detail
 level, one GL entry is created for each transaction/GL account in a batch. To create the
 description that will appear for each GL entry, you are given a list of detail options
 to choose from. Each option you select is then displayed in the Detail Transaction
 Description field, in the order of selection. When the GL entry is created, the
 description will comprise of the actual records as specified.
For example, for the GL Cost Interface, you
 specify Job/Phase/CT as the Detail Transaction Description. When the interface is
 implemented, the system uses the Job number, Phase code, and Cost Type for each
 transaction to create the description for each corresponding GL entry. The resulting
 description might look something like this:
1001/03110-  -   /1
The description will include the record of
 each item specified, so you could ultimately end up with a very long description if you
 use too many of the detail options in your description. It is suggested that you use
 whatever options will make the description short but meaningful.
