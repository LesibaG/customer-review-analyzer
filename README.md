**# AI Customer Review Analyzer**



A Python application that uses Google's Gemini AI to analyze customer reviews and return structured insights.



**## Features**



\- Classifies customer sentiment as positive, negative, or neutral

\- Identifies the main topic of a review

\- Extracts customer complaints

\- Assigns a priority level (low, medium, or high)

\- Rejects basic invalid inputs

\- Handles invalid JSON and Gemini API errors

\- Validates the presence of required response fields



**## Technologies**



\- Python

\- Google Gemini API

\- Google GenAI Python SDK

\- JSON



**## Installation**



1\. Clone the repository.

2\. Create and activate a Python virtual environment.

3\. Install dependencies:



&#x20;  `python -m pip install -r requirements.txt`



4\. Set the `GEMINI\_API\_KEY` environment variable to your Gemini API key.

5\. Run the application:



&#x20;  `python main.py`



**## Example**



\*\*Input:\*\*



**The delivery was late and the product arrived damaged.**



\*\*Example output:\*\*



**```json**

**{**

&#x20; **"sentiment": "negative",**

&#x20; **"category": "Delivery",**

&#x20; **"issues": \[**

&#x20;   **"Late delivery",**

&#x20;   **"Damaged product"**

&#x20; **],**

&#x20; **"priority": "high"**

**}**

**```**



The actual output may vary depending on Gemini's analysis.



**## Current Limitations**



\- The application uses a command-line interface.

\- Input validation only rejects basic invalid inputs.

\- Output validation checks required fields but not all value types or classifications.

\- AI-generated classifications may be inaccurate.

\- The application does not yet store review history.



**## Project Purpose**



Built as a beginner AI engineering portfolio project to demonstrate practical experience with LLM APIs, prompt engineering, structured outputs, input validation, and exception handling.

