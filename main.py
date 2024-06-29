from crewai import Crew
from textwrap import dedent
from resume_agents import ResumeAgent
from resume_tasks import ResumeTasks

from dotenv import load_dotenv
load_dotenv()
class ResumeCrew:
    
  def __init__(self, job_posting_url, candidate_information, resume):
    self.job_posting_url = job_posting_url
    self.candidate_information = candidate_information
    self.resume = resume

  def run(self):
    agents = ResumeAgent()
    tasks = ResumeTasks()

    skill_and_experience_research_agent = agents.skill_and_experience_research_agent()
    resume_writing_expert = agents.resume_writing_expert()
    revise_agent = agents.revise_agent()

    # Define the tasks
    resume_writing_task = tasks.resume_writing_task(
      skill_and_experience_research_agent,
      self.job_posting_url,
      self.candidate_information,
      self.candidate_information
    )
    revise_task = tasks.revise_task(
      resume_writing_expert,
      self.job_posting_url,
      self.job_posting_url
    )
    skill_and_experience_research_task = tasks.skill_and_experience_research_task(
      revise_agent,
      self.job_posting_url
    )

    crew = Crew(
      agents=[
        skill_and_experience_research_agent, resume_writing_expert, revise_agent
      ],
      tasks=[resume_writing_task, revise_task, skill_and_experience_research_task],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Resume Builder Crew")
  print('-------------------------------')
  job_posting_url = input(
    dedent("""
      Please provide the URL of the job posting you are interested in.
    """))
  candidate_information = input(
    dedent("""
      Please provide your information (e.g., work experiences, skills, accomplishments).
    """))
  resume = input(
    dedent("""
      Please provide your current resume (if available).
    """))
  
  resume_crew = ResumeCrew(job_posting_url, candidate_information, resume)
  result = resume_crew.run()
  print("\n\n########################")
  print("## Here is your Updated Resume")
  print("########################\n")
  print(result)
