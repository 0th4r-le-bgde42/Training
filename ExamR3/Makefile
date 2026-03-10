PYTHON = python3
MAIN_FILE = checker.py

.PHONY: run debug clean lint

run:
	@echo "Programme launching..."
	$(PYTHON) $(MAIN_FILE)

debug:
	@echo "Debug mode launching..."
	$(PYTHON) -m pdb $(MAIN_FILE)

clean:
	@echo "Cleaning temporary files..."
	@rm -rf __pycache__
	@rm -rf */__pycache__
	@echo "\033[32mFiles delated\033[0m"

lint:
	@echo "Style verification (\033[31mflake8\033[0m)..."
	@python3 -m flake8 .
	@echo "Type verification (\033[31mmypy\033[0m)..."
