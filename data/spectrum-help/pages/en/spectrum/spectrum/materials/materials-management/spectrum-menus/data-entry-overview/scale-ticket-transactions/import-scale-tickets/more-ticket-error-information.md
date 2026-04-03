---
title: "More Ticket Error Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/import-scale-tickets/more-ticket-error-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/import-scale-tickets/more-ticket-error-information"
---

# More Ticket Error Information

Use this window to enter specific information about the pricing of this scale ticket and correct any errors previously made.
If a valid truck code is entered in the Truck field, the software looks at the default hauler code entered in Truck File Maintenance You should enter the truck number first; if that truck number has a default hauler code, this will be defaulted in the hauler code for that ticket.
Make the corrections in the fields below if errors exist.
Fields
Descriptions

Freight

Truck
Enter or search for the truck code.

Truck gross weight Truck tare weight
Enter the truck's gross weight in pounds and the tare weight.

Hauler
Enter or search for available hauler codes.

Freight rate
Enter the freight haul rate.

Imported freight cost
If freight cost was included in the scale package import, the imported freight cost will be included in this field. This amount can be changed.
Note: If the Imported freight cost was not included on the Import File Layout, this field will be hidden.

Customer ticket info

These fields are available if the Ticket type is set to Customer, Receipt, or Transfer in Ticket Error Correction Entry.

Customer's job
If the customer's job is entered in this optional field, it is used for the customer's different pricing schedules for different sales purposes.
Entry in this field is validated against records set up for this customer in Customer Material Contract Maintenance.
Spectrum uses this amount when applying miscellaneous charges during the scale ticket update to Order Processing. If this field is blank, Spectrum applies any miscellaneous charges defined in the non-job-specific customer contract. If there is no non-job-specific contract, Spectrum applies the miscellaneous charges defined in the Materials Management Installation screen.

Salesperson
Enter or search for an available salesperson code. If there is no salesperson associated with this ticket, leave this field blank.

Sales tax code
Enter the sales tax amount for customer tickets that will be updated to Accounts Receivable. This field is not applicable for job, receipts, or transfers, however it is available for customer tickets being transfer to the Order Processing module.

C.O.D.?
This checkbox is selected if this ticket is C.O.D.

Job ticket info

These fields are available if the Ticket type is set to Job in Ticket Error Correction Entry.

Area code
Entry in this field is validated against records in Area Code File Maintenance. Enter or search for the customer job number.

Phase
The appropriate Phase code displays if a job number was specified for a Sales transaction. A search window is available for viewing valid phase codes.
Note: Data entry is prevented if the phase status is set to Complete. A warning displays if the status is set to Inactive.

Cost type
Enter the Cost type you want to display.
