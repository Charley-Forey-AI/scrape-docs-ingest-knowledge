---
title: "Using Your Own Equipment vs. an Outside Haul Vendor | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/hauling/using-your-own-equipment-vs.-an-outside-haul-vendor"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/hauling/using-your-own-equipment-vs.-an-outside-haul-vendor"
---

# Using Your Own Equipment vs. an Outside Haul Vendor

Materials can be hauled using your own equipment or the services of an outside haul vendor.
Material Sales provides the ability to
 post haul charges using one or both methods, and if set up to do so, will also
 update EM (own equipment) and AP (outside haul vendor).

## Using Your Own Equipment

If you will be using your own equipment
 to haul materials, you must set up each piece of equipment in the EM module. If you
 are not using EM, then you will only be able to use the Haul Vendor option for
 hauling materials. Some of the information defined for the equipment may be used as
 defaults when entering haul information on tickets or time sheets, such as the
 vehicle weights and capacity (tickets only), revenue code, PR Co# and Operator, and
 truck type.
Each time you post a ticket or time
 sheet, the equipment’s assigned revenue code (defined in EM Equipment) will
 automatically default into the revenue section of the screen. Typically, the revenue
 basis and rate will be based on the revenue code. If the revenue code’s basis (in EM
 Revenue Codes) is 'hour', the revenue basis amount will default from the number of
 hours entered on the ticket. If the basis is 'unit', the revenue basis amount will
 default from the material units. (When posting time sheets, no material units are
 entered, so the basis amount must be entered manually.) Revenue rates are defined by
 equipment category or equipment, so the default rate will be determined by the
 equipment specified on the ticket. If the ticket or time sheet is posted to a job,
 and the revenue code exists on a revenue template assigned to the job (in EM Job
 Templates), that revenue rate will be used. However, you can also base
 revenue-related defaults on values entered with the haul code. This is done by
 checking the “Based on MS Haul Charge” option for the revenue code in EM Revenue
 Codes. When the haul charges are entered for the ticket, the revenue-related fields
 are disabled, and the revenue basis and rate will default from the haul basis and
 rate. Although the standard rates (category or material) defined for the revenue
 code will not be used, breakdown rates will be used to provide a proportional
 distribution of revenue by breakdown code. For more information on posting equipment
 usage with haul charges, see “Linking Equipment Revenue to Haul Charges” topic in
 Related Topics below.
Note: If the revenue code is hourly based, only time
 units (hours) are updated to EM Revenue Detail (EMRD). However, if you are posting
 hours and the revenue code is unit-based, both work units and time units will be
 updated to EMRD.

## Using Outside Haul Vendors

If you will be using outside haul
 vendors to haul materials, you must set up each vendor truck in MS Vendor Trucks.
 Some of the information defined for the vendor/truck may be used as defaults when
 entering haul information on tickets or time sheets, such as the vehicle weights and
 capacity (tickets only), truck type, driver, and pay code.
When a ticket or time sheet batch is
 entered, the pay code assigned to the vendor truck automatically defaults into the
 payment section of the screen. The payment basis and rate will default based on the
 pay code. For example, if the pay code’s basis (defined in MS Pay Codes) is 'per
 unit', the payment amount will default from the material units. (Applies to tickets
 only, since when posting time sheets, no material units are entered and basis amount
 must be entered manually.) If the pay code’s basis is '% of haul charge', the pay
 basis amount will default the haul charge amount, and the resulting pay amount will
 be a percentage of that amount.
Note: If you have set up a quote for the customer,
 job, or location, override pay codes and rates defined on the quote will override
 the standard pay code and rates assigned to the vendor/truck in MS Vendor
 Trucks. 
Once the payment information is entered
 and the ticket processed, the payment information can be used to automatically
 generate AP invoices (in MS Haul Payment Worksheets).
