.PHONY: help validate test ci install-codex install-claude install-kimi install-agents verify-install release-check

help:
	@echo "Wiki Knowledge Base Share Kit maintenance commands:"
	@echo "  make validate       - Validate catalog, skill bundle structure, and synced doc snippets"
	@echo "  make test           - Run pytest"
	@echo "  make ci             - Run validate + test"
	@echo "  make install-codex  - Install the full bundle into ~/.codex/skills"
	@echo "  make install-claude - Install the full bundle into ~/.claude/skills"
	@echo "  make install-kimi   - Install the full bundle into ~/.kimi/skills"
	@echo "  make install-agents - Install the full bundle into ~/.agents/skills"
	@echo "  make verify-install - Verify the currently detected runtime install"
	@echo "  make release-check  - Run the checks we expect before cutting a release or PR"

validate:
	python3 scripts/validate_skill_bundle.py

test:
	python3 -m pytest tests/ -v

ci: validate test

install-codex:
	python3 scripts/install_skills.py --platform codex --force

install-claude:
	python3 scripts/install_skills.py --platform claude --force

install-kimi:
	python3 scripts/install_skills.py --platform kimi --force

install-agents:
	python3 scripts/install_skills.py --platform agents --force

verify-install:
	bash verify-installation.sh

release-check: ci
