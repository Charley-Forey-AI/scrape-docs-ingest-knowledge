---
title: "Materials Management Installation - Ticket Details | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/installation-overview/materials-management-installation---ticket-details"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/installation-overview/materials-management-installation---ticket-details"
---

# Materials Management Installation - Ticket Details

Use this tab to select ticket detail settings for the Materials Management module. These settings can be changed at any time.
Fields
Descriptions

Default phase
The software is prompting for the phase code to default for scale tickets. This code will be used in the Import Scale Tickets update and the Scale Ticket Transactions screen. You can enter up to 20 characters in this field.
If the import file phase is blank, then the software will first check the item file for the default phase to use. If no phase is set up for that item, then the phase entered here will default.
If the phase code on the import is shorter than the phase mask for the job, the software will automatically left-fill blanks to build the phase code.
If the phase code is blank on the import of a job ticket, then the phase will be set based on the default code in the Inventory Item File Maintenance screen as long as the phase length in Inventory Control is the same as the job set up. If not a match, the phase code field will be left blank. If the phase code field is blank on import and in the item fill, the phase code will be set based on this installation field, provided the phase length here matches that of the job.

Default cost type
The software is prompting for the cost type to default for scale tickets. This cost type will be used in the Import Scale Tickets update and the Scale Ticket Transactions screen.
If the import file phase is blank, then the software will first check the item file for the default cost type to use. If no cost type is setup for that item, then the cost type entered here will default.
The default phase and cost type will only default if there are no codes in the scale file being imported. Also, the first default would be from Inventory Item File Maintenance; if that is blank, then these fields would be used. If the scale ticket being imported has the COD flag set to Yes, then the user would set the terms code for that sale invoice to the code set up here in the Materials Management Installation.

Default sales tax code from
The software is asking the location from where the sales tax code will default:

- If you select Warehouse, the tax code will default from the warehouse set up for the ticket plant/pit.

- If you select Customer, the tax code will come from the customer file.

- If you select Customer job, the tax code will come from the Customer Material Contract Maintenance screen.

Miscellaneous charges

Billing amount
Enter the amount that will be used to calculate the miscellaneous charge on customer scale tickets. Depending on the miscellaneous charge type, this amount may be a fixed amount, a rate per quantity, or a percentage.
Spectrum uses this amount when applying miscellaneous charges during the scale ticket update to Order Processing if the customer job contract and the non-job-specific customer contract do not have miscellaneous charges.

Cost amount
Enter the amount that will be used to calculate the miscellaneous charge on job scale tickets. Depending on the miscellaneous charge type, this amount may be a fixed amount, a rate per quantity, or a percentage.

Charge category
Enter or search for the miscellaneous charge category to use when creating non-stock miscellaneous charge lines.
This entry will be used when creating job requisitions, and when creating invoices if miscellaneous charges are set to create separate invoice lines. The category code entered here must be set up in Inventory Control Category File Maintenance.

Show miscellaneous charge billing item separately on invoice?
The software is prompting you to decide whether the miscellaneous charges on scale tickets will create separate invoice lines.
If you select this checkbox is selected, any miscellaneous charges will be summarized on separate non-stock invoice lines from the material charges. The non-stock item code will default from this Materials Management Installation screen.
If the checkbox is not selected, the freight charges will be summarized into the total billing for the material line item. This entry, and the non-stock item code used if creating separate miscellaneous charge invoice lines, may be overridden for individual customers in the Customer Material Contract Maintenance.
This entry will default if no customer contract has been setup in that file.
This entry applies only to customer scale tickets; job tickets will always assign miscellaneous charges to separate non-stock lines.

Miscellaneous charge type
The software is prompting for the method for calculating any miscellaneous charges to be assigned to tickets.

- If you select Fixed, the miscellaneous charge will be calculated as a fixed amount on each ticket.

- If you select Rate, the miscellaneous charge will be calculated as a rate multiplied by the ticket net quantity.

- If you select Percent, the miscellaneous charge is calculated as a percentage of the ticket extension amount.

Nonstock item
The software is prompting for the non-stock item code to use when creating
 non-stock miscellaneous charge lines. The non-stock item code created will
 include the miscellaneous charge category + exclamation point (!) + the
 non-stock item code entered here.

Nonstock description
Enter a non-stock item description for miscellaneous charge items, or press Enter to leave this field blank.

Unit of measure
Enter a non-stock item unit of measure (UM) description for miscellaneous charge items, or press Enter to leave this field blank.
