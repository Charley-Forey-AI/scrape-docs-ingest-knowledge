---
title: "About Import Template Edit/Upload Parameters | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-import-template-editupload-parameters"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-import-template-editupload-parameters"
---

# About Import Template Edit/Upload Parameters

This tab is used to define how the system treats
 missing/incorrect cross references when importing the raw data, as well as how specific data
 (vendors, change orders, and standard item codes) is handled when uploading data into the
 Project Management tables.
The "Create cross reference record when
 missing" section allows you to specify whether to create cross-reference records for
 phases, cost types, units of measure, vendors, and/or materials when correcting errors
 found in the PM Edit Import Data form. For each of the cross reference options, you can
 specify whether to always create a cross-reference record, never create a
 cross-reference record, or to prompt for cross-reference records.
The Upload into Project Management Options section
 allows you to specify how certain information will be handled during the upload of
 imported data into Project Management. The Create Project Firm record for each vendor set up
 in firm master checkbox controls whether the upload process will
 automatically generate a project firm record (in PM Project Firms) for each vendor in
 the subcontract or material work tables. If checked, a project firm record will only be
 generated if the vendor is already set up in the PM Firms and at least one contact is
 set up for that firm. If multiple contacts are defined, the vendor will be set up in PM
 Project Firms with the first contact specified in the Firm Master. If this option is not
 checked, these vendors would need to be set up manually in PM Project Firms.
You also have the option to have the upload
 process create a change order item for each contract item that is uploaded for a change
 order. If you elect to use this option, you can then also have each contract item’s
 amount set as a fixed amount for the resulting change order item in the Totals screen.
The Create Standard Item Codes checkbox
 allows you to have the upload procedure add standard item codes to the JCSI (JC Std Item
 Codes) table if they do not already exist for the region. There must be a region on file
 for this feature to work.
