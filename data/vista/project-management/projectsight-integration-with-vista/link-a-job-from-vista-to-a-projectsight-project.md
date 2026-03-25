---
title: "Link a Job from Vista to a ProjectSight Project | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projectsight-integration-with-vista/link-a-job-from-vista-to-a-projectsight-project"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projectsight-integration-with-vista/link-a-job-from-vista-to-a-projectsight-project"
---

# Link a Job from Vista to
 a ProjectSight Project

Create a job in Vista and a project in ProjectSight, then link the records.
You should set up phase
 codes and cost types in Vista before
 linking to a ProjectSight project, as these
 values automatically flow into ProjectSight
 when the Vista job is linked. For
 information about setting up job phase codes, see [JC Job Phases Form](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:21000056).

1. Create or update a job in Vista by going to JC Jobs.For more information, see [JC Jobs Form](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:21000048).Note: You must assign the job to a
 Vista company that is
 already configured in your integration.

1. Create or update a project in ProjectSight to match the job you just
 created in Vista. ProjectSight Help: For more information about creating new
 projects in ProjectSight, see
 the ProjectSight Help: [Create a Project](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/Online_Help/Projects/Projects.htm#create).

1. In ProjectSight, link the project to a Vista job using Link this Project to
 ERP.Note: You can link a job in
 Vista to only one
 ProjectSight project at
 a time.

ProjectSight Help: For more information about linking in
 ProjectSight, see the
 ProjectSight Help on [Project Linking](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/ERP/Web-ERP-Project-Linking.htm).

1. After linking, you must maintain job / project
 data in both Vista and ProjectSight.

Note: After the JC Job is linked, prime
 contracts are automatically created in ProjectSight from Vista JC Contracts. However, you can't integrate prime
 contracts from ProjectSight into
 Vista.

If you delete the job in Vista, this
 unlinks the project in ProjectSight and
 removes the job from the ERP project dropdown list.
Associated fields in
 Vista and ProjectSight:
Vista JC Jobs Field NameProjectSight Project Field Name
Job NumberSequence
DescriptionName
