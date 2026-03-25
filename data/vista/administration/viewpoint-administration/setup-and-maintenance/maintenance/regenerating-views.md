---
title: "Regenerating Views | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/regenerating-views"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/regenerating-views"
---

# Regenerating Views

When you activate or update datatype security, you should regenerate views to update all tables with the security changes.
The VA View Generator form displays two list boxes: Available Views and Views to Regenerate.To regenerate views:

1. Click Add Unsynchronized Views.The Views to Regenerate list box displays all tables for which the Apply Security box is checked in the VA Data
 Security Setup form, Secure Tables tab.Note: This step does not apply
 if you
 accessed this form from the VA Programs folder.

1. To select specific views from the Available Views list, select
 any additional tables you wish to add. To select all tables from the Available Tables list, click All.Tip: Use control-click to select multiple, non-consecutive tables. Use shift-click to select multiple, consecutively listed tables.

1. Click Add. The selected tables move from the Available Tables list to the Views to Generate list.

1. Click Regenerate Views.If the system cannot regenerate a database table view, an error message appears at the bottom of the screen along with the view name.
