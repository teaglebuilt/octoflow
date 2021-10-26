
db:
	docker compose up postgresql

server: db
	uvicorn octoflow.server.main:app --reload

reload:
	pip uninstall octoflow -y && pip install --use-feature=in-tree-build .

reload_tenant:
	pip install --use-feature=in-tree-build ../tenants/tenant
	
clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete