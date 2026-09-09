import os
import json
import logging
import time
import sys
import config

# Setup logs dir and logging
os.makedirs(config.LOGS_DIR, exist_ok=True)
log_file = os.path.join(config.LOGS_DIR, "pipeline.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_file, encoding="utf-8")
    ]
)
logger = logging.getLogger("pipeline.orchestrator")

class Orchestrator:
    def __init__(self):
        self.state_file = os.path.join(config.DATA_INTERIM_DIR, "pipeline_state.json")
        self.state = self._load_or_init_state()
        
    def _load_or_init_state(self):
        default_state = {
            "framework": getattr(config, "PIPELINE_NAME", "DART-NET"),
            "version": getattr(config, "FRAMEWORK_VERSION", "2.0.0"),
            "prompt_version": getattr(config, "PROMPT_VERSION", "2026.1"),
            "start_time": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "last_updated": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "heartbeats": {
                "ScraperAgent": "PENDING",
                "SemanticValidatorAgent": "PENDING",
                "AnonymizerAgent": "PENDING",
                "NetnographyAgent": "PENDING",
                "QualityGuardAgent": "PENDING",
                "SynthesisAgent": "PENDING",
                "SummaryTableGenerator": "PENDING"
            },
            "netnography_progress": {
                "last_post_id": "N/A",
                "progress_pct": 0,
                "remaining_count": 0
            }
        }
        
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    state = json.load(f)
                
                if not isinstance(state, dict):
                    state = {}
                    
                for key, val in default_state.items():
                    if key not in state:
                        state[key] = val
                    elif isinstance(val, dict) and isinstance(state[key], dict):
                        for subkey, subval in val.items():
                            if subkey not in state[key]:
                                state[key][subkey] = subval
                                
                logger.info("Loaded and validated existing pipeline state.")
                return state
            except Exception as e:
                logger.error(f"Failed to load pipeline state: {e}. Reinitializing.")
                
        return default_state
        
    def _save_state(self):
        self.state["last_updated"] = time.strftime("%Y-%m-%dT%H:%M:%SZ")
        try:
            with open(self.state_file, "w", encoding="utf-8") as f:
                json.dump(self.state, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Failed to save pipeline state: {e}")

    def print_resume_banner(self):
        banner = """
================================================================================
|        DART-NET: AI AGENT FOR NETNOGRAPHIC COLLECTION & CODING v2.0          |
================================================================================
"""
        heartbeats = self.state["heartbeats"]
        for agent, status in heartbeats.items():
            status_str = f"[ {status} ]"
            if agent == "NetnographyAgent" and status == "RUNNING":
                progress = self.state["netnography_progress"]
                status_str = f"[ IN PROGRESS ({progress['progress_pct']}%) | Faltam {progress['remaining_count']} posts | Último: {progress['last_post_id']} ]"
            banner += f"* {agent:<25} : {status_str}\n"
            
        banner += "================================================================================"
        print(banner)
        logger.info("Pipeline Status Banner displayed.")

    def update_netnography_progress_callback(self, last_post_id, progress_pct, remaining_count):
        self.state["heartbeats"]["NetnographyAgent"] = "RUNNING"
        self.state["netnography_progress"] = {
            "last_post_id": last_post_id,
            "progress_pct": progress_pct,
            "remaining_count": remaining_count
        }
        self._save_state()
        logger.info(f"Netnography Progress: {progress_pct}% complete. Remaining posts: {remaining_count}. Last post: {last_post_id}")

    def run_pipeline(self):
        self.print_resume_banner()
        
        # Step 1: Scraper Agent
        if self.state["heartbeats"]["ScraperAgent"] != "COMPLETED":
            self.state["heartbeats"]["ScraperAgent"] = "RUNNING"
            self._save_state()
            try:
                from agents.scraper_agent import ScraperAgent
                scraper = ScraperAgent()
                scraped_posts = scraper.run()
                if not scraped_posts:
                    logger.warning("ScraperAgent returned no posts. Checking if mock data needs to be generated.")
                    # If empty, let's verify if we need to auto-generate
                    import data_generator
                    data_generator.generate_mock_data()
                    scraped_posts = scraper.run()
                    
                self.state["heartbeats"]["ScraperAgent"] = "COMPLETED"
                self._save_state()
            except Exception as e:
                self.state["heartbeats"]["ScraperAgent"] = "FAILED"
                self._save_state()
                logger.error(f"ScraperAgent failed: {e}")
                sys.exit(1)
        else:
            logger.info("ScraperAgent already COMPLETED. Skipping.")

        # Step 2: Semantic Validator Agent
        if self.state["heartbeats"]["SemanticValidatorAgent"] != "COMPLETED":
            self.state["heartbeats"]["SemanticValidatorAgent"] = "RUNNING"
            self._save_state()
            try:
                # Load scraped posts
                scraped_file = os.path.join(config.DATA_INTERIM_DIR, "scraped_posts.json")
                with open(scraped_file, "r", encoding="utf-8") as f:
                    scraped_posts = json.load(f)
                    
                from agents.semantic_validator_agent import SemanticValidatorAgent
                validator = SemanticValidatorAgent()
                validated_posts = validator.run(scraped_posts)
                
                self.state["heartbeats"]["SemanticValidatorAgent"] = "COMPLETED"
                self._save_state()
            except Exception as e:
                self.state["heartbeats"]["SemanticValidatorAgent"] = "FAILED"
                self._save_state()
                logger.error(f"SemanticValidatorAgent failed: {e}")
                sys.exit(1)
        else:
            logger.info("SemanticValidatorAgent already COMPLETED. Skipping.")

        # Step 3: Anonymizer Agent
        if self.state["heartbeats"]["AnonymizerAgent"] != "COMPLETED":
            self.state["heartbeats"]["AnonymizerAgent"] = "RUNNING"
            self._save_state()
            try:
                from agents.anonymizer_agent import AnonymizerAgent
                anonymizer = AnonymizerAgent()
                anonymized_posts = anonymizer.run()
                
                self.state["heartbeats"]["AnonymizerAgent"] = "COMPLETED"
                self._save_state()
            except Exception as e:
                self.state["heartbeats"]["AnonymizerAgent"] = "FAILED"
                self._save_state()
                logger.error(f"AnonymizerAgent failed: {e}")
                sys.exit(1)
        else:
            logger.info("AnonymizerAgent already COMPLETED. Skipping.")

        # Step 4: Netnography Agent (DART Analyst)
        if self.state["heartbeats"]["NetnographyAgent"] != "COMPLETED":
            self.state["heartbeats"]["NetnographyAgent"] = "RUNNING"
            self._save_state()
            try:
                from agents.netnography_agent import NetnographyAgent
                analyst = NetnographyAgent(state_update_callback=self.update_netnography_progress_callback)
                results = analyst.run()
                
                self.state["heartbeats"]["NetnographyAgent"] = "COMPLETED"
                self.state["netnography_progress"] = {
                    "last_post_id": results[-1]["post_id"] if results else "N/A",
                    "progress_pct": 100,
                    "remaining_count": 0
                }
                self._save_state()
            except Exception as e:
                self.state["heartbeats"]["NetnographyAgent"] = "FAILED"
                self._save_state()
                logger.error(f"NetnographyAgent failed: {e}")
                sys.exit(1)
        else:
            logger.info("NetnographyAgent already COMPLETED. Skipping.")

        # Step 5: Quality Guard Agent (Revisor)
        if self.state["heartbeats"]["QualityGuardAgent"] != "COMPLETED":
            self.state["heartbeats"]["QualityGuardAgent"] = "RUNNING"
            self._save_state()
            try:
                from agents.quality_guard_agent import QualityGuardAgent
                revisor = QualityGuardAgent()
                revisor.run()
                
                self.state["heartbeats"]["QualityGuardAgent"] = "COMPLETED"
                self._save_state()
            except Exception as e:
                self.state["heartbeats"]["QualityGuardAgent"] = "FAILED"
                self._save_state()
                logger.critical(f"QualityGuardAgent failed or audit did not pass: {e}")
                sys.exit(1)
        else:
            logger.info("QualityGuardAgent already COMPLETED. Skipping.")

        # Step 6: Synthesis Agent (Redator)
        if self.state["heartbeats"]["SynthesisAgent"] != "COMPLETED":
            self.state["heartbeats"]["SynthesisAgent"] = "RUNNING"
            self._save_state()
            try:
                from agents.synthesis_agent import SynthesisAgent
                redator = SynthesisAgent()
                redator.run()
                
                self.state["heartbeats"]["SynthesisAgent"] = "COMPLETED"
                self._save_state()
            except Exception as e:
                self.state["heartbeats"]["SynthesisAgent"] = "FAILED"
                self._save_state()
                logger.error(f"SynthesisAgent failed: {e}")
                sys.exit(1)
        else:
            logger.info("SynthesisAgent already COMPLETED. Skipping.")

        # Step 7: Summary Table Generator (Utilitário)
        if self.state["heartbeats"]["SummaryTableGenerator"] != "COMPLETED":
            self.state["heartbeats"]["SummaryTableGenerator"] = "RUNNING"
            self._save_state()
            try:
                from summary_table_generator import SummaryTableGenerator
                table_gen = SummaryTableGenerator()
                table_gen.run()
                
                self.state["heartbeats"]["SummaryTableGenerator"] = "COMPLETED"
                self._save_state()
            except Exception as e:
                self.state["heartbeats"]["SummaryTableGenerator"] = "FAILED"
                self._save_state()
                logger.error(f"SummaryTableGenerator failed: {e}")
                sys.exit(1)
        else:
            logger.info("SummaryTableGenerator already COMPLETED. Skipping.")

        logger.info("ALL PIPELINE AGENTS CONCLUDED SUCCESSFULLY!")
        self.print_resume_banner()

if __name__ == "__main__":
    orchestrator = Orchestrator()
    orchestrator.run_pipeline()
