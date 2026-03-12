PYTHON = python3
CHECK1 = checker.py
CHECK2 = checker2.py

.PHONY: 1 debug clean lint

1:
	@echo "Programme launching with 1rst checker..."
	$(PYTHON) $(CHECK1)
	@$(MAKE) clean --no-print-directory

2:
	@echo "Programme launching with 2nd checker..."
	$(PYTHON) $(CHECK2)
	@$(MAKE) clean --no-print-directory

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
