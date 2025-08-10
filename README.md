
# Chat with Newton 🍎
[](https://www.python.org/downloads/release/python-3130/)
[](https://www.langchain.com/)
[](https://www.gradio.app/)
[](https://opensource.org/licenses/MIT)

*“I can calculate the motion of heavenly bodies, but not the madness of people.”*

Engage in a conversation with a digital persona of Sir Isaac Newton through an interactive web interface. This AI-powered assistant, built with Python 3.13, **LangChain**, and **Gradio**, emulates the intellect and historical voice of one of history's greatest scientific minds. Ask about gravity, calculus, optics, or even his alchemical pursuits\!

-----

## 📸 Demo

A glimpse of the web interface you will be running locally.

-----

## ✨ Features

  * **Interactive Web UI**: A clean and simple chat interface powered by Gradio, allowing for easy interaction without the command line.
  * **Authentic Persona**: The AI's personality is carefully prompted and managed using LangChain to provide responses befitting Isaac Newton's formal, 17th-century tone.
  * **Conversation Memory**: Remembers the context of the current conversation for a more natural and coherent dialogue.
  * **Scientific Expertise**: Capable of discussing complex topics in physics and mathematics, complete with LaTeX support for formulas like $F=ma$.
  * **Modern Tech Stack**: Utilizes the latest in Python and AI application development tools for a robust and maintainable codebase.

-----

## 🛠️ Technology Stack

  * **Core Language:** [Python 3.13](https://www.python.org/)
  * **AI Orchestration:** [LangChain](https://www.langchain.com/)
  * **Web Interface:** [Gradio](https://www.gradio.app/)
  * **AI/LLM:** Backend agnostic (designed for use with any major LLM provider like OpenAI, Google, etc.)
  * **Environment Variables:** `python-dotenv`

-----

## ⚙️ Getting Started

To get the AI running on your local machine, please follow the steps below.

### Prerequisites

  * **Python 3.13** or newer.
  * An **API Key** from an LLM provider (e.g., OpenAI, Google AI Studio, Anthropic).

### Setup Instructions

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/<your-username>/Chat-with-Newton.git
    cd Chat-with-Newton
    ```

2.  **Create and Activate a Virtual Environment:**

      * On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
      * On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install Dependencies:**
    The necessary packages are listed in `requirements.txt`. Install them with pip:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    You must provide your API key for the language model to work.

      * Create a new file named `.env` in the root directory of the project.
      * Add your API key to the `.env` file. The variable name may depend on your provider (e.g., `OPENAI_API_KEY`).
        ```
        # Example for OpenAI
        OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        ```

-----

## 🚀 Usage

With the setup complete, you can now launch the web application.

1.  **Run the application from your terminal:**

    ```bash
    python app.py
    ```

    *(Note: If your main script is named differently, use that name instead of `app.py`.)*

2.  **Open the Interface:**
    The terminal will output a local URL, typically `http://127.0.0.1:7860`. Open this link in your web browser.

3.  **Start Chatting:**
    You can now type your questions into the chat interface and receive responses from Sir Isaac Newton.

-----

## 🤝 Contributing

Contributions are most welcome\! If you have an idea for an improvement or have found a bug, please feel free to:

1.  Fork the repository.
2.  Create a new feature branch (`git checkout -b feature/YourAmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/YourAmazingFeature`).
5.  Open a Pull Request.

Please open an issue first to discuss what you would like to change.

-----

## 📜 License

This project is licensed under the MIT License. See the `LICENSE.md` file for more details.
