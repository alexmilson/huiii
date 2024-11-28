from crewai import Task

from crewai import Task

class ResearchCrewTasks:

    def research_task(self, agent, inputs):
      return Task(
          agent=agent,
          description=f" Based {inputs} figure out what industry it belongs to and check https://www.thetoolbus.ai/ai-tools, and https://appsumo.com/collections/new/ for relevant tools that could be usefull ",
          expected_output=f"A clear explanation of the industry , company ,disciplines  , vision"

      )


    def analysis_task(self, agent, context):
      return Task(
        agent=agent,
        context=context,
        description=f"Analyze industry trends of the {inputs}. Based on the results, propose AI/ML use cases .",
        expected_output=f"List of proposed AI/ML use cases."
   
    )


    def writing_task(self, agent, context, inputs):
        return Task(
            agent=agent,
            context=context,
            description=f"Answer the users inquiry their request topics: {inputs} Given the following learning plan {context}, using web search, web scraping ,figure give 3 github links, 3 kaggle dataset links, 3 internet articles titles and their URL.",
            expected_output=f" 3 git hub links,3 kaggle dataset links , 3 internet articles titles and their URls",
        )




