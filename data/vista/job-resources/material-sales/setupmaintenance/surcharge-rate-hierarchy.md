---
title: "Surcharge Rate Hierarchy | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/surcharge-rate-hierarchy"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/surcharge-rate-hierarchy"
---

# Surcharge Rate Hierarchy

Surcharge rates follow a hierarchy; the system determines the rate to use based on how rates are defined at the quote level (overrides) or surcharge code level and the data entered on the parent ticket in MS Ticket Entry. (The parent ticket is the ticket for which the surcharge was assessed.)
The following tables identify the levels and search order used by the system to find a default rate; first at the quote level, then at the surcharge code level. The ‘X’s denote a value has been supplied; a blank indicates no value has been supplied.
The first row represents the minimum set of information required for a surcharge code. Each successive row provides more specific information, and overrides all preceding levels. For example, rates set up for a specific Location override those set up for the Location Group, rates referencing a Material, override those for the Category, and so forth.
Rate Hierarchy for Quote Overrides
Surcharge Code
Loc Grp
Location
Category
Material
Truck Type
UM

x
x

x
x

x

x
x

x

x
x

x
x

x
x

x

x
x

x

x

x
x

x

x

x
x

x

x
x

x
x

x

x
x

x

x

x
x

x

x

x
x

x

x
x

x
x
x

x
x
x

x

x
x
x

x

x
x
x

x
x

x
x
x
x

x
x
x
x

x

x
x
x
x

x

x
x
x
x

x
x

x
x
x
x
x

x
x
x
x
x

x

x
x
x
x
x
x

x
x
x
x
x
x
x

Rate Hierarchy for Surcharge Codes
Surcharge Code
Loc Grp
Location
Category
Material
Truck Type
UM
Zone

x
x

x
x

x

x
x

x

x
x

x
x

x
x

x

x
x

x

x

x
x

x
x

x
x

x
x
x

x
x

x

x
x

x

x

x
x

x

x

x
x

x

x
x

x
x

x

x

x
x

x

x

x

x
x

x

x
x

x
x

x

x
x
x

x
x

x
x

x
x

x
x

x

x
x

x
x

x

x
x

x
x

x
x

x
x

x
x
x

x
x

x
x
x

x

x
x

x
x
x
x

x
x

x
x
x
x
x

x
x
x

x
x
x

x

x
x
x

x

x
x
x

x
x

x
x
x

x

x
x
x

x

x

x
x
x

x
x

x
x
x

x
x
x

x
x
x
x

x
x
x
x

x

x
x
x
x

x

x
x
x
x

x
x

x
x
x
x

x

x
x
x
x

x

x

x
x
x
x

x
x

x
x
x
x

x
x
x

x
x
x
x
x

x
x
x
x
x

x

x
x
x
x
x

x

x
x
x
x
x

x
x

x
x
x
x
x
x

x
x
x
x
x
x

x

x
x
x
x
x
x
x

x
x
x
x
x
x
x
x

Related information

- [About the MS Surcharge Codes Form](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-surcharge-codes-form)
