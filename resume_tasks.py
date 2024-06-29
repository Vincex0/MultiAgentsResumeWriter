from crewai import Task
from textwrap import dedent
from datetime import date


class ResumeTasks():

  def resume_writing_task(self, agent, job_posting_url, resume, candidate_information):
        return Task(description=dedent(f"""
        Craft a tailored resume for the given job posting using the candidate's information.

        This task involves:
        - Analyzing the job posting to understand the specific requirements and expectations.
        - Reviewing the candidate's current resume and their information to identify relevant skills, experiences, and accomplishments.
        - Revise the resume that effectively highlights the candidate's qualifications and aligns with the job requirements.

        Your final answer must be a polished resume that includes:
        - Detailed descriptions of relevant work experiences, skills, and accomplishments.
        - Proper formatting and structure to ensure readability and impact.

        Job Posting URL: {job_posting_url}
        Candidate Information: {candidate_information}
        Original Resume: {resume}
      """),
                agent=agent)
        
  def revise_task(self, agent, resume, job_posting_url):
    return Task(description=dedent(f"""
    Review and revise the provided resume to ensure it is well-written, formatted, and tailored to the job posting.

    This task involves:
    - Analyzing the job posting to understand the specific requirements and expectations.
    - Reviewing the provided resume to identify areas for improvement in content, structure, and formatting.
    - Making revisions to enhance clarity, impact, and alignment with the job requirements.

    Your final answer must be a revised resume that includes:
    - Improved content that effectively highlights relevant skills and experiences.
    - Enhanced formatting and structure for better readability.
    - Alignment with the key requirements and expectations of the job posting.

    Job Posting URL: {job_posting_url}
    Original Resume: {resume}
  """),
            agent=agent)
    
  def skill_and_experience_research_task(self, agent, job_posting_url):
    return Task(description=dedent(f"""
        Analyze the given job posting to identify the most crucial skills and experiences required for the position.
        
        This task involves:
        - Scraping the job posting to extract detailed information about the role, required skills, and experience.
        - Researching similar job postings to compare and identify common requirements and qualifications.
        - Summarizing the findings into a comprehensive report highlighting the key skills and experiences necessary for the job.

        Your final answer must be a detailed report that includes:
        - A list of key skills and experiences required for the job.
        - An analysis of how these skills and experiences are prioritized in the job market.
        - Any additional insights or trends observed during your research.

        Job Posting URL: {job_posting_url}
      """),
                agent=agent)
    
  def __tip_section(self):
    return "If you do your BEST WORK, I'll tip you $100!"
