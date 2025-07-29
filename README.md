# Wikipedia Agent

A sophisticated AI-powered Wikipedia search agent built with LangGraph and LangChain. This agent provides intelligent Wikipedia search capabilities through a conversational interface, leveraging OpenAI's GPT models to understand queries and retrieve relevant information from Wikipedia.

## 🚀 Features

- **Intelligent Wikipedia Search**: Natural language queries to search Wikipedia articles
- **LangGraph Integration**: Built using LangGraph's reactive agent framework for robust conversation handling
- **OpenAI GPT Integration**: Powered by GPT-4.1-nano for intelligent query processing
- **Docker Support**: Containerized deployment for easy scaling and deployment
- **GitHub Actions CI/CD**: Automated Docker image building and publishing
- **LangSmith Tracing**: Built-in observability and debugging capabilities

## 🏗️ Architecture

The agent is built using the following key components:

- **LangGraph**: Provides the reactive agent framework and conversation management
- **LangChain Community Tools**: Wikipedia search functionality through `WikipediaQueryRun`
- **OpenAI GPT-4.1-nano**: Language model for understanding and processing queries
- **LangGraph Swarm**: Multi-agent orchestration capabilities

## 📋 Prerequisites

- Python 3.11+
- OpenAI API key
- LangSmith API key (required for tracing and observability)
- Redis instance (for caching and session management)
- PostgreSQL database (for persistent storage)

## 🛠️ Installation

### Local Development

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd wikipedia-agent
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your API keys and connection strings:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   LANGSMITH_API_KEY=your_langsmith_api_key_here
   LANGSMITH_PROJECT=wikipedia-agent
   REDIS_URI=redis://localhost:6379
   DATABASE_URI=postgresql://user:password@localhost:5432/wikipedia_agent
   API_KEY="your_api_key_for_authentication"
   ```

### Docker Deployment

1. **Build the Docker image**:
   ```bash
   docker build -t wikipedia-agent .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8000:8000 --env-file .env wikipedia-agent
   ```

## 🚀 Usage

### Running the Agent

1. **Start the LangGraph server**:
   ```bash
   langgraph up
   ```

2. **Access the agent**:
   - The agent will be available at `http://localhost:8123`
   - Use the LangGraph Studio interface to interact with the agent

### Example Queries

The Wikipedia agent can handle various types of queries:

- **Direct searches**: "Tell me about artificial intelligence"
- **Specific topics**: "What is quantum computing?"
- **Historical events**: "Explain the French Revolution"
- **Scientific concepts**: "How does photosynthesis work?"
- **Biographical information**: "Who was Marie Curie?"

## 📁 Project Structure

```
wikipedia-agent/
├── graph.py              # Main agent definition and graph setup
├── requirements.txt      # Python dependencies
├── langgraph.json       # LangGraph configuration
├── Dockerfile           # Docker container configuration
├── .env.example         # Environment variables template
├── .flake8             # Python linting configuration
├── .pre-commit-config.yaml  # Pre-commit hooks
├── .github/
│   └── workflows/
│       └── deploy.yml   # GitHub Actions CI/CD pipeline
└── README.md           # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for GPT model access | Yes |
| `LANGSMITH_API_KEY` | LangSmith API key for tracing and observability | Yes |
| `LANGSMITH_PROJECT` | LangSmith project name | Yes |
| `REDIS_URI` | Redis connection string for caching and sessions | Yes |
| `DATABASE_URI` | PostgreSQL connection string for persistent storage | Yes |
| `API_KEY` | Authentication key for API access | Yes |
| `LANGSMITH_TRACING` | Enable/disable LangSmith tracing | No |
| `LANGSMITH_ENDPOINT` | LangSmith API endpoint | No |

### LangGraph Configuration

The `langgraph.json` file configures:
- **Dependencies**: Local package dependencies
- **Graphs**: Agent graph definitions and entry points
- **Environment**: Environment file location
- **Image**: Base Docker image distribution

## 🧪 Development

### Code Quality

The project includes several code quality tools:

- **Flake8**: Python linting (configured in `.flake8`)
- **Pre-commit hooks**: Automated code formatting and linting

### Running Tests

```bash
# Install development dependencies
pip install -r requirements.txt

# Run linting
flake8 .

# Run pre-commit hooks
pre-commit run --all-files
```

### Adding New Features

1. **Extend the agent**: Modify `graph.py` to add new tools or capabilities
2. **Update dependencies**: Add new packages to `requirements.txt`
3. **Update configuration**: Modify `langgraph.json` if needed
4. **Test thoroughly**: Ensure new features work with existing functionality

## 🐳 Docker

### Building

```bash
docker build -t wikipedia-agent .
```

### Running

```bash
# With environment file
docker run -p 8000:8000 --env-file .env wikipedia-agent

# With inline environment variables
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=your_openai_key \
  -e LANGSMITH_API_KEY=your_langsmith_key \
  -e REDIS_URI=redis://your-redis-host:6379 \
  -e DATABASE_URI=postgresql://user:pass@your-db-host:5432/dbname \
  -e API_KEY="your_api_key_for_authentication" \
  wikipedia-agent
```

### GitHub Container Registry

The project automatically builds and publishes Docker images to GitHub Container Registry via GitHub Actions when changes are pushed to the `main` branch.

## 🔍 Monitoring and Debugging

### LangSmith Integration

When configured, the agent automatically traces all interactions to LangSmith for:
- **Performance monitoring**: Track response times and token usage
- **Debugging**: Inspect agent reasoning and tool usage
- **Analytics**: Understand user interaction patterns

### Logs

The agent provides structured logging for:
- Wikipedia API calls
- Agent reasoning steps
- Error handling and recovery

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Run tests and linting**: `pre-commit run --all-files`
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

1. **OpenAI API Key Error**:
   - Ensure your API key is correctly set in the `.env` file
   - Verify the API key has sufficient credits

2. **LangSmith Connection Issues**:
   - Verify your LangSmith API key is valid
   - Check if the LangSmith project exists
   - Ensure network connectivity to LangSmith endpoints

3. **Redis Connection Failures**:
   - Verify Redis server is running and accessible
   - Check the `REDIS_URI` format: `redis://host:port`
   - Test Redis connectivity: `redis-cli ping`

4. **Database Connection Issues**:
   - Ensure PostgreSQL server is running
   - Verify database credentials and connection string
   - Check if the database exists and is accessible
   - Test connection: `psql $DATABASE_URI`

5. **Wikipedia Search Failures**:
   - Check internet connectivity
   - Verify Wikipedia API is accessible

6. **Docker Build Issues**:
   - Ensure Docker is running
   - Check for sufficient disk space
   - Verify all required files are present

7. **LangGraph Server Issues**:
   - Check if port 8123 is available
   - Verify all dependencies are installed
   - Check the `langgraph.json` configuration
   - Ensure all required environment variables are set

### Getting Help

- Check the [LangGraph documentation](https://langchain-ai.github.io/langgraph/)
- Review [LangChain community tools](https://python.langchain.com/docs/integrations/tools/)
- Open an issue in this repository for project-specific problems

## 🚀 Deployment

The project includes automated deployment via GitHub Actions:

1. **Push to main branch** triggers the CI/CD pipeline
2. **Docker image** is built and tested
3. **Image is published** to GitHub Container Registry
4. **Deploy** the published image to your preferred platform

### Deployment Platforms

- **Docker**: Use the published container image
- **Kubernetes**: Deploy using the container image
- **Cloud Run**: Direct deployment from container registry
- **Heroku**: Container-based deployment