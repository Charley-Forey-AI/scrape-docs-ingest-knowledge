---
title: "About Import Template Cross-References | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-import-template-cross-references"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-import-template-cross-references"
---

# About Import Template Cross-References

You must set up cross-references (such as phase, cost type,
 and unit of measure) for your import templates to ensure your import data is correctly
 translated.
You will use the Phase Cross-Ref, Cost Type Cross-Ref, UM Cross-Ref, Material Cross-Ref,
 and Vendor Cross-Ref tabs to define the cross-references used during the import process
 to translate the raw data coming from the import file into Vista software values.
For example, if your import phase codes differ from those set up in the JC
 Phases, you can cross-reference each import phase code to the appropriate Viewpoint
 phase code. When data is uploaded into PM, the import phase codes will be replaced by
 the cross-reference codes.
Cost type cross-references are set up the same as any other cross-reference; you specify
 the import code that you are cross-referencing and the appropriate Viewpoint code.
However, because estimating data is
 generally at a much more detailed level than accounting, you may find it necessary to
 consolidate some of your import cost type codes into a single Viewpoint code. To allow
 consolidation of these cost types without duplicating the units associated with them, a
 Cost Only option is included to allow you to roll up only the costs, not the units. For
 example:
Import Code
Cost Type
Cost Only

Labor
1 (Labor)

Burden
1 (Labor)

Once you have completed defining
 import/upload parameters and code cross-references, you must then define the
 specifications for the individual record types included in the import file (i.e.
 contract items, phases, cost types, subcontract detail, material detail, and estimate
 information). This is done using the PM Import Estimates Detail form, which is accessed
 by clicking the Detail button above the tab pages.
