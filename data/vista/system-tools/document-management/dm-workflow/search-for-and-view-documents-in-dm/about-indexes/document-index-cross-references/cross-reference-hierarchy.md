---
title: "Cross-Reference Hierarchy | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/about-indexes/document-index-cross-references/cross-reference-hierarchy"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/about-indexes/document-index-cross-references/cross-reference-hierarchy"
---

# Cross-Reference Hierarchy

When adding document to the system, cross-references are applied based on the following hierarchy:

1. If a cross-reference exists at the form level, use it.

1. If a cross-references does not exist at the form level, check the module level. If one exists, use it.

1. If a cross-reference does not exist at the module level, check for a direct match (e.g., APCo = APCo, ARCustomer = ARCustomer, etc.). If one exists, use it.

1. If a direct match is not found, check for a pattern match (e.g. APCo = Company or Company = APCo, etc.). If one exists, use it.

1. If a pattern match is not found, check for a global match (i.e. cross-references with no module or form specified). If one exists, use it.

1. If a global match is not found, do not include.

Related information

- [Creating Document Index Cross-References](/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/about-indexes/document-index-cross-references/creating-document-index-cross-references)
