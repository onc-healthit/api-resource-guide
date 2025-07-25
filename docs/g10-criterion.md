<!-- $criterion-endpoint{"test-method/standardized-api-patient-and-population-services"} -->

# HL7 FHIR API Criterion at § 170.315(g)(10)

This section considers the HL7®[^1] FHIR® standardized API for patient and population services certification criterion, including all of the relevant content contained in the <a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-1162">ONC Cures Act Final Rule</a>, the <a target = "_blank" href = "https://www.federalregister.gov/d/2020-24376/p-136">ONC Interim Final Rule</a>, <a target = "_blank" href = "https://www.federalregister.gov/documents/2024/01/09/2023-28857/health-data-technology-and-interoperability-certification-program-updates-algorithm-transparency-and#h-105">HTI-1</a>, and the <a target = "_blank" href = "https://ecfr.federalregister.gov/current/title-45/subtitle-A/subchapter-D/part-170/subpart-C/section-170.315#p-170.315(g)(10)">regulation paragraphs in § 170.315(g)(10)</a>.

## Applicability
§ 170.315(g)(10) is applicable to all health IT developers who are certifying to the <a target = "_blank" href = "https://www.healthit.gov/topic/certification-ehrs/2015-edition-test-method/2015-edition-cures-update-base-electronic-health-record-definition">Base EHR definition</a>.

The API certification criterion finalized in § 170.315(g)(10) was included as part of the Base EHR Definition at <a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-3216">§ 170.102</a>. While developers of health information technology are not required by the ONC to meet certification requirements, including certification requirements that are included as part of the Base EHR Definition, several federal, state and tribal entities, including <a target = "_blank" href = "https://www.cms.gov/">Centers for Medicare & Medicaid Services</a>, <a target = "_blank" href = "https://www.cdc.gov/">Centers for Disease Control and Prevention</a>, and other programs reference the ONC Health IT Certification Program and require the use of certified health IT for program participation.

## Health IT Feedback and Inquiry Portal

To submit questions or comments to ONC please use our <a target = "_blank" href = "https://www.healthit.gov/feedback">Inquiry Portal</a>. Anonymized versions of the § 170.315(g)(10) inquires and responses that ONC has handled through this portal can be accessed on the [Health IT Feedback and Inquiry Portal: Standardized API Certification Criterion at § 170.315(g)(10)](inquiry-portal/g10-inquiries.md) page.

## Information and Clarifications

### Entire Criterion

