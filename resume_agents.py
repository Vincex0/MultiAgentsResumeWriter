from crewai import Agent
from langchain.llms import OpenAI

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools

from langchain.llms import Ollama
# ollama_openhermes = Ollama(model="agent")
# ollama_llm = Ollama(model="llama3")
ollama_llm = Ollama(model="llama3:70b")


# Pass Ollama Model to Agents: When creating your agents within the CrewAI framework, you can pass the Ollama model as an argument to the Agent constructor. For instance:

class ResumeAgent():

  def skill_and_experience_research_agent(self):
    return Agent(
        role='Skill and Experience Expert',
        goal='Research job postings and analyze the required skills and experience',
        backstory=
        'An expert in analyzing job postings and identifying the most important skills and experience',
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        llm = ollama_llm,
        verbose=True)

  def resume_writing_expert(self):
    return Agent(
        role='Resume Writing Expert',
        goal='Write a resume for a specific job posting',
        backstory="""A knowledgeable resume writer with years of experience""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        llm = ollama_llm,        
        verbose=True)

  def revise_agent(self):
    return Agent(
        role='Resume Revise Agent',
        goal="""you need to revise a resume to make sure it is well written, formatted, and fit job posting""",
        backstory="""You are a experienced tech AI hiring manager who are exellent at revising resumes""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        llm = ollama_llm,
        verbose=True)
