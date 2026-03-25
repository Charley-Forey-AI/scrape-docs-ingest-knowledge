---
title: "Cross-Reference Types | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/document-index-cross-references/cross-reference-types"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/document-index-cross-references/cross-reference-types"
---

# Cross-Reference Types

There are three types of cross-references that you can create in the system: module, form, or global.
Module cross-references are used when the master column name applies to multiple modules where the related column name differs from the master column name. For example, the master column name "JCContractItem" has the same meaning as the "Item" column in forms in the AR, JB, JC, and PM modules. In this case, you would set up the cross-reference as displayed in the following table. When adding documents, the cross-reference will apply to all forms in these modules.
Module
Form
Column Name
Description

AR
N/A
Item
Contract Item

JB
N/A
Item
Contract Item

JC
N/A
Item
Contract Item

PM
N/A
Item
Contract Item

Form cross-references are used when the master column name applies to one or more forms where the related column name does not match the master column name. For example, master column PMSMPItem applies to several forms: PM Submittals - 6.5, PM Meeting Minutes, PM Punch List, and PM Punch List Detail. In this case, the PMSMPItem column has multiple meanings; that is, it represents the submittal item, meeting minutes item, or punch list item. In this case you would set up the cross-reference as displayed in the following table. When adding documents, these cross-references will apply to these forms only.
Module
Form
Column Name
Description

PM
PMSubmittal
Item
PM Submittal

PM
PMMeetingMinutes
Item
PM Meeting

PM
PMPunchList
Item
PM Punch List

PM
PM PunchListDetail
Item
PM Punch List

Note: You are not required to specify the module on form level cross-references.
Cross-references can also be set up at a global level, without a module or form specified. This type of cross-reference applies to all modules and forms.
