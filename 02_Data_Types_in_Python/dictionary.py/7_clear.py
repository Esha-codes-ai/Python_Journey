# clear methode is used to remove the whole dictionary .
ai_models = {
    "OpenAI": {
        "GPT-5.5": "Advanced language model for coding, writing, reasoning, and conversations",
        "GPT-4.1": "Powerful multimodal model for text and image understanding",
        "o3": "Reasoning-focused model for complex problem solving",
        "o4-mini": "Fast and efficient reasoning model"
    },

    "Google": {
        "Gemini 2.5 Pro": "Best for advanced reasoning and coding",
        "Gemini 2.5 Flash": "Fast, lightweight, and cost-effective"
    },

    "Anthropic": {
        "Claude Opus": "Excellent for deep reasoning and long documents",
        "Claude Sonnet": "Balanced performance and speed",
        "Claude Haiku": "Fast and lightweight"
    },

    "Meta": {
        "Llama 3.3": "Open-weight language model",
        "Llama 4": "Multimodal AI model family"
    },

    "Mistral AI": {
        "Mistral Large": "Enterprise-grade language model",
        "Mixtral": "Mixture-of-Experts open-weight model"
    },

    "DeepSeek": {
        "DeepSeek-R1": "Reasoning model for mathematics and coding",
        "DeepSeek-V3": "General-purpose language model"
    },

    "xAI": {
        "Grok 4": "Conversational AI with reasoning capabilities"
    }
}

print(ai_models)
ai_models.clear() # clear the  entire dictionary
print("The dictionary after clearing:", ai_models)