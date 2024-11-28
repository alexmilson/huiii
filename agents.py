from crewai import Agent
#from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq  # Import Groq client
from langchain_openai import ChatOpenAI
import os
from crewai_tools import SerperDevTool,WebsiteSearchTool, ScrapeWebsiteTool 



class ResearchCrewAgents:

    def __init__(self):
        # Initialize tools if needed
        self.serper = SerperDevTool()
        self.web = WebsiteSearchTool()
        self.web_scrape=ScrapeWebsiteTool()


       # OpenAI Models
        self.gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.gpt4 = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.7)
        self.gpt3_5_turbo_0125 = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.7)
        self.gpt3_5_turbo_1106 = ChatOpenAI(model_name="gpt-3.5-turbo-1106", temperature=0.7)
        self.gpt3_5_turbo_instruct = ChatOpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.7)
        
        # Groq Models
        self.llama3_8b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="llama3-8b-8192")
        self.llama3_70b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="llama3-70b-8192")
        self.mixtral_8x7b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="mixtral-8x7b-32768")
        self.gemma_7b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="gemma-7b-it")
        
        # CHANGE YOUR MODEL HERE
        self.selected_llm = self.Mixtral_8x7B
    def researcher(self):
    # Detailed agent setup for the Research Expert
        return Agent(
        role='Expert',
        goal='Identify the industry of the company and gather relevant product information.',
        backstory="You are a research expert who can analyze web data to determine industry classification",
        verbose=True,
        allow_delegation=False,
        llm=self.selected_llm,
        max_iter=3,
        tools=[self.serper, self.web, self.web_scrape],
        ) 


    def analyst(self):
        # Detailed agent setup for the Analyst
        return Agent(
            role='Analyst',
            goal='Analyze industry trends and propose relevant AI/ML use cases for the company.',
            backstory="You are an analyst skilled in identifying opportunities for AI and ML applications in various industries.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            max_iter=3,


        )

    def writer(self):
        # Detailed agent setup for the Writer
        return Agent(
            role='Technical writer',
            goal='Use CrewAI tools to search and summarize findings of the previous agent, github links and their URLs, as well as kaggle dataset links and online resource to carry out the learning needed',
            backstory="You are an expert in curating datasets and finding online resources that help in executing AI and ML solutions, you are great at scraping the web links and resources geared to ward learning specific goals.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            tools=[self.serper, self.web, self.web_scrape],
            max_iter=3,


        )
