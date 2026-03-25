---
title: "Haul Vendor Payments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/haul-vendor-payments"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/haul-vendor-payments"
---

# Haul Vendor Payments

If you use the services of an outside haul vendor to deliver materials, you can track
 both haul income and costs within Material Sales.
You can enter haul charges (income) and hauler payment amounts (costs) in either MS Ticket Entry or MS Hauler Time Sheet Entry.

## Calculating Payments

When you enter haul information on tickets or time sheets, payment amounts are
 calculated depending on the pay code you specify. Pay codes are set up in MS Pay Codes,
 and are used to define the pay code basis and the pay rate. The pay code basis
 determines whether the pay rate will be calculated on a per unit, hour, or load basis,
 on a units per mile or hour basis, or as a percent of the haul charge basis. For
 example, if the pay code basis is 'per load', the pay basis will be determined by the
 number of loads that you specify on the ticket or time sheet.

## Haul Payment Taxes (Australia and Canada)

You have the ability to calculate taxes on
 haul payments to a vendor when entering tickets or hauler timesheets. If the Default
 Country in HQ Company Setup is AU (Australia) or CA (Canada), the MS
 Ticket Entry and MS Hauler Time Sheet Entry forms will display additional fields that
 allow entering haul pay tax information (tax type, tax code, and tax amount). The haul
 pay tax amount calculated during ticket or timesheet entry will be included when
 processing haul payments in MS Haul Payment Worksheet.

## Generating Invoices

Haul vendor payment information stored with
 tickets and hauler time sheets can be used to generate AP invoices. This is done in MS
 Haul Payment Worksheets. Once you initialize a payment worksheet and make any edits
 necessary, you can process the payment batch. The system will generate AP invoices based
 on the information on the payment worksheets. Once the batch is posted, the invoices are
 updated to AP where they can be processed as normal.Note: The update to AP only allows
 you to add invoices. It cannot be used to correct or delete previously interfaced
 information. If you need to change hauler payment information that has already been
 updated to AP, you should post additional tickets or time sheets with reversing
 entries, then create and post a new hauler payment batch. You can also delete the
 related transactions in AP Transaction Entry, and then edit the ticket in MS Ticket
 Entry.
Note: The AP Invoices created from a hauler payment batch may be edited
 or even deleted from the AP Transaction Entry program, but no automatic update will
 be made back to MS.
