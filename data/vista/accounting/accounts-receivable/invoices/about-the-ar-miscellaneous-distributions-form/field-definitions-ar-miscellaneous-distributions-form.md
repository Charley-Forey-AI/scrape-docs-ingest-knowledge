---
title: "Field Definitions: AR Miscellaneous Distributions Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-miscellaneous-distributions-form/field-definitions-ar-miscellaneous-distributions-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-miscellaneous-distributions-form/field-definitions-ar-miscellaneous-distributions-form"
---

# Field Definitions: AR Miscellaneous Distributions Form

The following is a list of field descriptions for the AR Miscellaneous Distributions form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Amount

Specify the distribution amount for this distribution code. Initially defaults to the transaction amount (taxes are excluded). If posting multiple distributions, the default for each distribution will reflect the transaction amount minus the previous distribution amounts. If this is a credit memo, write-off, or an adjustment with a negative amount, the default will display as a negative amount.
Note: If you not fully distribute the transaction amount, when moving off the miscellaneous distributions grid, a message displays indicating that the miscellaneous distributions do not equal the transaction’s total. However, the record will be saved and you will be able to post the batch.

##  Description

 Enter a description of this item, up to 30 characters.

## Misc Distribution Code

Specify the miscellaneous distribution code (from AR Misc Distribution
 Codes) by which this distribution will be tracked. Value will default as follows:
From AR Invoice Entry

- Automatic Distribution (Create Miscellaneous
 Distributions on Invoice box is checked for customer in AR Customers)
 - During batch validation, the system will create a single distribution per
 applicable invoice using the miscellaneous distribution code assigned to the contract
 ( contract-related invoices) or customer (non-contract invoices or contract invoices
 when no miscellaneous distribution code is assigned to the contract). If no
 miscellaneous distribution code is found, no distribution record is created.

Note: You can modify auto-generated distributions, if necessary, before posting the batch.

- Manual Distribution (Create
 Miscellaneous Distributions on Invoice box is unchecked for
 customer in AR Customers) - Defaults the miscellaneous distribution code assigned
 to the contract (contract-related invoices) or customer (non-contract invoices or
 contract invoices when no miscellaneous distribution code is assigned to the
 contract). If no miscellaneous distribution code is found, defaults as null.

Note: Default will only occur by double-clicking in this
 field, which opens the Miscellaneous Distributions form, or by skipping this field and
 entering a value in the Dist Date field.
From AR Cash Receipts

- Automatic Distribution (Create Miscellaneous
 Distributions on Payment box is checked for customer in AR Customers)
 - During batch validation, the system will create a single distribution record for
 each invoice during batch validation, using the miscellaneous distribution code
 assigned to the contract in JC Contracts (contract-related invoices) or customer in
 AR Customers (non-contract invoices or contract invoices when a miscellaneous
 distribution code is not assigned to the contract).

Note: When using this feature, you will be unable to edit generated distributions. If you need to modify a generated distribution, you will need to turn off this feature, make the necessary changes, then post the batch. For step-by-step instructions, click [here](/en/vista/vista/accounting/accounts-receivable/invoices/automatic-distributions).

- Manual Distribution (Create
 Miscellaneous Distributions on Payment box is checked for customer
 in AR Customers) - Defaults the miscellaneous distribution code assigned to the
 customer. If no miscellaneous distribution code is found, defaults as null.

Note: Default will only occur by double-clicking in this
 field, which opens the Miscellaneous Distributions form, or by skipping this field and
 entering a value in the Dist Date field.

##  Distribution Date

 Specify the date for this distribution.
