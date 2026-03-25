---
title: "Field Definitions: JB Miscellaneous Distributions Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-miscellaneous-distributions-form/field-definitions-jb-miscellaneous-distributions-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-miscellaneous-distributions-form/field-definitions-jb-miscellaneous-distributions-form"
---

# Field Definitions: JB Miscellaneous Distributions Form

The following is a list of field descriptions for the JB
 Miscellaneous Distribiutions form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Misc. Distribution Code

Specify the distribution code (AR Misc Distribution Codes) under which to track all or a portion of this invoice. For progress billings, this field defaults as null. For T&M billings, this field will default a value as follows:

- If adding miscellaneous distributions manually, default is null.

- If initialized billings have a 'Miscellaneous' type sequence, defaults from the template sequence. If a miscellaneous distribution code was not specified for the template sequence, defaults from the billing's contract (JB Contract Info). If a miscellaneous code is not specified for the contract, or a contract is not specified for the billing, defaults from the customer (AR Customers). Otherwise, defaults as null.

##  Distribution Date

 Specify the distribution date for the indicated Amount. Defaults the current date.

##  Description

 This field defaults the description for this distribution from AR Miscellaneous Distribution Codes; may be overridden.

##  Amount

 Specify the portion of this invoice on which this distribution is to be based. For example, a miscellaneous distribution code for a 5% sales commission must show the amount on which the commission will be based, not the amount of the commission. Later, AR reports will apply the distribution rate (defined in AR Misc Distribution Codes) to this amount in order to compute the actual commission amount.
 If adding distributions manually, this field initially defaults the total billed amount. If posting multiple distributions, the default for each distribution will reflect the billed amount minus the previous distribution amounts. If the billed amount is not fully distributed upon exiting, a message displays stating that total distribution amounts are not equal to the billed amount. However, exit is allowed.
 For T&M billings with 'Miscellaneous' type sequences, and billing was initialized, this field defaults the billed amount for the first distribution code, then 0.00 for all additional distribution codes. You will need to manually adjust the distribution amount for each additional distribution code.
