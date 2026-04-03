---
title: "Document Imaging Installation - Security | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/document-imaging/installation-overview/document-imaging-installation---security"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/document-imaging/installation-overview/document-imaging-installation---security"
---

# Document Imaging Installation - Security

This tab is used to establish the installation parameters for individual Document Imaging users. The fields listed in the top half of this tab will serve as defaults for any future operators that are assigned to this company. The fields in the lower half of the tab show any individual overrides for the same fields (in other words, the default may be set to grant all future users "Read/Write with Annotations" permission, but the operator's individual settings may be more restrictive and allow for "Read only" permission).
It is important to understand how Spectrum operator security limits access to document images. Image files in Spectrum are accessible only from Spectrum menu choices and these menu choices are restricted according to the normal Spectrum security setup. For example, if a user does not have access to Payroll functions, then that user will not have access to the screens in which Payroll transaction images would be accessed. Similarly, if you are using job-based security to control access to Job Cost inquiries for specific jobs for specific users, this will also control access to the related document images (for example, Accounts Payable invoices, purchase orders, and time cards).
Fields/ButtonsDescriptions
New operator security levelSelect the security level you want to assign to future operators when viewing or editing images.

- 0. None - The user cannot view or change image files; the Slider Bar does not display.

- 1. Read only - The user can only view image files; the Slider Bar displays but the Annotation and Page Manipulation options are not available.

- 2. Read with Annotations - The user may make annotations on files; the Slider Bar displays but the Page Manipulation options are not available.

- 3. Read / Write with Annotations - The user can add, change, delete, or annotate image files; the Slider Bar displays along with the Scan, Attach, and Batch buttons. The Annotation and Page Manipulations options are also available.

Note: Only the System Administrator should change a user's default security level.

Settings buttonSelect to open [Operator Security](/en/spectrum/spectrum/tools/document-imaging/installation-overview/operator-security).

Restore buttonSelect to reset the selections and search results to the original defaults (usually blank or ALL).
