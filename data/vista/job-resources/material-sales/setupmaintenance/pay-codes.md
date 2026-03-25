---
title: "Pay Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/pay-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/pay-codes"
---

# Pay Codes

Pay codes are used to identify how vendor payments are calculated.
You will only need to set them up if you will be
 using the services of haul vendors to deliver materials and wish to automatically
 generate haul vendor invoices in AP.

## Pay Basis

Each pay code is assigned a 'basis',
 which determines how the pay rate will be calculated. Pay codes can be unit-based;
 that is, the pay rate will be applied on a per unit, units per mile, or units per
 hour basis. If unit based, the pay basis will default from the material units;
 however, this applies only on tickets, since time sheets do not specify material
 units (in which case, the pay basis would need to be entered manually). For hourly
 or load-based pay codes, the pay basis will default from the number of hours or
 loads specified on the ticket or time sheet. Pay codes can also have a basis of “%
 of haul charge”. When this option is used, the pay basis on tickets and time sheets
 will default from the total haul charge amount. The pay rate is applied, resulting
 in a payment amount that is a percentage of the total haul charge.

## Pay Rates

Standard pay rates are defined for each pay code; however, if you
 are using quotes, you can override the standard values. See Pay Code/Rate Overrides
 on Quotes in Related Topics below.
Pay rates are defined by location group, but may also be specific
 to other factors such as location, material category, material, vendor, truck type,
 truck, and haul zone. For example, you may have a standard rate specified for each
 location, but you have a couple of vendors that give you a special rate on certain
 materials or categories of material. You can then set up a rate for each vendor, and
 that rate will be used whenever a ticket or time sheet is entered that specifies
 that vendor and material.
From the
 example above:

1. These two entries define standard pay rates at the Location level. All materials
 hauled from these locations by any haul vendor will use these pay rates.

1. These two entries define pay rates at the location/category/vendor level. All
 materials within the specified category hauled from these locations by the
 specified vendors, will use these rates. Because these entries contain more
 specific criteria, they will override the entries at the location level whenever
 materials in the specified category are entered on a ticket or time sheet along
 with the specified haul vendor.

The system uses a hierarchical
 method to determine which rate will actually be used when the pay code is specified
 on a ticket or time sheet. The pay basis also plays a part in determining what
 hierarchy the pay rate will follow.  For more information, the pay rate
 hierarchy topics in Related Topics below.
