# fin_bot

**Project Report: Fin Bot - AI Financial Assistant**

**1. Project Overview:**
Fin Bot is an AI-powered chatbot built using Streamlit and Google's Gemini API. It is designed to assist users with financial, stock market, and investment-related queries. The bot provides instant responses to user inputs by leveraging the capabilities of generative AI models. The intuitive and interactive user interface enhances user experience, making it easier to get financial insights quickly.

**2. Technologies Used:**
- **Streamlit**: A Python-based framework used for building the web application.
- **Google Gemini API**: Used to generate responses for user queries.
- **Python**: The primary programming language used for the development of the chatbot.
- **HTML & CSS (via Markdown)**: Used for designing the UI elements.

**3. Models Used:**
- **Google Gemini Models**: The project utilizes the `GenerativeModel` class from the `google.generativeai` package to process and generate AI-driven responses. The available models are dynamically fetched using `genai.list_models()`, ensuring that the chatbot remains updated with the latest versions.
- **Default Model**: If the API fails to fetch available models, it defaults to `gemini-pro`, ensuring uninterrupted service.

**4. Features:**
- **Chatbot Interface**: Allows users to enter financial queries and receive AI-generated responses.
- **Model Selection**: Users can choose from available Gemini models to customize response generation.
- **Chat History**: Maintains session-based chat history for user convenience.
- **Clear Chat**: Provides an option to clear previous chats and start fresh.
- **UI Enhancements**: Includes visually appealing elements such as icons, headers, and formatted text to enhance user engagement.

**5. Problems Solved:**
- **Financial Query Resolution**: Users can get instant AI-generated insights on stocks, investments, and market trends without needing manual research.
- **Ease of Access**: Provides a user-friendly interface for finance professionals, investors, and beginners to interact with an AI assistant.
- **Real-time AI Assistance**: Helps users make informed financial decisions based on AI-generated insights.
- **Personalized AI Model Selection**: Allows users to choose the most suitable AI model for their queries, ensuring flexibility and customization.

**7. Conclusion:**
Fin Bot is an innovative AI-powered financial assistant that simplifies financial analysis and investment decision-making. By leveraging Google's Gemini models and Streamlit's interactive UI capabilities, the chatbot provides a seamless experience for users seeking financial insights. Future enhancements can further improve its accuracy and usability, making it an essential tool for finance professionals and enthusiasts alike.

