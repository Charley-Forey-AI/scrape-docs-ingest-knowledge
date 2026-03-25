---
title: "Hauling | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/hauling"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/hauling"
---

# Hauling

Hauling is a service provided by many companies to move materials from one location to another - usually a job site.
The company selling the material might typically haul the materials themselves, or they might contract an outside hauler to move the materials for them. Material Sales provides a complete system that allows you to reference your own equipment set up in the EM module, as well as the outside haul vendors and trucks used to move materials. The haul codes and rates used to track revenue generated from delivery services are set up exclusively within MS.
Haul charges can be entered in one of two programs within Material Sales: MS Ticket Entry or MS Hauler Time Sheet Entry. If your haul charges are unit based (per unit or units per mile) you will typically want to enter them with tickets, since the amount on which haul charges are calculated (i.e. the haul basis) will default from the material units. If you typically deal with hourly-based haul charges and use some form of hauler time sheet to track and enter haul charges after material tickets have already been posted, then you would enter haul charges in MS Hauler Time Sheet Entry.
Note: If you use both programs to enter haul charges, make sure the haul charges entered on time sheets do not duplicate haul charges already entered on a ticket.

## Setup Options

Whether using your own equipment or an
 outside haul vendor, certain setup options may affect the entry and/or calculation
 of haul charges.

- Haul Codes – Haul Codes set up
 in MS Haul Codes define how haul charges are calculated, and at what rate.
 The basis defined for each haul code determines where the haul basis
 defaults from when entering tickets or time sheets.

- Unit-based haul codes
 (per unit, units per mile, or units per hour) will default a haul
 basis based on the material units sold. However, this only applies
 if entering haul charges with tickets. If using MS Hauler Time Sheet
 Entry, the haul basis must be entered manually, since material units
 are not specified on time sheets.

- Hourly-based haul codes
 (per hour) will default a haul basis from the number of hours
 specified on the ticket or time sheet.

- Load-based haul codes
 (per load) will default a haul basis from the number of loads
 specified on the ticket or time sheet.

- Revenue-based or Vendor
 Payment-based haul codes (Use EM Revenue/Hauler Pay Amounts option
 checked) will default a haul basis from the revenue basis (if using
 own equipment) or the pay basis (if using an outside haul vendor).
 This option is typically used when you want to pass the equipment
 use or vendor payment amount through as the haul charge amount.

- Equipment/Vendor Trucks – Each
 vehicle used to haul materials must be set up in either EM Equipment (if
 hauling with own equipment) or MS Vendor Trucks (if using an outside haul
 vendor). If you are using unit-based haul codes (i.e. based on material
 units), and materials units are calculated using net weight or capacity x
 loads, you should set up the tare weight and capacity for each vehicle. This
 applies to haul charges entered on tickets only.

- Truck Types – Each vehicle used
 to haul materials must be assigned a truck type; therefore, make sure each
 truck type is set up in MS Truck Types. In addition, any truck type can be
 referenced when defining haul rates in MS Haul Codes. When the truck type is
 specified in Ticket Entry or Hauler Time Sheets, if a haul rate has been set
 up specific to the truck type, it may be used to calculate the haul charge.
 See Pricing in Related Topics for more information.

- Revenue Codes – If using your
 own vehicles to haul materials, revenue codes (set up in EM Revenue Codes)
 allow for posting usage to the equipment used, and will determine how
 revenue amounts are calculated. If a haul code is revenue-based (see Haul
 Codes above), the haul basis, rate, and total will be based on the values
 entered for the revenue code.

- Pay Codes – If using an outside
 haul vendor to haul materials, pay codes (set up in MS Pay Codes) are used
 to determine the haul vendor’s payment. If a haul code is vendor
 payment-based (see Haul Codes above), the haul basis, rate, and total will
 be based on the values entered for the pay code.

- Quotes– If you have set up
 quotes for customers, jobs, or locations to which you will be selling
 materials, you have the option to set up haul code and haul rate overrides
 based on location, category, material, and/or truck type. If you specify an
 override haul rate, that rate will be used to calculate haul charges every
 time a ticket is posted to the customer, job, or location that specifies the
 override criteria.
