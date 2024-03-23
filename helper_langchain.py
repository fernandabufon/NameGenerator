from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

api_key = ""
llm = GooglePalm(google_api_key=api_key, temperature=0.6)

def generate_name_and_meaning(word):

    # Chain 1: name
    prompt_template_name = PromptTemplate(
        input_variables=['word'],
        template="I want a person name that rhymes with the word {word}. Give me only one name."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="name")

    # Chain 2: meaning
    prompt_template_meaning = PromptTemplate(
        input_variables = ['name'],
        template = "Give me the meaning of the name {name}"
    )

    meaning_chain = LLMChain(llm=llm, prompt=prompt_template_meaning, output_key="meaning")

    chain = SequentialChain(
        chains= [name_chain, meaning_chain],
        input_variables=['word'],
        output_variables=['name', 'meaning']
    )

    response = chain({'word':word})

    return response


if __name__ == "__main__":
    print(generate_name_and_meaning("Budy"))