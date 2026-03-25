---
title: "Customize a Template Using MS Word | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/create-and-send/about-creating-a-document-template/customize-a-template-using-ms-word"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/create-and-send/about-creating-a-document-template/customize-a-template-using-ms-word"
---

# Customize a Template Using MS Word

You can format and update the actual document associated with a document template
 using MS Word. This is especially important if you have added or removed merge fields and/or
 table merge fields on the document template.
To format and update your document:

1. Open PM Create & Send
 Templates, highlight a template on the Grid tab, and click the Edit
 Template button. This will open the selected template in MS Word. Note: Templates can only be edited by one user at a
 time. If another user is already working on the template, the top of the form will
 display ‘Read-Only’. You will be able to make changes to the template, but you
 won't be able to save them to the correct file name.

1. Format the appearance of the
 document, for example change the formatting of the text or add a logo just like you
 would on any other MS Word document.Note: If you have an existing document, paste it into the top
 of the MS Word file. For example, if you are creating a new subcontract document,
 paste your existing subcontract document into the top of the MS Word document.
 Once it has been inserted, cut and paste the applicable merge fields from the
 standard document into your existing document.

1. The set up in PM Create
 & Send Templates defines what information will be passed to the document when it
 is generated, and the merge fields on this document are placeholders for that
 information. This means if you made changes to the Merge Fields tab of PM Create
 & Send Templates, you should also update the document. For example, if you
 removed the job site address information using PM Create & Send Templates, you
 should also remove those fields from the actual document - the job site address merge
 fields won't display anything since the job site address information won't be passed
 to them.

1. Removed Merge Fields - If you removed a field
 from the template using the Merge Fields tab of PM Create & Send Templates,
 you should also remove the field from the document since it will not display
 any information. To remove a merge field, highlight the merge field and field
 label and press deleteIf you remove a merge field from the
 document but it is still included on the Merge Fields tab of PM Create &
 Send Templates, the document will still print.

1. Add Merge Fields - If you added a merge field to
 the Merge Fields tab of PM Create & Send Templates, you can also add it to
 the document using the Insert Merge Field option in the MS Word toolbar. The
 Insert Merge Fields option provides a list of fields that you can add to the
 template. The fields on the list are the merge fields defined on the Merge
 Fields tab of PM Create & Send Templates. (Table Merge Fields are not
 included in the Insert Merge Fields list.)

1. Edit the MS Word Item Table
 - If you modified the MS Word item table on the Table Merge Fields tab on PM Create
 & Send Templates, you must update the table on the document. An MS Word item table is a table on the
 document that will populate with detail information included on the Table Merge
 Fields tab of PM Create & Send Templates. There are three things you should
 consider when editing a MS Word item table:

1. The MS Word item table is defined using the
 Word
 Item Table field on the Info tab of [PM Create & Send Templates](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form). The value in
 this field determines which table on the MS Word document will populate with
 the detail items. For example, if there is a "1" in this field the detail
 information will populate in the first table on the MS Word document. If there
 is a "2" in this field the detail will populate in the second table on the MS
 word document.If you add a table to the document, make sure you update the
 value in the Word Item Table field.

1. The Merge Order field on the
 Table Merge Fields tab on PM Create & Send Templates determines the order
 that information will populate in the table. [More](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form/field-definitions-pm-create-and-send-templates-form#ID-0002610a--en)

1. The number of fields on the Table Merge Fields
 tab of PM Create & Send Templates must match the number of columns in the
 MS Word item table. If you added or removed a field on the Table Merge Fields
 tab, you need to update the MS Word item table.For example, if there are only three
 columns in the table but there are four fields on the Table Merge Fields tab,
 the table will populate incorrectly. Se example below. To fix this problem, add
 a column to the MS Word table or remove an item from the Table Merge Fields tab
 of PM Create & Send Templates.
Table 1. Table Merge Fields tabColumn Name
Merge Order

Item Number
1

Item Description
2

Item Cost
3

Item Units
4

Table 2. Table on the Document TemplateItem Number
Item
 Description
Item Cost

Merge Order
 #1
(Item
 Number)
Merge Order
 #2
(Item
 Description)
Merge Order
 #3
(Item Cost)

Merge Order
 #4
(Item Units)

1. Save the template and close
 MS Word. Do not change the file name or location of the MS Word file when you save
 it.

1. Now that you have created a
 custom version using the standard, you can set the standard template to 'inactive' so
 that it won't display in the template selection form. For example, if you created a
 custom RFQ, you can deactivate the standard RFQ so users don't accidentally use it
 instead of the custom RFQ. Open the standard template in PM Create & Send
 Templates and uncheck the Active Template box on the Info
 tab.

1. Use the Create & Send
 feature to create a document from the new template.

You can now use your template to test generating a project
 document. For more information, see [Test Your Document Template](/en/vista/vista/project-management/create-and-send/about-creating-a-document-template/test-your-document-template).
