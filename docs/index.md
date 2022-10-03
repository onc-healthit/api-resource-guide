# API Resource Guide

## How to use this resource guide

This informative resource supplements other public documentation available to help health IT developers certify to the API criteria in the ONC Health IT Certification Program and meet the requirements under the API Conditions and Maintenance of Certification. At the highest level, this document mirrors the organization of paragraphs in the Code of Federal Regulations, including headers for “§ 170.315(g)(10) Standardized API Certification Criterion” (the FHIR®-based standardized API), “§ 170.404 Conditions and Maintenance of Certification” (the broader API behavior requirements), and sub-paragraphs. It also contains standalone sections for topics that generate a lot of questions, like “Real World Testing of APIs” and “Standards Version Advancement Process and APIs.” Efforts have been made to make this resource easily navigable, searchable, and consumable. If you have recommendations to improve this resource, please submit an inquiry to the <a target = "_blank" href = "https://inquiry.healthit.gov/support/plugins/servlet/desk/portal/2">Health IT Feedback and Inquiry Portal</a> or submit an <a target = "_blank" href = "https://github.com/onc-healthit/api-resource-guide/issues">issue on GitHub</a>.

This resource is intended to provide clarifications to assist developers in implementing applicable provisions contained in <a target = "_blank" href = "https://ecfr.federalregister.gov/current/title-45/subtitle-A/subchapter-D/part-170">45 CFR part 170</a>. In developing and implementing APIs and other health IT, developers should remain mindful of the information blocking provisions of the ONC Cures Act Final Rule contained in <a target = "_blank" href = "https://ecfr.federalregister.gov/current/title-45/subtitle-A/subchapter-D/part-171">45 CFR part 171</a>. **This resource does not supersede existing statutory or regulatory requirements**. The use of the term “Health IT Module(s)” or “Certified Health IT Module(s)” in this resource refers to Health IT Modules certified through the ONC Health IT Certification Program.

This resource encompasses clarifications from the § 170.315(g)(10) Certification Companion Guide and <a target = "_blank" href = "https://www.healthit.gov/condition-ccg/application-programming-interfaces">§ 170.404 CCG</a>. Within each regulation paragraph, there is a section titled “Clarifications Included in [name of CCG],” which includes clarifications from the respective CCG, and “Additional Clarifications to the [name of CCG],” which includes additional clarifications not included in the respective CCG. This documentation accompanies the Certification Companion Guides and Test Procedures for the API certification criterion finalized in § 170.315(g)(10) and the CCG for API Conditions and Maintenance of Certification requirements finalized at § 170.404.

## Background on ONC and (g)(10) API Certification Criterion
The Office of the National Coordinator for Health IT (ONC) is a federal agency located in the Office of the Secretary of the U.S. Department of Health and Human Services. ONC's mission is to: 

!!! note ""
    "Improve the health and well-being of individuals and communities through the use of technology and health information that is accessible when and where it matters most"

Learn more at our website, <a target = "_blank" href = "https://www.healthit.gov/topic/about-onc">healthIT.gov</a> and please check out all our open source interoperability tools at the <a target = "_blank" href = "https://github.com/onc-healthit">ONC GitHub</a>!

The <a target = "_blank" href = "https://www.congress.gov/bill/114th-congress/house-bill/34/text">21st Century Cures Act (Section 4002)</a> and subsequent 21st Century Cures Act: Interoperability, Information Blocking, and the ONC Health IT Certification Program Final Rule (<a target = "_blank" href = "https://www.healthit.gov/curesrule/">ONC Cures Act Final Rule</a>) established a Condition of Certification requirement in the ONC Health IT Certification Program, which requires applicable health IT developers participating in the Program to develop and deploy a standardized API:

>“health information from such technology [is] to be accessed, exchanged, and used without special effort through the use of APIs or successor technology or standards, as provided for under applicable law.”

This requirement also states that a health IT developer must, through an API:

>“provide access to all data elements of a patient's electronic health record to the extent permissible under applicable privacy laws.”

ONC finalized a certification criterion for APIs for single and multiple patient services at § 170.315(g)(10) to replace the certification criterion at § 170.315(g)(8). Additionally, ONC finalized API Conditions and Maintenance of Certification requirements at § 170.404 that apply to health IT developers certified to § 170.315(g)(10).

--8<-- "includes/abbreviations.md"