---
title: "Accounts Payable Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/accounts-payable-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/accounts-payable-invoices"
---

# Accounts Payable Invoices

Additional information about the AP Invoices import
 form.
This template defaults 3-VAT for the Tax Type field when
 the default company is something other than US (in HQ Company Setup).
If you import attachments with your AP invoices, you must use a comma delimited
 file format. In addition, the lines that indicate the document files must
 begin in column 1 with #ATTACHMENT (case insensitive).
If you are importing line level attachments, you must also include the Record
 Type and invoice line number for the line attachment records.
For example, in the two attachment records highlighted below, record type APLB
 indicates that the attachment record is a line level attachment. The "1"
 shown after each record type indicates the attachment applies to invoice
 line "1" (of the associated invoice header).

For more information about setting up import templates to
 include attachments, see the Delimited File Format
 section of [About Import File Formats](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/about-import-file-formats).
Note: The APEnty and APEntryDetail import forms allow
 you to create templates that import invoice header records and
 invoice line (detail) records separately. However, you can import
 both header and detail records together by creating a single
 template that uses the APEntry import form, and then selecting the
 Multiple Table Import checkbox to indicate you are updating more
 than one table. You must then add the APLB record type (for invoice
 lines) to your template using the Record Types tab. The APLB
 identifiers will then appear in the template detail (Template Detail
 tab).[About Import File Formats](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/about-import-file-formats)
