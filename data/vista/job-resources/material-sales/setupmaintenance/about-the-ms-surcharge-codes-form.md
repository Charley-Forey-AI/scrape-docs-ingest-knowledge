---
title: "About the MS Surcharge Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-surcharge-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-surcharge-codes-form"
---

# About the MS Surcharge Codes Form

Use this form to set up and maintain surcharge codes.
Surcharge codes can represent any charge or fee your company institutes, such as fuel surcharges, short load, hazard fees, and reclamation fees. If you do not utilize surcharges, you do not need to use this form.
Note: If you plan to use surcharges, you must set up at least one surcharge material in HQ Materials. For more information, see [Setting Up a Surcharge Material](/en/vista/vista/administration/headquarters/material-setup/setting-up-a-surcharge-material).
For each surcharge code you set up, you must define the set of criteria that will be used to assess charges based on information provided on the parent ticket (i.e. the original ticket entered for material or haul charges in MS Ticket Entry). This includes the effective date, what the rate is based on, whether surcharges can be calculated on cash sales, pay code and revenue code assignments, and the related surcharge material. You must also define surcharge rates, which will be used in conjunction with the surcharge basis to determine the surcharge amount.
Once you set up surcharge codes, you will need to assign them to at least one surcharge group in [MS Surcharge Groups](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-surcharge-groups-form). Surcharges must be assigned to a group in order for them to be assessed when entering tickets (in [MS Ticket Entry](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-ticket-entry-form)).
[Setting up Surcharge Codes](/en/vista/vista/job-resources/material-sales/setupmaintenance/setting-up-surcharge-codes)
You will use the Rates tab to set up surcharge rates by location group, with additional options for application by specific location, material category, material, truck type, and/or haul zone. For each rate sequence, you must specify new and old minimum amounts, and new and old surcharge rates. The system uses the Effective Date (specified on the Info tab) in conjunction with the Sale Date on tickets to determine which rate and minimum amount to use when assessing surcharges. For information about the hierarchy used to determine surcharge rates, see [Surcharge Rate Hierarchy](/en/vista/vista/job-resources/material-sales/setupmaintenance/surcharge-rate-hierarchy).
Note: You can override surcharge rates at the quote level using the Surcharge Overrides tab on the [MS Quotes ](/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/about-the-ms-quotes-form) form.

Related information

- [Surcharge Rate Hierarchy](/en/vista/vista/job-resources/material-sales/setupmaintenance/surcharge-rate-hierarchy)

- [Setting up Surcharge Codes](/en/vista/vista/job-resources/material-sales/setupmaintenance/setting-up-surcharge-codes)

- [Setting Up Surcharge Rates](/en/vista/vista/job-resources/material-sales/setupmaintenance/setting-up-surcharge-rates)
