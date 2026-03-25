---
title: "Creating Document Routing Status Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-workflow/document-review-process/creating-document-routing-status-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-workflow/document-review-process/creating-document-routing-status-codes"
---

# Creating Document Routing Status Codes

Prior to initiating a document review process, you will need to create routing status codes.
Reviewers can use this codes to define where the document is in the approval process. You will use the DM Document Routing Status form to create these status codes.
The following details how to create document routing status codes.

1. In the Status Code field, enter a code, up to 6 characters,that identifies a status or stage in the review process (for example: New, Reject, etc.).

1. Enter a description of the code in the Description field.

1. Enter a sequence number for the code in the Sequence field. This number determines the order in which the status codes will be displayed in the Status drop-down field on the DM Document Review form. For example, you might call sequence number 1 "New".Tip: If you have several status codes that are used on a regular basis, you may assign them a lower sequence number than those status codes that are rarely used. This ensures that the frequently used codes are at the top of the list in the Status drop-down and the rarely used codes are at the bottom.

1. If this is the first status, check the Beginning Status box.Note: You can only check this box for one status code at a time, and the status is automatically assigned to each reviewer that is added to a document. If you need to assign the Beginning status to a different code, uncheck this box for the original code and then check it for the new code.

1. If this code represents a final status, check the Completed Status box.Note: You can assign this status to as many codes as you want. This status determines whether documents will display on the DM Document Review form when a user has checked the Hide Completed Items box.
Note: If the code represents a stage in the review process that is neither a beginning or completed status, do not check either the Beginning Status or the Completed Status box.

1. Save the record as normal.

Related information

- [Document Review Process](/en/vista/vista/system-tools/document-management/dm-workflow/document-review-process)
