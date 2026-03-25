---
title: "Step 3 - Optional: Generate the report(s) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/create-and-send/about-sending-messages/step-3---optional-generate-the-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/create-and-send/about-sending-messages/step-3---optional-generate-the-reports"
---

# Step 3 - Optional: Generate the report(s)

Generate a report and include it in the email that is being sent. You can only generate a report that is also associated with a form.

1. Open the Documents tab on the PM Send Documents form.

1. Add records to the Documents tab using the  icon. Each report must be associated with a unique record. For example add an ACO record to the Documents tab to generate a change order report associated with the PM Approved Change Orders form. To generate multiple reports, add multiple records to the Documents tab.

You can only generate a report that is associated with a form
The reports that are associated with a form display
 when you select Options >
 Reports in the toolbar at the top of a form. This means if you want to
 generate an RFI report, you need to add an RFI record to the Documents tab and the PM
 Request For Information form must be associated with the report that you want to
 generate.
 Click [here](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/associate-a-report-with-a-form) for information on how to associate a report with a form.
Added records associated with parent using the Related Items feature
When adding records to the Documents tab, every
 record that you add will also be related to the parent record using the [Related Items](/en/vista/vista/project-management/about-related-items) feature. The parent record is the
 record used to launch the PM Send Documents form.
Adding records to the Documents tab
Follow the steps below to add another record to the Documents tab.

1. Click the Select Records () icon in the toolbar at the top of the PM Send Document form.

1. The PM Search Documents form will display.

1. Use the PM Search Documents form to locate the
 records that you want to add. For example select an RFI, project issue, change
 order, and subcontract.

1. Move the new record to the Selected Documents
 section and then click OK.

1. The selected records will now display on the
 Documents tab of the PM Send Documents form. Use the Form
 Report column select the report that will be generated for each
 record.

You cannot generate a report and a document for the same record
A single email can include several reports and generated documents, but you cannot generate a report and a project document using the same record.
For example a single email can include several RFI documents and change order reports, but you cannot generate an RFI document and a PM Request For Information report for the same RFI record.

1. Select Report in
 the Document
 Source column next to each record that will be used to generate a
 report.

1. Select the report that you
 want to generate int he Document column.

You cannot generate an SSRS report
Currently SSRS reports are not compatible with the
 Create and Send feature. SSRS reports will not display in the Form
 Report drop down, even if they are associated with a form.

1. Click on the Report () icon next to the Form
 Reportcolumn to select how the report will be configured. This allows
 you to select what information will be included in the report that is
 generated.

1. Go to the next step, adding attachments. [More](/en/vista/vista/project-management/create-and-send/about-sending-messages/step-4---optional-add-the-attachments)

Related information

- [About the Create and Send Feature](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)

- [About Generating & Editing Project Documents](/en/vista/vista/project-management/create-and-send/about-generating--editing-project-documents)

- [About Sending Messages](/en/vista/vista/project-management/create-and-send/about-sending-messages)
