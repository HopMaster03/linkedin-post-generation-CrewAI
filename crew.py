from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.linkedin_tools import scrape_linkedin_posts_tool
import logging

from crewai_tools import SerperDevTool

SurfWeb=SerperDevTool()
ScrapeLinkedinPosts=scrape_linkedin_posts_tool

#Defining the crew, Agents and Tasks
@CrewBase
class LinkedInPostCrew():
    """LinkedIn Post crew"""  
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    @agent
    def linkedin_content_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['linkedin_content_strategist'],
            verbose=True,
            memory=False,
            allow_delegation=True,
        )
    @agent
    def audience_insight_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['audience_insight_analyst'],
            tools=[ScrapeLinkedinPosts,SurfWeb],
            verbose=True,
            memory=False,
            allow_delegation=False,
        )
    @agent
    def creative_copywriter(self) -> Agent:
        return Agent(
            config=self.agents_config['creative_copywriter'],
            verbose=True,
            memory=False,
            allow_delegation=False,        
        )
    @agent
    def seo_performance_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_performance_optimizer'],
            verbose=True,
            memory=False,
            allow_delegation=False,
        )
    @task
    def data_collection_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['data_collection_analysis'],
            agent=self.audience_insight_analyst(),         
        )
    @task
    def audience_profiling(self) -> Task:
        return Task(
            config=self.tasks_config['audience_profiling'],
            agent=self.audience_insight_analyst()
        )
    @task
    def content_creation(self) -> Task:
        return Task(
            config=self.tasks_config['content_creation'],
            agent=self.creative_copywriter(),
        )
    @task
    def emotional_appeal_integration(self) -> Task:
        return Task(
            config=self.tasks_config['emotional_appeal_integration'],
            agent=self.creative_copywriter()
        )
    @task
    def content_optimization(self) -> Task:
        return Task(
            config=self.tasks_config['content_optimization'],
            agent=self.seo_performance_optimizer()            
        )
    @task
    def final_evaluation_refinement(self) -> Task:
        return Task(
            config=self.tasks_config['final_evaluation_refinement'],
            agent=self.linkedin_content_strategist()           
        )
    @crew
    def crew(self) -> Crew:
        """Creates the LinkedIn Post crew"""
        logging.info('Creating the LinkedIn crew')
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
            output_log_file=True,#Logs the interation and output into Log.txt
           
        )
    