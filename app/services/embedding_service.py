import logging
import openai
from typing import Union, List, Dict, Any

logger = logging.getLogger(__name__)


class EmbeddingService:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def create_embedding(
        self, input_text: Union[str, List[str]], model: str, api_key: str
    ) -> Dict[str, Any]:
        """Create embeddings using OpenAI API"""
        try:
            client = openai.OpenAI(api_key=api_key, base_url=self.base_url)
            response = client.embeddings.create(input=input_text, model=model)
            return response
        except Exception as e:
            logger.error(f"Error creating embedding: {str(e)}")
            raise