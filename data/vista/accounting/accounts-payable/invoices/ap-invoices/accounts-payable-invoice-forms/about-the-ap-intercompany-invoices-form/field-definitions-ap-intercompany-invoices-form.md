---
title: "Field Definitions: AP Intercompany Invoices Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/about-the-ap-intercompany-invoices-form/field-definitions-ap-intercompany-invoices-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/about-the-ap-intercompany-invoices-form/field-definitions-ap-intercompany-invoices-form"
---

# Field Definitions: AP Intercompany Invoices Form

The following is a list of field descriptions for the AP Intercompany Invoices form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## MS Co#

The MS Co # field on the AP Intercompany Invoices form.
Specify the MS company from which the
 materials were sold. Must be valid MS company and cannot be equal to the current AP
 company.

## Restrict by Company

The Restrict by Company checkbox on the AP Intercompany Invoices form.
Select this checkbox to restrict
 initialization of invoices based on the purchasing (sold to) JC and/or IN company. When
 selected, the “Sold To” company is entered (below), and only those invoices referencing
 that company will be included in the batch.
Do not select this checkbox if you want to
 include all invoices from all purchasing JC and/or IN companies.

## Sold To Co#

The Sold To Co# field on the AP Intercompany Invoices form.
Specify the company (from HQ Company Setup) to
 which the materials were sold. Only invoices referencing this company will be included in
 the batch.

## Beginning/Ending Invoice Date

The Beginning/Ending Invoice Date fields on the AP Intercompany Invoices form.
Specify the beginning and ending in a range of invoice dates to
 include in the batch. Only invoices dated on or after the “Beginning Invoice Date” and
 dated on or before the “Ending Invoice Date” will be included in the batch.
Leave blank to include all invoices.
Once you have entered the restriction criteria, click the Update button to populate the grid with all invoices meeting the criteria. You can change the restriction criteria and refresh the grid as often as necessary until only those invoices you wish to process are listed. Then, click the Post button to process the invoices (in AP Batch Process). Once processed, the invoices can be paid normally in AP Payment Posting.
Invoice amounts can be edited or even deleted while in an AP Entry batch, but no update will be made to MS or AR reflecting your changes. If changes are needed, post correcting entries in MS, and process them as you would any other intercompany sale.
