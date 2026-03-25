---
title: "Field Definitions: DM Document Routing Status Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-workflow/document-review-process/about-the-dm-document-routing-status-form/field-definitions-dm-document-routing-status-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-workflow/document-review-process/about-the-dm-document-routing-status-form/field-definitions-dm-document-routing-status-form"
---

# Field Definitions: DM Document Routing Status Form

The following is a list of field descriptions for the DM
 Document Routing Status form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Status Code

 Enter a code, up to 6 characters, that uniquely identifies this status. It is suggested the code easily identify a stage in the review process (e.g. New, In Rev, Rescan, Complt, etc.).

##  Description

 Enter a description of this status code, up to 30 characters. This description displays in the drop-down menu when selecting status codes for attachments in DM Attachment Review.

##  Sequence

 Enter a sequence number (0 – 2,147,483,647) for this status code. The assigned sequence number determines the order in which the status code displays in the drop-down menu when associating status codes to attachments in DM Document Review. For example, if you want the Beginning status code to display first in the list, you would assign it a sequence of “0” or “1.” If grouping status codes together, you might assign codes without a specified status to sequences 2 – 10, and Completed status codes to sequences 11 – 20.

## Beginning Status

Check this box to identify this status code as the “beginning” status code. Only one status code can be assigned this status, so make sure you check this box for the most appropriate status code. The status code with this option checked is automatically assigned to each document when they are assigned a reviewer in DM Document Routing.
Do not check this box if this status code should not be used as the “beginning” status code, or if a status does not apply to this status code.

##  Completed Status

 Check this box to identify this status code as a Completed status code. Although you can assign this status to multiple status codes, you may want to limit the number of assignments. Checking this option determines visibility in the DM Document Review grid when using the Hide Completed Item option.
 Do not check this box if this status code should not be used as a Completed status code, or if a status does not apply to this status code.
