---
title: "Haul Charges | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/hauling/haul-charges"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/hauling/haul-charges"
---

# Haul Charges

The Material Sales system provides flexible setup of haul
 codes and rates based on how your company normally handles haul charges.
First, haul codes are set up in MS Haul Codes, each one assigned a haul basis. The haul basis determines how haul charges will be calculated (i.e. per unit, per hour, etc.).Then for each haul code, you must define the rates that will be used when calculating haul charges during ticket or hauler time sheet entry.

## Haul Basis

The following is a brief description of each of the haul basis options available, as
 well as an example of how each option is used to calculate haul charges.

- Material Units: 100.000

- Material Unit Cost: 1.00

- Hours: 8.00

- Hourly Rate: 40.00

- Units/Hourly Rate: .3000

- Loads: 6

- Load Rate: 50.000

- Miles: 10.000

- Units/Mile Rate: .25

Haul Basis
Description
Result

Per Unit
Material Units x
 Rate
100.00 X 1.00 =
 100.00

Per Hour
# of Hours x Rate

8.00 X 40.00 =
 320.00

Per Load
# of Loads x Rate

6 X 50.00 = $300.00


Units/Mile
Material Units x
 Rate x Miles
100.00 X .25 X 10.00
 = 250.00

Units/Hour
Material Units x
 Rate x Hours
100.00 x .30 x 8.00
 = 240.00

## Standard Haul Rates

Haul rates are defined by location group, but may also be specific to other criteria
 such as location, material category, material, truck type, and/or haul zone. Because
 of the different levels at which haul rates can be defined, the system must use a
 hierarchical method for determining which haul rate should be used.

## Override Haul Code and Haul Rates on Quotes

If you have special haul rates for a customer, job, or location that are based on
 specific criteria (such as location, material, category of materials, and/or truck
 type), you can set up the special rates for each applicable haul code on a quote.
 Then, whenever a ticket is entered for that customer, job, or location that
 references the specified criteria, the override haul code and haul rates defined on
 the quote will be used.

## Taxing Haul Charges

If you do not tax haul charges, make sure you leave the Subject to Sales
 Tax or Subject to VAT (Australia and
 Canada) box unchecked for each haul code (in MS Haul Codes). However, if you will be
 taxing haul charges, the appropriate box must be checked, and how taxes are
 calculated for haul charges will be based on the following:

- Tax Option (MS Company
 Parameters) – Determines where the tax code will default from (i.e.
 sales location, sale type/purchaser, or delivery).

- Sale Type (Ticket or Hauler
 Time Sheet) — If the Tax Option is based on the ‘sale type/purchaser’,
 tells the system which Haul Tax Option to use (e.g. if customer sale,
 use the Haul Tax Option for customer in AR Customers).

- Haul Tax Option (AR
 Customers, JC Jobs, IN Locations, or Quote) — Specifies whether haul
 charges are not taxable, taxable only if using a haul vendor, or always
 taxable.

- Hauler Type — The hauler
 type is specified on the ticket or hauler time sheet and depending on
 the haul tax option, determines whether haul charges are taxable. If
 haul tax option is 1 (Taxable if Haul Vendor), then haul charges will
 only be taxed if the hauler type is Haul Vendor. If haul tax option is 2
 (Always Taxable), then haul charges will be taxable whether posted to
 your own equipment or a haul vendor.

## Taxing Hauler Payments (Australia and Canada)

You have the ability to calculate taxes on haul payments to a vendor when entering
 tickets or hauler timesheets. If the Default Country in HQ Company
 Setup is AU (Australia) or CA (Canada), the MS Ticket Entry and MS Hauler Time Sheet
 Entry forms will display additional fields that allow entering haul pay tax
 information (tax type, tax code, and tax amount). The haul pay tax amount calculated
 during ticket or timesheet entry will be included when processing haul payments in
 MS Haul Payment Worksheet.

Related information

- [About the MS Haul Ticket Add-Ons Form](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-ticket-add-ons-form)
