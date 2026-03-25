---
title: "Add a Vista Deep Link to an SSRS Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/add-vista-deep-links-to-reports/add-a-vista-deep-link-to-an-ssrs-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/add-vista-deep-links-to-reports/add-a-vista-deep-link-to-an-ssrs-report"
---

# Add a Vista Deep Link to an SSRS Report

Once you have the form name, KeyName fields, and View name,
 you can add a deep link to an SSRS Report.

1. In SSRS, open the
 Dataset Properties window and create a query for your dataset. 

1. In the Query field, enter the SQL expression using the
 dbo.vfLinkToRecordPrefix(FormName) and dbo.vfURLEncode(Field) functions, and
 include the KeyName fields. The following example query
 creates a link to a specific record in the PM Project Locations form: 
select
 dbo.vfLinkToRecordPrefix('PMProjectLoc') + CAST(PMCo as varchar(3)) +
 '/Project=' + dbo.vfURLEncode(PMPL.Project) + '/Location=' +
 dbo.vfURLEncode(PMPL.Location) as URI from PMPL

1. Open a report and
 right-click a field to use as the deep link. In the context menu, select the
 Properties option. The following screenshot shows the Text Box
 Properties being opened to add a deep link for use in a text box field, but a
 deep link can be added to any element that supports Actions. 

1. In the Properties
 window, select the Action tab. In the Enable as an action field,
 select the Go to URL option. 

1. In the Select
 URL field, select the URL you just created. In this example, the
 URL was named “URI”. Click OK.
