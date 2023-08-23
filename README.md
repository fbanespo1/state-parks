# State Parks Travel Assistant

**Built by Tony Esposito**

The State Parks Travel Assistant is a Streamlit-powered application that uses the OpenAI GPT-3.5 Turbo language model to provide travel-related information and responses about state parks in Tennessee. Users can input questions and prompts related to state parks, and the application generates informative responses.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **State Parks Travel Assistant** is a user-friendly application designed to assist users in obtaining information about state parks in Tennessee. Powered by the OpenAI GPT-3.5 Turbo language model, the application offers detailed and informative responses to user queries, enhancing the travel planning experience.

## Installation

1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/your-username/state-parks-travel-assistant.git
   ```

2. Navigate to the project directory:
   ```shell
   cd state-parks-travel-assistant
   ```

3. Install the required dependencies using `pip`:
   ```shell
   pip install -r requirements.txt
   ```

## Usage

Follow these steps to use the State Parks Travel Assistant:

1. Obtain an API key from OpenAI and replace `'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'` with your actual API key in the `openai.api_key` line of the `travel.py` script.

2. Run the application using Streamlit:
   ```shell
   streamlit run travel.py
   ```

3. The application interface will open in a browser window. You will see an input area where you can ask questions or provide prompts related to state parks and travel in Tennessee.

4. Enter your question or prompt and press Enter. The application will validate your input and, if it contains relevant keywords (e.g., "Tennessee State Park," "State Parks," etc.), it will generate a response using the OpenAI GPT-3.5 Turbo language model. The generated response will be displayed on the screen.

## Configuration

The application offers limited configuration:

- **API Key:** Replace `'sk-xxxxxxxxx'` in the `travel.py` script with your actual OpenAI API key.

## Contributing

Contributions are welcome! If you have ideas, improvements, or bug fixes, please consider contributing. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes and ensure they are properly tested.
4. Submit a pull request to the `main` branch of the original repository.

## License

This project is licensed under the [MIT License](LICENSE).
