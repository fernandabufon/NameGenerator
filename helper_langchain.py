from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

api_key = ""
llm = GooglePalm(google_api_key=api_key, temperature=0.6)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: restaurant name

    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest one fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: menu items
    prompt_template_itens = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = "Suggest some menu items for {restaurant_name}. Return it as a comma separated list whithout title."
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_itens, output_key="menu_items")

    chain = SequentialChain(
        chains= [name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine':cuisine})

    return response


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))