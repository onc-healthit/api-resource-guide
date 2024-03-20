# Health IT Feedback and Inquiry Portal: API Conditions and Maintenance of Certification at § 170.404

This section contains anonymized feedback and inquiries, related to the API Conditions and Maintenance of certification requirements at § 170.404, that ONC has handled through the ONC <a target = "_blank" href = "https://www.healthit.gov/feedback">Health IT Feedback Portal</a>. The inquiries are organized by date under headers that mirror the organization of paragraphs in the Code of Federal Regulations at 45 CFR § 170.404.

!!! attention

    The date headers provide important context as some information may have changed since the time of an inquiry and response.

## Paragraph (a)(3)(iv): API Fees - Permitted Fee (Value-Added Services)
### Pre 2023
**Stakeholder Inquiry**: If an EHR developer’s API includes both certified and non-certified capabilities, does the entire API fall within the requirements of § 170.404?

- Can an API be certified if it also contains non-certified capabilities so long as it also meets the certification criteria?  
- Can the EHR developer charge for value-added services through an “app store” for the non-certified portion of such APIs?

**ONC Response**: The fees conditions at <a target = "_blank" href = "https://ecfr.federalregister.gov/current/title-45/subtitle-A/subchapter-D/part-170/subpart-D#p-170.404(a)(3)">45 CFR 170.404(a)(3)</a> all relate to fees administered by Certified API Developers for certified API technology. According to <a target = "_blank" href = "https://ecfr.federalregister.gov/current/title-45/subtitle-A/subchapter-D/part-170/subpart-D#p-170.404(c)">45 CFR 170.404(c)</a>, certified API technology “means the capabilities of Health IT Modules that are certified to any of the API-focused certification criteria adopted in § 170.315(g)(7) through (10).” The certification criteria in the ONC Health IT Certification Program include the minimum technical requirements Health IT Modules must support; health IT developers are not prohibited from exceeding the certification requirements included in the API-focused certification criteria at 45 CFR 170.315(g)(7) through (10).

