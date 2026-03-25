---
title: "Document Index Cross-References | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/document-index-cross-references"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/document-index-cross-references"
---

# Document Index Cross-References

When you attach a document to a data record, the system automatically adds an index record to the document.
An index enables you to search for the document when you don't know the exact location of the document in the system, but know some data about the document. You can also add indexes to unattached documents (stand alone or deleted) to help assist in finding those types.
The DM Attachment Index form lists the standard fields (master column names) for assigning index values, but there are some cases where a form field has the same purpose as a field in the DM Attachment Index form, but the database column names are different. In this case, a cross-reference must be added to associate the two fields/columns together.
For example, when attaching a document to an AP invoice record, an index is created based on the invoice's header and line detail. This index contains the invoice's AP company, vendor group, vendor, AP reference number, and check number (if applicable). In this example, the Check # field in AP Transaction Entry is associated with the AP Check Number field in DM Attachment Index. However, the database column name for Check # is "PrePaidChk", whereas the column name for AP Check Number is "APCheckNumber". In this instance, a cross-reference is needed to associate the two columns together.
Vista™ comes preloaded with all the necessary index cross-references for standard fields. However, there may be times where you will need to create your own cross-references. Typically this will occur when you create a custom field on a form, or you have created a UD form with a field that represents the same information as a standard field that has an index. When you create the cross-reference with the DM Index Cross Reference form, the system will search and display documents associated with the master column name. Using the example above, when you searched for a specific AP check number, the system will display documents associated with both the "APCheckNumber" and "PrePaidChk" database column names.
