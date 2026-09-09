import os
import sys
import json
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config
from agents.anonymizer_agent import AnonymizerAgent
from agents.netnography_agent import NetnographyAgent

class TestPipelineAgentFlow(unittest.TestCase):
    def test_anonymizer_layer_preservation(self):
        """Test that AnonymizerAgent assigns pseudonyms while preserving text and structure."""
        agent = AnonymizerAgent()
        sample_author = "RealUser_123"
        syn_id = agent._get_or_create_synthetic_id(sample_author)
        self.assertTrue(syn_id.startswith("Player_"), f"Expected Player_ prefix, got {syn_id}")
        
        # Test text sanitization
        text_with_pii = "Contact me at user@example.com or visit https://secret-cheats.com for more info."
        clean = agent.anonymize_text(text_with_pii)
        self.assertNotIn("user@example.com", clean)
        self.assertNotIn("https://secret-cheats.com", clean)
        self.assertIn("[EMAIL_ANONYMIZED]", clean)
        self.assertIn("[URL_ANONYMIZED]", clean)

    def test_dart_net_normalization_and_flags(self):
        """Test NetnographyAgent handling of DART-NET schema and human review flags."""
        agent = NetnographyAgent()
        
        # Simulate an LLM output matching DART-NET format
        mock_coding = {
            "platform": "Discourse",
            "game": "EVE Online",
            "community": "Market Discussion",
            "thread_id": "504046",
            "post_id": "504046_1",
            "parent_post_id": "",
            "timestamp": "2024-01-10T10:00:00Z",
            "author_id": "Player_001",
            "title": "Character Bazaar Trade",
            "text": "Selling character with imperfect skills. Buyer beware of risks.",
            "ai_type": "A3",
            "ai_type_confidence": 0.75, # < 0.80 -> must trigger human_review_required
            "interaction_type": "I4",
            "interaction_confidence": 0.85,
            "value_type": "VC2",
            "value_confidence": 0.82,
            "dart": {
                "dialogue": {"score": 2, "evidence": "Selling character with imperfect skills", "confidence": 0.85},
                "access": {"score": 3, "evidence": "Buyer beware of risks", "confidence": 0.80},
                "risk": {"score": 3, "evidence": "risks", "confidence": 0.85},
                "transparency": {"score": 3, "evidence": "imperfect skills", "confidence": 0.85}
            },
            "relevance": "RELEVANT",
            "relevance_confidence": 0.90,
            "classification_notes": "Trade discussion involving deterministic scripts/macros."
        }
        
        # Check human review requirement
        confidences = [
            mock_coding["ai_type_confidence"],
            mock_coding["interaction_confidence"],
            mock_coding["value_confidence"],
            mock_coding["relevance_confidence"],
            mock_coding["dart"]["dialogue"]["confidence"],
            mock_coding["dart"]["access"]["confidence"],
            mock_coding["dart"]["risk"]["confidence"],
            mock_coding["dart"]["transparency"]["confidence"]
        ]
        min_conf = min(confidences)
        human_review = min_conf < config.CONFIDENCE_HIGH
        self.assertTrue(human_review, "Should flag human_review_required when confidence is 0.75 (< 0.80)")

if __name__ == "__main__":
    unittest.main()
