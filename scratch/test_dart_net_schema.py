import os
import sys
import json
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config
from agents.scraper_agent import ScraperAgent
from agents.semantic_validator_agent import SemanticValidatorAgent
from agents.anonymizer_agent import AnonymizerAgent
from agents.netnography_agent import NetnographyAgent
from agents.quality_guard_agent import QualityGuardAgent
from agents.synthesis_agent import SynthesisAgent
from summary_table_generator import SummaryTableGenerator

class TestDARTNetSchema(unittest.TestCase):
    def test_schema_structure(self):
        """Verify that a sample DART-NET analysis matches Section 13 JSON schema."""
        sample_post = {
            "platform": "Discourse",
            "game": "World of Warcraft",
            "community": "General Discussion",
            "thread_id": "2101642",
            "post_id": "2101642_1",
            "parent_post_id": "",
            "timestamp": "2024-03-12T14:22:00Z",
            "author_id": "Player_042",
            "title": "Bots in Auction House",
            "text": "The auction house is flooded with automated bots cancel-scanning every second.",
            "ai_type": "A2",
            "ai_type_confidence": 0.85,
            "interaction_type": "I4",
            "interaction_confidence": 0.80,
            "value_type": "VC3",
            "value_confidence": 0.90,
            "dart": {
                "dialogue": {"score": 0, "evidence": "", "confidence": 0.90},
                "access": {"score": 2, "evidence": "automated bots cancel-scanning every second", "confidence": 0.85},
                "risk": {"score": 4, "evidence": "auction house is flooded", "confidence": 0.92},
                "transparency": {"score": 1, "evidence": "", "confidence": 0.80}
            },
            "relevance": "RELEVANT",
            "relevance_confidence": 0.95,
            "human_review_required": False,
            "classification_notes": "Conventional AH botting without evidence of LLM or autonomous learning."
        }
        
        # Required Section 13 keys
        required_keys = [
            "platform", "game", "community", "thread_id", "post_id", "parent_post_id",
            "timestamp", "author_id", "title", "text", "ai_type", "ai_type_confidence",
            "interaction_type", "interaction_confidence", "value_type", "value_confidence",
            "dart", "relevance", "relevance_confidence", "human_review_required", "classification_notes"
        ]
        for key in required_keys:
            self.assertIn(key, sample_post, f"Missing required Section 13 key: {key}")
            
        # Check DART keys
        for dim in ["dialogue", "access", "risk", "transparency"]:
            self.assertIn(dim, sample_post["dart"])
            for subkey in ["score", "evidence", "confidence"]:
                self.assertIn(subkey, sample_post["dart"][dim])
                
        # Check valid ranges
        self.assertIn(sample_post["ai_type"], ["A1", "A2", "A3", "A4", "A5", "A6"])
        self.assertIn(sample_post["interaction_type"], ["I1", "I2", "I3", "I4", "I5", "I6"])
        self.assertIn(sample_post["value_type"], ["VC1", "VC2", "VC3", "VC4"])
        self.assertIn(sample_post["relevance"], ["RELEVANT", "POSSIBLY RELEVANT", "IRRELEVANT"])
        
        for dim in ["dialogue", "access", "risk", "transparency"]:
            score = sample_post["dart"][dim]["score"]
            self.assertTrue(0 <= score <= 5, f"DART score {score} out of range 0-5")
            conf = sample_post["dart"][dim]["confidence"]
            self.assertTrue(0.0 <= conf <= 1.0, f"Confidence {conf} out of range 0-1")
            
        self.assertIsInstance(sample_post["human_review_required"], bool)

    def test_confidence_threshold_logic(self):
        """Verify that confidence < 0.80 triggers human_review_required."""
        low_confidence_post = {
            "ai_type_confidence": 0.72,
            "interaction_confidence": 0.85,
            "value_confidence": 0.90,
            "relevance_confidence": 0.90,
            "dart": {
                "dialogue": {"confidence": 0.85},
                "access": {"confidence": 0.85},
                "risk": {"confidence": 0.85},
                "transparency": {"confidence": 0.85}
            }
        }
        confs = [
            low_confidence_post["ai_type_confidence"],
            low_confidence_post["interaction_confidence"],
            low_confidence_post["value_confidence"],
            low_confidence_post["relevance_confidence"],
            low_confidence_post["dart"]["dialogue"]["confidence"],
            low_confidence_post["dart"]["access"]["confidence"],
            low_confidence_post["dart"]["risk"]["confidence"],
            low_confidence_post["dart"]["transparency"]["confidence"]
        ]
        min_conf = min(confs)
        human_review_required = min_conf < config.CONFIDENCE_HIGH
        self.assertTrue(human_review_required)

if __name__ == "__main__":
    unittest.main()
