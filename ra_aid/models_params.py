"""
List of model parameters
"""

DEFAULT_TOKEN_LIMIT = 100000
DEFAULT_TEMPERATURE = 0.7

models_params = {
    "openai": {
        "gpt-3.5-turbo-0125": {
            "token_limit": 16385,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-3.5": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-3.5-turbo": {
            "token_limit": 16385,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-3.5-turbo-1106": {
            "token_limit": 16385,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-3.5-turbo-instruct": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-0125-preview": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-turbo-preview": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-turbo": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-turbo-2024-04-09": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-1106-preview": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-vision-preview": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-0613": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-32k": {
            "token_limit": 32768,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-32k-0613": {
            "token_limit": 32768,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4o": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4o-2024-08-06": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4o-2024-05-13": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4o-mini": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "o1-preview": {"token_limit": 128000, "supports_temperature": False},
        "o1-mini": {"token_limit": 128000, "supports_temperature": False},
        "o1": {"token_limit": 200000, "supports_temperature": False},
        "o3-mini": {"token_limit": 200000, "supports_temperature": False},
    },
    "azure_openai": {
        "gpt-3.5-turbo-0125": {
            "token_limit": 16385,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-3.5": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-3.5-turbo": {
            "token_limit": 16385,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-3.5-turbo-1106": {
            "token_limit": 16385,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-3.5-turbo-instruct": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-0125-preview": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-turbo-preview": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-turbo": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-turbo-2024-04-09": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-1106-preview": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-vision-preview": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-0613": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-32k": {
            "token_limit": 32768,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4-32k-0613": {
            "token_limit": 32768,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4o": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gpt-4o-mini": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "chatgpt-4o-latest": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "o1-preview": {"token_limit": 128000, "supports_temperature": False},
        "o1-mini": {"token_limit": 128000, "supports_temperature": False},
    },
    "google_genai": {
        "gemini-pro": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gemini-1.5-flash-latest": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gemini-1.5-pro-latest": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "models/embedding-001": {
            "token_limit": 2048,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
    },
    "google_vertexai": {
        "gemini-1.5-flash": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gemini-1.5-pro": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gemini-1.0-pro": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
    },
    "ollama": {
        "command-r": {
            "token_limit": 12800,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "codellama": {
            "token_limit": 16000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "dbrx": {
            "token_limit": 32768,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "deepseek-coder:33b": {
            "token_limit": 16000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "falcon": {
            "token_limit": 2048,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama2": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama2:7b": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama2:13b": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama2:70b": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama3": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama3:8b": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama3:70b": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama3.1": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama3.1:8b": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama3.1:70b": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "lama3.1:405b": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama3.2": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama3.2:1b": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama3.2:3b": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama3.3:70b": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "scrapegraph": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mistral-small": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mistral-openorca": {
            "token_limit": 32000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mistral-large": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "grok-1": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llava": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mixtral:8x22b-instruct": {
            "token_limit": 65536,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "nomic-embed-text": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "nous-hermes2:34b": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "orca-mini": {
            "token_limit": 2048,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "phi3:3.8b": {
            "token_limit": 12800,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "phi3:14b": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "qwen:0.5b": {
            "token_limit": 32000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "qwen:1.8b": {
            "token_limit": 32000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "qwen:4b": {
            "token_limit": 32000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "qwen:14b": {
            "token_limit": 32000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "qwen:32b": {
            "token_limit": 32000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "qwen:72b": {
            "token_limit": 32000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "qwen:110b": {
            "token_limit": 32000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "stablelm-zephyr": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "wizardlm2:8x22b": {
            "token_limit": 65536,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mistral": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gemma2": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gemma2:9b": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gemma2:27b": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        # embedding models
        "shaw/dmeta-embedding-zh-small-q4": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "shaw/dmeta-embedding-zh-q4": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "chevalblanc/acge_text_embedding": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "martcreation/dmeta-embedding-zh": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "snowflake-arctic-embed": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mxbai-embed-large": {
            "token_limit": 512,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
    },
    "oneapi": {
        "qwen-turbo": {
            "token_limit": 6000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        }
    },
    "nvidia": {
        "meta/llama3-70b-instruct": {
            "token_limit": 419,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "meta/llama3-8b-instruct": {
            "token_limit": 419,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "nemotron-4-340b-instruct": {
            "token_limit": 1024,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "databricks/dbrx-instruct": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "google/codegemma-7b": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "google/gemma-2b": {
            "token_limit": 2048,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "google/gemma-7b": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "google/recurrentgemma-2b": {
            "token_limit": 2048,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "meta/codellama-70b": {
            "token_limit": 16384,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "meta/llama2-70b": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "microsoft/phi-3-mini-128k-instruct": {
            "token_limit": 122880,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mistralai/mistral-7b-instruct-v0.2": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mistralai/mistral-large": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mistralai/mixtral-8x22b-instruct-v0.1": {
            "token_limit": 32768,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mistralai/mixtral-8x7b-instruct-v0.1": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "snowflake/arctic": {
            "token_limit": 16384,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
    },
    "groq": {
        "llama3-8b-8192": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "llama3-70b-8192": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mixtral-8x7b-32768": {
            "token_limit": 32768,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "gemma-7b-it": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "claude-3-haiku-20240307'": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
    },
    "toghetherai": {
        "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mistralai/Mixtral-8x22B-Instruct-v0.1": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "stabilityai/stable-diffusion-xl-base-1.0": {
            "token_limit": 2048,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "NousResearch/Hermes-3-Llama-3.1-405B-Turbo": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "Gryphe/MythoMax-L2-13b-Lite": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "Salesforce/Llama-Rank-V1": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "meta-llama/Meta-Llama-Guard-3-8B": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "meta-llama/Meta-Llama-3-70B-Instruct-Turbo": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "meta-llama/Llama-3-8b-chat-hf": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "meta-llama/Llama-3-70b-chat-hf": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "Qwen/Qwen2-72B-Instruct": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "google/gemma-2-27b-it": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
    },
    "anthropic": {
        "claude_instant": {
            "token_limit": 100000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "claude2": {
            "token_limit": 9000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "claude2.1": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "claude3": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "claude3.5": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "claude-3-opus-20240229": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "claude-3-sonnet-20240229": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "claude-3-haiku-20240307": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "claude-3-5-sonnet-20240620": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "claude-3-5-sonnet-20241022": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": 1.0,
        },
        "claude-3-5-haiku-latest": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
    },
    "bedrock": {
        "anthropic.claude-3-haiku-20240307-v1:0": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "anthropic.claude-3-sonnet-20240229-v1:0": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "anthropic.claude-3-opus-20240229-v1:0": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "anthropic.claude-3-5-sonnet-20240620-v1:0": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "claude-3-5-haiku-latest": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "anthropic.claude-v2:1": {
            "token_limit": 200000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "anthropic.claude-v2": {
            "token_limit": 100000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "anthropic.claude-instant-v1": {
            "token_limit": 100000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "meta.llama3-8b-instruct-v1:0": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "meta.llama3-70b-instruct-v1:0": {
            "token_limit": 8192,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "meta.llama2-13b-chat-v1": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "meta.llama2-70b-chat-v1": {
            "token_limit": 4096,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mistral.mistral-7b-instruct-v0:2": {
            "token_limit": 32768,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mistral.mixtral-8x7b-instruct-v0:1": {
            "token_limit": 32768,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mistral.mistral-large-2402-v1:0": {
            "token_limit": 32768,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "mistral.mistral-small-2402-v1:0": {
            "token_limit": 32768,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "amazon.titan-embed-text-v1": {
            "token_limit": 8000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "amazon.titan-embed-text-v2:0": {
            "token_limit": 8000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "cohere.embed-english-v3": {
            "token_limit": 512,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "cohere.embed-multilingual-v3": {
            "token_limit": 512,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
    },
    "mistralai": {
        "mistral-large-latest": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "open-mistral-nemo": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
        "codestral-latest": {
            "token_limit": 32000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        },
    },
    "togetherai": {
        "Meta-Llama-3.1-70B-Instruct-Turbo": {
            "token_limit": 128000,
            "supports_temperature": True,
            "default_temperature": DEFAULT_TEMPERATURE,
        }
    },
}
