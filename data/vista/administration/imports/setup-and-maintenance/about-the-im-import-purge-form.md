---
title: "About the IM Import Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-import-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-import-purge-form"
---

# About the IM Import Purge Form

Use this program to purge both templates and import IDs.
To purge a template, select the Import Template Purge radio button and specify the template to purge in the Import Template field. Click the Purge button. The purge process will delete all record of the template, including the template header (IMTH), template detail (IMTD), record types (IMTR), and cross-references (IMXH, IMXD). Additionally, the process will delete any pending imports in IM Work Edit (IMWH, IMWE) or IM Upload that are associated with the template.
To purge a specific import ID, select the Import ID Purge radio button and specify the template and import ID to purge in the Import Template and Import ID fields. Click the Purge button. The purge process will delete the specified import ID for the specified template from IM Work Edit (IMWH, IMWE); however, the import template is left intact.

Related information

- [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems)
