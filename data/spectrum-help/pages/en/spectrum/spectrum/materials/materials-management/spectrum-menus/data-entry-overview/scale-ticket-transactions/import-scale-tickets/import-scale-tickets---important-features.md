---
title: "Import Scale Tickets - Important Features | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/import-scale-tickets/import-scale-tickets---important-features"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/import-scale-tickets/import-scale-tickets---important-features"
---

# Import Scale Tickets - Important Features

The Import Scale Tickets screen
 accommodates import files containing both job and customer codes.
 If a ticket contains both a job and a customer, the job code will be used if valid rather
 than the customer. The customer code will be used if the job code is blank or invalid. If
 both the job and customer fields are in the file for a ticket, but the job is not set up in
 Spectrum, the job information is not used for pricing purposes.

- If the Taxable field
 is set to No Default in Accounts Receivable > Customer File Maintenance, you need to specify taxability during data entry. The warehouse only
 comes into play if it is selected in the [Materials Management Installation - Ticket Details](/en/spectrum/spectrum/materials/materials-management/installation-overview/materials-management-installation---ticket-details) screen.

- A sales tax code is required in the customer.
The import function looks at the default hauler code entered in [Truck File Maintenance](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/truck-file-maintenance) only if the hauler code is not mapped in the data format. If it is mapped and the code is not blank, then that code will be used as the hauler code during import. However, if it is blank or it is not mapped in the data format, then this field will be used as the hauler code during import.
Spectrum allows for blanks in between variables with a comma delimited file, to allow for times without a "0" if before 10:00 (for example, 9:59 instead of 09:59), and to automatically adjust the time to military time if a PM is found in the time string (for example, 1:30 PM will automatically be converted to 13:30). If both the job and customer fields are in the file for a ticket but the job is not set up, the job string is blanked out before any pricing is done.
When scale tickets are created with freight charges but no hauler code, and separate freight lines are produced when building O/P invoices, then the item code will be created by combining the G/L category for that line plus "!", rather than only "!", for the item code.
For stock items sold to customers, the Inventory Control Item Master Maintenance sell price is determined based on the material level specified in Customer Material Contract Maintenance if set up; otherwise, the material level from Customer File Maintenance is used. If none is specified, list price (level 1) is assumed.
