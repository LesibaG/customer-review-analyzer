
from google import genai
from google.genai import errors
import json

client = genai.Client()


def validate_analysis(analysis):

    required_fields = [
        "sentiment",
        "category",
        "issues",
        "priority"
    ]

    for field in required_fields:
        if field not in analysis:
            return False

    return True


def validate_review(review):

    review = review.strip()

    if not review:
        return False

    if review.isdigit():
        return False

    if not any(char.isalpha() for char in review):
        return False

    return True


def analyze_review(review):

    if not validate_review(review):
        return {
            "error": "Invalid review. Please enter a meaningful customer review."
        }

    prompt = (
        "Analyze this customer review and return a JSON object "
        "containing these four fields: "
        "sentiment (positive, negative, or neutral), "
        "category (main topic of the review), "
        "issues (a list of customer complaints), "
        "priority (low, medium, or high). "
        "Return an empty issues list if there are no complaints. "
        f"Customer review: {review}"
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )

        analysis = json.loads(response.text)

        if not validate_analysis(analysis):
            return {
                "error": "Gemini returned incomplete analysis."
            }

        return analysis

    except json.JSONDecodeError:
        return {
            "error": "Gemini returned invalid JSON."
        }

    except errors.APIError:
        return {
            "error": "Gemini API request failed."
        }


customer_review = input("Enter a customer review: ")

result = analyze_review(customer_review)

print(result)

