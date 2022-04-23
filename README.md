# DeepBio
DeepBio is a tool that helps to create biographies for older people. The app creates a biography based on a list of questions with the use of GPT3 from OpenAi. The application was created during the TUM.ai Makeathon in April 2022.

![Alt text](https://github.com/RobinFalter/DeepBio/view/images/deepbio.gif)

# Installation
Clone the repository and create a new conda environment with: 
 `conda create --name <your env name> python=3.9`
 
Install the neccessary packages with: 
`pip install -r requirements.txt`

Open the config.json file. Go to https://beta.openai.com/account/api-keys. Copy the key from the website and replace the key in the config.json file. This is neccessary because the key expires after every GitHub commit. 
