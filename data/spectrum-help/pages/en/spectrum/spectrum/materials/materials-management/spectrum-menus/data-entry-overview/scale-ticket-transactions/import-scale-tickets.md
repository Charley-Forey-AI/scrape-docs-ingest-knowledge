---
title: "Import Scale Tickets | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/import-scale-tickets"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/import-scale-tickets"
---

# Import Scale Tickets

Use this screen to import scale tickets so that it is unnecessary to manually enter data twice. Import files with up to 2,000 characters per line. To import a file, first create the import file in the source (scale) software. Then use this screen to transfer that information into Spectrum. Once the information has been transferred, the import file format used on each ticket is saved.
If fields are not validated by the software during an import, they are flagged invalid and their codes are saved to the ticket. Additionally, the calculation flags in the import file are activated if changes are made to an invalid field on the ticket in the New/Edit Scale Ticket or the Revise All Import Errors screen. The fields that are flagged include Truck, Hauler, Customer / Job, Salesperson and Order number. When importing an invalid sales tax code for an import file format that does not calculate sales tax or validate the tax code, the software automatically sets the tax code using the default tax code for the selected customer. If the Utilize value added tax (VAT) tracking? checkbox is selected in Company Installation, sales transactions with a VAT code assigned to the Plant/Pit will be calculated and imported.
This update will set the 'Taxable' flag in the Material Detail when the 'Material Taxable' variable is included in the import file and record 'Freight Hours', if imported.

- If the import file includes the 'Material Taxable' variable, the scale ticket materials will be flagged as taxable if the Field # (or Start/Stop position) in the import file contains a "Y".

- If the import file does not include the 'Material Taxable' variable, the taxable hierarchy will default from customer and item setup.

- If the import file includes the 'Freight Hours' variable, set the Scale ticket freight hours equal to the number of hours imported.

- If the import file does not include the 'Freight Hours' variable, this field will remain blank.

If errors occur during the import, they are saved and can be viewed using the [Ticket Error Correction Entry](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/ticket-error-correction-entry) screen. More info Data that must be validated (based on settings specified in [Scale Data Format Maintenance](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/scale-data-format-maintenance)) appears on the Ticket Error Correction Entry screen where it can be validated once the errors are resolved. Note that if any of the item codes have an error, the entire ticket will appear in the Error Display screen. Those fields that are not validated will still be saved on the ticket, and calculation flags found on the import file will also be used if changes are made to the ticket in [Scale Ticket Transactions](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions) or Ticket Error Correction Entry screens. On the Error Display screen, click the Multiple Items button to display the [Multiple Items on Ticket](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/import-scale-tickets/multiple-items-on-ticket) window. This shows all item codes for a ticket. This display window is valuable as the Ticket Error Correction Entry screen only shows one line for each ticket.

Related information

- [Import Scale Tickets - Important Features](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/import-scale-tickets/import-scale-tickets---important-features)

- [Sales Tax Code Chart](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/sales-tax-code-chart)

- [Ticket Error Correction Entry](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/ticket-error-correction-entry)
