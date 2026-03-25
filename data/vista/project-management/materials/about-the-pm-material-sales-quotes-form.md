---
title: "About the PM Material Sales Quotes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/materials/about-the-pm-material-sales-quotes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/materials/about-the-pm-material-sales-quotes-form"
---

# About the PM Material Sales Quotes Form

Use this form to edit header/item detail for quotes created in PM Material Detail.
Note: You will only be able to access this program if you have
 selected the MS
 in Use checkbox in PM Company Parameters.
Although information entered on this form corresponds to information entered in MS Quotes, much of the information entered for MS quotes is not required here. For example, quotes entered here will always be Job quotes; therefore, you will not be required to specify a quote type. You will also not have the ability to set up pricing or discount overrides, haul code defaults, haul zones, pay codes, or haul overrides.
Note: Only one quote can exist per job; therefore, only one record
 may be set up for a project/MS Company.
Quote information is typically set up via the PM
 Material Detail form (recommended method); however, you can add quote detail manually in
 this form as necessary. When a quote is set up here, one material line is added in PM
 Material Detail (Non-Interfaced tab) for every material entered on the quote.

## Quote Header

The Info tab is used to set up the quote
 header information. In addition to the project, MS Co, quote number, and contact
 information, you can specify the price template for material pricing, as well as the
 tax code and haul tax option, if applicable. When you are ready to use the quote,
 you must select the Active checkbox.
If you are using the oil price
 escalation/de-escalation feature (that is, you have set up price indexes in HQ
 Escalation Index), you can apply price escalators to the job quote by selecting the
 Apply Price Escalators checkbox and setting a Bid Index Date. The MS Oil Price
 Escalation report will track sales of the applicable materials (e.g. asphalt mixes,
 etc.) to the job in MS Ticket Entry and determine increases/decreases in pricing
 based on the bid index date specified for the quote and the pricing index (monthly
 escalation/de-escalation).
Note: If you selected the Apply Price
 Escalators checkbox for the job/project (in JC Jobs/PM Projects),
 the bid index date specified on the quote takes precedence over the job/contract
 start date. The job/contract start date is only used if no quote exists for the job.
You can use the MS Oil Price Escalation
 report to review pricing adjustments. For more information about this feature, see
 [About the HQ Escalation Index Form](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-escalation-index-form) and [How the System Uses Pricing Indexes](/en/vista/vista/administration/headquarters/material-setup/how-the-system-uses-pricing-indexes).
Once you enter a quote, the system
 creates a header recorded in the MS Quote Header table (MSQH). However, quote detail
 (entered on the Non-Interfaced Detail tab) is only updated after the quote is
 interfaced.

## Non-Interfaced Detail / Interfaced Items

Use the Non-Interfaced Detail tab to
 enter, modify, or delete quote detail. If you entered quote material lines in PM
 Material Detail, this grid is automatically populated with the information set up
 for each material. Additional information about the material is displayed above the
 tab pages and includes original estimate units, as well as unit cost information for
 the standard, purchase, and sales units of measure.Note: All information added,
 deleted, or modified in this grid automatically updates PM Material Detail.
 However, quote detail is not updated to the MS Quote Detail table (MSQD) until
 the quote is interfaced.
 Once you interface quote detail (using PM
 Interface), it is moved to the Interfaced Detail tab and cannot be edited or
 deleted.

Related concepts

- [PM Material Detail Form](/en/vista/vista/project-management/materials/pm-material-detail-form)

- [About the MS Quotes Form](/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/about-the-ms-quotes-form)
