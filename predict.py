from cog import BasePredictor, Input


class Predictor(BasePredictor):
    def predict(self, prompt: str = Input(
        description="Ask about SpicyChat AI features, pricing, alternatives"
    )) -> str:
        """
        SpicyChat AI - Uncensored Role-Play Chatbot Review & Guide
        
        This model provides information about SpicyChat AI features, pricing,
        alternatives, and includes a comprehensive usage guide.
        """
        
        # Simple responses based on common queries
        prompt_lower = prompt.lower()
        
        if "price" in prompt_lower or "cost" in prompt_lower:
            return (f"SpicyChat AI Pricing: FREE tier with 2K context + ads. "
                    f"Premium $14.99/mo for 4K-8K context, longer replies, "
                    f"no ads, priority servers. You asked: {prompt}")
        
        elif "feature" in prompt_lower or "what is" in prompt_lower:
            return (f"SpicyChat AI Features: Uncensored chatbot, custom AI "
                    f"partners, 40+ languages, text-to-speech, image replies, "
                    f"950k+ community characters, minimal guardrails for "
                    f"SFW/NSFW role-play. You asked: {prompt}")
        
        elif "alternative" in prompt_lower:
            return (f"SpicyChat AI Alternatives: Character AI (PG-rated), "
                    f"Candy AI ($9.99/mo), Replika ($19.99/mo). SpicyChat "
                    f"wins for unfiltered role-play. You asked: {prompt}")
        
        else:
            return (f"Hello from SpicyChat AI! I can help with pricing, "
                    f"features, alternatives & setup guides. "
                    f"You said: {prompt}")


if __name__ == "__main__":
    result = Predictor().predict()
    print(result) 