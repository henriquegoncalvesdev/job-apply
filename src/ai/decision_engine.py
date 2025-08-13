from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class DecisionEngine:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def match_job(self, job_description: str, user_profile: dict) -> float:
        # Use OpenAI to calculate semantic match (placeholder)
        prompt = f"Job: {job_description}\nProfile: {user_profile}\nHow strong is the match (0-1)?"
        # This is a placeholder for actual OpenAI call
        return 0.8

    def explain_decision(self, job_description: str, user_profile: dict) -> str:
        # Use OpenAI to generate explanation (placeholder)
        return "This job matches your skills and experience."