<!-- $ref{g-10:CCG["Applies to Entire Criterion"], tabbed} -->
??? quote "*Clarifications included in the (g)(10) CCG that apply to the entire criterion*"
	***Clarifications:***
	
	**Applies to all applicable base regulatory and SVAP standards:**
	
	* Health IT Modules are not required to support patient-facing API-enabled “read” services for multiple patients for the purposes of this certification criterion.
	* The clinical note text included in any of the notes described in the “Clinical Notes Guidance” section of a US Core Implementation Guide (IG) adopted in § 170.215(b)(1) must be represented in a “plain text” form, and it would be unacceptable for the note text to be converted to another file or format (e.g., .docx, PDF) when it is provided as part of an API response. The intent of this policy is to prohibit Health IT Modules from converting clinical notes from a “machine readable” format to a non-“machine readable” format (e.g., PDF). Clinical note text that originates from outside Health IT Modules should be exchanged using its original format. Additionally, “plain text” does not necessarily mean the FHIR® “contentType” “text/plain.”
	* The US Core IG Profile “StructureDefinition-us-core-patient” element “name.suffix” is required for testing and certification in the Certification Program to meet the USCDI requirement to support the “Patient Demographics” Data Class: “Suffix” Data Element.
	* A Health IT Module must support at least one Choice or Reference for US Core IG “must support” elements with multiple Choices or References, respectively.
	* A Health IT Module must be conformant to the US Core IG for all Choices and References included in its standardized API, and cannot misrepresent Choices via the standardized API (e.g. a Health IT Module cannot transform “integer” values to “string” values).
	* A health IT developer must document which US Core IG Choices and References are supported by their Health IT Module via public technical documentation to meet the requirements at § 170.315(g)(10)(viii) and the transparency conditions at § 170.404(a)(2).
	* Information originating from the (g)(10)-certified Health IT Module must conform to the requirements included in the criterion, but legacy information and information from outside systems is not required to be mapped to the USCDI “Applicable Standards” and the US Core IG terminologies and value sets. However, health IT developers are encouraged to exceed the minimum requirements described in § 170.315(g)(10) to support the mapping of legacy information to the terminologies and value sets included in the USCDI and US Core IG where possible.
	* In order to mitigate potential interoperability errors and inconsistent implementation of the Fast Healthcare Interoperability Resources (FHIR®) Bulk Data Access (Flat FHIR®) (v1.0.0: STU 1) standard, ONC assesses, approves, and incorporates corrections (errata) as part of required certification and testing to this criterion. Compliance with the following errata is necessary because the errata implements technical corrections and clarifications to the FHIR® Bulk Data Access (Flat FHIR®) (v1.0.0: STU 1) standard. There is a 90-day delay from the time the CCG has been updated with the ONC-approved errata to when compliance with the errata will be required to pass testing. Similarly, there will be an 18-month delay before a finding of an erratum’s absence in a Certified Health IT Module during surveillance would constitute a non-conformity under the Certification Program.
		+ Version: [FHIR® Bulk Data Access (Flat FHIR®) (v1.0.1: STU 1)](https://hl7.org/fhir/uv/bulkdata/STU1.0.1/). Effective for testing on October 25, 2021. Surveillance compliance date on January 27, 2023.
	* Through the [US Core Patch Process](https://confluence.hl7.org/display/CGP/US+Core+%27Patch%27+Process), the HL7® Cross-Group Projects Work Group (CGP WG) approves US Core “patches”, which are corrections for issues with the US Core implementation guide (US Core IG). US Core “patches” include corrections for issues such as ambiguous requirements and requirements incompatible with real world deployment. Similar to US Core “patches” are US Core “additional guidance”. US Core “additional guidance” approved by the CGP WG indicates guidance included in a newer version of the US Core IG as being relevant to a previous version of the US Core IG. Though US Core “patches” and “additional guidance” are not required for certification purposes (unless indicated in the Certification Companion Guide), health IT developers may optionally implement US Core “additional guidance” in their Health IT Module and still be conformant with § 170.315(g)(10) criterion requirements.
	* More information regarding the US Core Patch Process and US Core “patches” and “additional guidance” approved by the CGP WG is available on the HL7® Confluence pages of [US Core 'Patch' Process](https://confluence.hl7.org/display/CGP/US+Core+%27Patch%27+Process) and [Approved Patches and Additional Guidance](https://confluence.hl7.org/display/CGP/Approved+Patches+and+Additional+Guidance).
	* Consistent with Executive Order (EO) 14168 and OPM guidance, Health IT Modules certifying and/or currently certified to certification criteria that cross-reference the USCDI standard at 45 CFR 170.213 are only required to demonstrate the capability to categorize data on individuals for the sex data element in accordance with the following SNOMED CT® codes:
		+ 248152002 |Female (finding)| and
		+ 248153007 |Male (finding)|
	* Further, these Health IT Modules are no longer required to support the following USCDI data elements for purposes of certification:
		+ Sexual orientation in USCDI version 4;
		+ Gender identity in USCDI version 4;
		+ Sex parameter for clinical use in USCDI version 5;
		+ Name to use in USCDI version 5;
		+ Pronouns in USCDI version 5.
	
	**Applies to USCDI v1 and US Core 3.1.1 and SVAP approved standards US Core 4.0.0 (expires on January 1, 2026):**
	
	* The HL7® Cross-Group Projects workgroup, through the [US Core 'Patch' Process](https://confluence.hl7.org/display/CGP/US+Core+%27Patch%27+Process) ticket [FHIR-40299](https://jira.hl7.org/browse/FHIR-40299), approved patching the US Core Patient Profile in US Core 3.1.1 and US Core 4.0.0. The USCDI data element “Patient Demographics: Previous Name” must be supported by including the capability to set the US Core Patient Profile element “Patient.name.use” to “old” or provide an end date in “Patient.name.period” element or support both. Additionally, the USCDI data element “Patient Demographics: Previous Address” must be supported by including the capability to set the US Core Patient Profile “Patient.address.use” element to “old” or provide an end date in “Patient.address.period” element or support both. Also, support for the US Core Patient Profile “Patient.address.period” element is not required for purposes of testing and certification.
	
*Additional clarifications that apply to the entire (g)(10) criterion:*

- The API certification criterion in § 170.315(g)(10) replaces the “application access—data category request” certification criterion (§ 170.315(g)(8)) and supports API-enabled “read” services for single and multiple patients.
- The term “services” includes all § 170.315(g)(10)-related technical capabilities included in a Health IT Module presented for testing and certification. The API-enabled “read” services for single patients is intended to support EHI requests and responses for individual patient records and the API-enabled “read” services for multiple patients is intended to support EHI requests and responses for multiple patients’ records.
- The scope of patient cohorts for “population services” can include various groups defined at the discretion of the user of the API-enabled “read” services for multiple patients, including, for example, a group of patients that meet certain disease criteria or fall under a certain insurance plan.
- The <a target = "_blank" href = "https://www.ecfr.gov/cgi-bin/text-idx?SID=034c12732e5cb9328303ecdf94ecde87&mc=true&tpl=/ecfrbrowse/Title45/45cfr171_main_02.tpl">information blocking policies</a> do not compel
healthcare providers to implement Health IT Modules certified to requirements in
§ 170.315(g)(10).
- While there may be slight variation between each instance of a Standardized API for patient and population services Health IT Module implemented by API Information Sources, ONC believes the standards that form the basis of the § 170.315(g)(10) certification criterion will enable interoperability across implementations.

!!! note ""
	[Health IT Feedback and Inquiry Portal Q&A: Applies to Entire Criterion (g)(10)](inquiry-portal/g10-inquiries.md#applies-to-entire-criterion)

### Data Response (Single Patient)
???+ quote "**Regulation text at § 170.315(g)(10)(i)(A)**" 
    (i) *Data response*. (A) Respond to requests for a single patient's data according to the standards and implementation specifications adopted in § 170.215(a) and in § 170.215(b)(1), including the mandatory capabilities described in “US Core Server CapabilityStatement,” for each of the data included in the standards adopted in § 170.213. All data elements indicated as “mandatory” and “must support” by the standards and implementation specifications must be supported.

<!-- $ref{g-10:CCG["Paragraph (g)(10)(i)(A) Data response – single patient"], tabbed} -->
??? quote "*Clarifications included in the (g)(10) CCG that apply to paragraph § 170.315(g)(10)(i)(A)*"
	Technical outcome – Respond to requests for a single patient’s data according to the standards and implementation specifications adopted in § 170.215(a) and (b)(1), including the mandatory capabilities described in “US Core Server CapabilityStatement,” for each of the data included in the corresponding standard adopted in § 170.213. All data elements indicated as “mandatory” and “must support” by the standards and implementation specifications must be supported.
	
	***Clarifications:***
	
	**Applies to all applicable base regulatory and SVAP standards:**
	
	* All data elements and operations indicated as “mandatory” and “must support” by the standards and implementation specifications must be supported and are in-scope for testing.
	* Health IT Modules must support provenance according to the [“Basic Provenance Guidance” section of the US Core IG](https://www.hl7.org/fhir/us/core/STU3.1.1/basic-provenance.html).
	* For purposes of ONC Health IT Certification, health IT developers that always provide HL7® FHIR® “observation” values are not required to demonstrate Health IT Module support for “dataAbsentReason” elements. These include “dataAbsentReason” elements contained in the US Core implementation guide profiles and FHIR® Vital Sign profiles that build on the HL7® FHIR® “observation” and its derived profiles including HL7® FHIR® “observation-vitalsigns”, and HL7® FHIR® “observation-oxygensat”, including “component.dataAbsentReason” elements. However, health IT developers are still required to adhere to and demonstrate Health IT Module support for the [“Missing Data” section](http://hl7.org/fhir/us/core/STU3.1.1/general-guidance.html#missing-data) of the US Core implementation guide.
	* For purposes of testing and certification, health IT developers are not required to demonstrate Health IT Module support for the “USCoreFetchDocumentReferences” ($docref) US Core IG operation.
	
	**Applies to USCDI v1 and US Core 3.1.1 (expires on January 1, 2026)**
	
	* The HL7® Cross-Group Projects work group, through the [US Core 'Patch' Process](https://confluence.hl7.org/display/CGP/US+Core+%27Patch%27+Process) ticket [FHIR-28393](https://jira.hl7.org/browse/FHIR-28393), approved patching US Core 3.1.1 to remove "must support" from the "DocumentReference.custodian" data element. For the purposes of testing and certification, health IT developers are not required to demonstrate Health IT Module support for the “custodian” data element in the “DocumentReference” US Core 3.1.1 IG Profile.
	
	**Applies to USCDI v1 and US Core 3.1.1 and SVAP approved standard US Core 4.0.0 (expires on January 1, 2026):**
	
	* For “Encounter,” “Organization,” and “Practitioner,” US Core IG profiles, only the “read” type interaction must be supported and will be included in testing and certification. For the “Location” FHIR® resource, Health IT Modules must either demonstrate support for the “read” type interaction or demonstrate support for providing the “Location” and FHIR® resource references as a contained resource. The “search” type interactions for these profiles and resource are not in scope for testing and certification. Health IT Modules must support these US Core IG profiles / FHIR® resource because they are included as “must support” data elements in US Core IG profiles required by the United States Core Data for Interoperability (USCDI).
	* Health IT Modules must support provenance according to the [“Basic Provenance Guidance” section of the US Core IG.](https://www.hl7.org/fhir/us/core/STU3.1.1/basic-provenance.html)
	
	**Applies to USCDI v3 and US Core 6.1.0 (required by December 31, 2025):**
	
	* The HL7® Cross-Group Projects workgroup approved the [US Core 'Patch' Process](https://confluence.hl7.org/display/CGP/US+Core+%27Patch%27+Process) ticket [FHIR-45319](https://jira.hl7.org/browse/FHIR-45319) for US Core 6.1.0. In alignment with that issued guidance, the Health IT Module must support all four codes from the US Core Screening Assessment Observation Category ValueSet for the US Core Observation Screening Assessment Profile for “Observation.category:screening-assessment”. Additionally, the Health IT Module must support the “sdoh” code from the US Core Screening Assessment Condition Category ValueSet for the US Core Condition Problems and Health Concerns Profile for “Condition.category:screening-assessment”.
	* For the “Organization” and "Practitioner" US Core IG profile, only the “read” type interaction must be supported and will be included in testing and certification. For the “Location” FHIR® resource, Health IT Modules must either demonstrate support for the “read” type interaction or demonstrate support for providing the “Location” FHIR® resource reference as a contained resource. The “search” type interactions for these profiles and resource are not in scope for testing and certification. Health IT Modules must support these US Core IG profiles / FHIR® resource because they are included as “must support” data elements in US Core IG profiles required by the United States Core Data for Interoperability (USCDI).
	* For purposes of testing and certification, health IT developers are not required to demonstrate Health IT Module support for the “QuestionnaireResponse” US Core IG profile.
	* The HL7® Cross-Group Projects workgroup, through the [US Core 'Patch' Process](https://confluence.hl7.org/display/CGP/US+Core+%27Patch%27+Process) ticket [FHIR-43355](https://jira.hl7.org/browse/FHIR-43355), approved patching the US Core Smoking Status Observation Profile in US Core 6.1.0. For purposes of certification, the clinically relevant time/time-period for observation for the US Core Smoking Status Observation Profile may be supported using either Observation.effectiveDateTime or Observation.effectivePeriod data elements, where Observation.effectivePeriod has the [“Period”](https://hl7.org/fhir/R4/datatypes.html#Period) type.
	* The HL7® Cross-Group Projects workgroup, through the [US Core 'Patch' Process](https://confluence.hl7.org/display/CGP/US+Core+%27Patch%27+Process) ticket [FHIR-44693](https://jira.hl7.org/browse/FHIR-44693), approved patching the US Core Practitioner Profile in US Core 6.1.0. For purposes of certification, Practitioner.address from the US Core Practitioner Profile is not required to be supported if the Health IT Module supports the US Core PractitionerRole Profile.
	* The HL7® Cross-Group Projects workgroup, through the [US Core 'Patch' Process](https://confluence.hl7.org/display/CGP/US+Core+%27Patch%27+Process) ticket [FHIR-46240](https://jira.hl7.org/browse/FHIR-46240), approved patching the US Core DiagnosticReport Profile for Report and Note Exchange in US Core 6.1.0. For purposes of certification, DiagnosticReport.media and DiagnosticReport.media.link from the US Core DiagnosticReport Profile for Report and Note Exchange are not required to be supported.
	* The HL7® Cross-Group Projects workgroup, through the [US Core 'Patch' Process](https://confluence.hl7.org/display/CGP/US+Core+%27Patch%27+Process) ticket [FHIR-50283](https://jira.hl7.org/browse/FHIR-50283), approved patching the US Core Coverage Profile in US Core 6.1.0. For purposes of certification for the US Core Coverage Profile:
		+ Coverage.class:group.name is not required to be supported
		+ Coverage.class:group.value should represent “Group Identifier”
	* The HL7® Cross-Group Projects workgroup, through the [US Core 'Patch' Process](https://confluence.hl7.org/display/CGP/US+Core+%27Patch%27+Process) ticket [FHIR-50239](https://jira.hl7.org/browse/FHIR-50239), approved patching the US Core MedicationDispense Profile in US Core 6.1.0. For purposes of certification, references to US Core Practitioner Profile are not required to be supported for the MedicationDispense.performer.actor for the US Core MedicationDispense Profile.
	* The HL7® Cross-Group Projects workgroup, through the [US Core 'Patch' Process](https://confluence.hl7.org/display/CGP/US+Core+%27Patch%27+Process) ticket [FHIR-50288](https://jira.hl7.org/browse/FHIR-50288), approved patching the US Core Condition Encounter Diagnosis Profile in US Core 6.1.0. For purposes of certification, Condition.extension:assertedDate, Condition.onset[x],  Condition.abatement[x], Condition.clinicalStatus, and Condition.verificationStatus from the US Core Condition Encounter Diagnosis Profile are not required to be supported.
	
	**Applies to SVAP approved standards USCDI v4 and US Core 7.0.0:**
	
	* For the “Organization” and “Practitioner” US Core IG profiles, only the “read” type interaction must be supported and will be included in testing and certification. The “search” type interactions for these profiles are not in scope for testing and certification. Health IT Modules must support these US Core IG profiles because they are included as “must support” data elements in US Core IG profiles required by the United States Core Data for Interoperability (USCDI).
	* For purposes of testing and certification, health IT developers are not required to demonstrate Health IT Module support for the “QuestionnaireResponse” US Core IG profile.
	* The HL7® Cross-Group Projects workgroup, through the [US Core 'Patch' Process](https://confluence.hl7.org/display/CGP/US+Core+%27Patch%27+Process) ticket [FHIR-50283](https://jira.hl7.org/browse/FHIR-50283), approved patching the US Core Coverage Profile in US Core 7.0.0. For purposes of certification for the US Core Coverage Profile:
	  + Coverage.class:group.name is not required to be supported
	  + Coverage.class:group.value should represent “Group Identifier”
	* The HL7® Cross-Group Projects workgroup, through the [US Core 'Patch' Process](https://confluence.hl7.org/display/CGP/US+Core+%27Patch%27+Process) ticket [FHIR-50239](https://jira.hl7.org/browse/FHIR-50239), approved patching the US Core MedicationDispense Profile in US Core 7.0.0. For purposes of certification, references to US Core Practitioner Profile are not required to be supported for the MedicationDispense.performer.actor for the US Core MedicationDispense Profile.
	* The HL7® Cross-Group Projects workgroup, through the [US Core 'Patch' Process](https://confluence.hl7.org/display/CGP/US+Core+%27Patch%27+Process) ticket [FHIR-50288](https://jira.hl7.org/browse/FHIR-50288), approved patching the US Core Condition Encounter Diagnosis Profile in US Core 7.0.0. For purposes of certification, Condition.extension:assertedDate, Condition.onset[x],  Condition.abatement[x], Condition.clinicalStatus, and Condition.verificationStatus from the US Core Condition Encounter Diagnosis Profile are not required to be supported.
	

!!! example "Examples of “must support” in the US Core IG 3.1.1:"
    In US Core 3.1.1, the profile element Observation.value[x] contains the following Choices:
    `Quantity, CodeableConcept, string, boolean, integer, Range, Ratio, SampledData, time, dateTime, Period`
    A Health IT Module must support at least one of these Choices via the (g)(10) standardized API.

    In US Core 3.1.1, the profile element Provenance.agent.who contains the following References:
    `US Core Practitioner Profile, US Core Patient Profile, US Core Organization Profile`
    A Health IT Module must support at least one of these References via the (g)(10) standardized API.

	:material-video: Additionally, a guided walk through of "must support" in FHIR and US Core 3.1.1 can be found on YouTube <a target = "_blank" href = "https://youtu.be/CRsR4pViS4c">here</a>.

!!! note ""
	[Health IT Feedback and Inquiry Portal Q&A: Paragraph (g)(10)(i)(A): Data Response (Single Patient))](inquiry-portal/g10-inquiries.md#paragraph-g10ia-data-response-single-patient)

### Data Response (Multiple Patients)
???+ quote "**Regulation text at § 170.315(g)(10)(i)(B)**"
    (B) Respond to requests for multiple patients' data as a group according to the standards and implementation specifications adopted in § 170.215(a), (b)(1), and (d), for each of the data included in the standards adopted in § 170.213. All data elements indicated as “mandatory” and “must support” by the standards and implementation specifications must be supported.

<!-- $ref{g-10:CCG["Paragraph (g)(10)(i)(B) Data response – multiple patients"], tabbed} -->
??? quote "*Clarifications included in the (g)(10) CCG that apply to paragraph § 170.315(g)(10)(i)(B)*"
	Technical outcome – Respond to requests for multiple patients’ data as a group according to the standards and implementation specifications adopted in § 170.215(a), (b)(1) and (d), for each of the data included in the corresponding standard adopted in § 170.213. All data elements indicated as “mandatory” and “must support” by the standards and implementation specifications must be supported.
	
	***Clarifications:***
	
	**Applies to all applicable base regulatory and SVAP standards:**
	
	* Health IT Modules may support scopes using either the system wildcard scope syntax or a list of -system resource scopes- to enable the export of multiple patients’ data as a group.
	* During testing and certification for multiple patient services, Health IT Modules must demonstrate support for “Encounter,” “Organization,” and “Practitioner” US Core IG FHIR® Profiles.
	* Health IT Modules must support provenance according to the “Basic Provenance Guidance” section of the US Core IG.
	
	**Applies to USCDI v1 and US Core 3.1.1 and SVAP approved standards US Core 4.0.0 (expires on January 1, 2026) and USCDI v3 and US Core 6.1.0 (required by December 31, 2025):**
	
	* Health IT Modules must demonstrate support for the “Location” FHIR® resource by either by providing this resource as part of the multiple patient services response, or by including it as a contained resource as part of the multiple patient services response.
	
!!! note ""
	[Health IT Feedback and Inquiry Portal Q&A: Paragraph (g)(10)(i)(B): Data Response (Multiple Patients)](inquiry-portal/g10-inquiries.md#paragraph-g10ib-data-response-multiple-patients)

### Supported Search Operations (Single Patient)
???+ quote "**Regulation text at § 170.315(g)(10)(ii)(A)**"
    (ii) *Supported search operations*. (A) Respond to search requests for a single patient's data consistent with the search criteria included in the implementation specifications adopted in § 170.215(b)(1), specifically the mandatory capabilities described in “US Core Server CapabilityStatement.”

<!-- $ref{g-10:CCG["Paragraph (g)(10)(ii)(A) Supported search operations – single patient"], tabbed} -->
??? quote "*Clarifications included in the (g)(10) CCG that apply to paragraph § 170.315(g)(10)(ii)(A)*"
	Technical outcome – Respond to search requests for a single patient’s data consistent with the search criteria included in the implementation specification adopted in § 170.215(b)(1), specifically the mandatory capabilities described in “US Core Server CapabilityStatement”.
	
	***Clarifications:***
	
	**Applies to all applicable base regulatory and SVAP standards:**
	
	* All data elements indicated as “mandatory” and “must support” by the standards and implementation specifications must be supported and are in scope for testing.
	* The § 170.315(g)(10) certification criterion requires Health IT Modules to support API-enabled “read” services for single and multiple patients. “Read” services include those that allow authenticated and authorized third-party applications to view EHI through a secure API. These services specifically exclude “write” capabilities, where authenticated and authorized third-party applications would be able to create or modify EHI through a secure API.
	
*Additional Clarifications to the (g)(10) CCG:*

 - The scope of data available in the data responses defined in § 170.315(g)(10)(i) must be supported for searches for multiple patients via the supported search operations finalized in § 170.315(g)(10)(ii).

### Supported Search Operations (Multiple Patients)
???+ quote "**Regulation text at § 170.315(g)(10)(ii)(B)**"
    (B) Respond to search requests for multiple patients' data consistent with the search criteria included in the implementation specification adopted in § 170.215(d).

<!-- $ref{g-10:CCG["Paragraph (g)(10)(ii)(B) Supported search operations  - multiple patients "], tabbed} -->
??? quote "*Clarifications included in the (g)(10) CCG that apply to paragraph § 170.315(g)(10)(ii)(B)*"
	Technical outcome – Respond to search requests for multiple patients' data consistent with the search criteria included in an implementation specification adopted in § 170.215(d).
	
	***Clarifications:***
	
	**Applies to all applicable base regulatory and SVAP standards:**
	
	* No additional clarifications.
	
*Additional Clarifications to the (g)(10) CCG:*

- The scope of data available in the data responses defined in § 170.315(g)(10)(i) must be supported for searches for multiple patients via the supported search operations finalized in § 170.315(g)(10)(ii).
- The HL7® FHIR® Bulk Data Access (Flat FHIR®) (v1.0.1: STU 1) implementation specification adopted in § 170.215(d) includes mandatory support for the “group-export” "OperationDefinition."
- ONC has not included a requirement for Bulk FHIR® import because the standards for these features are still being developed by industry. Applications or systems seeking to import information formatting according to the <a target = "_blank" href = "https://hl7.org/fhir/uv/bulkdata/STU1.0.1/">HL7® FHIR® Bulk Data Access (Flat FHIR®) (V1.0.1:STU 1)</a> can use several methods developed by industry, or can refer to Bulk FHIR® import methods being defined by <a target = "_blank" href = "https://github.com/smart-on-fhir/bulk-import/blob/master/import.md">HL7® at the HL7® FHIR® Bulk Data GitHub page</a>.

### Application Registration
???+ quote "**Regulation text at § 170.315(g)(10)(iii)**"
    (iii) *Application registration*. Enable an application to register with the Health IT Module's “authorization server.”

<!-- $ref{g-10:CCG["Paragraph (g)(10)(iii) Application registration"], tabbed} -->
??? quote "*Clarifications included in the (g)(10) CCG that apply to paragraph § 170.315(g)(10)(iii)*"
	Technical outcome – Enable an application to register with the Health IT Module’s “authorization server.”
	
	***Clarifications:***
	
	**Applies to all applicable base regulatory and SVAP standards:**
	
	* Health IT presented for testing and certification must support app registration regardless of the scope of patient search utilized by the application (e.g., single or multiple).
	* This certification criterion requires a health IT developer, as finalized in the Condition of Certification requirements, to demonstrate its registration process, but does not require conformance to a standard.
	* The third-party application registration process that a health IT developer must meet under this criterion is not a form of review or “vetting” for purposes of this criterion.
	
	**Applies to USCDI v1 and US Core 3.1.1 and SVAP approved standard US Core 4.0.0 (expires on January 1, 2026):**
	
	* For demonstration of the SMART IG "Standalone Launch" steps, health IT developers are permitted to scope US Core IG resources that do not exist in either the standard adopted at § 170.213(a) (USCDI v1) or the "Compartment Patient" section of the standard adopted at § 170.215(a)(1) (HL7® FHIR® Release 4.0.1) as either patient/[Resource] or user/[Resource]. These resources include “Encounter,” “Device,” “Location,” “Medication,” “Organization,” “Practitioner,” and “PractitionerRole.” Health IT developers must document their supported scopes according to the technical documentation requirements at § 170.315(g)(10)(viii)(A) and § 170.404(a)(2).
	
	**Applies to USCDI v3 and US Core 6.1.0 (required by December 31, 2025):**
	
	* For demonstration of the SMART IG “Standalone Launch” steps, health IT developers are permitted to scope US Core IG resources that do not exist in either the standard adopted at § 170.213(b) (USCDI v3) or the “Compartment Patient” section of the standard adopted at § 170.215(a)(1) (HL7® FHIR® Release 4.0.1) as either patient/[Resource] or user/[Resource]. These resources include “Device,” “Location,” “Medication,” “Organization,” “Practitioner,” and “PractitionerRole.” Health IT developers must document their supported scopes according to the technical documentation requirements at § 170.315(g)(10)(viii)(A) and § 170.404(a)(2).
	
	**Applies to SVAP approved standards USCDI v4 and US Core 7.0.0:**
	
	* For demonstration of the SMART IG “Standalone Launch” steps, health IT developers are permitted to scope US Core IG resources that do not exist in either USCDI v4 or the “Compartment Patient” section of the standard adopted at § 170.215(a)(1) (HL7® FHIR® Release 4.0.1) as either patient/[Resource] or user/[Resource]. These resources include “Device,” “Medication,” “Organization,” “Practitioner,” and “PractitionerRole.” Health IT developers must document their supported scopes according to the technical documentation requirements at § 170.315(g)(10)(viii)(A) and § 170.404(a)(2).
	
*Additional Clarifications to the (g)(10) CCG:*

- ONC expects that apps executed within an implementer’s clinical environment will be registered with an authorization server, but ONC does not require a health IT developer to demonstrate its registration process for these “provider-facing” apps.
- The requirement that health IT developers must enable an application to register with the § 170.315(g)(10)-certified Health IT Module’s authorization server only applies for the purposes of demonstrating technical conformance to the finalized certification criterion and API Condition and Maintenance of Certification requirements. The practices by all parties (including implementers of Health IT Modules) other than developers of Certified Health IT Modules are not in scope for this certification criterion nor the associated Condition and Maintenance of Certification requirements.
- Any practices associated with third-party application review or “vetting” by implementers must not violate the <a target = "_blank" href = "https://www.ecfr.gov/cgi-bin/text-idx?SID=034c12732e5cb9328303ecdf94ecde87&mc=true&tpl=/ecfrbrowse/Title45/45cfr171_main_02.tpl">information blocking provisions</a>.

!!! note ""
	[Health IT Feedback and Inquiry Portal Q&A: Paragraph (g)(10)(iii): Application Registration](inquiry-portal/g10-inquiries.md#paragraph-g10iii-application-registration)

### Secure Connection
???+ quote "**Regulation text at § 170.315(g)(10)(iv)**" 
    (iv) *Secure connection*. (A) Establish a secure and trusted connection with an application that requests data for patient and user scopes in accordance with the implementation specifications adopted in § 170.215(b)(1) and (c). (B) Establish a secure and trusted connection with an application that requests data for system scopes in accordance with the implementation specification adopted in § 170.215(d).

<!-- $ref{g-10:CCG["Paragraph (g)(10)(iv) Secure connection"], tabbed} -->
??? quote "*Clarifications included in the (g)(10) CCG that apply to paragraph § 170.315(g)(10)(iv)*"
	Technical outcome - (A) Establish a secure and trusted connection with an application that requests data for patient and user scopes in accordance with the implementation specifications adopted in § 170.215(b)(1) and (c). (B) Establish a secure and trusted connection with an application that requests data for system scopes in accordance with an implementation specification adopted in § 170.215(d).
	
	***Clarifications:***
	
	**Applies to all applicable base regulatory and SVAP standards:**
	
	* TLS version 1.2 or above must be enforced for the appropriate connections.
	* Health IT developers are encouraged but not required to follow [TLS Best Current Practice (BCP 195)](https://www.rfc-editor.org/info/bcp195) for TLS version enforcement, referenced in [section 6.1.0.3 of the HL7](http://hl7.org/fhir/R4/security.html#http)® 4.0.1 Fast Healthcare Interoperability Resources Specification (FHIR®) Release 4, October 30, 2019, which recommends TLS 1.2 or above to be used for all production data exchange and limits support for lower versions of TLS. To meet ONC Certification requirements, Health IT developers must document how the Health IT Module enforces TLS version 1.2 or above to meet the API documentation requirements at § 170.315(g)(10)(viii) and API Transparency Conditions at 45 CFR 170.404(a)(2).
	

!!! note ""
	[Health IT Feedback and Inquiry Portal Q&A: Paragraph (g)(10)(iv): Secure Connection](inquiry-portal/g10-inquiries.md#paragraph-g10iv-secure-connection)
	
### First time Authentication / Authorization for Single Patient Services
???+ quote "**Regulation text at § 170.315(g)(10)(V)(A)(1)**"
    (v) *Authentication and authorization*—(A) *Authentication and authorization for patient and user scopes*—(1) *First time connections*—(i) Authentication and authorization must occur during the process of granting access to patient data in accordance with the implementation specification adopted in § 170.215(c) and standard adopted in § 170.215(e). (ii) Authentication and authorization must occur during the process of granting access to patient data in accordance with the implementation specification adopted in § 170.215(c) and standard adopted in § 170.215(e). (iii) A Health IT Module's authorization server must issue a refresh token for a period of no less than three months to native applications capable of securing a refresh token.

<!-- $ref{g-10:CCG["Paragraph (g)(10)(v)(A)(1) Authentication and authorization – Authentication and authorization for patient and user scopes – First time connections"], tabbed} -->
??? quote "*Clarifications included in the (g)(10) CCG that apply to paragraph § 170.315(g)(10)(v)(A)(1)*"
	Technical outcome – For first time connections, authentication and authorization must occur during the process of granting access to patient data in accordance with an implementation specification adopted in § 170.215(c) and standard adopted in § 170.215(e)(1). Additionally, a Health IT Module’s authorization server must issue a refresh token valid for a period of no less than three months to applications using the “confidential app” profile according to an implementation specification adopted in § 170.215(c). Finally, a Health IT Module’s authorization server must issue a refresh token for a period of no less than three months to native applications capable of securing a refresh token.
	
	***Clarifications:***
	
	**Applies to all applicable base regulatory and SVAP standards:**
	
	* Health IT Modules will be explicitly tested for US Core IG operations using authentication and authorization tokens acquired via the process described in an implementation specification adopted in § 170.215(c).
	* Only the relevant parts of the OpenID Connect Core 1.0 including errata set 1 adopted in § 170.215(e)(1) that are also included in an implementation specification adopted in § 170.215(c) will be in-scope for testing and certification.
	* Although Health IT Modules presented for testing and certification must include the ability for patients to authorize an application to receive their EHI based on FHIR® resource-level scopes, Health IT Modules are not prohibited from presenting authorization scopes in a more user-friendly format (e.g. grouping resources under categories, renaming the scopes for easier comprehension by the end-user, using more granular scopes), as long as the ability for patients to authorize applications based on resource-level scopes is available, if requested by the patient.
	* For § 170.315(g)(10) criterion requirements at § 170.315(g)(10)(v)(A) regarding authorization for patient and user scopes, we clarify wildcard scopes as defined in the implementation specifications at § 170.215(c) are not required to be supported.
	* Health IT Modules will only be tested for the "Patient Access for Standalone Apps" and "Clinician Access for EHR Launch" "Capability Sets” described in an implementation specification adopted at § 170.215(c).
	* Since the “Patient Access for Standalone Apps” and “Clinician Access for EHR Launch” “Capability Sets” do not include “context-standalone-encounter" ONC will not test Health IT Modules for support for the "context-standalone-encounter" SMART on FHIR® Capability described in an implementation specification adopted at § 170.215(c).
	* Implementers of § 170.315(g)(10)-certified Health IT Modules should be mindful of the information blocking provisions.
	* As part of the requirements at § 170.315(g)(10)(v)(A)(1)(iii), health IT developers must publish the method(s) by which their Health IT Modules support the secure issuance of an initial refresh token to native applications according to the technical documentation requirements at § 170.315(g)(10)(viii) and transparency conditions at § 170.404(a)(2).
	* Application developer affirmations to health IT developers regarding the ability of their applications to secure a refresh token, a client secret, or both, must be treated in a good faith manner consistent with the provisions established in the openness and pro-competitive conditions at § 170.404(a)(4).
	* Health IT developers can determine the method(s) they use to support interactions with native applications and clarify that health IT developers are not required to support all methods third-party application developers seek to use.
	* ONC recognizes there may be some ambiguity in the HL7® SMART Application Launch Framework Implementation Guide (incorporated by reference at § 170.215(c)) in its guidance for supporting native applications, in particular, in providing references to best practices, strategies, and examples such as “OAuth 2.0 for Native Apps: 8.5. Client Authentication”, “OAuth 2.0 Dynamic Client Registration Protocol”, and “universal redirect\_uris” without a standardized solution. ONC provides flexibility for how the health IT developer implements the HL7® SMART Application Launch Framework implementation specification, as long as the Certified Health IT Module supports for first time connections the issuance of three-month refresh tokens to native applications capable of securing a refresh token.
	* The paragraph at § 170.215(c) requires health IT developers to support the SMART Application Launch Framework Implementation Guide (SMART IG) “SMART [on FHIR®] Core Capabilities,” including “permission-offline,” which grants support for refresh tokens. The implementation specifications adopted in § 170.215(c) require that patients have the ability to explicitly enable the “offline\_access” scope during authorization. If the “offline\_access” scope is not enabled by patients, patients will be required to re-authenticate and re-authorize an application's access to their EHI after the application's access token expires. However, the ability of a patient to explicitly enable the “offline\_access” scope during authorization is not described in the implementation specification. ONC clarifies that health IT developers must support the ability for patients to be provided information about an application’s request for persistent access prior to the patient sharing their health information, in order to enable patients to make an informed decision during authorization. Examples include, but are not limited to a health IT developer allowing patients to granularly grant “offline-access” scopes during authorization or clearly providing this information as a notice during authorization. The critical requirement is that patients are empowered to deny authorization for offline access.
	* The SMART capabilities in § 170.215(c) are explicitly required for testing and certification because these capabilities are otherwise indicated as optional in the implementation specification.
	
	**Applies to USCDI v1 and US Core 3.1.1 and SVAP approved standard US Core 4.0.0 (expires on January 1, 2026):**
	
	* Since "Encounter" is not a USCDI v1 data class or data element, ONC will not test Health IT Modules for support for "context-ehr-encounter" SMART on FHIR® Core Capabilities described in an implementation specification adopted at § 170.215(c).
	
	**Applies to SMART App Launch Framework 1.0.0 (expires on January 1, 2026):**
	
	* As part of the “permission-patient” “SMART on FHIR® Core Capability” in § 170.215(c), Health IT Modules presented for testing and certification must include the ability for patients to authorize an application to receive their electronic health information (EHI) based on FHIR® resource-level scopes. Specifically, this means patients would need to have the ability to authorize access to their EHI at the individual FHIR® resource level, from one specific FHIR® resource (e.g., “Immunization”) up to all FHIR® resources necessary to implement a standard adopted in § 170.213 and corresponding implementation specification adopted in § 170.215(b)(1).
	* As described in the ONC Cures Act Final Rule, we encourage implementers to adhere to industry best practices to mitigate Cross-Site Request Forgery (CSRF) and other known security threats ([85 FR 25742](https://www.federalregister.gov/d/2020-07419/p-1186)). Proof Key for Code Exchange (PKCE) ([Internet Engineering Task Force Request for Comments 7636](https://datatracker.ietf.org/doc/html/rfc7636)) is an industry standard that can help mitigate CSRF and other known security threats. The ONC Health IT Certification Program will support the optional use of PKCE during authentication and authorization testing. Health IT developers that implement and require the use of PKCE should include documentation for their PKCE implementation as part of the API Documentation requirement at [45 CFR 170.315(g)(10)(viii)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-D/part-170/subpart-C#p-170.315(g)(10)(viii)) and API Transparency Conditions at [45 CFR 170.404(a)(2)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-D/part-170/subpart-D#p-170.404(a)(2)).
	
	**Applies to SMART App Launch 2.0.0 (required by December 31, 2025) and SVAP approved standard SMART App Launch 2.2.0:**
	
	* For certification purposes, a Health IT Module is not required to support authorization requests nor responses including a combination of SMART v1 and SMART v2 scopes. For example, an authorization request including simultaneously the SMART v1 scope of “patient/Observation.read” and the SMART v2 scope of “patient/Condition.rs” is not required to be supported.
	* A Health IT Module may optionally support the "fhirContext" launch context parameter defined in the SMART App Launch 2.0.0 implementation guide. If the "fhirContext" parameter is supported, the Health IT Module must conform to the requirements for the parameter detailed in the SMART App Launch implementation guide.
	* We clarify the following SMART App Launch capabilities must be supported as part of fulfilling the authentication and authorization requirements at § 170.315(g)(10)(v)(A) when certifying using the implementation specification at § 170.215(c)(2):
		+ To support patient access for standalone apps, the Health IT Module must support:
			- the capabilities of "launch-standalone" and "context-standalone-patient"; and
			- the capabilities in subsections "Authorization Methods", "Client Types", "Single Sign-on", and "Permissions" except the "permission-online" and "permission-user" capabilities
		+ To support clinician access for EHR launch, the Health IT Module must support:
			- the capabilities of "launch-ehr", "context-banner", "context-style", "context-ehr-patient", and "context-ehr-encounter" (if supporting USCDI v2 or v3); and
			- the capabilities in subsections "Authorization Methods", "Client Types", "Single Sign-on", and "Permissions" except the "permission-online" capability
	* As finalized in the HTI-1 Final Rule ([89 FR 1294](https://www.federalregister.gov/d/2023-28857/p-1250)), Health IT Modules are required to support SMART App Launch "Finer-grained resource constraints using search parameters" for the “category” parameter for the Condition resource with Condition sub-resources Encounter Diagnosis, Problem List, and Health Concern, and the Observation resource with Observation sub-resources Clinical Test, Laboratory, Social History, SDOH, Survey, and Vital Signs. We defer to the implementation guides referenced at § 170.215(b)(1) and § 170.215(c) for specific implementation guidance for this requirement. In the context of the US Core 6.1.0 implementation guide, the Observation sub-resources of Clinical Test and SDOH may have scopes supported as follows:
		+ support for scopes for the Observation sub-resource Clinical Test using the "procedure" code from the [US Core Clinical Result Observation Category value set](https://hl7.org/fhir/us/core/STU6.1/ValueSet-us-core-clinical-result-observation-category.html).
		+ support for scopes for the Observation sub-resource SDOH using the "sdoh" code from the [US Core Category code system](https://hl7.org/fhir/us/core/STU6.1/CodeSystem-us-core-category.html).
	* The US Core 7.0.0 IG includes requirements for how scopes for the Condition and Observation resources must be supported, including  requirements in the [“SMART on FHIR Obligations and Capabilities” section](https://hl7.org/fhir/us/core/STU7/scopes.html#smart-on-fhir-obligations-and-capabilities) as well as Condition and Observation profiles sections.
	* For certification and testing purposes the Health IT Module must demonstrate support for patients and users to authorize an app to receive patient data using scopes with “Finer-grained resource constraints using search parameters” for the sub-resources specified in the HTI-1 Final Rule. We require a Health IT Module to support a patient’s ability to provide authorization at the individual sub-resource scope level.
	* Although Health IT Modules presented for testing and certification must include the ability for patients to authorize an application to receive their EHI based on individual FHIR resource level and individual sub-resource level scopes, Health IT Modules are not prohibited from presenting authorization scopes in a more user-friendly format (e.g. grouping scopes under categories, renaming the scopes for easier comprehension by the end-user), as long as the ability for patients to authorize applications based on individual resource level and individual sub-resource level scopes is available, if requested by the patient.
	* As part of supporting the SMART App Launch “permission-v2” capability for the purposes of certification, if an app requests authorization for a resource level scope for the “Condition” or “Observation” resources, then for patient authorization purposes a Health IT Module must support presentation of the required sub-resource scopes to the patient for authorization. Specifically, sub-resource scopes must be presented for patient authorization as follows:
		+ “Condition” sub-resource scopes “Encounter Diagnosis”, “Problem List”, and “Health Concern” if a “Condition” resource level scope is requested
		+ “Observation” sub-resource scopes “Clinical Test”, “Laboratory”, “Social History”, “SDOH”, “Survey”, and “Vital Signs” if an “Observation” resource level scope is requested
	* For purposes of certification to the § 170.315(g)(10) criterion, a Health IT Module is not required to support for authorization purposes presentation of sub-resource scopes to the user during clinician access for EHR launch.
	
*Additional Clarifications to the (g)(10) CCG:*

- ONC expects implementers of § 170.315(g)(10)-certified Health IT Modules to have the capability of revoking refresh tokens where appropriate.
- Neither § 170.315(g)(10) nor applicable API Condition and Maintenance of Certification requirements require restricting discretion of implementers (healthcare providers, clinician practices, hospitals, etc.) to set the length of refresh tokens for users of the API including patients and healthcare providers to align with their institutional policies.
- Implementers of § 170.315(g)(10)-certified Health IT Modules are not prohibited from implementing their § 170.315(g)(10)-certified Health IT Modules in accordance with their organizational security policies and posture, including by instituting policies for reauthentication and re-authorization (e.g., healthcare providers and/or patients could always be required to re-authenticate and re-authorize after a set number of refresh tokens have been issued).
- Patients are not prohibited from changing the length of refresh tokens to the degree this option is available to them.
- Implementers of § 170.315(g)(10)-certified Health IT Modules should be mindful of <a target = "_blank" href = "https://www.ecfr.gov/cgi-bin/text-idx?SID=034c12732e5cb9328303ecdf94ecde87&mc=true&tpl=/ecfrbrowse/Title45/45cfr171_main_02.tpl">information blocking provisions</a> applicable to them and that requiring patients to reauthenticate and re-authorize at a high frequency could inhibit patient access and implicate information blocking.

??? info "First time Authentication / Authorization for Single Patient Services: Sequence Diagram"
	**First time connections:**
	``` mermaid
	sequenceDiagram
		participant app as App
		participant authz as Health IT Module's Authorization Server
		participant fhir as Health IT Module's FHIR® Server

		alt EHR Launch
			authz ->> authz: EHR user launches app
			authz ->> app: Launch Request
		else Standalone Launch
			app ->> app: App user connects to EHR
		end
		app ->> fhir: Discovery request
		fhir -->> app: Discovery response
		app ->> authz: Authorization request
		authz -->> authz: End-user authorization
		alt Granted
			authz -->> app: Authorization granted
            alt App is a “confidential app” according to an implementation specification adopted in § 170.215(c) (SMART App Launch IG)
			app ->> authz: Access token request
			note over app,authz: Client secret used for authentication
            else App is a native app capable of securing a refresh token
			app ->> authz: Access token request
            note over app,authz: Proof Key for Code Exchange (PKCE) can be used by <br/> any OAuth 2.0 app type to increase security when <br/> requesting a token on first time connections
            end
			authz -->> app: Initial access token and initial refresh token response
			loop while initial access token is valid
				app ->> fhir: Initial access token used to request resources
			end
		else Denied
			authz -->> app: Authorization error
		end
	```
	As specified in <a target = "_blank" href = "https://tools.ietf.org/html/rfc6749">RFC 6749</a> and the <a target = "_blank" href = "https://hl7.org/fhir/smart-app-launch/1.0.0/">HL7® SMART Application Launch Framework Implementation Guide</a>, some native applications are unable to claim they are confidential. By definition, these non-confidential (i.e., "public") native applications do not have a client secret and thus cannot authenticate with the authorization server when receiving access and refresh tokens. However, there are additional methods that non-confidential native applications can use to increase refresh token security during “First time connections.” Methods like Proof Key for Code Exchange (PKCE), the use of secure redirect URI schemes[^2], and utilizing on-device secure storage techniques to securely store the refresh token can increase the security of an initial refresh token. Methods like these ensure that an authorization server issues initial access and refresh tokens to the correct corresponding authorized application. The paragraph at § 170.315(g)(10)(v)(A)(1)(iii) requires that Health IT Modules issue an initial refresh token to native applications capable of securing a refresh token.

	See [Subsequent Authentication / Authorization for Single Patient Services](#subsequent-authentication-authorization-for-single-patient-services) for sequence diagram once the initial access token is invalid (e.g., expiration).

!!! tip "OAuth Implementation Presentations"
	:material-video: Below is a list of presentations that can be used by Certified Health IT Developers to kick-start their OAuth implementations.

	These presentations are best when consumed in the following order:

	1. <a target = "_blank" href = "https://youtu.be/rURoGATC4L8">OAuth2 Overview</a> - Overview of the OAuth2.0 standard and the Authorization Code Grant Type.
	1. <a target = "_blank" href = "https://youtu.be/zKudZCwTU4Q">SMART App Authorization Overview</a> - Overview of the SMART App Authorization and its value in implementing an interoperable OAuth2 compliant server.
	1. <a target = "_blank" href = "https://youtu.be/X7l3a_jN24g">SMART App Client Registration</a> - Information on different concepts and software code for Client Registration.
	1. <a target = "_blank" href = "https://youtu.be/MjTskVYjDNc">SMART App Client Authorization Part 1</a> - Indepth look at the authorization process, the requests and the specification.
	1. <a target = "_blank" href = "https://youtu.be/lFolfRSVWJE">SMART App Client Authorization Part 2</a> - Indepth look at the code used for Client Authorization in Part 1.

	Video downloads and PowerPoint slides can be found here: <a target = "_blank" href = "https://github.com/onc-healthit/oauth-samples">oauth-samples</a>

!!! note ""
	[Health IT Feedback and Inquiry Portal Q&A: Paragraph (g)(10)(v)(A)(1): First Time Authentication / Authorization for Single Patients](inquiry-portal/g10-inquiries.md#paragraph-g10va1-first-time-authentication-authorization-for-single-patients)

### Subsequent Authentication / Authorization for Single Patient Services
???+ quote "**Regulation text at § 170.315(g)(10)(V)(A)(2)**"
    (2) *Subsequent connections*. (i) Access must be granted to patient data in accordance with the implementation specification adopted in § 170.215(c) without requiring re-authorization and re-authentication when a valid refresh token is supplied by the application. (ii) A Health IT Module's authorization server must issue a refresh token valid for a new period of no less than three months to applications using the “confidential app” profile according to an implementation specification adopted in § 170.215(c).

<!-- $ref{g-10:CCG["Paragraph (g)(10)(v)(A)(2) Authentication and authorization – Authentication and authorization for patient user scopes – Subsequent connections"], tabbed} -->
??? quote "*Clarifications included in the (g)(10) CCG that apply to paragraph § 170.315(g)(10)(V)(A)(2)*"
	Technical outcome – For subsequent connections, access must be granted to patient data in accordance with an implementation specification adopted in§ 170.215(c) without requiring re-authorization and re-authentication when a valid refresh token is supplied by the application. Additionally, a Health IT Module’s authorization server must issue a refresh token valid for a new period of no less than three months to applications using the “confidential app” profile according to an implementation specification adopted in § 170.215(c).
	
	***Clarifications:***
	
	**Applies to all applicable base regulatory and SVAP standards:**
	
	* For subsequent connections of applications capable of storing a client secret, Health IT Modules are required to issue a refresh token valid for a new period of no shorter than three months per the API certification criterion requirement finalized in § 170.315(g)(10)(v)(A)(2)(ii).
	
*Additional Clarifications to the (g)(10) CCG:*

- For subsequent connections, Certified Health IT Modules are not required to issue a new
refresh token, but must issue a refresh token valid for a new period of no less than three
months. Whether the application receives a “new” refresh token is an implementation
decision left to the health IT developer, as long as the “refreshed” refresh token is valid for a
new period of no less than three months.

??? info "Subsequent Authentication / Authorization for Single Patient Services: Sequence Diagram"
    As specified in <a target = "_blank" href = "https://tools.ietf.org/html/rfc6749">RFC 6749</a> and the <a target = "_blank" href = "https://hl7.org/fhir/smart-app-launch/1.0.0/">HL7® SMART Application Launch Framework Implementation Guide</a>, authorization servers can send and receive refresh tokens to and from apps in two different OAuth 2.0 connection flows. On [first time connections (see sequence diagram above)](#first-time-authentication-authorization-for-single-patient-services), an app requests an authorization code and is granted an authorization code after obtaining end-user authorization. An app can then exchange a valid authorization code for an initial access token and initial refresh token.
	
	After an access token expires, an app can subsequently connect to an authorization server to exchange a valid refresh token for a new access token and also have its refresh token renewed without needing to obtain end-user authorization. During both exchanges, security is increased (i.e., greater protection against leaked refresh tokens) when confidential apps use their client secret for client authentication. The (g)(10) criterion paragraphs at § 170.315(g)(10)(v)(A)(1)(ii) and § 170.315(g)(10)(v)(A)(2)(ii) require that apps using the “confidential app” profile and thus capable of authenticating themselves, must be given a refresh token upon valid first time connections and have their refresh tokens renewed upon valid subsequent connections. This enables persistent access for apps using the “confidential app” profile without requiring end-user re-authorization.

	**Subsequent connections:**
	``` mermaid
		sequenceDiagram
			participant app as App
			participant authz as Health IT Module's Authorization Server
			participant fhir as Health IT Module's FHIR® Server

			loop while refresh token is valid
				alt App is a “confidential app” according to an implementation specification adopted in § 170.215(c) (SMART App Launch IG)
					app ->> authz: Refresh token
					note over app,authz: Client secret used for authentication
					note over authz: The (g)(10) criterion paragraph at § 170.315(g)(10)(v)(A)(2)(ii) requires <br/> that apps using the “confidential app” profile have their refresh tokens renewed <br/> (i.e., made valid for a new period of no less than three months). This could <br/> include the authorization server issuing a new refresh token or renewing the <br/> existing refresh token.
					alt Health IT Module's Authorization Server issues a new refresh token
						authz -->> app: New access token and new refresh token response
					else Health IT Module's Authorization Server renews existing refresh token
						authz -->> app: New access token response
						authz -->> authz: Existing refresh token renewed
					end
				else App is not a “confidential app” according to an implementation specification adopted in § 170.215(c) (SMART App Launch IG)
					app ->> authz: Refresh token
					authz -->> app: New access token response
				end
				loop while new access token is valid
					app ->> fhir: New access token used to request resources
				end
			end
	```

### Authentication / Authorization for Multiple Patient Services
???+ quote "**Regulation text at § 170.315(g)(10)(v)(B)**" 
    (B) *Authentication and authorization for system scopes*. Authentication and authorization must occur during the process of granting an application access to patient data in accordance with the “SMART Backend Services: Authorization Guide” section of the implementation specification adopted in § 170.215(d) and the application must be issued a valid access token.

<!-- $ref{g-10:CCG["Paragraph (g)(10)(v)(B) Authentication and authorization – Authentication and authorization for system scopes"], tabbed} -->
??? quote "*Clarifications included in the (g)(10) CCG that apply to paragraph § 170.315(g)(10)(v)(B)*"
	Technical outcome – Authentication and authorization must occur during the process of granting an application access to patient data in accordance with the “SMART Backend Services: Authorization Guide” section of an implementation specification adopted in § 170.215(d) and the application must be issued a valid access token.
	
	***Clarifications:***
	
	**Applies to all applicable base regulatory and SVAP standards:**
	
	* Health IT Modules may use access control schemes other than OAuth 2.0 for controlling access to the file server, such as capability URLs. The HL7® FHIR®-I Work Group has documented expectations for the use of capability URLs with the Bulk Data Access IG on the [HL7® confluence website](https://confluence.hl7.org/x/RGvUB). For purposes of Certification testing, Health IT Modules will be tested for the ability to share bulk data files either using OAuth 2.0 bearer tokens or via capability URLs accessible without preconditions or additional steps.
	
<!-- https://sequencediagram.org/ -->
??? info "Authentication / Authorization for Multiple Patient Services: Sequence Diagrams"
	The Bulk Data Export and Authentication/Authorization sequences, according to the §170.315(g)(10) requirements, are described below.

	First, according to <a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-3468">§170.315(g)(10)(v)(B)</a>, Authentication and authorization must occur during the process of granting an application access to patient data in accordance with the “<a target = "_blank" href = "https://hl7.org/fhir/uv/bulkdata/STU1.0.1/authorization/index.html">SMART Backend Services: Authorization Guide</a>” section of the Bulk Data implementation guide.
	
	``` mermaid
	sequenceDiagram
	Backend Service->>FHIR Authorization Server: Client Registration (may be out of band)
	Backend Service ->> FHIR Resource Server: Discovery request
	FHIR Resource Server -->> Backend Service: Discovery response
	Backend Service ->> FHIR Authorization Server: Access token request
	note over FHIR Authorization Server: On approval
	FHIR Authorization Server -->> Backend Service: Access token response
	Backend Service->>FHIR Resource Server: Bulk data kick-off request (including access token)
	note over FHIR Resource Server: On success
	FHIR Resource Server -->> Backend Service: URL of an endpoint for subsequent status requests
	Backend Service ->>FHIR Resource Server: Bulk data status request
	note over FHIR Resource Server: On export generation completion
	FHIR Resource Server -->> Backend Service: Link(s) to the generated bulk data files (output manifest)
	```

	*Note that generated Bulk Data files <a target = "_blank" href = "https://hl7.org/fhir/uv/bulkdata/STU1.0.1/export/index.html#response---complete-status">may</a> be served by file servers other than a FHIR-specific server.*

	There are different ways for a client to receive generated Bulk Data files including via <a target = "_blank" href = "https://confluence.hl7.org/display/FHIRI/Capability+URLs+for+Download+Links">Capability URLs for Download Links</a>. The client will refer to the `requiresAccessToken` field included in the output manifest when retrieving files.

	If `reqiresAccessToken = true`

	```mermaid
	sequenceDiagram
	Backend Service->>File Server: Request files (using access token)
	note over File Server: On success
	File Server-->>Backend Service: Receive files
	```

	If `reqiresAccessToken = false`	

	```mermaid
	sequenceDiagram
	Backend Service->>File Server: Request files
	note over File Server: On success
	File Server-->>Backend Service: Receive files
	```

	It is critical that server developers follow the HL7 guidance on  <a target = "_blank" href = "https://confluence.hl7.org/display/FHIRI/Capability+URLs+for+Download+Links">Capability URLs for Download Links</a> when choosing to generate output manifests with `requiresAccessToken = false`.

!!! note ""
	[Health IT Feedback and Inquiry Portal Q&A: Paragraph (g)(10)(v)(B): Authentication / Authorization for Multiple Patient Services](inquiry-portal/g10-inquiries.md#paragraph-g10vb-authentication-authorization-for-multiple-patient-services)

### Patient Authorization Revocation
???+ quote "**Regulation text at § 170.315(g)(10)(vi)**" 
    (vi) *Patient authorization revocation*. A Health IT Module's authorization server must be able to revoke and must revoke an authorized application's access at a patient's direction within 1 hour of the request.

<!-- $ref{g-10:CCG["Paragraph (g)(10)(vi) Patient authorization revocation"], tabbed} -->
??? quote "*Clarifications included in the (g)(10) CCG that apply to paragraph § 170.315(g)(10)(vi)*"
	Technical outcome – A Health IT Module’s authorization server must be able to revoke and must revoke an authorized application’s access at a patient’s direction within one hour of the request.
	
	***Clarifications:***
	
	**Applies to all applicable base regulatory and SVAP standards:**
	
	* This is a functional requirement to allow health IT developers the ability to implement it in a way that best suits their existing infrastructure and allows for innovative models for authorization revocation to develop.
	* Patients are expected to have the ability to revoke an authorized application’s access to their EHI at any time.
	* For authorization revocation, Health IT Modules presented for certification are permitted to allow short-lived access tokens to expire in lieu of immediate access token revocation. ONC recommends health IT developers limit the lifetime of access tokens to one hour or less as recommended in the implementation specifications adopted at § 170.215(c). For purposes of testing and certification, Health IT Modules will be tested for patient authorization revocation occurring within one hour of the request.
	

!!! note ""
	[Health IT Feedback and Inquiry Portal Q&A: Paragraph (g)(10)(vi): Patient Authorization Revocation](inquiry-portal/g10-inquiries.md#paragraph-g10vi-patient-auhtorization-revocation)
	
### Token Introspection
???+ quote "**Regulation text at § 170.315(g)(10)(vii)**" 
    (vii) *Token introspection*. A Health IT Module's authorization server must be able to receive and validate tokens it has issued in accordance with an implementation specification in § 170.215(c).

<!-- $ref{g-10:CCG["Paragraph (g)(10)(vii) Token introspection"], tabbed} -->
??? quote "*Clarifications included in the (g)(10) CCG that apply to paragraph § 170.315(g)(10)(vii)*"
	Technical outcome – A Health IT Module’s authorization server must be able to receive and validate tokens it has issued in accordance with an implementation specification in § 170.215(c).
	
	***Clarifications:***
	
	**Applies to all applicable base regulatory and SVAP standards:**
	
	* Health IT Developers must update their § 170.315(g)(10)-certified Health IT Modules to support token introspection as defined in the SMART App Launch 2.0.0 or 2.2.0 implementation specification, and provide such updated Certified Health IT Modules to their customers by December 31, 2025.
	
### Technical API Documentation Content
???+ quote "**Regulation text at § 170.315(g)(10)(viii)(A)**" 
    (viii) *Documentation*. (A) The API(s) must include complete accompanying documentation that contains, at a minimum: (1) API syntax, function names, required and optional parameters supported and their data types, return variables and their types/structures, exceptions and exception handling methods and their returns. (2) The software components and configurations that would be necessary for an application to implement in order to be able to successfully interact with the API and process its response(s). (3) All applicable technical requirements and attributes necessary for an application to be registered with a Health IT Module's authorization server.

<!-- $ref{g-10:CCG["Paragraph (g)(10)(viii)(A) Documentation – minimum requirements"], tabbed} -->
??? quote "*Clarifications included in the (g)(10) CCG that apply to paragraph § 170.315(g)(10)(viii)(A)*"
	Technical outcome – The API(s) must include complete accompanying documentation that contains, at a minimum: (*1*) API syntax, function names, required and optional parameters supported and their data types, return variables and their types/structures, exceptions and exception handling methods and their returns; (*2*) The software components and configurations that would be necessary for an application to implement in order to be able to successfully interact with the API and process its response(s); and (*3*) All applicable technical requirements and attributes necessary for an application to be registered with a Health IT Module’s authorization server.
	
	***Clarifications:***
	
	**Applies to all applicable base regulatory and SVAP standards:**
	
	* Health IT developers are not required to re-publish documentation from the adopted standards and implementation specifications. However, health IT developers must publish documentation that goes beyond the adopted standards and implementation specifications.
	* Health IT developers are expected to disclose any additional data their § 170.315(g)(10)-certified Health IT Module supports in the context of the adopted standards and implementation specifications.
	
### Technical API Documentation Availability
???+ quote "**Regulation text at § 170.315(g)(10)(viii)(B)**"
    (B) The documentation used to meet paragraph (g)(10)(viii)(A) of this section must be available via a publicly accessible hyperlink without any preconditions or additional steps.

<!-- $ref{g-10:CCG["Paragraph (g)(10)(viii)(B) Documentation – public access"], tabbed} -->
??? quote "*Clarifications included in the (g)(10) CCG that apply to paragraph § 170.315(g)(10)(viii)(B)*"
	Technical outcome – The documentation used to meet paragraph (g)(10)(viii)(A) of this section must be available via a publicly accessible hyperlink without any preconditions or additional steps.
	
	***Clarifications:***
	
	**Applies to all applicable base regulatory and SVAP standards:**
	
	* No additional clarifications.
	

## Testing and Certification
### Test Procedure
The § 170.315(g)(10) test procedure provides the structure for evaluating conformance of a Health IT Module to the <a target = "_blank" href = "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-D/part-170/subpart-C/section-170.315#p-170.315(g)(10)">(g)(10) certification criterion requirements</a>. 

The § 170.315(g)(10) test procedure is located <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services#test_procedure">here on healthit.gov</a>.

### Inferno Framework
The <a target = "_blank" href = "https://inferno.healthit.gov/onc-certification-g10-test-kit">(g)(10) Standardized API Test Kit</a>, built using the <a target = "_blank" href = "https://inferno-framework.github.io/inferno-core/">Inferno Framework</a>, is used for (g)(10) API testing in the ONC Health IT Certification Program. The (g)(10) Standardized API Test Kit comes with all of the services necessary to test health IT modules seeking to meet the requirements of the Standardized API for patient and population services criterion finalized at § 170.315(g)(10). It is based on the requirements in the ONC Cures Act Final Rule and <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services#test_procedure">associated test procedure for § 170.315(g)(10)</a>.

!!! note ""
	<p align="center">
		![Inferno (g)(10) testing tool logo](images/inferno-logo.PNG){: style="height:100px"}
	</p>
	<p style="text-align: center;"><a target = "_blank" href = "https://inferno.healthit.gov/"><span style="font-size:larger;">inferno.healthit.gov</a></span></p>

??? tip "Explore Inferno for (g)(10) Testing"	
	**Get Involved and Ask Questions**

	 - Join the <a target = "_blank" href = "https://chat.fhir.org/#narrow/stream/179309-inferno">Inferno Zulip Stream</a> on chat.fhir.org (*creating a Zulip account is free*). This stream is actively monitored by Inferno's development team.
	 - Submit inquiries to ONC via the <a target = "_blank" href = "https://www.healthit.gov/feedback">Health IT Feedback Portal</a>.
	 - Submit discovered technical issues on <a target = "_blank" href = "https://github.com/onc-healthit/inferno-program/issues">GitHub</a>.
	 - Join the <a target = "_blank" href = "https://groups.google.com/g/inferno-testing">Inferno Google Group</a> (*Google account required, join by clicking "joining the group"*). Here you will also find information on the **Inferno Monthly Tech Talk** meeting which is open to anyone and occurs on the second Wednesday of each month from 1 - 2 PM EST.

!!! note ""
	[Health IT Feedback and Inquiry Portal Q&A: Inferno](inquiry-portal/g10-inquiries.md#inferno)

### Real World Testing Condition and Maintenance of Certification

**Health IT developers are required to test the real-world use of APIs.**

The § 170.315(g)(10) criterion is included under the <a target = "_blank" href = "https://www.ecfr.gov/current/title-45/section-170.405">Real World Testing Condition and Maintenance of Certification requirements</a> in §170.405, which state:

!!! note ""
     “A health IT developer with one or more Health IT Module(s) certified to any one or more of the ONC Certification Criteria for Health IT in § 170.315(b), (c)(1) through (3), (e)(1), (f), (g)(7) through (10), and (h) must successfully test the real world use of those Health IT Module(s) for interoperability (as defined in 42 U.S.C. 300jj(9) and § 170.102) in the type of setting in which such Health IT Module(s) would be/is marketed.” 
 
 More information can be found on the <a target = "_blank" href = "https://www.healthit.gov/sites/default/files/page/2021-02/Real-World-Testing-Fact-Sheet.pdf">Real World Testing Fact Sheet</a> and <a target = "_blank" href = "https://www.healthit.gov/sites/default/files/page/2021-08/ONC-Real%20World%20Testing%20Resource%20Guide_Aug%202021.pdf">Real World Testing Resource Guide</a>.

## Standards Version Advancement Process
**Health IT developers are permitted to test and certify using newer versions of implementation guides that have been approved by the ONC National Coordinator.**

ONC has established the voluntary Standards Version Advancement Process (SVAP) to enable health IT developers to incorporate newer versions of approved standards and implementation specifications, as part of the Real World Testing Condition and Maintenance of Certification requirements (§ 170.405) of the 21st Century Cures Act. 

Using SVAP, Certified Health IT Developers are permitted to voluntarily use a more advanced version of the standard(s) and implementation specification(s) approved by the National Coordinator, than is adopted in the ONC Certification Criteria. Currently, this flexibility is limited to standards and implementation specifications that are adopted in the certification criteria required to meet the Real World Testing Condition of Certification, which include § 170.315(b), (c)(1) through (3), (e)(1), (f), (g)(7) through (10), and (h). Health IT developers must ensure that they address standards adopted under SVAP in their Real World Testing plans and results submitted to Authorized Certification Bodies. More information can be found on the <a target = "_blank" href = "https://www.healthit.gov/isa/standards-version-advancement-process">SVAP landing page</a>.

{==

<p style="text-align: center;"><a target = "_blank" href = "https://www.healthit.gov/buzz-blog/health-it/advancements-in-health-it-oncs-approved-svap-standards-for-2024">Advancements in Health IT: ONC’s Approved SVAP Standards for 2024</a></p>

==}

[^1]: HL7®, and FHIR® are the registered trademarks of Health Level Seven International and their use of these trademarks does not constitute an endorsement by HL7.
[^2]: See RFC 8252 section <a target = "_blank" href = "https://www.rfc-editor.org/rfc/rfc8252#section-7">7 Receiving the Authorization Response in a Native App</a>

--8<-- "includes/abbreviations.md"
