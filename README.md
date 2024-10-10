# Task: Develop a Validation Pipeline with Parameterized Inputs, Two Extractors, and Two Validators

We need to build a pipeline to validate PDF data, specifically targeting the company name and date on the first (cover) page. Use as an input file `report.pdf`.

### Requirements for General Pipeline Logic:
- *Modular Design:* The pipeline should be easily extendable, allowing the addition of new extractors and validators without modifying the core logic.
- *Type Safety:* Use type annotations to enhance code clarity and catch potential issues early.
- *Component Separation:* Structure the code into distinct modules for extraction, validation, and the core pipeline logic, enabling independent operation and reusability of each module.
- *Independent Extractors and Validators:* The extractors and validators should function independently from the main pipeline logic, ensuring ease of integration and future modifications.
- *Error Handling and Reporting:* Include error handling within the pipeline to manage any unexpected issues during extraction or validation. Log or print clear error messages to facilitate troubleshooting.

### Requirements for Extractors:
- *Modular and Extensible:* Each extractor should be a separate class or module that can be easily replaced or extended with minimal impact on the main pipeline.
- *PDF Data Extraction:* The extractors should be able to identify and extract specific values from the PDF, in our case, the company_name and date from the cover page.
- *Error Handling:* If an extractor fails to find the required value, it should handle the error gracefully and return an appropriate response or log an error message.

### Requirements for Validators:
- *Ease of Expansion:* New validators should be simple to add, following a standard interface or protocol.
- *Field-Specific Validations:*
  - *Company Name Validator:* Confirms that the extracted company name matches the provided company_name argument.
  - *Date Validator:* Validates that the extracted date field aligns with the provided date argument and that it follows the YYYY-MM-DD format.
  - *Clear Feedback:* In case of validation failure, each validator should return a detailed message indicating what failed, along with the expected versus actual values.

### Expected Result
####Modules:
- *General Pipeline Logic:* Manages the extraction and validation flow, coordinating data between extractors and validators.
- *Two Extractors:*
  - *Company Name Extractor:* Extracts the company name from the PDF's cover page.
  - *Date Extractor:* Extracts the date field from the cover page of the PDF.
- *Two Validators:*
  - *Company Name Validator:* Compares the extracted company name with the expected company_name parameter.
  - *Date Validator:* Checks that the extracted date matches the expected date parameter.

### Example Usage
For a successful validation:
```bash
python pipeline.py --company_name "Bluegem III GP SARL" --date "2023-12-31"
```
Expected output:
```bash
Company name validation passed.
Date validation passed.
```

For an unsuccessful validation:
```bash
python etl_pipeline.py --company_name "no name" --date "2025-12-31"
```
Expected output:
```bash
Company name validation failed: expected "Lol", found "Bluegem III GP SARL".
Date validation failed: expected "2025-12-31", found "2023-12-31".
```

### How to Send Results for Review
- *Fork the repository.*
- *Create a new branch* for your solution.
- *Push your code* to the new branch.
- *Send the results* for review via Telegram: @ashugaev