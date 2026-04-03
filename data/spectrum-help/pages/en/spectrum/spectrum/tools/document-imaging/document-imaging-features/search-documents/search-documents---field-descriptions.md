---
title: "Search Documents - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/document-imaging/document-imaging-features/search-documents/search-documents---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/document-imaging/document-imaging-features/search-documents/search-documents---field-descriptions"
---

# Search Documents - Field Descriptions

Click the Search button and the Search Images window displays. Use this table as a reference when completing the fields in the window. In addition, A 'Create date' and 'Latest revision' columns will display on the main Search Documents screen. These columns let you know when the transaction was created and the last date it was revised.
Fields/Buttons
Descriptions

Cabinet
Enter a cabinet code, or select from a list of valid cabinets.
The following cabinets are pre-defined:

- Archive Reports

- Cash Management

- Components

- Contracts

- Customer

- Employee

- Equipment

- Fixed Asset

- GL

- Insurance

- Items

- Job

- Projects

- Scale

- Site

- Subcontracts

- Titles

- Vendor

- WO
In addition, you can set up your own cabinets in the [Cabinet File Maintenance](/en/spectrum/spectrum/tools/document-imaging/document-imaging-features/cabinet-file-maintenance) screen.

Drawer
Enter a drawer, or select from a list of valid cabinets.

Folder
Enter a folder, or select from a list of valid folders.
Folders located in the G/L cabinet are designated with the year and month (for example, 00/12).

- In order to designate specific folders, you must enter two forward slash marks (for example, 01//01).

- In order to search for a range of entries (for example, 01/12-03/13) using the SuperSelect option you would need to type 01//12/03//13.
Note: If you try to open the Search window while searching on an invalid cabinet, an error message will display.

Created by
Enter an operator code, or select from a list of valid operators.

From/to create date
Enter the transaction date range that you want to search. Leave the 'From' field blank to use the earliest system processing date.

Image description
Enter a partial description of the image you wish to locate.

Contains the words
This field is only relevant if OCR indexing is enabled in the [Full-text Indexing Setup (FTI)](/en/spectrum/spectrum/tools/document-imaging/document-imaging-features/full-text-indexing-setup-fti) screen.
Enter any identifying words from the document you would like the software to search for. For example, if the document name was "INVOICE 524," you could simply type the vendor's name or the invoice number or date, and more.
Note: Full-text indexing does not work for keywords, image descriptions, or annotations added in Document Imaging.

Keywords
Enter a keyword to search for. If no keywords are specified, and if the Any of these keywords option is selected on the right of the screen, then all of the items will display.

Include records containing
Select to include records containing either all or any of the keywords entered in the Keywords field.

The following table describes the buttons and resulting actions found on the main Search Documents screen.
Buttons
Action

New button
Click this button to open the [New Document](/en/spectrum/spectrum/tools/document-imaging/document-imaging-features/new-document) screen in a separate Spectrum tab.

Listing button
Click this button to open the Document Listing window where you can designate the desired Crystal Report format and choose to Preview, Export, or Distribute the report.
 If you click the Distribute button, the Export Report and Image Files for
 Distribution window opens. As the window states, the update creates a zip
 file on your server that includes a Crystal Reports format version of the
 report and image files. If you don't already have it installed, you will
 want to download and install the [free SAP Crystal
 Reports Viewer](http://www54.sap.com/solutions/sme/software/analytics/crystal-reports-viewer/index.html).
