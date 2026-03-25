---
title: "Setting up Surcharge Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/setting-up-surcharge-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/setting-up-surcharge-codes"
---

# Setting up Surcharge Codes

Surcharges generally represent extra fees or additional charges that your company institutes, such as fuel surcharges, hazard fees, and/or reclamation fees.
 If you will be assessing surcharges on Material Sales tickets, you must set up a minimum of one surcharge material, one surcharge code, and one surcharge group.
 You will use the [MS
 Surcharge Codes](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-surcharge-codes-form) form to set up the surcharge codes you will be using,
 along with the various surcharge rates that will be applied when entering tickets in
 MS Ticket Entry.
 To set up surcharge codes:

1. In the Surcharge
 Code field, enter a number (0-255) to represent the surcharge.


1. In the Description field, enter a description that identifies the surcharge.

1. In the Effective Date field, enter or select the effective date for this surcharge code.

1. From the Rate is Based On drop-down, select the option that applies to this surcharge code. The option selected here determines which value the rate will be applied against (e.g. if basis is Material Total, the surcharge amount will be a calculation of Rate x Material Total). For more information about each of the options, see the [F1](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-surcharge-codes-form/field-definitions-ms-surcharge-codes-form#ID-0001dc82--en) help.

1. From the Phase and Cost Type Based On drop-down, select 1-Haul to post surcharges to the haul phase/cost type or 2-Material to post surcharges to the material phase/cost type.

1. In the Surcharge
 Material field, enter the surcharge material associated with
 this surcharge code (i.e. the [material you set up in HQ Materials to track
 surcharges](/en/vista/vista/administration/headquarters/material-setup/setting-up-a-surcharge-material)). Press F4 for a list of valid
 materials.

1. Select the Active checkbox to activate this surcharge code. Surcharge code must be active in order to be available for assessing fees/surcharges.

1. Select the Allow Discounts with Material Discounts checkbox to apply discounts to surcharges. For more information, refer to the [F1](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-surcharge-codes-form/field-definitions-ms-surcharge-codes-form#ID-0001dcb5--en) help.Do not select this checkbox If you do not extend discounts to surcharges.

1. Select the Subject to Sales Tax When Material is Taxable checkbox to apply sales tax to surcharges. For more information, refer to the [F1](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-surcharge-codes-form/field-definitions-ms-surcharge-codes-form#ID-0001dcbd--en) help.Do not select this checkbox If you do not extend taxes to surcharges.

1. Select the Calculate Surcharge on Cash Sales checkbox to calculate surcharges when entering cash sale tickets in MS Ticket Entry (tickets using the C-Cash or X- Credit Card payment option).Do not select this checkbox if you do not apply surcharges to cash sales.

1. In the Pay Code field, enter the pay code to use in determining how much of the surcharge will passed to the haul vendor (must be a pay code with the Pay Rate is Based On field set to 7-Percent of Surcharge Total.Leave blank if you do not pass surcharges to the haul vendor or if pay rates are set up to include surcharges.

1. In the Revenue
 Code field, enter the revenue code to use in determining how
 much of the surcharge will passed to the equipment revenue account (must be a
 revenue code with the Based on MS Haul
 Charge/Surcharge box checked.Leave blank if you do not pass
 surcharge revenue to the equipment revenue account or if revenue rates are
 set up to include surcharges.

[Setting Up Surcharge Rates](/en/vista/vista/job-resources/material-sales/setupmaintenance/setting-up-surcharge-rates#task-1221--en__task-1221)

Related information

- [About the MS Surcharge Codes Form](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-surcharge-codes-form)

- [About the MS Surcharge Groups Form](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-surcharge-groups-form)
