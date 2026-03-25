---
title: "Copy submittals to a different project | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/copy-submittals-to-a-different-project"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/copy-submittals-to-a-different-project"
---

# Copy submittals to a different project

You can copy the submittals from one project to another, which can save time and reduce data entry.
For example if you have two projects with similar submittals, you can enter the submittals in one project and then copy them to the other.
This WILL NOT copy any of the following on the submittals:

- Submittal Package / Package Revision

- Dates - Activity date, due from, due to, sent to, or received from dates

- Status

- Subcontracts/purchase orders

- Our Firm / Our Firm Contact - This will only be copied if the "our firm" on both projects is the same (PM Projects form, PM Info tab, Project Our Firm field).

Note: This process will copy any information entered in custom fields on the submittals. You can add a custom field to the PM Submittal Register, and PM Submittal Package forms using the [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form).
Follow the steps below to copy the submittals from one project to another.

1. Open the [About the PM Submittal Register Form](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-register-form) form.

1. Select the destination project in the Project field. This is the project where the submittals will be copied to.

1. Select Tasks Copy Submittal Register. This will open the PM Submittal Register Copy form.

1. The Destination Project field will display the selected project.

1. Enter the project that contains the submittals that you would like to copy in the Source Project field or press F4 to select it from a list.

1. The lower portion of the form will populate with the submittal register of the selected project, including closed submittals.

1. Use the Copy Options section to select what will be copied to the destination project.

- Exclude Revisions - Check this box if by default only the highest revision number of each submittal should be copied. When this box is checked, the lower portion of the form will only display the highest revision number of each submittal and by default they will all be selected.

- Note: When this box is not checked, all of the revisions of each submittal will display in the lower portion of the form. This allows you to select which submittal revisions will be copied.

- Approving Firm/Contact - Check this box if the Approving Firm and Approving Firm Contact fields should be copied on each submittal. You can see the approving firm of each submittal using the Approving Firm column in the lower portion of the form.

- Responsible Firm/Contact - Check this box if the Responsible Firm and Responsible Firm Contact fields should be copied on each submittal.

- Include Attachments - Check this box if the attachments on the submittal revisions should be copied. When you add an attachment on the PM Submittal Register form by clicking on the Attachments icon () and then selecting Add Attachment, you are adding an attachment to a specific submittal revision. Checking the Include Attachments box will copy these attachments to the new submittal.

- Overwrite duplicates - Check this box if submittals in the destination project should be overwritten by any copied submittals that have the same submittal and revision number. For example if you use the PM Submittal Register Copy form to copy the submittals to a different project but forget to check the Approving Firm/Contact box, you can open the PM Submittal Register Copy form, check the Overwrite duplicates box, and then copy the submittal revisions again. The previously copied submittals will be overwritten.

1. Check the Copy box in the lower portion of the form next to each submittal revision that should be copied to the destination project.

1. Click the Copy button when complete. The selected submittals will be copied to the destination project.

1. Click the Close button to close the PM Submittal Register Copy form.

Related information

- [About Submittals](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-submittals)