According to <a target = "_blank" href = "https://ecfr.federalregister.gov/current/title-45/subtitle-A/subchapter-D/part-170/subpart-D#p-170.404(a)(3)(iv)">45 CFR 170.404(a)(3)(iv)</a>, “A Certified API Developer is permitted to charge fees to an API User for value-added services related to certified API technology, so long as such services are not necessary to efficiently and effectively develop and deploy production-ready software that interacts with certified API technology.” 
Additionally, we clarified in the 21st Century Cures Act: Interoperability, Information Blocking, and the ONC Health IT Certification Program Final Rule (ONC Cures Act Final Rule) that “To the degree that a health IT developer administers an “app store” and offers value-added services associated with certified API technology, the Condition of Certification covers its practices related to certified API technology only. Conversely, this Condition of Certification would not apply to any practices that do not involve certified API technology. However, health IT developers would need to be mindful of any applicable information blocking rules that may apply to their app store practices given applicable facts and circumstances” (<a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-1365">85 FR 25760</a>).

If a Certified Health IT Developer does not abide by applicable Conditions and Maintenance of Certification requirements, the nonconformities can be addressed through the <a target = "_blank" href = "https://www.healthit.gov/topic/certified-health-it-complaint-process">Certified Health IT Complaint Process</a>. 

While we read and responded to this question as being specifically about the fees conditions at <a target = "_blank" href = "https://ecfr.federalregister.gov/current/title-45/subtitle-A/subchapter-D/part-170/subpart-D#p-170.404(a)(3)">45 CFR 170.404</a>, for fees administered by Certified API Developers for certified API technology, we note in closing that health IT developers need to remain mindful that practices that do not violate 45 CFR 170.404 could still implicate the information blocking definition (45 CFR 171,103). For example, a practice that does not involve certified API technology would not be directly addressed by 45 CFR 170.404 but could implicate the information blocking regulations. To be certain their fees or other business practices will not be considered information blocking as defined in 45 CFR 171.103, the developer can choose to conform their practices to the conditions of relevant information blocking exception(s) such as the Fees Exception (45 CFR 171.302) and Licensing Exception (45 CFR 171.303).

We are not able to provide individualized advice on whether a specific fact pattern would or would not satisfy an exception or constitute information blocking.

Anyone who believes they may have experienced or observed information blocking by <a target = "_blank" href = "https://www.healthit.gov/cures/sites/default/files/cures/2020-03/InformationBlockingActors.pdf">any health care provider, health IT developer of Certified Health IT, or health information network or health information exchange</a> is encouraged to share their concerns with us through the <a target = "_blank" href = "https://healthit.gov/report-info-blocking">Information Blocking Portal</a> on ONC’s website, HealthIT.gov.

## Paragraph (b)(2): Service base URL publiciation
### June 2023
**Stakeholder Inquiry**: I have questions about the regulatory text in the ONC Cures Act Final Rule found here: <a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-1405">https://www.federalregister.gov/d/2020-07419/p-1405</a>.

Should this list be published on CHPL? We see the "place" for the information on CHPL, but we are seeing that many EHRs have very little to no information published and most don't have their customer list. Is this a violation of the requirements? Are there any exceptions to publishing this information?

**ONC Response**: Thank you for your inquiry. In order to interact with a FHIR RESTful API, an app needs to know the “FHIR Service Base URL,” which is often referred to colloquially as a “FHIR server's endpoint.” The public availability and easy accessibility of this information is a central necessity to assuring the use of FHIR-based APIs without special effort for patient access apps. As per the API Maintenance of Certification requirement at 45 CFR 170.404(b)(2), a Certified API Developer must publish the service base URLs for all Health IT Modules certified to § 170.315(g)(10) that can be used by patients to access their electronic health information (EHI). The Certified API Developer must publicly publish the service base URLs for all of its customers regardless of whether the Health IT Modules certified to § 170.315(g)(10) are centrally managed by the Certified API Developer or locally deployed by an API Information Source, and in a machine-readable format at no charge.

For a Health IT Module certified to § 170.315(g)(10), a hyperlink to the list of service base URLs is published with the product information on the ONC Certified Health IT Product List (CHPL). The hyperlink to the list of service base URLs can be found in the "Service Base URL List" attribute under a CHPL product's details regarding the § 170.315(g)(10) criterion.

For more information about the API Maintenance of Certification requirements, please see the <a target = "_blank" href = "https://www.healthit.gov/condition-ccg/application-programming-interfaces">API Conditions & Maintenance of Certification Certification Companion Guide</a>.

To be open and transparent to the public, developers must provide a hyperlink to the list of service base URLs to be published with the product on the ONC Certified Health IT Product List (CHPL). Certified API Developers are encouraged to use a standardized format when publishing the service base URLs for all of its customers. ONC recommends Certified API Developers leverage the HL7 FHIR 4.0.1 “Endpoint” resource, or profiles of this resource such as the Validated Healthcare Directory Implementation Guide STU1 “<a target = "_blank" href = "https://hl7.org/fhir/uv/vhdir/2018Jan/StructureDefinition-vhdir-endpoint.html">vhdir-endpoint</a>” profile, to represent service base URLs that can be used by patients to access their health information. ONC also encourages developers to provide as much information about the service base URLs as available, including the API Information Source’s organization details, such as name, location, and provider identifiers (e.g., NPI, CCN, or health system ID). These steps will help industry coalesce around standards that enable application developers to more easily and consistently provide patients access to their electronic health information.

There are no exceptions to the requirement that Certified API Developers must publish service base URLs for all Health IT Modules certified to § 170.315(g)(10) that can be used by patients to access their EHI.

### Older (Pre 2023)
**Stakeholder Inquiry**: If an EHR vendor chooses to obtain and integrate a 3rd party solution that is certified to 170.315(g)(10), who is responsible for publish the service base URLs?

**ONC Response**: The API Maintenance of Certification requirement at § 170.404(b)(2) requires a Certified API Developer to publish the service base URLs for all Health IT Modules certified to § 170.315(g)(10) that can be used by patients to access their electronic health information. This includes publishing the service base URLs for all of its customers regardless of whether the Health IT Modules certified to § 170.315(g)(10) are centrally managed by the Certified API Developer or locally deployed by an API Information Source.

ONC provides discussion regarding Certified API Developer publication of service base URLs in the ONC Cures Act Final Rule (<a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/page-25765">85 FR 25765</a>): "*We believe that Certified API Developers will have adequate relationships with API Information Sources in the process of providing Health IT Modules certified to § 170.315(g)(10) and will be able to collect and publish all service base URLs that support patient access on behalf of their customers. Furthermore, we note that API Information Sources would be obligated to share such service base URLs with Certified API Developers to avoid violating the Technical Interference Information Blocking provisions ...*"

The ONC Cures Act Final Rule at <a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-1909">85 FR 25813</a> provides an example which discusses API Information Sources providing Certified API Developers service base URLs in the context of Information Blocking.

## Paragraph (b)(3): Rollout of (g)(10)-Certified APIs
### Pre 2023
**Stakeholder Inquiry**: According to the 21st Century Cures Act: Interoperability, Information Blocking, and the ONC Health IT Certification Program Final Rule (ONC Cures Act Final Rule) timeline, ONC Cures Update Certification Criteria must be made available by 12/31/2022. Can you clarify what "made available" means?

**ONC Response**: The API Maintenance of Certification requirement at 45 CFR 170.404(b)(3) requires that a Certified API Developer with certified API technology previously certified to the certification criterion in § 170.315(g)(8) must deploy to all of their API Information Sources (e.g., customers) API technology certified to the criterion in § 170.315(g)(10) no later than December 31, 2022.

The Maintenance of Certification requirement also includes the deadline of December 31, 2022 for Certified Health IT Developers to upgrade and certify API technology to § 170.315(g)(10) and to deploy to production.

Additional context and background discussion of this Maintenance of Certification requirement is also available in the ONC Cures Act Proposed Rule (<a target = "_blank" href = "https://www.federalregister.gov/d/2019-02224/p-969">84 FR 7495</a>), Final Rule (<a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-1406">85 FR 25765</a>), and Interim Final Rule (<a target = "_blank" href = "https://www.federalregister.gov/d/2020-24376/p-101">85 FR 70072</a>), as well as the <a target = "_blank" href = "https://www.healthit.gov/condition-ccg/application-programming-interfaces">§ 170.404 Application Programming Interfaces Certification Companion Guide</a>.

We encourage all Certified Health IT Developers to work with their ONC-ACBs and customers to develop a certification and roll-out strategy to meet ONC Health IT Certification Program requirements by the required regulatory deadlines.

### Older (Pre 2023)
**Stakeholder Inquiry**: If an EHR system that is currently certified to (g)(7)-(g)(9) is unable to get certified to (g)(10) by January 1, 2023, what is the outcome with respect to their certification? 

- If they then certify to (g)(10) at some point in CY 2023 how is their CHPL entry effected? 
- If they are not certified to (g)(10) by April 2023, for bi-annual ONC attestations, how do they answer the attestation of APIs now that they are not certified on (g)(10)? 
- Finally, to comply with the ONC attestations, if an EHR is certified to (g)(10), must this (g)(10) functionality be deployed into ALL customer production sites by December 31, 2022 to meet the ONC attestation compliance for API, or is acceptable (i.e., can mark “Yes” on the attestation) to have it certified by December 31, 2022 but with an incomplete installation into production setting for all customers until later in CY 2023?

**ONC Response**: The API Maintenance of Certification requirement at <a target = "_blank" href = "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-D/part-170/subpart-D/section-170.404#p-170.404(b)(3)">45 CFR 170.404(b)(3)</a> requires that a Certified API Developer with certified API technology previously certified to the certification criterion in § 170.315(g)(8) must deploy to all of their API Information Sources (e.g., customers) API technology certified to the criterion in § 170.315(g)(10) by no later than December 31, 2022.

The Maintenance of Certification requirement also includes the deadline of December 31, 2022 for Certified Health IT Developers to upgrade and certify API technology to § 170.315(g)(10) and to deploy to production.

Additional context and background discussion of the Maintenance of Certification requirement is available in the ONC Cures Act Proposed Rule (<a target = "_blank" href = "https://www.federalregister.gov/d/2019-02224/p-969">84 FR 7495</a>), Final Rule (<a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-1406">85 FR 25765</a>), and Interim Final Rule (<a target = "_blank" href = "https://www.federalregister.gov/d/2020-24376/p-101">85 FR 70072</a>), as well as the <a target = "_blank" href = "https://www.healthit.gov/condition-ccg/application-programming-interfaces">§ 170.404 Application Programming Interfaces Certification Companion Guide</a>.

Certified Health IT Modules must meet Cures Update compliance (i.e., certified to all eligible and applicable Cures Update criteria) in order to receive the “2015 Edition Cures Update” designation on their CHPL listings. All Certified Health IT Modules with an active certification status must meet this designation by the compliance date of December 31, 2022. Please see our <a target = "_blank" href = "https://www.healthit.gov/sites/default/files/page/2022-03/Cures-Update-Fact-Sheet.pdf">Cures Update Fact Sheet</a>, <a target = "_blank" href = "https://www.healthit.gov/sites/default/files/page/2020-11/Cures_Update_Quick_Reference_2020.pdf">2015 Edition Cures Update Reference</a>, and <a target = "_blank" href = "https://www.healthit.gov/sites/default/files/page/2020-11/Key_Dates_2020.pdf">2015 Edition Cures Update Key Dates</a> resources for additional information on the 2015 Edition Cures Update and the compliance deadlines.

Additionally, if a Certified Health IT Developer does not comply with the Conditions and Maintenance of Certification requirements, ONC may initiate the <a target = "_blank" href = "https://www.healthit.gov/sites/default/files/page/2022-03/Draft_Review_Factsheet.pdf">Direct Review</a> process to ensure Certified Health IT Developers remedy the issue and regain compliance with Certification Program requirements in a timely manner. ONC could take the more serious step of terminating the affected certification(s) and/or issuing a certification ban to the Certified Health IT Developer if identified issues are not corrected.

We encourage all Certified Health IT Developers to work with their ONC-ACBs and customers to develop a certification and roll-out strategy to meet all ONC Health IT Certification Program requirements by the required regulatory deadlines.

***

**Stakeholder Inquiry**: Can you provide some more information on what the requirement below entails?

*A Certified API Developer with certified API technology previously certified to the certification criterion in § 170.315(g)(8) must provide all API Information Sources with such certified API technology deployed with certified API technology certified to the certification criterion in § 170.315(g)(10) by no later than December 31, 2022.*

**ONC Response**: The API Maintenance of Certification requirement at 45 CFR 170.404(b)(3) requires that "A Certified API Developer with certified API technology previously certified to the certification criterion in § 170.315(g)(8) must provide all API Information Sources with such certified API technology with certified API technology certified to the criterion in § 170.315(g)(10) by no later than December 31, 2022."

If a health IT developer currently has Health IT Modules certified to 45 CFR 170.315(g)(8) under the ONC Health IT Certification Program, it must meet this Maintenance of Certification requirement no later than December 31, 2022, to continue participating in the ONC Health IT Certification Program. Failure to comply with a Condition and Maintenance of Certification requirement could result in a Certified Health IT Module being non-compliant, and ONC could initiate Direct Review (<a target = "_blank" href = "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-D/part-170/subpart-E/section-170.580#p-170.580(a)(2)(iii)">45 CFR 170.580(a)(2)(iii)</a>) and pursue corrective actions to enforce the requirement. ONC’s goal is to work with Certified Health IT Developers to remedy any non-conformities in a timely manner, but failure to conform with requirements of the ONC Health IT Certification Program can ultimately result in terminating the affected Health IT Modules and/or issuing a certification ban to the Certified Health IT Developer. For more information on Direct Review, please visit <a target = "_blank" href = "http://www.healthit.gov/Direct-Review">http://www.healthit.gov/Direct-Review</a> and our <a target = "_blank" href = "https://www.healthit.gov/sites/default/files/page/2022-03/Draft_Review_Factsheet.pdf">Direct Review fact sheet</a>.

We encourage health IT developers to work with their ONC-ACB and customers to develop a certification and roll-out strategy to meet ONC Health IT Certification Program requirements by the required regulatory deadlines.

***

**Stakeholder Inquiry**: Do all products have to be HL7® FHIR capable by Dec 31, 2022, or just the certified products?

**ONC Response**: The API compliance requirement for certified products is contained in 45 CFR 170.404: API Conditions and Maintenance of Certification requirements. According to 170.404(b)(3):

*“A Certified API Developer with certified API technology previously certified to the certification criterion in § 170.315(g)(8) must provide all API Information Sources with such certified API technology deployed with certified API technology certified to the certification criterion in § 170.315(g)(10) by no later than December 31, 2022.”*

According to these requirements, if a health IT developer had technology that was previously certified to § 170.315(g)(8), it must be upgraded and certified to the requirements in § 170.315(g)(10) by the compliance deadline of December 31, 2022. Please consider reviewing the <a target = "_blank" href = "https://www.healthit.gov/condition-ccg/application-programming-interfaces">Certification Companion Guide for § 170.404</a> for more information.

--8<-- "includes/abbreviations.md"