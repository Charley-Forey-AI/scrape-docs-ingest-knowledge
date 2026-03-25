---
title: "Set up Job Level Security | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/set-up-job-level-security"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/set-up-job-level-security"
---

# Set up Job Level Security

If you
 are implementing data level security at the job level, you can assign security
 groups to projects in [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form). This can be very useful if you
 regularly create projects because it allows you to designate who should have access
 to the project without using [VA Data Security Access ](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-data-security-access-form).
Follow the steps below to implement this feature. You must have access to the Viewpoint Administration module

1. Open [VA Data Security Setup ](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form).

1. Select the ‘bJob’ datatype using the Grid tab.

1. Check the Secure
 Datatype box on the Info tab.

1. Enter a security group
 in the Default Security Group field.

1. Open the Secure Tables
 tab and check the Apply Security box next to
 the Job Master table (bJCJM), and any other table that should have job level
 security.

1.  Click the Regenerate
 Viewsbutton, specifying the views to generate, and clicking the
 Generate Views button). Once you have completed these
 steps, the Security Group input is enabled on the PM Projects form, allowing
 you to designate which security group will have access to information about
 the selected project.
Note: It is important to note that in addition
 to the security group specified in JC Jobs, access to information about the
 selected job will also be granted to the Default Security Group you
 specified in VA Data Security Setup, as well as to any other security groups
 that have been granted access in VA Data Security Access.
[](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)VA
 Data Security Setup
