---
title: "Base Haul Charges on Revenue or Pay Code | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-entering-haul-charges-with-tickets/base-haul-charges-on-revenue-or-pay-code"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-entering-haul-charges-with-tickets/base-haul-charges-on-revenue-or-pay-code"
---

# Base Haul Charges on Revenue or Pay Code

Base haul charges on revenue or pay code.
If you want haul charges based on values
 entered with the revenue code or pay code, set up the haul code as follows (in MS Haul
 Codes):

- Based on Rev Code — Set the haul code basis to be equal to the revenue
 code basis. For example, if the revenue code’s Revenue Basis is set to Hour,
 then set the haul code’s Haul Rate is Based On field to
 2-Per Hour

- Based on Pay Code — Setup is the same, except that the haul basis must be
 equal to pay code basis.

- Do not set up any rate information for the haul code, as it will not be
 used.

- Check the Use EM Revenue/Hauler Pay Amounts
 box. This will flag the haul code so that when entering tickets or hauler time
 sheets, the haul basis, rate, and total will default from the values entered for the
 revenue code (if Hauler Type is E-Equipment) or
 from the pay code (if Hauler Type is H-Haul Vendor).

When tickets and hauler time sheets are entered,
 the program will check to make sure that the basis of the haul code is consistent with
 the posted revenue code or pay code. If the Hauler Type is Equipment, haul information
 will be based on values for the revenue code. If the Hauler Type is Haul Vendor, then
 haul information will be based on values entered for the pay code. If the haul code is
 unit based, the revenue code (or pay code) must also be unit based, and its unit of
 measure must match the material unit of measure entered for the ticket. Likewise, if the
 haul code is hourly based, the revenue code (or pay code) must also be hourly based.
If the validation is successful, the values
 entered for the revenue code or pay code will then default into the related haul charge
 fields. For example:
Rev CodeBasisRateTotal_Haul CodeBasisRateTotal
1 (Per Hour) 8 15.00 $120.00 2 (Per Hour) 8 15.00 120.00

Related information

- [About Entering Haul Charges with Tickets](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-entering-haul-charges-with-tickets)
