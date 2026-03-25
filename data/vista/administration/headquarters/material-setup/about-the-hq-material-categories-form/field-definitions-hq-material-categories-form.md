---
title: "Field Definitions: HQ Material Categories Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/material-setup/about-the-hq-material-categories-form/field-definitions-hq-material-categories-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/material-setup/about-the-hq-material-categories-form/field-definitions-hq-material-categories-form"
---

# Field Definitions: HQ Material Categories Form

The following is a list of field descriptions for the HQ
 Material Categories form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Category

 Enter a code, up to 10 characters, that identifies this material category. This category will be used to group similar materials together for reporting and for overriding material costs by vendor/category (in PO Category Discount).

##  Description

 Enter a description of this material category, up to 30 characters.

## Non-Stocked GL Account

Specify the GL Account to debit when non-stocked materials in this category are specified on an expense invoice (in AP Transaction Entry) or to credit when non-stocked materials in this category are posted to a job or equipment.

- If a non-stocked material in this category is specified on an expense invoice (in AP Transaction Entry), the sub ledger code for this account must be blank (null).

- If materials in this category will only be posted to jobs, the subledger code must be 'J-Jobs' or blank (Null).

- If materials in this category will only be posted to equipment (in EM Work Order Parts Posting, EM Fuel Usage, or EM Cost Adjustments), the subledger code for this account must be blank (null).

- If materials in this category will be posted to both equipment and jobs, subledger code must be blank (Null).
