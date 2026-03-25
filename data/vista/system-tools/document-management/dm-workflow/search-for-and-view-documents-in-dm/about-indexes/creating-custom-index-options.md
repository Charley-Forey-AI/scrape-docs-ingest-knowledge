---
title: "Creating Custom Index Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/about-indexes/creating-custom-index-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/about-indexes/creating-custom-index-options"
---

# Creating Custom Index Options

When searching for documents (DM Attachment Index Search
 form), you can enter specific criteria in the form fields to narrow the number of documents
 returned.
For example the standard AP module indexes are AP company, vendor group, vendor, AP reference #, and AP check. You may find that you would like to search using an additional option. If you also want to index and search attachments by the tax id number associated with vendors, you can create a custom index option for the tax id # and then refresh the indexes so that it is automatically added to all of the relevant documents.
Creating a custom index option has two basic steps: creating the new index option using the DM Index Cross Reference form, and then refreshing the indexes using the DM Attachment Index Refresh form which will automatically add the new option to all of the relevant documents.
The following steps detail how to create a custom index options.

1. From the DM Programs folder in the Main Menu, select the DM Index Cross Reference form.

1. Press F4 in the Master Column Name field and select one of the UserCustom fields.Note: There are only five UserCustom fields. This means that you have a limit of creating five custom index criteria options.

1. Select the New Record icon () at the top to create a new record in the grid.

1. Enter the module for the new index option in the Module field. For example, enter AP if you are creating a new index option to track the tax id # associated with AP module vendors.

1. Use the Form and Column Name fields to select
 the column that you want to add to the index. For example, if you are creating a
 custom index for the tax id# that displays on the AP Vendors form, use
 F4 to select APVendMaster in the Form field and then enter TaxId in the Column
 Name field. Tip: You cannot use the F4 key from the Column Name field. To
 determine what to enter in this field, locate the field that you want to use
 as an index option and press F3 to open the Field
 Properties form. The name of the field will display in the Column
 Name display field at the top of the Field Properties form.
 Enter that name in the Column Name field on the
 DM Attachment Cross Reference form.

1. Save the record as normal.

1. From the DM Programs folder, select the DM Attachment Index Refresh form.

1. In the Modules with Attachments section, select the module for updating documents . For example, if you are creating a custom index for the AP vendor tax id, check the AP box. This means the system will refresh all indexes for all documents associated with the AP module.Tip: You can select All to check all of the module boxes. You can also select None to uncheck all of the boxes.

1. Select Refresh Indexes.  The status bar indicates the refresh progress. Note: Depending on the number of attachments that you have selected, this process can take several minutes. If you need to stop the process for any reason, select Stop.

1. When the process is complete, select Close to close the form. When searching for documents (DM Attachment Index Search) you can now use the relevant fields on the Custom tab. For example, if you used the UserCustom1 field for the custom index option (step 2 above), you can use the Custom 1 field in DM Attachment Index Search to search for documents using your custom option.
Tip: If you want results for the custom field to display in the Results grid of DM Attachment Index Search, you might have to set the grid options appropriately. For more information, see [Viewing Document Search Results](/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/about-organizing-document-search-results).
