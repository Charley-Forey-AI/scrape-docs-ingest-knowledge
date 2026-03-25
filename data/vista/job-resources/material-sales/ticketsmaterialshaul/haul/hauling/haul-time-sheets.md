---
title: "Haul Time Sheets | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/hauling/haul-time-sheets"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/hauling/haul-time-sheets"
---

# Haul Time Sheets

Whether you haul materials with your own equipment or using the services of an outside haul vendor, Material Sales provides a program that allows you to record and track hauling activities.
Unit-based haul charges are typically recorded with Ticket Entry, while hourly-based charges can best be entered using the Hauler Time Sheet Entry program. This program allows you to record haul activity even after material tickets have been entered and processed, as well as reconcile time sheets with existing material tickets.
Note: Entry of haul charges in either program is optional. If you always enter haul charges with tickets, you do not need to use the Hauler Time Sheet Entry program. Likewise, if you always enter haul charges on time sheets, you will not need to enter them on tickets. However, if you do use both programs to enter haul charges, make sure that haul charges entered on time sheets do not duplicate haul charges already entered on a ticket.
Entry of time sheets is similar to entry of material tickets except that material units are never recorded. Therefore, if you base haul charges on material units, then you will most likely want to enter haul charges with material tickets. The Hauler Time Sheet Entry program is typically used for hourly-based haul charges, but can also be use to enter load-based and mileage-based haul charges since those methods do not rely on material units to determine the haul basis. If unit-based haul charges are entered, basis amounts must be entered manually.

## Removing Fields from Haul Time Sheets

If you do not require entry in all of the fields available on the time sheet screen,
 the “Remove from Haul Sheet Entry” option in MS Company Parameters (Haul Sheet tab)
 allows you to remove certain fields from the form. Included fields are:

- Material Vendor

- Start/Stop Times

- Loads

- Miles (US)/Kilometers (AU or CA)

- Hours

- Haul Zone

- EM Revenue Info (Rev Code, Basis, Rate, and Total)

- Vendor Pay Info (Pay Code, Basis Rate, and Total)

- Tax Info (Tax Type, Code, Basis, and Total)

- Discount Info

For Australia and Canada only (i.e,
 Default
 Country is AU or CA in HQ Company Setup), the Tax Info fields also
 include Haul Pay Tax Type, Haul Pay Tax Code, and Haul Pay Tax Amt.
Note: Removal of fields from the entry screens does
 not necessarily prevent values from defaulting and/or being calculated. For example,
 if you remove the revenue-related fields from the screen, a revenue code will still
 default if one has been assigned to the specified equipment in EM Equipment. Revenue
 basis, rate, and amount will be calculated based on the revenue code and other
 values entered on the ticket or time sheet.

## Posting Haul Revenue to Attachments

If you are using your own equipment to haul materials, and are posting equipment
 usage with tickets or time sheets, you have the option to also post revenue to
 attachments for equipment.
This is done by checking the “Post
 Revenue to Attachment” option for the attachment in EM Equipment. When haul charges
 are entered, usage will be recorded for the primary piece of equipment, and the same
 revenue code and hours will be used to create entries for the attachment. The
 revenue rate will be either the standard rate for the attachment/revenue code (by
 category) or an override rate (by equipment). If posting to a job, and the revenue
 code exists on a revenue template assigned to the job (in EM Job Templates), that
 revenue rate will be used.A separate sequence (transaction) is created for each
 attachment with just the revenue amounts. Although the sequence is created upon
 entry, it will not be displayed until the form is refreshed (Records menu).
Note: You have the option to base your equipment
 revenue on haul charges, or have haul charges based on the equipment revenue. These
 options are controlled by haul code and/or revenue code setup options. For more
 detailed information, see [Linking Equipment Revenue to Haul Charges](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-entering-haul-charges-with-tickets/about-linking-equipment-revenue-to-haul-charges).
