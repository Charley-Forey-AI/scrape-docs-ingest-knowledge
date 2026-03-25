---
title: "About Posting Costs to Components | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/component-tracking/about-posting-costs-to-components"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/component-tracking/about-posting-costs-to-components"
---

# About Posting Costs to Components

If you want to track costs at the component level, you must
 check the Post Costs to Components option in EM Equipment (Comp/Attach tab).
When costs are posted to the
 equipment, they are posted for the component as will. If a component is moved to
 another piece of equipment, all of the previous costs posted to that component will be
 carried with it. This allows you to track the costs of the equipment with any component
 on it, or the cost of the component, regardless of what piece of equipment it was
 attached to.
Note: When costs are posted to a piece of equipment and
 its component, only one record is created; the costs are not duplicated. However, certain
 reports allow you to view those costs either by equipment or by component.
Example:
Equipment
Component
Total Cost

10101
900
$1000

10101
900
$650

20101
900
$3500

10101
900
$300

Total Cost by Equipment


10101:
$1950.00

20101:
$3500.00

Total Cost by Component


900:
$5450.00

Costs can also be posted to a component when
 not attached to a primary piece of equipment. Typically, this situation would only occur
 when the component is in a shop for repairs and has been detached from the equipment to
 do so. Since components cannot exist independently, you would need to transfer the
 component to a 'dummy' equipment number (the one specified in the Unattached Component
 Equipment Number field in EM Company Parameters) using the EM Component Transfer
 program. That way, costs can be posted to the component without affecting the primary
 piece of equipment.
