---
title: "User Defined Forms and Lookups Integration with Field View | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/user-defined-forms-and-lookups-integration-with-field-view"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/user-defined-forms-and-lookups-integration-with-field-view"
---

# User Defined Forms and Lookups Integration with Field View

Using Viewpoint Field View™, Viewpoint Team™, and Vista™, you can create Field View form templates from Vista User Defined (UD) forms, and Field View predefined answers from Vista UD lookups, and keep your data in sync across all applications.
When you convert a Vista UD form to a form template in Field View, once you update the form in Field View and change the status to Closed, the updates are written back to the corresponding UD form in Vista every five minutes. If you need to make subsequent updates to the Field View form template, you can do so. When you change the status back to Closed, the updates will write back to Vista. This allows you to maintain Vista as the single source for up-to-date data.
Converting Vista UD lookups to predefined answers in Field View enables you to use data from Vista tables with Form templates created in Field View. For example, A UD lookup based on a Vista equipment table could be used on a safety form created entirely in Field View.
Note: Take note of the following limitations:

- Only UD forms and UD lookups can be converted to Field View form templates and predefined answers at this time; standard (non-UD) forms and system (non-UD) lookups cannot.

- Once Field View forms have been written back to Vista, updates to the form in Vista do not result in automatic updates to the form or lookup table in Field View.

- Parameter-based lookups (any lookup that includes a question mark parameter) in a Vista UD form do not convert to the form template in Field View. For details, see [System Requirements](/en/vista/vista/administration/user-database/user-defined-forms-and-lookups-integration-with-field-view/system-requirements).

- The UD Datatype "bTime" is not supported at this time. If a UD field is set up with a Datatype of "bTime," after it is converted to Field View, it will not write back correctly to Vista.
