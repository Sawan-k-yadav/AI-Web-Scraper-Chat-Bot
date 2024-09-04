# AI-Web-Scraper-Chat-Bot

This project used to do the webscrapping using pre-trained LLM model.

## Steps to run the run the Project
1. clone the github repo in of your folder on local
   ``` git clone https://github.com/Sawan-k-yadav/AI-Web-Scraper-Chat-Bot.git ```
3. Create virtual environment
   ``` conda create -p venv python=3.8 -y ```
4. Activate environment
   ``` source activate venv/ ``` or ``` conda activate venv/ ```
5. For running this web scrapping chrome driver to fetch the given website. So you need to download latest version of chrome driver from this link:
   https://googlechromelabs.github.io/chrome-for-testing/#stable  and download which matches from your browser chrome version.
6. The model which needs to give the prompts with the DOM content of webpage can be of your choice.
   I am using ollama model gemma2:2b. Ollama helps to run llama models locally for free. You can choose ollama3 or higher performance model.
   Selection of model depends of system specification. Higher size model will require high GPU and TPU.
   I am using gemma2:2b as it small size but still it was giving response with some delay. You read this ollama [Github](https://github.com/ollama/ollama?tab=readme-ov-file) for more details.

7. Keep your application file of downloaded and unziped, chrome driver in your project folder.
8. Install requirements
   ``` pip install -r requirements.txt ```
9. Run the streamlit app to run the Chat Bot
10. First it will ask to give website link
    ![alt text](Chat-bot-2-image.png?raw=true "Parsing DOM content")
11. Then after clicking on scrape website, it will check the whole webpage and fetch all the DOM content and show in big text area
12. According the website details you can ask your questions and hit parse content to check the response from LLM.
13. It will parse whole DOM content as per the your request question. Pasring details will appear on the termial
    ![alt text](Chat-bot-3-image.png?raw=true "Parsing DOM content").
14. Finally after parsing whole DOM content it will show the parse result as per your questions. It may take long time as per your system specification
    and model selection.
    ![alt text](Chat-bot-1-image.png?raw=true "Parsing DOM content")
