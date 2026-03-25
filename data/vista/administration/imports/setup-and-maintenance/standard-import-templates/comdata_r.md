---
title: "COMDATA_R | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/comdata_r"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/comdata_r"
---

# COMDATA_R

This is a "direct import" template for importing reconciliation files from Comdata for credit service payments.
Imports using this template will insert new records only; updates to existing records do not occur.
The Virtual Card Invoice Number field
 found in the Comdata files holds both the CM Company and CM Reference. This field is
 populated during the creation of the PS20 file (in AP Credit Service Download). When you
 import the reconciliation file from Comdata, the first three characters populate the
 CMCo (Company) field and the remaining characters populate the ChkNo (Check Number)
 field.
