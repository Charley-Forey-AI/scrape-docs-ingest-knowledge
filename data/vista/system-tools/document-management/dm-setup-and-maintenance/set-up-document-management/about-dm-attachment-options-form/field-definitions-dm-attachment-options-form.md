---
title: "Field Definitions: DM Attachment Options Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/about-dm-attachment-options-form/field-definitions-dm-attachment-options-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/about-dm-attachment-options-form/field-definitions-dm-attachment-options-form"
---

# Field Definitions: DM Attachment Options Form

The following is a list of field descriptions for the DM
 Attachment Options form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Attachment Storage Location

Select a storage location for scanned images.

- File System – Select this option to store images in a specified location on your network directory.

- Database – Select this option to store images in the Viewpoint database or a separate document database.

## Root Directory

Specify the root directory for storing scanned documents. If everyone in your company is mapped to the network share using the same drive letter, you can reference this directory by a mapped drive (for example, V:\ScannedDocs). Otherwise, you must reference the directory using the UNC path (for example, \\server\ScannedDocs).
Note: It is recommended that you do not place the root directory in the Viewpoint directory, or use the Viewpoint directory as the root directory.
This is the directory in which scanned documents are stored . The options selected in the ‘Subdirectory Structure’ section below are used to create subdirectories within the root directory.

## By Company

Check this box to store documents by company. If checked, documents will be stored in subdirectories (of the root directory) named 'Company' followed by the company number.
Example:
\\server\Viewpoint\Scanned Docs\Company1
\\server\Viewpoint\Scanned Docs\Company2
Do not check this box if you do not want to store documents by company. Doocuments will be stored in the root directory unless you specify to use any of the other subdirectory options.
Note: If you elect to use multiple subdirectory options, subdirectories follow the order in which these options are listed. For example, if you check all options, subdirectory structure will look like this:
\\server\Viewpoint\Scanned Docs\Company\Module\Form\Month
If you wish to change the order in which the subdirectories are created, use the Custom option below.

## By Module

Check this box to store documents by module. If checked, documents will be stored in subdirectories (of the root directory) based on module.
Example:
\\server\Viewpoint\Scanned Docs\AP
\\server\Viewpoint\Scanned Docs\AR
Do not check this box if you do not want to store documents by module. Documents will be stored in the root directory unless you specify to use any of the other subdirectory options.
Note: If you elect to use multiple subdirectory options, subdirectories follow the order in which these options are listed. For example, if you check all options, subdirectory structure will look like this:
\\server\Viewpoint\Scanned Docs\Company\Module\Form\Month
If you wish to change the order in which the subdirectories are created, use the Custom option below.

## By Form

Check this box to store documents by form. If checked, documents will be stored in subdirectories (of the root directory) based on form names.
Example:
\\server\Viewpoint\Scanned Docs\APUnappInv
\\server\Viewpoint\Scanned Docs\ARInvoiceEntry
Do not check this box if you do not want to store documents by form. Images will be stored in the root directory unless you specify to use any of the other subdirectory options.
Note: If you elect to use multiple subdirectory options, subdirectories follow the order in which these options are listed. For example, if you check all options, subdirectory structure will look like this:
\\server\Viewpoint\Scanned Docs\Company\Module\Form\Month
If you wish to change the order in which the subdirectories are created, use the Custom option below.

## By Month

Check this box to store documents by month. If checked, documents will be stored in subdirectories (of the root directory) based on the month/year.
Example:
\\server\Viewpoint\Scanned Docs\05-2011
\\server\Viewpoint\Scanned Docs\06-2011
Do not check this box if you do not want to store documents by month. Documents will be stored in the root directory unless you specify to use any of the other subdirectory options.
Note: If you elect to use multiple subdirectory options, subdirectories follow the order in which these options are listed. For example, if you check all options, subdirectory structure will look like this:
\\server\Viewpoint\Scanned Docs\Company\Module\Form\Month
If you wish to change the order in which the subdirectories are created, use the Custom option below.

## Custom

Check this box to store documents based on a customized subdirectory structure using one or more of the available subdirectory structure options (above). In the space provided below, define the subdirectory structure to use.
Do not check this box if you are not using a customized subdirectory structure. Images will be stored in the root directory or in subdirectories based on options selected above.

## Custom (Text Box)

Define the subdirectory structure to use for storing scanned documents. You can include any combination of the available subdirectory options and place them in any order desired, separating each option with a backslash (\). When adding subdirectory options, they should be entered as follows:
 Company = %C  Module = %M  Form = %F  Month = %D
For example, if you want subdirectories by Month, Company, and Module, set up the subdirectory structure as follows:
%D\%C\%M
You can also combine variables to create a single folder. For example:
%C\%M - %D
This would give you a subdirectory similar to this: main directory\Company1\AP – 05-2008
Note: This field is inaccessible if you do not check the
 Custom box; however, it will display the results of the subdirectory
 options you select.

## Scanning File Format

Select the default file format for scanned images.

- TIF

- PDF

##  Use .JPG Files for Single Page Color Documents

 Check this box if you will be scanning single-page color documents. If you scan multiple pages, or if the single-page document is black and white, the system will automatically scan in TIFF format.
 Do not check this box if you want scanned images to always be in TIFF format. This is the standard format used for multiple-page scanning.

## PDF View Resolution

Enter the view resolution value for PDFs that
 display in the DM Document Viewer, Batch Scan Viewer, and Single Scan Viewer. Click
 Use
 Default to reset this field to its default of 120 dpi (dots per inch).

##  Use Viewpoint Viewer

 Check this box to enable the DM Document Viewer. This viewer allows you to view TIF, JPG, and PDF files from within the system. If you do not check this box, the system uses the default viewer to open documents.

## Retain Attachments after Record Delete

Check this box if the system should keep a document when the associated data record is deleted - for example if you delete an RFI, any attachments associated with that RFI will stay in the system as stand alone documents. See [Document States](/en/vista/vista/system-tools/document-management/about-document-states) for more information on stand alone documents and other document states.
This functionality works only for maintenance forms, not batch processing forms.

## Archive Deleted Attachments

Select this checkbox if the system should save a document when it is deleted. The system will assign it a document status of Deleted, but it can still be viewed using the [DM Attachment Index Search ](/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/about-the-dm-attachment-index-search-form) form.

## Use Attachment Auditing

Check this box to have the system keep an audit record for this document. The audit record is available on the Log tab of the Attachment form.
