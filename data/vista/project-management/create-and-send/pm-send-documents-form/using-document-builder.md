---
title: "Using Document Builder | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/create-and-send/pm-send-documents-form/using-document-builder"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/create-and-send/pm-send-documents-form/using-document-builder"
---

# Using Document Builder

Use the Document Builder launched from the PM Send Documents form to configure how the generated documents, attachments, and reports will be organized in the email sent to the project contacts.
This is part of the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature.
Follow the steps below to configure how the project documents (RFIs, submittals, etc.), reports, and attachments included in the email will be organized into a single PDF, or multiple PDFs. Once the set up is complete, you can preview how the PDF(s) will appear.

1. Open the Documents tab on the PM Send Documents form.

1. By default the Collate into a single PDF document box is checked. Leave this box checked if you want all of the documents, reports, and attachments included in the email to be combined into a single PDF document. If you uncheck this box, the system will create a separate PDF for each generated document and report on the Documents tab. The associated attachments will also be added to the communication as separate documents (standalone attachments).
You can also use the Document Builder to group the attachments with a document or report. This will be covered later in this process.

1. Click the Document
 Builderbutton to configure the PDF that is included in the
 email. This will open the PM Send Document Builder form.

1. Drag and drop the items on the Document Order tab to change the order of the items included in the PDF. The records associated with the documents and reports will display
Each record associated with a generated document and
 report included in the email (the documents and reports on the Documents tab
 of the PM Send Documents form) will display as a separate item on the tab.
 For example if the email includes an RFI and subcontract document, and a
 change order report, the RFI, subcontract, change order record associated
 with those items will each display as a separate item in the tab.
The selected attachments associated with those records will also display
The selected attachments that are associated with
 the records will also display on the tab. These are the attachments that
 were selected using the Attachments tab on the PM Send Document form.

- The attachments grouped with a generated document or
 report will be added to the end of the generated PDF. For example an
 attachment that is grouped with an RFI will be added to the end of the
 PDF document generated for the RFI.

- The attachments in the Standalone Attachments section will be added to the email as separate files.

- Drag and drop the attachments to change how the documents, reports, and attachments will be included in the email.

1. Select a file on the Document Order tab and then use the Options section to set the print options. Orientation and Scaling fields enable based on the type of file selected
The Orientation and
 Scaling fields are enabled based on the type of file that
 is selected.

- Orientation - .bmp, .gif, .jpeg, .jpg, .msg, .tif, .tiff, .txt, .png

- Scaling - .bmp, .gif, .jpeg, .jpg, .tif, .tiff, .txt, .png, .xls, .xlsx.

-

1. Use the Document Layout tab to configure the headers and footers, table of contents, and page numbers on the PDF.

1. Use the
 Include drop down to
 select what will be included in the PDF. If you include a header and/or
 footer, they will display on every page of the PDF, including the table
 of contents and cover page.

1. Use the
 Header and Footer fields to customize the header and footer of the
 PDF. These fields are enabled/disabled based on the selection in the
 Include field.

1. Check the Include Table of Contents box if the PDF should include a table of contents. Each item on the Document Order tab will display as an unique entry on the table of contents. Users will be able to click on these entries to jump to specific items.

1. Check the Show Page Numbers box to include page numbers on the PDF. This will enable the Page Number Alignment field to select where the page number will be placed.

1. Use the Document Cover
 tab to add a cover page to the PDF. If you included a table of contents in the
 PDF, the cover page will display before the table of contents.Check the Include
 Document Cover box and then enter the information that
 should display on the cover page in the section in the lower portion of the
 tab.

1. Click OKto save your changes and close the Document Builder. This will
 return you to the PM Send Documents form.

File name of the PDF
The file name of the PDF is set up using the [PM Create & Send Settings](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form) form (Info> Document File Naming Convention section). [More](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form/field-definitions-pm-create-and-send-settings-form#ID-00025e18--en)

1. Optional: Use the
 Tasks drop down at the top of the PM Send Documents form to
 preview, save, or attach the document. There are several options in the
 Tasks drop down at the top of the PM Send Documents form.

- Save
 Document As - Generate and save a PDF document.

- Attach
 to source - Generate a PDF and attachment it to the
 source record. The source record is the record that was used to launch
 the PM Send Documents form. For example if you select a submittal in the
 PM Submittal Register form and then launch the PM Send Document form,
 the submittal that you selected on the PM Submittal Register form is the
 source record.

- View Document - Generate and view a PDF document.
What is included in the
 PDF?

- The Collate
 into single PDF document box on the Documents tab of the
 PM Send Documents form determines what is included in the PDF generated
 by the Save Document As,
 Attach Document To
 Source, and View Document
 options.

- When
 Collate into single PDF document is checked - All of the
 documents and reports on the Documents tab of the PM Send Documents form
 are generated and compiled into a single PDF. The attachments selected
 on the Attachments tab of the PM Send Documents form are also included
 in the PDF unless they are set up as standalone attachments using the
 Document Builder (Doc Builderbutton on
 the Documents tab).

- Note:To set up an attachment
 as a standalone, click on the Doc Builder
 button on the Documents tab of the PM Send Documents form. This will
 open the PM Send Document Builder form. Open the Document Order tab,
 and then drag and drop the attachment down to the Standalone Attachments section.

- When
 Collate into a single PDF document is not checked - When
 the Collate into single PDF
 document box is not checked, only the document or report
 that is selected on the Documents tab of the PM Send Documents form is
 included in the PDF. The attachments selected on the Attachments tab of
 the PM Send Documents form that are associated with the document or
 report are also included in the PDF unless they are set up as standalone
 attachments using the Document Builder (Doc
 Builder button on the Documents tab).

Related information

- [About the Create and Send Feature](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)

- [PM Send Documents Form](/en/vista/vista/project-management/create-and-send/pm-send-documents-form)
