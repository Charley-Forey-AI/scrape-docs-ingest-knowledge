---
title: "Field Definitions: AP On Workfile Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/ap-on-cost-invoice-forms/ap-on-cost-workfile-form/field-definitions-ap-on-workfile-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/ap-on-cost-invoice-forms/ap-on-cost-workfile-form/field-definitions-ap-on-workfile-form"
---

# Field Definitions: AP On Workfile Form

The following is a list of field descriptions for the AP On Cost Worklife form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Invoice Selection Criteria

Invoice Selection Criteria section on the AP On-Cost Workfile form.
Use the following fields to enter filtering criteria.

- Vendor -
 Enter a value in this field if you want to add a specific vendor's invoices to the
 workfile. Press F4 for a list of vendors.

- Exp Month
 - Enter a value in this field if you want to add invoices based on a specific expense
 month. Press F4 for a list of expense months.

- Pay Control - Enter a value in this field if you want to add
 invoices based on a specific pay control code.

Once you have entered your criteria, click Fill Grid to populate the grid with all invoices
 meeting the specified criteria. The system also populates the detail grid with all invoice
 lines associated with the selected invoices.
If you leave all of these fields blank, the system will add all invoices that are subject
 to on-cost.

## Month and AP Trans

The Month and AP Trans fields on the AP On-Cost Workfile form.
Use the Month and AP Trans fields to enter the
 month and transaction number of the on-cost invoice you want to add to the workfile. If
 needed, you can press F4 from each field for a list of valid
 selections.
Note: If you are adding an invoice with all lines set as not subject to on-cost (the
 Subject to On-Cost box in AP Transaction Entry is not checked), then the
 system will not display the invoice's transaction numbers in the F4 lookup. However, you
 can manually enter a number to bring the invoice into the workfile.

Once you save the record, the system defaults the invoice lines to the detail grid. You can
 add as many invoices as needed.

## Line #

This field displays the line number for each invoice line. You can also use this field to add additional invoice lines to the workfile. This is useful if you need to reset the invoice line's status.
To add a line, enter the line number. Press
 F4
 to see a list of available lines.

## On-Cost Action

Select a processing action for the invoice line. The following options are available:

- 0 - Awaiting Process - Select this item to have the system ignore this invoice during on-cost processing, but be available in the grid for future processing. If this line's invoice is brought back into the workfile, this field will default 1-Process.

- 1 - Process - This is the initial default for invoice lines in the workfile. Select this option to have the system create an on-cost invoice for the specified invoice. Once you process the on-cost batch, the system disables this field and you cannot change this setting.

- 2 - Never Process - Select this option to have the system always ignore this invoice during on-cost batch processing. If this line's invoice is brought back into the workfile, this line will not appear. If you want to change this line from this option, you will need to bring the line into the workfile manually.
