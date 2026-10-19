from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


load_dotenv()

def main() -> None:
    print("Hello from my-langchain-learning!")
    information = """
    Kriti Sanon (/ˈkrɪti ˈsænɒn/ KRIT-ee SAN-on; born 27 July 1990) is an Indian actress who primarily works in Hindi films. She is a recipient of several accolades including a National Film Award and two Filmfare Awards. Sanon was featured in Forbes India's Celebrity 100 list of 2019.

After pursuing a degree in engineering from the Jaypee Institute of Information Technology, Sanon briefly worked as a fashion model. She began her acting career by playing the female lead in the 2014 action films 1: Nenokkadine and Heropanti. The latter earned her the Filmfare Award for Best Female Debut. Her career progressed with starring roles in the commercially successful romantic comedies Bareilly Ki Barfi (2017) and Luka Chuppi (2019), and her highest-grossing releases came with the ensemble comedies Dilwale (2015) and Housefull 4 (2019).

Sanon won the National Film Award and the Filmfare Award for Best Actress for her performance in the title role of a surrogate mother in the comedy-drama Mimi (2021). This was followed by a series of commercially unsuccessful films, including the controversial mythological film Adipurush (2023), with the exception of the horror-comedy Bhediya (2022), in which she had a brief role. She has since achieved commercial successes with the comedies Teri Baaton Mein Aisa Uljha Jiya and Crew (both 2024), and the romantic drama Tere Ishk Mein (2025).

In addition to acting, she is a celebrity endorser for several brands and products. Sanon has launched her clothing line Ms. Taken, fitness company The Tribe, skin-care brand Hyphen, as well as her production company Blue Butterfly Films.[1]
    """

    summary_template = """
        given the information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    #llm = ChatOllama(temperature=0, model="gemma3:270m")
    llm = ChatOllama(temperature=0, model="gpt-oss")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()