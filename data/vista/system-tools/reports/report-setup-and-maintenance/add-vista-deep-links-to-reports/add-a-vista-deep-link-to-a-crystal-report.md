---
title: "Add a Vista Deep Link to a Crystal Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/add-vista-deep-links-to-reports/add-a-vista-deep-link-to-a-crystal-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/add-vista-deep-links-to-reports/add-a-vista-deep-link-to-a-crystal-report"
---

# Add a Vista Deep Link to a Crystal Report

Once you have the form name, KeyName fields, and View name,
 you can add a deep link to a Crystal Report.

1. In Crystal Reports,
 connect to the Vista database and
 create or open a report.

1.  In the Field Explorer,
 right-click SQL Expression Fields and then name the SQL expression in the SQL
 Expression Name window.

1. In the SQL Expression
 Editor, enter the SQL expression using the dbo.vfLinkToRecordPrefix(FormName)
 and dbo.vfURLEncode(Field) functions, and include the KeyName fields. In this example of creating a
 link to a specific record in the PM Project Locations form, the query would
 be: 
dbo.vfLinkToRecordPrefix('PMProjectLoc') + CAST(PMCo as varchar(3)) +
 '/Project=' + dbo.vfURLEncode(Project) + '/Location=' +
 dbo.vfURLEncode(Location)

1. Click Save and
 close.

1. On a report field where
 you want to include a hyperlink, right-click and select Format in the context menu. The Format Editor opens. 

1. In the Format Editor,
 select the Common tab. In the Tool Tip Text field, enter
 the URI. Click OK. Note: Viewpoint links use the custom URI
 protocol “viewpoint://”. As a security measure, Crystal Reports disables
 custom URI protocols by default, so Viewpoint links created as Hyperlinks
 will not work. To work around this, Viewpoint looks for the URI in the Tool
 Tip Text field.
